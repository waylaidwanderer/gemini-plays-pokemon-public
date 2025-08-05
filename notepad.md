# I. Current Objective: Solve Victory Road Puzzles
- **Priority:** Solve the western boulder puzzle on Victory Road 3F as per the system directive. The target switch is at (4, 6).
- **Status:** Party is critically injured. I am currently on the eastern side of the map, which is geographically separated from the western puzzle area. I need to find a new route.

# II. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Defeated Trainers:** Confirmed to be impassable obstacles.
- **Puzzle Resets:** Confirmed that using ladders between floors resets the boulder puzzles on both floors.
- **Boulder/Item Interaction:** Confirmed that pushing a boulder onto an item collects the item and moves the boulder into that space.

## A. Tile Mechanics
- **`cleared_boulder_barrier`:** Acts as a one-way ramp. It is possible to move from a higher elevation tile (like `elevated_ground`) DOWN to the barrier tile, and from the barrier tile DOWN to `ground`. It is IMPOSSIBLE to move UP the ramp (e.g., from `ground` to the barrier, or from the barrier to `elevated_ground`).
- **`steps`:** Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- **`ladder_down` / `ladder_up`:** Warps between floors.
- **`hole`:** Warps the player (or a boulder) to the floor below.

# III. Battle Intelligence

## A. Type Effectiveness Chart (OBSERVATION-ONLY)
*This chart will be built exclusively from in-game battle observations to avoid reliance on external knowledge.*
- **(Placeholder for verified matchups)**

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon (CRAG) can be selected to use a field move like Strength.

# IV. Core Principles & Methodology
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Scientific Method:** Form a hypothesis, test it, and document the conclusion.
- **Trust System Directives:** A system directive is the source of truth and MUST be trusted over personal assumptions or agent outputs. If a directive contradicts observations, the observation or interpretation is flawed.

# V. Paused Investigations & Archived Conclusions
- **Victory Road 1F (Eastern Boulder Puzzle):** This puzzle is currently a dead end. The boulder at (11, 3) cannot be moved past the item at (10, 3), and the item cannot be reached. The solution must lie elsewhere.
- **Victory Road 2F (Eastern Boulder Puzzle):** **[ARCHIVED]** My `puzzle_strategist_agent` and `complex_boulder_pusher_tool` initially concluded the puzzle was unsolvable from this floor. This was superseded by a directive for 3F.
- **Victory Road 3F (Western Boulder Puzzle):** **[ACTIVE INVESTIGATION]** My `puzzle_strategist_agent` initially concluded the puzzle at switch (4,6) was unsolvable. However, a system directive has since confirmed the puzzle *is* solvable. The agent's revised analysis, incorporating the directive, suggests the solution involves pushing the boulder from (14, 13) through a supposedly impassable tile at (12, 11). This is the current working hypothesis.

# VI. Meta & Self-Correction
- **Type Chart Verification:** As per Overwatch critique, I must ensure the Type Effectiveness Chart is built *exclusively* from in-game battle observations to avoid relying on external knowledge.