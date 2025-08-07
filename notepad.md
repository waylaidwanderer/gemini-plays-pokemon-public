# I. Current Objective
- **Primary Objective:** Defeat the Elite Four and become the Pokémon League Champion.
- **Secondary Objective:** Fully explore Victory Road.

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
- **`cleared_boulder_barrier`**: [FALSIFIED] Functions as a one-way ramp. [CORRECTED] A tile that becomes traversable after a boulder switch is activated. It is at the same elevation as `elevated_ground`. Movement between it and `ground` is impossible without `steps`.
- **`hole`**: Warps the player (or a boulder) to the floor below.
- **`ledge`**: Can only be traversed downwards (from a higher Y to a lower Y).

## B. Follower Pokémon Mechanics
- **Pikachu Position Swap:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. This is a newly observed mechanic that requires further testing to confirm if it's consistent under all conditions.

# III. Puzzles & Navigation

## A. Puzzle Mechanics
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.

## B. Current Puzzle Plan (Victory Road 3F)
- **Governing Directive:** A system directive indicates the solution involves a multi-floor boulder puzzle, with the target switch being at (4, 6).
- **Current Status:** I am on Victory Road 3F. The `landmass_analyzer` tool confirmed the map is split into disconnected areas, and the target switch is unreachable from my current position.
- **Hypothesis:** A boulder from 3F must be pushed down a hole to solve the puzzle on 2F, which will likely unlock a path back to the main puzzle area of 3F.
- **Objective:** Push the boulder at (23, 16) into the hole at (24, 16).
- **Step-by-Step Plan:**
  1. Navigate to (22, 16).
  2. Push the boulder at (23, 16) RIGHT into the hole at (24, 16).

# IV. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):
  - Ground > Rock/Ground (4x damage, verified via GRAVELER's EARTHQUAKE vs CRAG).
  - Electric > Flying (Verified: SPARKY vs GOLBAT)
  - Water > Rock/Ground (Verified: NEPTUNE vs GOLEM, TITANESS vs GRAVELER)
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock/Ground (Verified: CRAG vs GRAVELER's SELFDESTRUCT)
- **Immune (0x damage):**
  - Ground immune to Electric (Verified via battle)

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Body Slam:** Can cause paralysis.

# V. Methodology & Lessons Learned
## A. Tool Usage & Debugging
- **Tool Failure Protocol:** If any tool fails, especially a pathfinder: 1. Use `landmass_analyzer` to confirm physical connectivity. 2. Add verbose logging/debug prints to the failing tool. 3. Re-run the tool to generate a detailed log. 4. Use the `tool_debugger_agent` to analyze the log and identify the root cause. This tiered approach MUST be followed before any manual debugging attempts.
- **Code Patch Verification:** When fixing a tool, I MUST use the `code_patch_verifier_agent` to ensure the new code is not identical to the old code. This prevents careless repetitive errors and debugging loops.
- **Code Patch Verification:** When fixing a tool, I MUST use the `code_patch_verifier_agent` to ensure the new code is not identical to the old code. This prevents careless repetitive errors and debugging loops.
- **Landmass Analyzer Limitations:** The `landmass_analyzer` tool now correctly accounts for boulders as obstacles, but it still does not understand one-way traversal tiles like ledges or `cleared_boulder_barrier` ramps. It can report a single landmass even if sections are unreachable due to these mechanics.
- **Surfing Navigation:** The `pathfinder` tool requires `movement_mode='surfing'` to navigate over water.

## B. Agent/Tool Development Ideas
- **Journey Planner Agent:** Create an agent to automate multi-stage travel plans across disconnected landmasses (like Route 23). It would take a final destination, use `landmass_analyzer`, and generate a sequence of pathing/surfing commands.
- **Pathfinder Refinement:** Enhance the `pathfinder` tool. When a path fails due to disconnected landmasses, it should identify this and return a path to the nearest transition point (e.g., a shoreline) instead of just failing.
- **Exploration Strategist Agent:** An agent to automate multi-stage navigation. It would take a final destination, use `landmass_analyzer` to check connectivity, and if disconnected, it would plot a path to the correct transition point (e.g., a ladder or warp) to reach the target landmass.
- **Pathfinder Refinement:** Enhance the `pathfinder` tool. When a path fails, it should internally use logic similar to `landmass_analyzer` to determine if the failure is due to disconnected landmasses and return a more informative error message (e.g., "Destination is on a different, unreachable landmass.").

## C. Core Principles
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Trust System Directives:** A system directive or system warning is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **Tool Maintenance:** Faulty tools must be fixed or deleted IMMEDIATELY. Continuing to use a known-broken tool is inefficient and leads to errors.
- **Puzzle Pre-Planning:** Before attempting any multi-step puzzle (especially boulder puzzles), I MUST first document the intended step-by-step sequence of actions in my notepad. This prevents careless errors and soft-locks.

# VI. Archived & Falsified Hypotheses
- **[FALSIFIED] `steps` at (6, 11) are one-way down.** I successfully used these steps to move from `ground` up to `elevated_ground`, proving they are bi-directional.
- **[FALSIFIED] Victory Road 1F is always a single connected landmass.** My initial `landmass_analyzer` tool was flawed because it did not account for boulders as impassable obstacles. The corrected tool confirmed that misplaced boulders can and do split the map into disconnected areas.
- **[FALSIFIED] Victory Road 2F Disconnected Landmass Hypothesis:** The landmass_analyzer tool's conclusion that this floor is split into disconnected landmasses was proven false by a system warning (Turn 124003) which confirmed the eastern warp at (24, 8) is reachable from the west. The connection is via the elevated platforms.
- **[FALSIFIED] Defeated trainers are impassable obstacles:** A system warning (Turn 124270) indicated that the warp at (2, 2) on Victory Road 1F was reachable, despite being blocked by a defeated trainer at (4, 3). This proves the hypothesis is false and the pathfinder has been updated.
- **[FALSIFIED] Victory Road 1F - West Switch Puzzle Plan:** The plan to push the boulder at (3, 11) UP onto the switch at (3, 10) was executed. This action successfully placed the boulder on the switch, but also blocked the path to the ladder at (2, 2).
- **[LESSON] Victory Road 1F Puzzle Nuance:** Pushing the boulder at (3, 11) UP to the switch at (3, 10) blocks the direct path to the ladder at (2, 2), but does NOT create an inescapable area. A path to the southern exit at (9, 18) remains, making a map reset unnecessary.
- **[ARCHIVED] Debugging Loop Failure:** Repeatedly failed to apply a simple code fix due to carelessness (submitting identical code, introducing typos). This highlights a need for a more robust debugging process.
- **[ARCHIVED] Agent Opportunity - Code Verifier:** The `reflection_agent` suggested creating a 'code patch verifier' agent, which was successfully implemented. This addressed an inefficient debugging loop.
- **[ARCHIVED] Victory Road 2F - East Boulder Puzzle Plan:** Objective was to move boulder from (6, 6) to switch at (10, 17). This was falsified when `landmass_analyzer` confirmed the area was unreachable from the west side of the map.