# I. Current Objective
- **Primary Objective:** Defeat the Elite Four and become the Pokémon League Champion.
- **Secondary Objective:** Fully explore Route 23.

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
- **`cleared_boulder_barrier`**: A traversable tile that appears after a boulder switch is activated. It connects to adjacent `elevated_ground` tiles.
- **`hole`**: Warps the player (or a boulder) to the floor below.
- **`ledge`**: Can only be traversed downwards (from a higher Y to a lower Y). Attempting to move up or sideways onto a ledge tile is impossible.

## B. Follower Pokémon Mechanics
- **Pikachu Movement Rule:** If Pikachu is directly adjacent in the direction you want to move, but you are not facing him, the first button press will only turn you to face him. A second button press in the same direction is required to move onto his tile.

# III. Puzzles & Navigation

## A. Puzzle Mechanics
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.

## B. Navigational Insights (Verified)
- **Victory Road 3F Layout:** Landmass analysis confirmed this floor is split into three disconnected areas.

# IV. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Ground > Rock/Ground (Verified via battle)
  - Electric > Flying (Verified: SPARKY vs GOLBAT)
  - Water > Rock/Ground (Verified: NEPTUNE vs GOLEM)
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
- **Landmass Analyzer Limitations:** The `landmass_analyzer` tool now correctly accounts for boulders as obstacles, but it still does not understand one-way traversal tiles like ledges or `cleared_boulder_barrier` ramps. It can report a single landmass even if sections are unreachable due to these mechanics.
- **Surfing Navigation:** The `pathfinder` tool requires `movement_mode='surfing'` to navigate over water.

## B. Agent/Tool Development Ideas
- **Journey Planner Agent:** Create an agent to automate multi-stage travel plans across disconnected landmasses (like Route 23). It would take a final destination, use `landmass_analyzer`, and generate a sequence of pathing/surfing commands.
- **Pathfinder Refinement:** Enhance the `pathfinder` tool. When a path fails due to disconnected landmasses, it should identify this and return a path to the nearest transition point (e.g., a shoreline) instead of just failing.

## C. Core Principles
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Trust System Directives:** A system directive or system warning is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **Tool Maintenance:** Faulty tools must be fixed or deleted IMMEDIATELY. Continuing to use a known-broken tool is inefficient and leads to errors.
- **Puzzle Pre-Planning:** Before attempting any multi-step puzzle (especially boulder puzzles), I MUST first document the intended step-by-step sequence of actions in my notepad. This prevents careless errors and soft-locks.

# VI. Archived & Falsified Hypotheses
- **[FALSIFIED] Victory Road 1F is always a single connected landmass.** My initial `landmass_analyzer` tool was flawed because it did not account for boulders as impassable obstacles. The corrected tool confirmed that misplaced boulders can and do split the map into disconnected areas.
- **[HYPOTHESIS] Victory Road 2F Puzzle Solution requires a boulder from 3F:** The boulders on 2F cannot reach the switch at (10, 17). The next step is to return to 3F and search for a hole that drops a boulder into the eastern section of 2F.
- **[FALSIFIED] Victory Road 2F Disconnected Landmass Hypothesis:** The landmass_analyzer tool's conclusion that this floor is split into disconnected landmasses was proven false by a system warning (Turn 124003) which confirmed the eastern warp at (24, 8) is reachable from the west. The connection is via the elevated platforms.
- **[FALSIFIED] Defeated trainers are impassable obstacles:** A system warning (Turn 124270) indicated that the warp at (2, 2) on Victory Road 1F was reachable, despite being blocked by a defeated trainer at (4, 3). This proves the hypothesis is false and the pathfinder has been updated.
- **[FALSIFIED] Victory Road 1F - West Switch Puzzle Plan:** The plan to push the boulder at (3, 11) UP onto the switch at (3, 10) was executed. This action successfully placed the boulder on the switch, but also blocked the path to the ladder at (2, 2).
- **[LESSON] Victory Road 1F Puzzle Nuance:** Pushing the boulder at (3, 11) UP to the switch at (3, 10) blocks the direct path to the ladder at (2, 2), but does NOT create an inescapable area. A path to the southern exit at (9, 18) remains, making a map reset unnecessary.
- **Debugging Loop Failure:** Repeatedly failed to apply a simple code fix due to carelessness (submitting identical code, introducing typos). This highlights a need for a more robust debugging process.
- **[ARCHIVED] Agent Opportunity - Code Verifier:** The `reflection_agent` suggested creating a 'code patch verifier' agent, which was successfully implemented. This addressed an inefficient debugging loop.

# VII. Reflection Takeaways (Turn 125016)
- **Map Marker Discipline:** I will be more diligent in marking picked-up items and key NPC dialogue to create a comprehensive record and avoid redundant actions.
- **Victory Road 1F Puzzle Hypothesis:** My next attempt at the 1F puzzle will test the hypothesis that the eastern boulder puzzle must be solved *before* the western one to maintain access to the ladder.

# VII. Current Puzzle Plan (Victory Road 2F)
- **Hypothesis:** The western boulder puzzle must be solved first to open the barrier at (8, 9). This involves pushing the boulder at (5, 15) to the switch at (2, 17).
- **Test Plan (Attempt 1):**
  1. Path to (5, 14) to stand above the boulder.
  2. Push boulder from (5, 15) DOWN to (5, 16).
  3. Path to (6, 16) to stand right of the boulder.
  4. Push boulder from (5, 16) LEFT to (4, 16).
  5. Path to (4, 15) to stand above the boulder.
  6. Push boulder from (4, 16) DOWN to (4, 17).
  7. Path to (5, 17) to stand right of the boulder.
  8. Push boulder from (4, 17) LEFT to (3, 17).
  9. Path to (4, 17) to stand right of the boulder.
  10. Push boulder from (3, 17) LEFT to (2, 17) onto the switch.
- **Expected Outcome:** The barrier at (8, 9) and (8, 10) will change to `cleared_boulder_barrier`, granting access to the eastern part of the map.

# VIII. Reflection Takeaways (Turn 125224)
- **Tool Design Lesson:** Monolithic tools like `boulder_puzzle_solver` are prone to failure. A better design is a modular approach: a `puzzle_data_extractor` tool to gather information, and a `puzzle_strategist_agent` to reason about the solution. This will be a future development goal.
- **New Hypothesis:** The `steps` tile at (6, 11) might be a one-way path (down only). This would explain why my pathfinder failed to find a route to the eastern platform and needs to be tested.