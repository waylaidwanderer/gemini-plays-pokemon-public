# I. Current Objective
- **Primary Objective:** Solve the Victory Road boulder puzzles to reach the Indigo Plateau.
- **Secondary Objective:** Find an opportunity to heal my critically injured party.

# II. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Puzzle Resets:** Confirmed that using ladders between floors resets the boulder puzzles on both floors.
- **Boulder/Item Interaction:** Confirmed that pushing a boulder onto an item collects the item and moves the boulder into that space.

## A. Tile Mechanics (Verified)
- **`impassable`**: Walls, rocks, defeated trainers. Cannot be entered.
- **`ground`**: Walkable tile.
- **`elevated_ground`**: Walkable ground at a higher elevation.
- **`steps`**: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- **`ladder_down` / `ladder_up`**: Warps between floors.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable barrier linked to a boulder switch.
- **`cleared_boulder_barrier`:** Acts as a one-way ramp. It is possible to move from a higher elevation tile DOWN to the barrier tile, and from the barrier tile DOWN to `ground`. It is IMPOSSIBLE to move UP the ramp.
- **`hole`:** Warps the player (or a boulder) to the floor below.

# III. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
*(Placeholder for verified matchups)*

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.

# IV. Methodology & Future Development
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Agent-First Debugging:** When a custom tool fails, I MUST use my `tool_debugger_agent` for analysis before attempting any manual fixes.
- **Trust System Directives:** A system directive or system warning is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **Breaking Unproductive Loops:** If a tool proves unfixable or manual navigation repeatedly fails, I MUST pivot to a new strategy to maintain forward momentum.
- **Future Agent Idea:** A 'paradox resolution' agent to deduce solutions when system data contradicts map data.
- **Future Agent Refinement:** Update `puzzle_strategist_agent` to consider player's physical accessibility to puzzle elements.

# V. Anomalies & Unverified Mechanics
- **Horizontal Push Anomaly (Victory Road 2F):** At (4, 14) and (4, 16), pushing boulders horizontally did not move the player character. Needs more testing.

# VI. Archived Conclusions & Hypotheses
- **[ARCHIVED] Victory Road 2F (Puzzle @ Switch 10,17):** [CONCLUSION] A system directive confirmed this requires a multi-floor solution. The current working hypothesis is that the boulder at (23, 16) on Victory Road 3F must be pushed down the hole at (24, 16) to solve this puzzle.
- **[ARCHIVED] Pathfinder Tool Bug:** My pathfinder tool is likely working correctly. My manual path tracing was flawed, leading me to believe the tool was bugged. I must trust my tools more.
- **[ARCHIVED] Hallucinated Tool:** Overwatch critique mentioned a `complex_boulder_pusher_tool`. My attempt to delete it failed because the tool does not exist. This was a hallucination.
- **[ARCHIVED] Victory Road 1F (Western Area):** The ladder from Victory Road 2F at (1, 9) leads to a small, isolated area on Victory Road 1F. This area is a dead end.

# VII. Navigational Insights
- **Victory Road (Floors 2F & 3F):** These floors are composed of multiple, disconnected platforms. Direct traversal between sections is impossible. Progress requires using the correct sequence of ladders/warps to move between these isolated areas.
- **Victory Road 3F Layout:** This floor consists of multiple, disconnected landmasses. I am currently on the western landmass, which contains the puzzle switch at (4,6) and a boulder at (23,4). The puzzle solution must be on this same landmass.
- **Pathfinding Failure Protocol:** If the pathfinder fails, my first step is to use the `landmass_analyzer` tool to verify physical connectivity before assuming the tool is bugged.