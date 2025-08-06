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
- **[CORRECTED AGAIN] Victory Road 2F Layout:** The `landmass_analyzer` tool confirms this floor is split into two disconnected landmasses. Landmass 0 is the main, large area where the puzzle is. Landmass 1 is a small, isolated platform in the northeast corner accessible only via a specific ladder from 3F. My previous conclusion that it was one contiguous area was a hallucination.
- **Victory Road 3F Layout:** Landmass analysis confirmed this floor is split into three disconnected areas. My previous navigation loops were caused by failing to understand this and attempting to pathfind between them.

# VI. Archived & Falsified Hypotheses
- **[FALSIFIED] Victory Road 3F Hidden Passage (12,7):** The puzzle agent hypothesized a secret passage at (12,7). This was also based on being on the wrong platform. This hypothesis is likely incorrect.
- **[HYPOTHESIS] Victory Road 2F Secret Passage:** The puzzle agent suggests a secret passage at (9, 16) is the key to solving the puzzle for the switch at (10, 17). The plan is to push the boulder from (5,15) down and then east to test this hypothesis.
- **[CORRECTED] Victory Road 2F Navigation:** The ground floor is split into two disconnected eastern and western sections by impassable walls. The only way to cross is by using the elevated platforms, accessible via the steps at (22, 16) in the east and (6, 11) in the west.