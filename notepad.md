# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Data Trust:** The map XML data is the ultimate source of truth for traversal.
- **Off-Screen State Changes:** An object's state (e.g., a `boulder_barrier` changing to `cleared_boulder_barrier`) will not update in the map data until the object is visible on-screen.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile. All elevation changes must use 'steps' tiles.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier, now acts as `ground`.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `ladder_up` / `ladder_down`: Warps between floors.
- `cuttable`: A tree that can be removed with the HM Cut.
- **Defeated Trainers (Hypothesis):** Some defeated trainers may be impassable obstacles. The Juggler at (22, 14) on Victory Road 2F was confirmed to be impassable. However, this may not apply to all defeated trainers. Further testing is required.

# II. Battle Intel
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

# III. Tool Development & Debugging
- **`gem_pathfinder_v2` Status:** The tool is critically bugged. It is generating paths through impassable tiles. My previous assumption about being able to step down from `elevated_ground` was proven false by a blocked path. I must use a scientific approach of logging and forming evidence-based hypotheses to fix it.
- **`puzzle_strategist_agent` Status:** The agent's solution for the western boulder puzzle was based on a flawed premise, as the starting position was unreachable. The agent itself is likely fine, but my inputs and understanding of the map were wrong.
- **Debugging Principle:** Trust direct, in-game evidence over personal assumptions. When a tool fails after being corrected, re-evaluate the map data and my own understanding to find the true obstacle and form a new plan.
- **Lesson on Confirmation Bias:** I must be wary of confirmation bias. I previously wasted time assuming a path was blocked because my tools were flawed and my understanding of game mechanics was incorrect. I must actively try to disprove my own assumptions and be more willing to change my strategy when my tools contradict my beliefs.
- **New Tool Idea:** Create a `pathfinder_log_analyzer` agent or tool. It would take the pathfinder's debug logs as input and output a specific hypothesis for the failure (e.g., 'Failure at (X, Y) due to invalid transition from type A to type B'). This would automate the most difficult part of the debugging cycle.

# IV. Current Plans & Tasks
## A. New Plan: Victory Road 2F Eastern Path
My previous plan to solve the western boulder puzzle was based on a flawed premise; the boulder at (6, 6) is in an isolated, unreachable area. My pathfinder tool also has a critical bug. My new hypothesis is that the solution to the eastern barrier at (24, 15) involves accessing the area via the eastern ladder at (24, 8), which leads to 3F.

## B. Archived Plan: Victory Road 2F Western Boulder Puzzle (INVALID)
My `puzzle_strategist_agent` has provided a 19-step solution to move the boulder at (6, 6) to the switch at (10, 17), which will clear the barrier at (24, 15). THIS PLAN IS INVALID BECAUSE (6,5) IS UNREACHABLE.

## C. Future Tasks
- Systematically test the passability of all defeated trainers in Victory Road to confirm which ones act as impassable obstacles.