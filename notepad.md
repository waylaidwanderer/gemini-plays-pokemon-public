# I. Current Objective: Escape Victory Road & Heal
- **Priority:** Navigate Victory Road 2F to solve the eastern boulder puzzle, which will grant access to the exit.
- **Status:** Party is critically injured. Mandated by system to solve puzzle.

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
- `ladder_up`/`ladder_down`: Warp tiles between floors. Can be used to move between `ground` and `elevated_ground` if they connect different levels.
- `ledge`: One-way traversal. Can only be jumped DOWN.
- `impassable`: Wall. Defeated trainers are impassable obstacles.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a switch.
- `cleared_boulder_barrier`: A former barrier. Acts as a normal traversable tile.
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
- **IMMEDIATE ACTION:** Flaws in tools or data management must be addressed immediately. This includes implementing useful tool ideas instead of deferring them.
- **Confirmation Bias:** I must be willing to question my own strategic assumptions. If a reliable tool consistently fails to find a path, the most likely cause is that my understanding of the map is wrong, not that the tool is broken.
- **Trust System Directives:** If a system directive contradicts direct, repeated in-game observations and specialist agent analysis, the directive is the source of truth. My observations or agent's analysis must be flawed.

# V. Solved Puzzles & Verified Mechanics
- **Victory Road 3F (Boulder Puzzle):** Solved by maneuvering the boulder from (7, 2) to the switch at (4, 6).
- **Victory Road 2F (Western Boulder Puzzle):** The system has confirmed the barrier corresponding to the switch at (2, 17) is already cleared.
- **Victory Road 2F (Puzzle Resets):** Confirmed that using ladders between floors does NOT reset a puzzle.
- **Victory Road 1F (Boulder/Item Interaction):** Confirmed that pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Victory Road 1F (Pathfinder Bug):** Corrected a critical logic flaw in `gem_pathfinder_v2` related to ladder traversal, which was causing it to fail on valid paths.

# VI. Paused Investigations & Archived Conclusions
- **Victory Road 1F (Eastern Boulder Puzzle):** This puzzle is currently a dead end. The boulder at (11, 3) cannot be moved past the item at (10, 3), and the item cannot be reached. The solution must lie elsewhere.
- **Victory Road 2F (Floor-Contained Solution):** My conclusion that the puzzle was unsolvable on this floor was incorrect. This was based on my own flawed testing and my agent's analysis, both of which were superseded by a direct system directive.
- **Complex Boulder Pusher Tool v2 Failure (Turn 121344):** The tool generated another invalid path, attempting to move from `elevated_ground` at (10, 9) to `ground` at (10, 8). **Conclusion:** The tool's internal A* pathfinder for player movement does not account for elevation differences. **Action:** Refactoring the tool to incorporate the elevation-aware traversal logic from `gem_pathfinder_v2`. This is a critical fix.
- **Victory Road 2F (Cleared Boulder Barrier):** Confirmed that `cleared_boulder_barrier` acts as a one-way ramp. It is possible to move from a higher elevation tile (like `elevated_ground`) DOWN to the barrier tile, and from the barrier tile DOWN to `ground`. It is IMPOSSIBLE to move UP the ramp (e.g., from `ground` to the barrier, or from the barrier to `elevated_ground`).