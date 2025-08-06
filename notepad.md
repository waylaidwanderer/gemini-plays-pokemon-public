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
- **Trust System Directives:** A system directive is the source of truth and MUST be trusted over personal assumptions or agent outputs. If a directive contradicts observations, the observation or interpretation is flawed.
- **Breaking Unproductive Loops (Overwatch Mandate):** If a tool proves unfixable after a few focused attempts, or if manual navigation repeatedly fails, I MUST abandon the current approach and pivot to a new strategy to maintain forward momentum. Persisting in a failing strategy is a critical error. My `gem_pathfinder_v2` tool will be tested one final time; if it fails, it will be abandoned in favor of manual navigation.
- **Future Agent Idea:** A 'debugging manager' agent to propose novel debugging steps and prevent repetitive action loops.

# V. Paused Investigations & Archived Conclusions
- **Victory Road 1F (Eastern Boulder Puzzle):** This puzzle is currently a dead end. The boulder at (11, 3) cannot be moved past the item at (10, 3), and the item cannot be reached. The solution must lie elsewhere.
- **Victory Road 3F (Western Boulder Puzzle):** [NEW HYPOTHESIS - AGENT/DIRECTIVE DRIVEN] A system directive confirms the puzzle at switch (4, 6) is solvable. My agent suggests a 'secret passage' solution, pushing the boulder at (14, 13) through impassable tiles at (12, 11), (9, 6), (6, 6), and (5, 6).
- **Type Chart Verification:** As per Overwatch critique, I must ensure the Type Effectiveness Chart is built *exclusively* from in-game battle observations to avoid relying on external knowledge.
- **Hallucinated Tool:** Overwatch critique mentioned a `complex_boulder_pusher_tool` that needed fixing/deleting. My attempt to delete it failed because the tool does not exist. This was a hallucination on my part; I must be more careful tracking my custom tools.

- **Victory Road 1F (Western Area):** The ladder from Victory Road 2F at (1, 9) leads to a small, isolated area on Victory Road 1F around (2, 2). This area is a dead end and does not connect to the main floor. The only exit is back up the ladder.
- **Horizontal Push Anomaly (Victory Road 2F):** At (4, 14), pushing the boulder from (5, 14) to (6, 14) did not move the player character to (5, 14), contradicting previous observations. This needs further verification.
- **Horizontal Push Anomaly 2 (Victory Road 2F):** At (4, 16), pushing the boulder from (5, 16) to (6, 16) did not move the player character, contradicting the general horizontal push rule again.
- **Future Tool Idea:** A `multi_step_boulder_pusher` tool that can take a sequence of push commands (e.g., from the puzzle_strategist_agent) and execute them automatically. This would automate non-linear boulder puzzles.

## A. Victory Road 2F (Eastern Puzzle @ 10,17)
- **[FALSIFIED - AGENT HYPOTHESIS]** Agent suggested impassable tiles from (6, 17) to (9, 17) were a 'fake wall' for the southern boulder. Test failed; the wall is solid.
- **[NEW HYPOTHESIS - DIRECTIVE DRIVEN]** A system directive states the solution is on this floor, overriding previous conclusions. The new plan is to maneuver the northern boulder at (6, 6) south, then east, and down the ramp at (8, 9) to reach the switch at (10, 17).
- **[FALSIFIED - SYSTEM DIRECTIVE]** Multiple system directives have confirmed the solution is on Victory Road 2F. The multi-floor hypothesis is incorrect.

## Archived Hypotheses
- **[CORRECTED] Pikachu Movement Mechanic:** Pikachu is a special NPC that can be walked through. If adjacent and not facing him, the first directional press turns the player, and the second moves onto his tile. The hypothesis that I needed to wait for him to move at Victory Road 2F (6, 11) was incorrect.

## C. Victory Road 3F (Eastern Puzzle)
- **[FALSIFIED - MANUAL HYPOTHESIS]** The impassable tile at (24, 10) is a 'fake wall'. Test failed; the wall is solid.