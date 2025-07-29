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
- **Defeated Trainers:** Are **IMPASSABLE** obstacles. They do not respawn and block movement.

# III. Puzzle Mechanics & Problem Solving
## A. Solved Puzzles & Key Discoveries
- **Route 23 Navigation:** The route is split by a large body of water. The eastern path is a dead end for reaching Victory Road. The correct path is the western one, which requires backtracking from the eastern fork.
- **Victory Road 2F - Correct Puzzle Sequence:** This floor must be solved in a single visit without leaving the map. Leaving and re-entering resets the puzzles.
  1.  Enter from the ladder at (1, 9).
  2.  Solve the **western puzzle**: Push the boulder from (5, 15) to the switch at (2, 17). This opens the barrier at (8, 9) and (8, 10).
  3.  Solve the **eastern puzzle**: Push the boulder from (6, 5) to the switch at (10, 17). This opens the barrier at (24, 15), clearing the path to the exit ladder.
- **Victory Road 3F - Hole Puzzle:** Pushing the boulder at (14, 13) south into the hole at (14, 15) causes it to appear on the floor below.
- **Victory Road 1F - Boulder/Steps Interaction (Confirmed):** Boulders cannot be pushed onto `steps` tiles. This was confirmed after multiple failed attempts to push the boulder at (6, 15) north onto the steps at (6, 14).
- **Elevation Rule:** Movement between `ground` and `elevated_ground` is only possible via `steps` tiles. Direct movement from an elevated tile to an adjacent lower ground tile is impossible, even if the tile is a `cleared_boulder_barrier`, unless it specifically acts as a ramp between the two levels.

# IV. Archived Lessons & Tool Development
- **Systematic Problem-Solving:** Trust the game state data over intuition.
- **Efficient Debugging:** Vary test conditions to gather new diagnostic data.
- **Immediate Action:** Log all data in the turn of discovery. This includes disproven hypotheses to avoid repeating mistakes.
- **Trust Direct Observation:** Base understanding of mechanics on in-game observations.
- **Tool Development Status (Under Debugging):**
  - `gem_pathfinder_v2`: The pathfinder is highly unreliable on Route 23, consistently failing on complex paths with narrow corridors and obstacles. Confirmed as a tool bug by the diagnostics agent. It is under active debugging.

# V. Future Development Ideas
- **Team Composition Advisor:** An agent to suggest optimal team compositions.
- **Pathfinder Debugging Agent:** An agent to parse pathfinder debug output and provide a concise summary of why a path failed. This would automate the multi-step process I currently do manually.
- **Route Analysis Agent:** An agent to analyze map connectivity and suggest high-level navigation strategies.

# VI. Agent & Tool Development Notes
- **`puzzle_strategist_agent`:** The agent's original plan for the eastern boulder puzzle on Victory Road 1F may have been correct. My pathfinder was too buggy to execute it. With the pathfinder now stable, this plan can be re-tested in the future if needed. The agent needs refinement to better process all impassable map data.

# VII. Reflection Learnings (Turn 109575)
- **Confirmation Bias:** I had a major hallucination that the eastern path on Route 23 was the correct one. I clung to this belief despite my pathfinder repeatedly failing, leading to dozens of wasted turns. I must learn to trust my tools and data over my own intuition, and actively try to disprove my own hypotheses.
- **Immediate Documentation:** I failed to immediately log my discovery that the eastern path on Route 23 was a dead end, causing me to waste turns on a flawed navigation plan. I must log all critical findings as soon as they are confirmed to maintain an accurate knowledge base.