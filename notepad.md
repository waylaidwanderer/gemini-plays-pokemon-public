# I. Active Investigations

## A. Victory Road 2F (Eastern Boulder Puzzle)
- **Directive:** The system is forcing the solution of this puzzle. The target is the switch at (10, 17).
- **Hypothesis:** The puzzle is unsolvable from this floor alone and likely requires a multi-floor solution, as concluded by the `puzzle_strategist_agent`. This requires accessing the western part of the map.
- **Blocker:** My `gem_pathfinder_v2` tool has a bug that prevents it from finding a path to the western side of the map, creating a hallucinated soft-lock. Fixing this tool is the top priority.

# II. Core Gameplay & World Rules

## A. Game Mechanics
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A' to access Pokémon Storage. 'Gem's PC' is for items.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a map (e.g., Victory Road 1F to Route 23) resets its boulder puzzles. Using ladders between floors (e.g., 1F to 2F) does NOT reset them.
- **Off-Screen State Changes:** An object's state (like a `boulder_barrier`) will not update in the map data until it is visible on-screen.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile (Elevation 0).
- `elevated_ground`: Walkable tile at a higher elevation (Elevation 2). It is IMPOSSIBLE to step directly between `ground` and `elevated_ground`.
- `steps`: Allows two-way movement between `ground` and `elevated_ground`. Boulders cannot be pushed onto `steps` tiles.
- `cleared_boulder_barrier`: A former barrier. On Victory Road 2F, this acts as a normal two-way path between `ground` and `elevated_ground`. On other maps, it may function as a one-way ramp.
- `ladder_up`: Warp tile leading to a higher floor.
- `ladder_down`: Warp tile leading to a lower floor.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `impassable`: Wall. Defeated trainers are impassable obstacles.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a switch.
- `hole`: Drops to a lower floor. Pushing a boulder into one moves it to the floor below.

# III. Battle Intelligence

## A. Verified Type Effectiveness Chart
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.

# IV. Core Principles & Methodology
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Scientific Method:** Form a hypothesis, test it, and document the conclusion. Do not modify tools to test hypotheses; test them with in-game actions first.
- **Trust System Feedback:** System feedback is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management must be addressed immediately.

# V. Solved Puzzles & Discarded Hypotheses

## A. Solved Puzzles & Verified Mechanics
- **Victory Road 3F (Boulder Puzzle):** Solved by maneuvering the boulder from (7, 2) to the switch at (4, 6).
- **Victory Road 2F (Western Boulder):** Solved. The system has confirmed the barrier corresponding to the switch at (2, 17) is already cleared.
- **Victory Road 2F (Puzzle Resets):** Confirmed that using ladders between floors does NOT reset a puzzle.

## B. Discarded Hypotheses
- **Victory Road 2F (Southern Boulder Trap):** The southern boulder at (5, 15) cannot reach the eastern switch at (10, 17). It gets trapped by an impassable wall at (9, 16).
- **Victory Road 2F (Northern Boulder Trap):** The northern boulder at (6, 6) is also trapped. It cannot be moved into a position to reach the eastern switch due to impassable walls and the defeated Pokemaniac at (5, 3).

# VI. Tool Development Notes

## A. Tool Notes
- **gem_pathfinder_v2:** **Under critical repair.** The tool has a persistent bug related to its traversal logic, specifically how it handles `cleared_boulder_barrier` tiles. It is currently unable to find valid paths on Victory Road 2F, contradicting system feedback. Fixing this is the highest priority.

# VII. Lessons Learned & Heuristics
- **Verify 'Trapped' Scenarios:** If a pathfinder tool reports 'No path found' and I believe I am trapped, I must trust the game state's list of reachable warps over my tool's output and prioritize debugging the tool.
- **Boulders cannot be pushed up `steps` tiles:** This was tested and confirmed on Victory Road 2F.