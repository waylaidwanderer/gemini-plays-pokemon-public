# I. Current Objective: Victory Road 2F

## A. Eastern Boulder Puzzle
- **Goal:** Get a boulder onto the switch at (10, 17).
- **Status:** The western puzzle switch at (2, 17) is already solved. The solution must involve the northern boulder at (6, 6).

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

# VI. Tool Development Notes

## A. Tool Notes
## B. Tool Status
- **gem_pathfinder_v2:** UNDER OBSERVATION. The tool was generating invalid paths by moving through boulders because a previous fix incorrectly removed collision detection. The correct logic to treat boulders as impassable has been restored.

# VII. Lessons Learned & Heuristics
- **Trust System Directives:** If a system directive contradicts direct, repeated in-game observations and specialist agent analysis, the directive is the source of truth. My observations or agent's analysis must be flawed.
- **Hypothesis Under Test:** Boulders can be pushed from `elevated_ground` down onto `steps` tiles. My previous conclusion that this was impossible is now being re-tested, as it is the only remaining potential solution to the puzzle mandated by the system directive.
- **Victory Road 2F (Floor-Contained Solution):** My conclusion that the puzzle was unsolvable on this floor was incorrect. This was based on my own flawed testing and my agent's analysis, both of which were superseded by a direct system directive.

# VIII. Paused Investigations & Archived Conclusions
- **Victory Road 1F (Eastern Boulder Puzzle):** Investigation paused. I trapped the boulder at (15, 3), making the puzzle unsolvable without a reset. I am currently on 2F.
- **Victory Road 2F (Failed Hypothesis - Paradoxical Push):** The agent's plan to push the boulder at (5, 15) onto the impassable tile at (9, 16) failed. The tile is truly impassable. The agent's reasoning was flawed due to its deference to a system directive.
- **Victory Road 2F (Failed Hypothesis - Traversable Trainer):** The pathfinder returned 'No path found' when trying to route past the defeated Pokemaniac at (5, 3), even when ignoring the trainer's coordinates. This indicates the path is blocked by other impassable terrain, and the hypothesis that the trainer is the sole obstacle is incorrect or insufficient.