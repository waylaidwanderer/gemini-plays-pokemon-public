# I. Current Objective: Solve Victory Road Puzzles
- **Priority:** Solve the eastern boulder puzzle on Victory Road 2F as per the system directive. The target switch is at (10, 17).
- **Status:** Party is critically injured. My `gem_pathfinder_v2` tool is broken, which is the highest priority to fix.

# II. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.

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
- **Victory Road 2F (Western Boulder Puzzle):** The system has confirmed the barrier corresponding to the switch at (2, 17) is already cleared.
- **Victory Road 2F (Puzzle Resets):** Confirmed that using ladders between floors DOES reset the boulder puzzles on both floors.
- **Victory Road 1F (Boulder/Item Interaction):** Confirmed that pushing a boulder onto an item collects the item and moves the boulder into that space.
- **`cleared_boulder_barrier` Mechanic:** Confirmed that `cleared_boulder_barrier` acts as a one-way ramp. It is possible to move from a higher elevation tile (like `elevated_ground`) DOWN to the barrier tile, and from the barrier tile DOWN to `ground`. It is IMPOSSIBLE to move UP the ramp (e.g., from `ground` to the barrier, or from the barrier to `elevated_ground`).

# VI. Paused Investigations & Archived Conclusions
- **Victory Road 1F (Eastern Boulder Puzzle):** This puzzle is currently a dead end. The boulder at (11, 3) cannot be moved past the item at (10, 3), and the item cannot be reached. The solution must lie elsewhere.
- **Victory Road 2F (Eastern Boulder Puzzle):** **[CORRECTED]** My `puzzle_strategist_agent` and `complex_boulder_pusher_tool` initially concluded the puzzle was unsolvable from this floor. However, a system directive has mandated I solve it now. This implies a hidden mechanic or a flaw in my tools' understanding of the map.
- **Victory Road 3F (Western Boulder Puzzle):** **[CORRECTED]** My `puzzle_strategist_agent` initially concluded the puzzle at switch (4,6) was unsolvable. However, a system directive has since confirmed the puzzle *is* solvable. The agent's revised analysis, incorporating the directive, suggests the solution involves pushing the boulder from (14, 13) through a supposedly impassable tile at (12, 11). This is the current working hypothesis.