# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Data Trust:** The map XML data is the ultimate source of truth for traversal.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. Movement between elevations is *only* possible via `steps` tiles.
- `steps`: Allows movement between `ground` and `elevated_ground`.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier, now acts as `ground`.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `ladder_up` / `ladder_down`: Warps between floors.
- `cuttable`: A tree that can be removed with the HM Cut.

# II. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Trainer Battle Rules
- **Defeated Trainers:** Defeated trainers do NOT respawn and are **IMPASSABLE** obstacles. My previous assumption that they were traversable, based on misleading system feedback, was definitively proven false when the game engine blocked my movement onto a defeated trainer's tile.

# III. Puzzle Mechanics & Problem Solving

## A. Active Puzzles
- **Victory Road 1F - Eastern Boulder Puzzle:**
  - **Observation:** The `puzzle_strategist_agent` provided a complex, multi-step solution. However, the `gem_pathfinder` tool was unable to navigate to the agent's proposed starting position, making the plan untestable.
  - **Hypothesis #1:** The agent's plan is correct, but the pathfinder is too buggy to execute it.
  - **Hypothesis #2 (Failed):** Pushing the boulder at (15, 3) left resulted in soft-locking it at (11, 3) between an impassable wall and an item object. Conclusion: This is not the correct solution.
- **Hypothesis #3 (Failed - Attempt #2):** My pathfinder is not broken; it correctly identifies that the path to the exit is blocked by the western boulder puzzle. To proceed, I must solve this puzzle by moving the boulder at (3, 11).
  - **Test:** Push the boulder at (3, 11) down to (3, 12).
  - **Conclusion:** FAILED. Pushing the boulder did not open a path to the exit. My hypothesis was incorrect. The path remains blocked, confirming the pathfinder's original assessment.
- **Hypothesis #4 (Failed):** The paradox of the 'reachable' ladder at (2, 2) being blocked by the defeated trainer at (4, 3) is due to the trainer being a traversable exception.
  - **Test:** Attempt to walk from (4, 4) onto the trainer's tile at (4, 3).
  - **Conclusion (Attempt #1):** FAILED. The game blocked my movement, confirming defeated trainers are always impassable. My analysis was flawed; a clear, unobstructed path to the ladder exists by simply walking around the trainer via (3, 4).

## B. Solved Puzzles & Key Discoveries
- **Victory Road 2F - Correct Puzzle Sequence:** This floor must be solved in a single visit without leaving the map. Leaving and re-entering resets the puzzles.
  1.  Enter from the ladder at (1, 9).
  2.  Solve the **western puzzle**: Push the boulder from (5, 15) to the switch at (2, 17). This opens the barrier at (8, 9) and (8, 10).
  3.  Solve the **eastern puzzle**: Push the boulder from (6, 5) to the switch at (10, 17). This opens the barrier at (24, 15), clearing the path to the exit ladder.
- **Victory Road 3F - Hole Puzzle:** Pushing the boulder at (14, 13) south into the hole at (14, 15) causes it to appear on the floor below.
- **Victory Road 1F - Boulder/Steps Interaction (Confirmed):** Boulders cannot be pushed onto `steps` tiles. This was confirmed after multiple failed attempts to push the boulder at (6, 15) north onto the steps at (6, 14).
- **Elevation Rule:** Movement between `ground` and `elevated_ground` is only possible via `steps` tiles. Direct movement from an elevated tile to an adjacent lower ground tile is impossible, even if the tile is a `cleared_boulder_barrier`, unless it specifically acts as a ramp between the two levels.

# IV. Archived Lessons & Tool Development
- **Systematic Problem-Solving:** When faced with a navigation paradox, I must trust the game state data as the source of truth. My failure to trust the `navigable_warps` data led to a long loop.
- **Efficient Debugging:** Repetitively running the same failing test case is inefficient. I must vary test conditions to gather new diagnostic data.
- **Immediate Action:** All maintenance and data logging must be done in the immediate turn of discovery.
- **Trust Direct Observation:** My understanding of mechanics requires trusting my own in-game observations.
- **Tool Development Status (Ongoing):**
  - **`gem_pathfinder_v2`**: **CRITICALLY UNRELIABLE.** This tool is fundamentally broken. Despite a complete rewrite, it cannot reliably pathfind on multi-level maps or even avoid basic impassable tiles. It is not to be used until it has been completely rebuilt or thoroughly debugged.

# V. Future Development Ideas
- **Team Composition Advisor:** An agent that analyzes my PC box and suggests optimal team compositions for specific challenges.
- **Debugging Assistant:** An agent that can parse the debug output of `gem_pathfinder_v2` to help identify the root cause of pathing failures.

# VI. Agent & Tool Development Notes
- **Overwatch Feedback (Action Item):** The `puzzle_strategist_agent`'s plan was likely correct. My pathfinder was too buggy to execute it. Once the pathfinder is reliable, I MUST re-test the agent's original, complex solution for the eastern boulder puzzle.