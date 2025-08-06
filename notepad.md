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
- **Victory Road 3F (Western Boulder Puzzle):** [AGENT HYPOTHESIS] A system directive confirms the puzzle at switch (4, 6) is solvable. The only viable hypothesis, proposed by my agent, is a 'secret passage' solution, pushing the boulder at (14, 13) through impassable tiles. This is the main long-term goal for this floor.
- **Victory Road 2F (Puzzle @ Switch 10,17):** [CONCLUSION] The solution requires a boulder from another floor. The current working hypothesis is that the boulder at (6, 6) on 2F must be maneuvered to the switch.
- **Horizontal Push Anomaly (Victory Road 2F):** At (4, 14) and (4, 16), pushing boulders horizontally did not move the player character, contradicting the general rule. This needs further verification.
- **[CORRECTED] Pathfinder Tool Bug:** My pathfinder tool is likely working correctly. My manual path tracing was flawed, leading me to believe the tool was bugged. I must trust my tools more.
- **[ARCHIVED] Hallucinated Tool:** Overwatch critique mentioned a `complex_boulder_pusher_tool`. My attempt to delete it failed because the tool does not exist. This was a hallucination.
- **[ARCHIVED] Victory Road 1F (Western Area):** The ladder from Victory Road 2F at (1, 9) leads to a small, isolated area on Victory Road 1F. This area is a dead end.

## A. Victory Road 2F (Puzzle @ Switch 10,17) - Investigation Log
1. **[INITIAL CONCLUSION - FALSIFIED]** My initial analysis concluded that all on-floor boulders were unable to reach the switch, leading to the hypothesis that a multi-floor solution was required.
2. **[OVERRIDE - SYSTEM DIRECTIVE]** Received a system directive stating the solution IS on the current floor. This falsified the multi-floor hypothesis.
3. **[AGENT HYPOTHESIS - FALSIFIED]** My `puzzle_strategist_agent` suggested the impassable tiles from (6, 17) to (9, 17) were a 'fake wall'. Test failed; the wall is solid.
4. **[CURRENT HYPOTHESIS - DIRECTIVE DRIVEN]** The only remaining on-floor option is the northern boulder at (6, 6). The new plan is to maneuver this boulder south, then east, and down the ramp at (8, 9) to reach the switch.

## A. Victory Road 2F (Puzzle @ Switch 10,17) - Investigation Log
1. **[INITIAL CONCLUSION - FALSIFIED]** My initial analysis concluded that all on-floor boulders were unable to reach the switch, leading to the hypothesis that a multi-floor solution was required.
2. **[OVERRIDE - SYSTEM DIRECTIVE]** Received a system directive stating the solution IS on the current floor. This falsified the multi-floor hypothesis.
3. **[AGENT HYPOTHESIS - FALSIFIED]** My `puzzle_strategist_agent` suggested the impassable tiles from (6, 17) to (9, 17) were a 'fake wall'. Test failed; the wall is solid.
4. **[CURRENT HYPOTHESIS - DIRECTIVE DRIVEN]** The only remaining on-floor option is the northern boulder at (6, 6). The new plan is to maneuver this boulder south, then east, and down the ramp at (8, 9) to reach the switch.