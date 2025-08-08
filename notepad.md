# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.

# II. Tile Mechanics (Verified)
- `ground`: Walkable tile.
- `grass`: Tall grass where wild Pokémon appear. Walkable like `ground`.
- `elevated_ground`: Walkable ground at a higher elevation. Movement to/from `ground` tiles requires `steps` or a one-way drop.
- `cleared_boulder_barrier`: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground`.
- `steps`: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- `ledge`: Can only be traversed downwards.
- `water`: Crossable using HM Surf.
- `impassable`: Walls, rocks. Cannot be entered.
- `ladder_down` / `ladder_up`: Warps between floors.
- `hole`: Warps the player (or a boulder) to the floor below.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.

# III. Puzzle Mechanics & Solutions
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Multi-floor Puzzles:** The puzzles in Victory Road often require elements from multiple floors (e.g., pushing a boulder through a hole from 3F to solve a puzzle on 2F).

## Solved Puzzles (Victory Road)
- **3F to 2F:** Pushed boulder from (14, 13) into hole at (14, 15).
- **2F Main Barrier:** Used boulder from 3F (landed at (5, 15)) and pushed it onto switch at (2, 17).
- **3F Main Barrier:** Pushed boulder from (23, 2) to switch at (4, 6). Solution: [L, L, L, L, L, L, L, L, L, L, L, L, L, L, L, L, D, L, L, L, L, D, D, D, R]
- **2F Western Barrier:** The switch at (2, 17) is empty, but the barrier is already cleared. This puzzle is solved.

# IV. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Electric > Flying
  - Water > Rock/Ground
  - Ground > Rock/Ground
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock/Ground
- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Body Slam:** Can cause paralysis.

# V. Methodology & Lessons Learned
- **Hypothesis-Driven Approach:** When faced with a puzzle, I must form a single, testable hypothesis, document it, test it, and record the conclusion. This avoids chaotic, assumption-driven actions.
- **Confirmation Bias & Untested Assumptions:** I must treat negative results from my tools (e.g., 'no path found') as valid data that should prompt a re-evaluation of my strategy, not just the tool itself. I must actively try to *disprove* my own hypotheses. A tool's failure to find a path is data about the game state (e.g., an obstacle exists).
- **Tool Reliability & Inefficient Debugging:** A tool that produces an incorrect or impossible result is a critical failure. However, getting stuck in a prolonged debugging cycle while ignoring the actual game state is a critical strategic failure. I must prioritize making progress in the game over perfecting a tool, especially when manual navigation is a viable alternative.
- **Strategic Flexibility:** Fixating on a single, stalled objective is inefficient. If multiple paths are available, and one is blocked by a difficult puzzle, exploring the alternate path or resetting the puzzle state is a better strategy than repeated failed attempts.
- **Agent & Tool Limitations:**
    - Reasoning-based agents (like `battle_strategist_agent`) are ill-suited for complex, state-based computational problems like boulder puzzles. These tasks require dedicated computational tools (`boulder_puzzle_solver`).
    - The `landmass_analyzer` ignores boulders by design to check theoretical terrain connectivity. Its output does not account for the current puzzle state and should not be misinterpreted as a guarantee of a currently open path.
- **`battle_strategist_agent` Refinement:** The agent needs to be more cautious. It previously recommended an attack with a low-HP NEPTUNE against a faster Gengar, resulting in a KO. The prompt should be updated to heavily penalize high-risk plays with low-HP Pokémon that do not have a guaranteed speed advantage. (Note: Recent performance has been excellent, but this lesson remains valuable).

# VI. Future Tool/Agent Ideas
- **`puzzle_master_agent`:** A high-level agent to strategize the *order* of operations for complex, multi-stage puzzles. It could analyze the puzzle state and suggest testable hypotheses (e.g., "Hypothesis: The eastern boulder puzzle must be solved first. Test: Attempt to move the boulder at (15,3) to the switch at (18,14).").
- **`boulder_puzzle_solver_tool`:** A dedicated computational tool to solve boulder puzzles. It would take the map state (player, boulders, switches, walls) as input and return an optimal sequence of pushes. This would automate the tedious and error-prone process of manual puzzle-solving.
- **`battle_calculator_tool`:** A computational tool to calculate damage ranges, speed tiers, and KO probabilities to provide purely data-driven battle advice, avoiding potential LLM reasoning fallacies.
- **`fly_menu_navigator_tool`:** A tool that can parse the screen text of the Fly menu to identify the currently selected location and determine the number of 'Down' presses required to reach a target destination.
- **`route_planner_tool`:** A computational tool to analyze `landmass_analyzer` output for complex routes with multiple landmasses (like Route 23). It would identify optimal surf/landing points to generate a high-level navigation plan.
- **Victory Road 1F Central Path:** SOLVED. Pushing the boulder from (7, 17) to (8, 17) cleared the path to the eastern section.
- **Victory Road 1F Central Path:** SOLVED. Pushing the boulder from (7, 17) to (8, 17) cleared the path to the eastern section.