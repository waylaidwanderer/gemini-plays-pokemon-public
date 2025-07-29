# I. Game Mechanics & Traversal

## A. Core Rules
- **Level Cap:** The level cap with 8 badges is 65.
- **"No Will to Fight" Message:** Appears when the party menu cursor is on a fainted Pokémon. It is a cursor error, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** To use a PC, stand directly below it, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points for SURF.
- **Boulder Pushing:** Activate Strength from the party menu. Face the boulder and press the directional button. The boulder moves one tile. **CRITICAL MECHANIC (3rd Revision):** The player's position does NOT change after pushing a boulder, regardless of direction. My previous assumptions based on external tool data were incorrect; direct observation confirms the player remains stationary.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Data Trust:** The map XML data is the ultimate source of truth for traversal. If a tile is marked `impassable` in the XML, it cannot be walked on, even if it appears visually open on screen.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. Movement to a lower elevation is *only* possible via `steps` tiles or `cleared_boulder_barrier` tiles. Direct movement to a lower `ground` tile is impossible.
- `steps`: Allows movement between elevations.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier, now acts as `ground`. Allows movement between adjacent `elevated_ground` and `ground` tiles, effectively acting as a ramp.
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
  - **Hypothesis #2 (Active):** A simpler solution exists. I can solve the puzzle by pushing the boulder at (15, 3) to the left, navigating it around the central rock formation.
  - **Test (In Progress):** I am currently at (15, 3), having pushed the boulder from (16,3) to (14,3) and then to (13,3). I will continue to push it left.
  - **Conclusion:** TBD.

## B. Solved Puzzles & Key Discoveries
- **Victory Road 2F - Correct Puzzle Sequence:** This floor must be solved in a single visit without leaving the map. Leaving and re-entering resets the puzzles.
  1.  Enter from the ladder at (1, 9).
  2.  Solve the **western puzzle**: Push the boulder from (5, 15) to the switch at (2, 17). This opens the barrier at (8, 9) and (8, 10).
  3.  Solve the **eastern puzzle**: Push the boulder from (6, 5) to the switch at (10, 17). This opens the barrier at (24, 15), clearing the path to the exit ladder.
- **Victory Road 3F - Hole Puzzle:** Pushing the boulder at (14, 13) south into the hole at (14, 15) causes it to appear on the floor below.
- **Victory Road 1F - Boulder/Steps Interaction (Confirmed):** Boulders cannot be pushed onto `steps` tiles. This was confirmed after multiple failed attempts to push the boulder at (6, 15) north onto the steps at (6, 14).
- **Elevation Rule:** Movement between `ground` and `elevated_ground` is only possible via `steps` tiles. Direct movement from an elevated tile to an adjacent lower ground tile is impossible, even if the tile is a `cleared_boulder_barrier`, unless it specifically acts as a ramp between the two levels.

# IV. Archived Lessons & Tool Development
- **Systematic Problem-Solving:** When faced with a navigation paradox, I must avoid chaotic, repeated manual attempts. The correct approach is to trust the game state data (e.g., `navigable_warps`) as the source of truth and systematically eliminate possibilities. I will use the 'Active Puzzles' section to document my reasoning process in real-time.
- **Efficient Debugging:** Repetitively running the same failing test case is inefficient. I must vary the test conditions (e.g., change the target destination) to gather new diagnostic data and isolate bugs more effectively. My recent failure loop with `gem_pathfinder` is a key example of what not to do.
- **Immediate Action:** Deferring tasks like tool repair or documentation is a critical error. All maintenance and data logging must be done in the immediate turn of discovery to maintain a coherent internal state.
- **Trust Direct Observation:** My understanding of the boulder pushing mechanic required three revisions because I failed to trust my own in-game observations over incorrect prior assumptions. Direct gameplay evidence is the ultimate source of truth and must always take precedence.
- **Tool Development Status (Ongoing):**
  - **gem_pathfinder:** **CRITICALLY UNRELIABLE.** The tool is currently unable to correctly pathfind across different elevation levels using 'steps' tiles and has also demonstrated fundamental failures in avoiding basic `impassable` walls. It is under active debugging with extensive logging added and should not be trusted for any navigation until its core logic is resolved.

# V. Future Development Ideas
- **Team Composition Advisor:** An agent that analyzes my PC box and suggests optimal team compositions for specific challenges, like the Elite Four.