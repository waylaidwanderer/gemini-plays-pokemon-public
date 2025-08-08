# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.

# II. Tile Mechanics (Verified)
- **`ground`**: Walkable tile.
- **`elevated_ground`**: Walkable ground at a higher elevation. One-way drops to adjacent `ground` tiles below are possible.
- **`cleared_boulder_barrier`**: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground` and allows one-way drops.
- **`steps`**: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- **`ledge`**: Can only be traversed downwards.
- **`water`**: Crossable using HM Surf.
- **`impassable`**: Walls, rocks. Cannot be entered.
- **`ladder_down` / `ladder_up`**: Warps between floors.
- **`hole`**: Warps the player (or a boulder) to the floor below.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable barrier linked to a boulder switch.

# III. Puzzle Mechanics
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.

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
- **Pathfinding Verification:** When a pathfinding tool reports no path, it is a strong indicator of a genuine barrier, not a tool bug. The `landmass_analyzer` tool should be used to confirm physical connectivity before assuming the pathfinder is flawed.
- **Agent Limitations:** Reasoning-based agents (like `puzzle_strategist_agent`) are ill-suited for complex, state-based computational problems like boulder puzzles. These tasks require dedicated computational tools (`boulder_puzzle_solver`).
- **Strategic Flexibility:** Fixating on a single, stalled objective is inefficient. If multiple paths are available, and one is blocked by a difficult puzzle, exploring the alternate path is a better strategy than repeated failed attempts.
- **Tool Reliability:** A tool that produces an incorrect or impossible result is a critical failure. Tool maintenance and debugging must take precedence over any other gameplay action to ensure a reliable toolchain.

# VI. Future Tool/Agent Ideas
- **`puzzle_master_agent`:** An agent to automate the entire puzzle-solving workflow: identify puzzle type, call the correct data extractor, call the solver, and parse the solution.

# VII. Victory Road Puzzles
## A. Floor 1F
- **Objective:** Open barrier at (10, 13) by activating switch at (18, 14).
- **Hypothesis 1:** Use boulder at (15, 3). **Outcome:** `boulder_puzzle_solver` reported no path. Hypothesis denied.
- **Hypothesis 2:** Use boulder at (6, 16). **Outcome:** `boulder_puzzle_solver` reported no path. Hypothesis denied.
- **Conclusion:** Puzzle is likely unsolvable from 1F alone. Requires an element from another floor.
## B. Floor 2F
- **Objective:** Open barrier at (24, 15) by activating switch at (10, 17).
- **Hypothesis 1:** Use boulder at (6, 6). **Outcome:** `boulder_puzzle_solver` reported no path. Hypothesis denied.
- **Hypothesis 2:** Use boulder at (5, 15). **Outcome:** `boulder_puzzle_solver` reported no path. Hypothesis denied.
- **Conclusion:** Puzzle is unsolvable from 2F alone. Requires an element from another floor.
## C. Floor 3F
- **Objective:** Activate switch at (4, 6).
- **Directive:** Must solve from the current state. A mistake was made, pushing a boulder to an unsolvable position at (14, 14).
- **Plan:** Analyze all available boulders ((18, 2), (14, 14), (25, 11), (23, 16)) with `boulder_puzzle_solver` to find a valid path to the switch.