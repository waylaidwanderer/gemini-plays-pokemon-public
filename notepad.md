# I. Current Objective: Solve Victory Road 2F Puzzle
- **Priority:** Solve the eastern boulder puzzle as mandated by the system directive. The target is the switch at (10, 17).
- **Status:** Party is critically injured. Retreat to heal is not an option until the puzzle is solved.

# II. Core Gameplay & World Rules

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
- **Complex Boulder Pusher Tool v2 Fix (Turn 121441):** Refactored the tool to use the elevation-aware traversal logic from `gem_pathfinder_v2`, resolving a critical bug where it would generate invalid paths between different elevations.

# VI. Paused Investigations & Archived Conclusions
- **Victory Road 1F (Eastern Boulder Puzzle):** This puzzle is currently a dead end. The boulder at (11, 3) cannot be moved past the item at (10, 3), and the item cannot be reached. The solution must lie elsewhere.
- **Victory Road 2F (Floor-Contained Solution):** My conclusion that the puzzle was unsolvable on this floor was incorrect. This was based on my own flawed testing and my agent's analysis, both of which were superseded by a direct system directive.
- **Victory Road 2F (Cleared Boulder Barrier):** Confirmed that `cleared_boulder_barrier` acts as a one-way ramp. It is possible to move from a higher elevation tile (like `elevated_ground`) DOWN to the barrier tile, and from the barrier tile DOWN to `ground`. It is IMPOSSIBLE to move UP the ramp (e.g., from `ground` to the barrier, or from the barrier to `elevated_ground`).