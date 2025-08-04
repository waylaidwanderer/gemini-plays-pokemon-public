# I. Current Objective: Escape Victory Road & Heal
- **Priority:** Navigate Victory Road 1F to reach the ladder to 2F at (2,2), then re-evaluate. The eastern puzzle is a dead end for now.
- **Status:** Party is critically injured.

# II. Core Gameplay & World Rules

## A. Game Mechanics
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A' to access Pokémon Storage. 'Gem's PC' is for items.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a map (e.g., Victory Road 1F to Route 23) resets its boulder puzzles. Using ladders between floors (e.g., 1F to 2F) does NOT reset them.
- **Off-Screen State Changes:** An object's state (like a `boulder_barrier`) will not update in the map data until it is visible on-screen.
- **Boulder Push (Horizontal):** When pushing a boulder horizontally, the player moves into the boulder's previous space, *unless* the tile directly behind the player is blocked by an object or impassable terrain. If blocked, only the boulder moves.
- **Boulder/Item Interaction:** Pushing a boulder onto a tile containing an item will collect the item and move the boulder into that space.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile (Elevation 0).
- `elevated_ground`: Walkable tile at a higher elevation (Elevation 2). It is IMPOSSIBLE to step directly between `ground` and `elevated_ground`.
- `steps`: Allows two-way movement between `ground` and `elevated_ground`.
- `cleared_boulder_barrier`: A former barrier. Acts as a normal traversable tile. Direct movement from `ground` to this tile is IMPOSSIBLE.
- `ladder_up`/`ladder_down`: Warp tiles between floors.
- `ledge`: One-way traversal. Can only be jumped DOWN.
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

# V. Solved Puzzles & Verified Mechanics
- **Victory Road 3F (Boulder Puzzle):** Solved by maneuvering the boulder from (7, 2) to the switch at (4, 6).
- **Victory Road 2F (Western Boulder Puzzle):** The system has confirmed the barrier corresponding to the switch at (2, 17) is already cleared.
- **Victory Road 2F (Puzzle Resets):** Confirmed that using ladders between floors does NOT reset a puzzle.
- **Victory Road 1F (Boulder/Item Interaction):** Confirmed that pushing a boulder onto an item collects the item and moves the boulder into that space.

# VI. Tool Development Notes

## B. Tool Status
- **gem_pathfinder_v2:** RELIABLE (Basic Pathing). The tool is now reliable for standard navigation on this map, after it was determined that previous failures were due to a flawed world model on my part, not a bug in the tool's logic for valid paths.

# VII. Lessons Learned & Heuristics
- **Trust System Directives:** If a system directive contradicts direct, repeated in-game observations and specialist agent analysis, the directive is the source of truth. My observations or agent's analysis must be flawed.
- **Hypothesis Under Test:** Boulders can be pushed from `elevated_ground` down onto `steps` tiles. My previous conclusion that this was impossible is now being re-tested, as it is the only remaining potential solution to the puzzle mandated by the system directive.
- **Victory Road 2F (Floor-Contained Solution):** My conclusion that the puzzle was unsolvable on this floor was incorrect. This was based on my own flawed testing and my agent's analysis, both of which were superseded by a direct system directive.

# VIII. Paused Investigations & Archived Conclusions
- **Victory Road 2F (Failed Hypothesis - Paradoxical Push):** The agent's plan to push the boulder at (5, 15) onto the impassable tile at (9, 16) failed. The tile is truly impassable. The agent's reasoning was flawed due to its deference to a system directive.
- **Victory Road 2F (Failed Hypothesis - Traversable Trainer):** The pathfinder returned 'No path found' when trying to route past the defeated Pokemaniac at (5, 3), even when ignoring the trainer's coordinates. This indicates the path is blocked by other impassable terrain, and the hypothesis that the trainer is the sole obstacle is incorrect or insufficient.