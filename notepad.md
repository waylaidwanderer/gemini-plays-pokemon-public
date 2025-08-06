# I. Current Objective
- **Primary Objective:** Solve the Victory Road boulder puzzles to reach the Indigo Plateau.
- **Secondary Objective:** Utilize the new puzzle_strategist_agent to solve the next boulder puzzle.

# II. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Puzzle Resets:** Confirmed that using ladders between floors resets the boulder puzzles on both floors.
- **Boulder/Item Interaction:** Confirmed that pushing a boulder onto an item collects the item and moves the boulder into that space.

## A. Tile Mechanics (Verified)
- **`impassable`**: Walls, rocks, defeated trainers. Cannot be entered.
- **`ground`**: Walkable tile.
- **`grass`**: Tall grass for wild Pokémon encounters. Walkable like `ground`.
- **`water`**: Crossable using HM Surf.
- **`elevated_ground`**: Walkable ground at a higher elevation. Cannot be stepped up to or down from `ground` tiles directly.
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

# IV. Methodology & Lessons Learned
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Trust System Directives:** A system directive or system warning is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **Pathfinding Failure Protocol:** If a pathfinder tool repeatedly fails, my first step MUST be to use the `landmass_analyzer` tool to verify physical connectivity before assuming the tool is bugged. This is to combat my confirmation bias where I blame tools for my own flawed understanding of the map layout.
- **Tool Maintenance:** Faulty tools must be fixed or deleted IMMEDIATELY. Continuing to use a known-broken tool is inefficient and leads to errors.

# V. Navigational Insights (Verified)
- **Victory Road 3F Layout:** Landmass analysis confirmed this floor is split into three disconnected areas. My previous navigation loops were caused by failing to understand this and attempting to pathfind between them.

# VI. Archived & Falsified Hypotheses
- **[HYPOTHESIS] Victory Road 2F Puzzle Solution requires a boulder from 3F:** The boulders on 2F cannot reach the switch at (10, 17). The next step is to return to 3F and search for a hole that drops a boulder into the eastern section of 2F.
- **[FALSIFIED] Victory Road 2F Disconnected Landmass Hypothesis:** The landmass_analyzer tool's conclusion that this floor is split into disconnected landmasses was proven false by a system warning (Turn 124003) which confirmed the eastern warp at (24, 8) is reachable from the west. The connection is via the elevated platforms.
- **[FALSIFIED] Victory Road 2F Secret Passage (9, 16):** The puzzle agent's hypothesis of a secret passage at (9, 16) was tested by attempting to push the boulder at (8, 16) east. The push failed, proving the tile is impassable. This hypothesis is incorrect.
- **[FALSIFIED] Victory Road 3F Hidden Passage (12,7):** The puzzle agent hypothesized a secret passage at (12,7). This was also based on being on the wrong platform. This hypothesis is likely incorrect.
- **[FALSIFIED] Victory Road 2F 'Cleared Path' Hypothesis:** The puzzle agent's hypothesis that solving the switch at (2, 17) would clear the impassable tiles along the same row was tested by attempting to push the boulder at (5, 17) east. The push failed, proving the tiles remain impassable. This hypothesis is incorrect.
- **[FALSIFIED] Victory Road 2F 'Secret Path' Hypothesis (Agent-Generated):** The agent's hypothesis that the impassable tile at (5, 10) was cleared was tested by attempting to move there. The move failed, proving the tile remains impassable. This hypothesis is incorrect.