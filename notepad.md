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
- **Future Agent Idea:** A 'debugging manager' agent to propose novel debugging steps and prevent repetitive action loops.

# V. Paused Investigations & Archived Conclusions
- **Victory Road 1F (Eastern Boulder Puzzle):** This puzzle is currently a dead end. The boulder at (11, 3) cannot be moved past the item at (10, 3), and the item cannot be reached. The solution must lie elsewhere.
- **Victory Road 3F (Western Boulder Puzzle):** My `puzzle_strategist_agent` initially concluded the puzzle at switch (4,6) was unsolvable. However, a system directive has since confirmed the puzzle *is* solvable. The agent's revised analysis, incorporating the directive, suggests the solution involves pushing the boulder from (14, 13) through a supposedly impassable tile at (12, 11). This is the current working hypothesis.
- **Type Chart Verification:** As per Overwatch critique, I must ensure the Type Effectiveness Chart is built *exclusively* from in-game battle observations to avoid relying on external knowledge.
- **Hallucinated Tool:** Overwatch critique mentioned a `complex_boulder_pusher_tool` that needed fixing/deleting. My attempt to delete it failed because the tool does not exist. This was a hallucination on my part; I must be more careful tracking my custom tools.

- **Victory Road 1F (Western Area):** The ladder from Victory Road 2F at (1, 9) leads to a small, isolated area on Victory Road 1F around (2, 2). This area is a dead end and does not connect to the main floor. The only exit is back up the ladder.
- **Horizontal Push Anomaly (Victory Road 2F):** At (4, 14), pushing the boulder from (5, 14) to (6, 14) did not move the player character to (5, 14), contradicting previous observations. This needs further verification.
- **Victory Road 2F (Eastern Puzzle @ 10,17):** Hypothesis to use the southern boulder (at 7, 14) has been falsified. The path to the switch is blocked by an impassable tile at (9, 17). The solution must involve the northern boulder at (6, 6).

## Archived Hypotheses
- **[ARCHIVED] Hypothesis (Victory Road 2F):** Interacting with Pikachu at (6, 11) failed to move him. He is a standard moving NPC who is currently blocking the 'steps' tile, which is the only path to the northern boulder. The only option is to wait for him to move on his own.

- **Horizontal Push Anomaly 2 (Victory Road 2F):** At (4, 16), pushing the boulder from (5, 16) to (6, 16) did not move the player character, contradicting the general horizontal push rule again.
- **Future Tool Idea:** A `multi_step_boulder_pusher` tool that can take a sequence of push commands (e.g., from the puzzle_strategist_agent) and execute them automatically. This would automate non-linear boulder puzzles.
- **[FALSIFIED] Victory Road 2F (Southern Boulder):** All agent-led hypotheses regarding the southern boulder have been falsified. Attempts to push it east through presumed secret passages at (9,16), (9,14), and (6,17) were all blocked by impassable tiles. The solution must involve the northern boulder.
  1. Navigate to (6, 4) to get above the northern boulder at (6, 5).
  2. Push the boulder down to approximately y=16.
  3. Reposition to the left of the boulder and push it right to x=10.
  4. Reposition above the boulder and push it down onto the switch at (10, 17).
- - [FALSIFIED] Victory Road 2F (Eastern Puzzle @ 10,17): The agent's paradoxical hypothesis, based on a system directive, that the southern boulder at (8, 16) could be pushed through a secret passage at (9, 16) was incorrect. The push was re-tested (Attempt #2) and blocked again. The solution must involve the northern boulder.
- **Current Plan (Victory Road 2F @ 10,17):**
  1. Navigate to (6, 4) to get above the northern boulder at (6, 5).
  2. Push the boulder down to approximately y=14.
  3. Reposition to the left of the boulder and push it right to test the agent's new hypothesis about a secret passage at (9, 14).
  4. If successful, push the boulder to x=10.
  5. Reposition above the boulder and push it down onto the switch at (10, 17).

- **Current Plan (Victory Road 2F @ 10,17):**
  1. Navigate to (6, 7) to get below the northern boulder at (6, 6).
  2. Push the boulder UP to (6, 5).
  3. Navigate around to (4, 5) to get to the left of the boulder.
  4. Push the boulder RIGHT to (9, 5).
  5. Navigate around to (9, 4) to get above the boulder.
  6. Push the boulder DOWN onto the switch at (10, 17).
- **[FALSIFIED] Victory Road 2F (Southern Boulder):** All agent-led hypotheses regarding the southern boulder at (5,15) and (5,17) have been falsified. Attempts to push it east through presumed secret passages at (9,16), (9,14), and (6,17) were all blocked by impassable tiles. The solution must involve the northern boulder.