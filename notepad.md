# I. Current Objective & Hypotheses
- **Primary Objective:** Solve the Victory Road boulder puzzles to reach the Indigo Plateau.
- **Secondary Objective:** Find an opportunity to heal my critically injured party.

# II. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Defeated Trainers:** Confirmed to be impassable obstacles.
- **Puzzle Resets:** Confirmed that using ladders between floors resets the boulder puzzles on both floors.
- **Boulder/Item Interaction:** Confirmed that pushing a boulder onto an item collects the item and moves the boulder into that space.

## A. Tile Mechanics (Verified)
- **`impassable`**: Walls, rocks, etc. Cannot be entered.
- **`ground`**: Walkable tile.
- **`elevated_ground`**: Walkable ground at a higher elevation.
- **`steps`**: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- **`ladder_down` / `ladder_up`**: Warps between floors.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable barrier linked to a boulder switch.
- **`cleared_boulder_barrier`:** Acts as a one-way ramp. It is possible to move from a higher elevation tile (like `elevated_ground`) DOWN to the barrier tile, and from the barrier tile DOWN to `ground`. It is IMPOSSIBLE to move UP the ramp (e.g., from `ground` to the barrier, or from the barrier to `elevated_ground`).
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

# IV. Methodology & Future Development
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Agent-First Debugging:** When a custom tool fails, I MUST use my `tool_debugger_agent` for analysis before attempting any manual fixes.
- **Trust System Directives:** A system directive or system warning is the source of truth and MUST be trusted over personal assumptions or agent outputs. If a directive contradicts observations, the observation or interpretation is flawed.
- **Breaking Unproductive Loops (Overwatch Mandate):** If a tool proves unfixable after a few focused attempts, or if manual navigation repeatedly fails, I MUST abandon the current approach and pivot to a new strategy to maintain forward momentum. Persisting in a failing strategy is a critical error.
- **Future Agent Idea:** A 'debugging manager' agent to propose novel debugging steps and prevent repetitive action loops.

# V. Paused Investigations & Archived Conclusions
- **Victory Road 3F (Western Boulder Puzzle):** [AGENT HYPOTHESIS] The puzzle at switch (4, 6) is solvable via a 'secret passage' for the boulder at (14, 13). This is a long-term goal.
- **Victory Road 2F (Puzzle @ Switch 10,17):** [CONCLUSION] Confirmed multi-floor solution. Hypothesis: Push boulder at (23, 16) on 3F down the hole at (24, 16).
- **Horizontal Push Anomaly (Victory Road 2F):** Horizontal boulder pushes at (4, 14) and (4, 16) didn't move the player. Needs more testing.
- **[ARCHIVED] Hallucinated Tool:** `complex_boulder_pusher_tool` does not exist.
- **[ARCHIVED] Victory Road 1F (Western Area):** Area from 2F ladder at (1, 9) is a confirmed dead end.