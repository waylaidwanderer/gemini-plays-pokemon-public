# I. Current Objective
- **Primary Objective:** Solve the Victory Road boulder puzzles to reach the Indigo Plateau.

# II. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Puzzle Resets:** Confirmed that using ladders between floors or leaving/re-entering a map resets boulder puzzles.
- **Boulder/Item Interaction:** Confirmed that pushing a boulder onto an item collects the item and moves the boulder into that space.

## A. Tile Mechanics (Verified)
- **`impassable`**: Walls, rocks. Cannot be entered.
- **`ground`**: Walkable tile.
- **`grass`**: Tall grass for wild Pokémon encounters. Walkable like `ground`.
- **`water`**: Crossable using HM Surf.
- **`elevated_ground`**: Walkable ground at a higher elevation. Cannot be stepped up to or down from `ground` tiles directly.
- **`steps`**: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- **`ladder_down` / `ladder_up`**: Warps between floors.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable barrier linked to a boulder switch.
- **`cleared_boulder_barrier`**: Acts as a one-way ramp. It is possible to move from a higher elevation tile DOWN to the barrier tile, and from the barrier tile DOWN to `ground`. It is IMPOSSIBLE to move UP the ramp.
- **`hole`**: Warps the player (or a boulder) to the floor below.
- **`ledge`**: Can only be traversed downwards (from a higher Y to a lower Y). Attempting to move up or sideways onto a ledge tile is impossible.

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
- **Defeated Trainers are Passable:** System warnings confirmed that defeated trainers are not obstacles, even though they are objects. My pathfinder tool has been updated to reflect this.
- **Surfing Navigation:** The `pathfinder` tool requires `movement_mode='surfing'` to navigate over water.

# V. Navigational Insights (Verified)
- **Victory Road 3F Layout:** Landmass analysis confirmed this floor is split into three disconnected areas.
- **Victory Road 1F Layout:** Landmass analysis confirmed the floor is a single connected area, but paths can be blocked by misplaced boulders.

# VI. Archived & Falsified Hypotheses
- **[HYPOTHESIS] Victory Road 2F Puzzle Solution requires a boulder from 3F:** The boulders on 2F cannot reach the switch at (10, 17). The next step is to return to 3F and search for a hole that drops a boulder into the eastern section of 2F.
- **[FALSIFIED] Victory Road 2F Disconnected Landmass Hypothesis:** The landmass_analyzer tool's conclusion that this floor is split into disconnected landmasses was proven false by a system warning (Turn 124003) which confirmed the eastern warp at (24, 8) is reachable from the west. The connection is via the elevated platforms.
- **[FALSIFIED] Victory Road 2F Secret Passage (9, 16):** The puzzle agent's hypothesis of a secret passage at (9, 16) was tested by attempting to push the boulder at (8, 16) east. The push failed, proving the tile is impassable. This hypothesis is incorrect.
- **[FALSIFIED] Victory Road 3F Hidden Passage (12,7):** The puzzle agent hypothesized a secret passage at (12,7). This was also based on being on the wrong platform. This hypothesis is likely incorrect.
- **[FALSIFIED] Victory Road 2F 'Cleared Path' Hypothesis:** The puzzle agent's hypothesis that solving the switch at (2, 17) would clear the impassable tiles along the same row was tested by attempting to push the boulder at (5, 17) east. The push failed, proving the tiles remain impassable. This hypothesis is incorrect.
- **[FALSIFIED] Victory Road 2F 'Secret Path' Hypothesis (Agent-Generated):** The agent's hypothesis that the impassable tile at (5, 10) was cleared was tested by attempting to move there. The move failed, proving the tile remains impassable. This hypothesis is incorrect.
- **[FALSIFIED] Defeated trainers are impassable obstacles:** A system warning (Turn 124270) indicated that the warp at (2, 2) on Victory Road 1F was reachable, despite being blocked by a defeated trainer at (4, 3). This proves the hypothesis is false.
- **Puzzle Pre-Planning:** Before attempting any multi-step puzzle (especially boulder puzzles), I MUST first document the intended step-by-step sequence of actions in my notepad. This prevents careless errors and soft-locks.

# VII. Active Puzzle Plans

## Victory Road 1F - East Switch Puzzle
- **Target:** Switch at (18, 14)
- **Solution Steps (from boulder_puzzle_solver):**
  1. Push boulder at (6, 16) Down
  2. Push boulder at (6, 17) Right
  3. Push boulder at (7, 17) Right
  4. Push boulder at (8, 17) Right
  5. Push boulder at (9, 17) Up
  6. Push boulder at (9, 16) Right
  7. Push boulder at (10, 16) Up
  8. Push boulder at (10, 15) Right
  9. Push boulder at (11, 15) Right
  10. Push boulder at (12, 15) Right
  11. Push boulder at (13, 15) Right
  12. Push boulder at (14, 15) Right
  13. Push boulder at (15, 15) Right
  14. Push boulder at (16, 15) Right
  15. Push boulder at (17, 15) Up
  16. Push boulder at (17, 14) Up
  17. Push boulder at (17, 13) Right
  18. Push boulder at (18, 13) Down