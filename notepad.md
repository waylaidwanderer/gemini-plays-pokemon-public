# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.

## A. Tile Mechanics (Verified)
- **`impassable`**: Walls, rocks. Cannot be entered.
- **`ground`**: Walkable tile.
- **`water`**: Crossable using HM Surf.
- **`elevated_ground`**: Walkable ground at a higher elevation. Cannot be stepped up to or down from `ground` tiles directly.
- **`steps`**: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- **`ladder_down` / `ladder_up`**: Warps between floors.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable barrier linked to a boulder switch.
- **`cleared_boulder_barrier`**: A tile that becomes traversable after a boulder switch is activated. It is at the same elevation as `elevated_ground`. Movement between it and `ground` is impossible without `steps`.
- **`hole`**: Warps the player (or a boulder) to the floor below.
- **`ledge`**: Can only be traversed downwards (from a higher Y to a lower Y).

## B. Follower Pokémon Mechanics
- **Pikachu Position Swap:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions.

# II. Puzzles & Navigation

## A. Puzzle Mechanics
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.

## B. Current Puzzle Status (Victory Road 2F)
- **Governing Directive:** A system directive has confirmed the current puzzle is on 2F. The goal is to move a boulder to the switch at (10, 17).
- **Current Hypothesis (Hypothesis 8):** The boulder at (5, 15) can be pushed to the switch at (10, 17). The path is: push UP to (5, 12), then push RIGHT to (10, 12), then push DOWN to (10, 17).

# III. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Electric > Flying (Verified: SPARKY vs GOLBAT)
  - Water > Rock/Ground (Verified: NEPTUNE vs GOLEM, TITANESS vs GRAVELER)
  - Ground > Rock/Ground (Verified: Wild GRAVELER's EARTHQUAKE vs CRAG)
- **Super Effective (2x damage):**
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

# IV. Methodology & Lessons Learned
## A. Tool Usage & Debugging
- **Tool Failure Protocol:** If any tool fails, especially a pathfinder: 1. Use `landmass_analyzer` to confirm physical connectivity. 2. Add verbose logging/debug prints to the failing tool. 3. Re-run the tool to generate a detailed log. 4. Use the `tool_debugger_agent` to analyze the log and identify the root cause. This tiered approach MUST be followed before any manual debugging attempts.
- **Landmass Analyzer Limitations:** The `landmass_analyzer` tool now correctly accounts for boulders as obstacles, but it still does not understand one-way traversal tiles like ledges or `cleared_boulder_barrier` ramps. It can report a single landmass even if sections are unreachable due to these mechanics.
- **Surfing Navigation:** The `pathfinder` tool requires `movement_mode='surfing'` to navigate over water.

## B. Agent & Tool Ideas
- **Puzzle Reset Planner:** An agent or tool that determines the most efficient path to reset the current map's puzzle (e.g., finding the nearest ladder/exit).

## C. Deprecated Agents
- **[DELETED] Exploration Strategist Agent:** This agent was designed for multi-stage navigation but was unusable due to requiring a non-existent helper tool. It has been deleted to maintain a clean and functional agent list.

## D. Core Principles
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Trust System Directives:** A system directive or system warning is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **Tool Maintenance & Verification:** I MUST use the `code_patch_verifier_agent` before every `define_tool` call to prevent debugging loops caused by submitting identical code. This is a non-negotiable step in my process.
- **Puzzle Pre-Planning:** Before attempting any multi-step puzzle (especially boulder puzzles), I MUST first document the intended step-by-step sequence of actions in my notepad. This prevents careless errors and soft-locks.

# V. Archived & Falsified Hypotheses
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 4:** Pushing the boulder at (6, 7) south to the switch at (10, 17) is impossible due to an impassable elevation change between a `ground` tile and an `elevated_ground` tile.
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 1:** The boulder at (8, 15) can be pushed directly right to column 10. Failed due to impassable wall at (9, 15).
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 2:** The boulder at (8, 15) can be moved north, then east, then south. Failed due to impassable wall at (9, 12).
- **[FALSIFIED] Defeated trainers are impassable obstacles:** A system warning (Turn 124270) indicated that the warp at (2, 2) on Victory Road 1F was reachable, despite being blocked by a defeated trainer at (4, 3). This proves the hypothesis is false and the pathfinder has been updated.
- **[ARCHIVED] Victory Road 1F Puzzle Nuance:** Pushing the boulder at (3, 11) UP to the switch at (3, 10) blocks the direct path to the ladder at (2, 2), but does NOT create an inescapable area. A path to the southern exit at (9, 18) remains, making a map reset unnecessary.
- **[ARCHIVED] Debugging Loop Failure:** Repeatedly failed to apply a simple code fix due to carelessness (submitting identical code, introducing typos). This highlights a need for a more robust debugging process.
- **[ARCHIVED] Agent Opportunity - Code Verifier:** The `reflection_agent` suggested creating a 'code patch verifier' agent, which was successfully implemented. This addressed an inefficient debugging loop.
- **[ARCHIVED] Victory Road 2F Boulder Puzzle - Hypothesis 5:** The boulder at (6, 6) can be pushed to the switch at (10, 17). The path is: push DOWN to (6, 17), then push EAST to (10, 17). This avoids impassable walls and seems to be the correct path within this landmass.
  - **[FALSIFIED]** The path south is blocked by an impassable elevation change between a `ground` tile (6, 8) and an `elevated_ground` tile (6, 9). The boulder cannot be pushed up.
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 6:** Pushing the boulder at (5, 15) to (10, 17) via (8, 17) is impossible due to an impassable wall at (9, 17).
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 7:** The boulder at (5, 15) can be pushed to (10, 17) via (10, 16). Failed because the path right from (8, 16) is blocked by an impassable wall at (9, 16).
- **[ARCHIVED] Victory Road 2F Puzzle Status & Reset Plan:** All hypotheses for solving the puzzle on the 2F landmass failed. The plan was to reset the puzzle by traveling to the ladder at (2, 2), ascending to 3F, and immediately returning to 2F. This plan was superseded by the discovery that the solution lies on 3F.
- **[ARCHIVED] `landmass_analyzer` & `pathfinder` Debugging:** Both tools were failing on Victory Road 3F because they could not handle movable obstacles (boulders). The temporary fix was to make them ignore boulders, which led to invalid path generation. The permanent fix was to restore boulder collision, forcing manual puzzle solving.