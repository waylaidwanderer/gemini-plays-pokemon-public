# I. Current Objective
- **Primary Objective:** Solve the Victory Road boulder puzzles to reach the Indigo Plateau.

# II. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.

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

# III. Puzzles & Navigation

## A. Puzzle Mechanics
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.

## B. Navigational Insights (Verified)
- **Victory Road 3F Layout:** Landmass analysis confirmed this floor is split into three disconnected areas.
- **Victory Road 1F Layout:** Landmass analysis confirmed the floor is a single connected area, but paths can be blocked by misplaced boulders.

## C. Active Puzzle Plans
### Victory Road 1F - West Switch Puzzle
- **Insight:** The eastern puzzle (switch at 18,14) is separate from the puzzle blocking the ladder to 2F. The path to the ladder is blocked by the boulder at (3,11).
- **Target:** Switch at (3, 10)
- **Plan:** 
  1. Navigate to (3, 12).
  2. Push the boulder at (3, 11) UP onto the switch at (3, 10).

# IV. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
*(Placeholder for verified matchups)*

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.

# V. Methodology & Lessons Learned
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Trust System Directives:** A system directive or system warning is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **Tool Failure Protocol:** If any tool fails, especially a pathfinder: 1. Use `landmass_analyzer` to confirm physical connectivity. 2. Add verbose logging/debug prints to the failing tool. 3. Re-run the tool to generate a detailed log. 4. Use the `tool_debugger_agent` to analyze the log and identify the root cause. This tiered approach MUST be followed before any manual debugging attempts.
- **Tool Maintenance:** Faulty tools must be fixed or deleted IMMEDIATELY. Continuing to use a known-broken tool is inefficient and leads to errors.
- **Landmass Analyzer Limitation:** The `landmass_analyzer` tool does not account for one-way traversal tiles like ledges or `cleared_boulder_barrier` ramps. It can report a single landmass even if sections are unreachable due to these mechanics.
- **Surfing Navigation:** The `pathfinder` tool requires `movement_mode='surfing'` to navigate over water.
- **Puzzle Pre-Planning:** Before attempting any multi-step puzzle (especially boulder puzzles), I MUST first document the intended step-by-step sequence of actions in my notepad. This prevents careless errors and soft-locks.

# VI. Archived & Falsified Hypotheses
- **[HYPOTHESIS] Victory Road 2F Puzzle Solution requires a boulder from 3F:** The boulders on 2F cannot reach the switch at (10, 17). The next step is to return to 3F and search for a hole that drops a boulder into the eastern section of 2F.
- **[FALSIFIED] Victory Road 2F Disconnected Landmass Hypothesis:** The landmass_analyzer tool's conclusion that this floor is split into disconnected landmasses was proven false by a system warning (Turn 124003) which confirmed the eastern warp at (24, 8) is reachable from the west. The connection is via the elevated platforms.
- **[FALSIFIED] Defeated trainers are impassable obstacles:** A system warning (Turn 124270) indicated that the warp at (2, 2) on Victory Road 1F was reachable, despite being blocked by a defeated trainer at (4, 3). This proves the hypothesis is false and the pathfinder has been updated.