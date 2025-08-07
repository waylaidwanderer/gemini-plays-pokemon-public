# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.

## A. Tile Mechanics (Verified)
- **`impassable`**: Walls, rocks. Cannot be entered.
- **`ground`**: Walkable tile.
- **`water`**: Crossable using HM Surf.
- **`elevated_ground`**: Walkable ground at a higher elevation. Cannot be stepped up to or down from `ground` tiles directly. This has been confirmed by attempting to move from (10, 3) to (10, 2) and failing.
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

# III. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Electric > Flying
  - Water > Rock/Ground
  - Ground > Rock/Ground
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock/Ground
- **Immune (0x damage):**
  - Ground immune to Electric

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

## B. Methodology Improvements & Future Plans
- **Tool Idea - Puzzle Reset Planner:** An agent or tool that determines the most efficient path to reset the current map's puzzle (e.g., finding the nearest ladder/exit).
- **Tool Idea - Puzzle Solver:** An agent or tool that can analyze the map state (boulders, switches, walls) and output a sequence of moves to solve the puzzle.
- **Tool Idea - Tool Debugger Pipeline:** An agent that automates the debugging process. It would take a tool name and arguments as input, run the tool with verbose logging enabled, and then automatically feed the resulting log to the `tool_debugger_agent` to get a diagnosis. This would streamline the `Tool Failure Protocol` into a single action.
- **Pathfinder Permanent Fix Plan:** The `pathfinder`'s elevation logic is fundamentally broken. The temporary fix of commenting it out is unsustainable. I need to dedicate time to rewriting this logic from scratch to correctly handle `steps`, `ladders`, and one-way movements between `ground` and `elevated_ground`. Before deploying a new fix, I must test it on a simple, controlled map with known elevation changes to verify its correctness.

## C. Deprecated Agents
- **[DELETED] Exploration Strategist Agent:** This agent was designed for multi-stage navigation but was unusable due to requiring a non-existent helper tool. It has been deleted to maintain a clean and functional agent list.

## D. Core Principles
- **Agent-First Approach:** Before attempting any manual solution for a complex problem, I MUST consult the relevant specialist agent first.
- **Trust System Directives:** A system directive or system warning is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **Tool Maintenance & Verification:** I MUST use the `code_patch_verifier_agent` before every `define_tool` call to prevent debugging loops caused by submitting identical code. This is a non-negotiable step in my process.
- **Puzzle Pre-Planning:** Before attempting any multi-step puzzle (especially boulder puzzles), I MUST first document the intended step-by-step sequence of actions in my notepad. This prevents careless errors and soft-locks.

# V. Current Puzzle Plan
## A. Victory Road 3F Boulder Puzzle
- **Hypothesis 2:** The boulder at (23, 4) can be pushed to the switch at (4, 6).
- **Plan:**
    1. Navigate to (22, 4) to get into position to push the boulder.
    2. Push the boulder LEFT from (23, 4) to (22, 4).
    3. Push LEFT to (21, 4).
    4. Push DOWN to (21, 5).
    5. Maneuver around to (21, 6) and push DOWN to (21, 7).
    6. Continue pushing the boulder west through the main corridor towards the switch at (4, 6).

# VI. Archived & Falsified Hypotheses
- **[FALSIFIED] Victory Road 3F Boulder Puzzle - Hypothesis 1:** The boulder at (14, 13) can be pushed to the switch at (4, 6). This fails because it is impossible to get into position at (14, 14) to push the boulder north. The tiles at (13, 13) and (15, 13) are impassable walls, completely blocking access from the south.
- **[FALSIFIED] Victory Road 3F Boulder Puzzle - Initial Attempt:** My initial thought was that the boulder at (14, 13) was stuck. Pushing it UP requires standing at (14, 14), and I incorrectly assumed the direct path was the only path, which is blocked by impassable tiles. A longer, wrap-around path exists.
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 9:** The boulder at (7, 12) can be pushed DOWN to (7, 17) and then RIGHT to the switch at (10, 17). This fails because the tile at (6, 17) is an impassable wall, making it impossible to get into position to push the boulder to the right.
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 8:** The boulder at (5, 15) can be pushed to the switch at (10, 17). The path is: push UP to (5, 12), then push RIGHT to (10, 12), then push DOWN to (10, 17). This fails because the path right is blocked by an impassable wall at (9, 12).
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 7:** The boulder at (5, 15) can be pushed to (10, 17) via (10, 16). Failed because the path right from (8, 16) is blocked by an impassable wall at (9, 16).
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 6:** Pushing the boulder at (5, 15) to (10, 17) via (8, 17) is impossible due to an impassable wall at (9, 17).
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 5:** The boulder at (6, 6) can be pushed to the switch at (10, 17). The path is: push DOWN to (6, 17), then push EAST to (10, 17). This fails due to an impassable elevation change between a `ground` tile (6, 8) and an `elevated_ground` tile (6, 9).
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 4:** Pushing the boulder at (6, 7) south to the switch at (10, 17) is impossible due to an impassable elevation change between a `ground` tile and an `elevated_ground` tile.
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 2:** The boulder at (8, 15) can be moved north, then east, then south. Failed due to impassable wall at (9, 12).
- **[FALSIFIED] Victory Road 2F Boulder Puzzle - Hypothesis 1:** The boulder at (8, 15) can be pushed directly right to column 10. Failed due to impassable wall at (9, 15).
- **[FALSIFIED] Defeated trainers are impassable obstacles:** A system warning (Turn 124270) indicated that the warp at (2, 2) on Victory Road 1F was reachable, despite being blocked by a defeated trainer at (4, 3). This proves the hypothesis is false and the pathfinder has been updated.
- **Battle Strategist Agent Failure (Turn 126296):** The agent recommended switching in a Lv. 24 SUBTERRA against a Lv. 47 GRAVELER. It failed to properly weigh the massive level difference, which resulted in an immediate KO. The agent's system prompt has now been updated with a strict rule (Rule #13) to forbid recommending significantly underleveled Pokémon. The agent has been further refined with rules to avoid switching in low-HP 'avengers' and to account for neutral coverage moves.