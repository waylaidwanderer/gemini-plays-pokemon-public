# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Data Trust:** The map XML data is the ultimate source of truth for traversal.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.

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
- **Defeated Trainers (Confirmed):** Defeated trainers in Victory Road act as impassable obstacles.

# II. Battle Intel
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

# III. Tool Development & Debugging
## A. Tool & Agent Status
- **`gem_pathfinder_v2` Status:** The tool's script is confirmed to be functional via `run_code`. However, the custom tool definition itself is corrupted, causing silent failures. The current workaround is to execute the script via `run_code` for all pathfinding needs.
- **`pathfinder_log_analyzer` Agent:** This agent has been created and used. Its purpose is to take debug logs from the pathfinder and output a specific hypothesis for the failure.

## B. Debugging Principles & Lessons
- **Scientific Method:** When debugging, I must use a scientific approach: form a hypothesis, create a minimal test case, and incrementally build up complexity. Blindly re-running a full, complex script is inefficient and must be avoided.
- **Trust In-Game Evidence:** Direct, in-game evidence must always be trusted over personal assumptions.
- **Avoid Confirmation Bias:** I must actively try to disprove my own assumptions.

## C. Future Tool/Agent Ideas
- **`tile_inspector` Tool:** Would take coordinates (x, y) and return a JSON of all tile properties. Useful for rapid, targeted data verification during debugging.
- **`trainer_passability_tester` Agent:** Would take a list of trainer coordinates and return a report on whether each is passable. This would automate the task of systematically testing trainer impassability.
- **`puzzle_state_verifier` Agent:** Would take puzzle element data and player position to confirm a puzzle solution is still valid before execution.

# IV. Current Plans & Tasks
## A. Current Plan: Navigate Victory Road 3F
My immediate goal is to explore this floor. The map is segmented, and I need to find my way to the exit.
**Hypothesis:** The path forward involves solving a boulder puzzle to open the barrier at (8, 11).
**Execution Plan:**
1.  Navigate out of the initial starting area via the steps at (2, 10).
2.  Explore the western section of the floor to find a boulder and push it onto the switch at (4, 6).
3.  Proceed through the now-open barrier to the eastern section.
4.  Explore the eastern section and find the exit.

## B. Archived Plans
- **Victory Road 2F Western Boulder Puzzle:** I have completed this puzzle and moved to 3F.
- **Victory Road 2F Boulder at (6, 6):** PROVEN IMPOSSIBLE. My agent confirmed this specific boulder cannot reach the switch.
- **Victory Road 2F Eastern Path:** Invalidated. The western puzzle was the correct path.