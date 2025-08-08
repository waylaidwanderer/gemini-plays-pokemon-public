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
- **Agent Limitations:** Reasoning-based agents (like `battle_strategist_agent`) are ill-suited for complex, state-based computational problems like boulder puzzles. These tasks require dedicated computational tools (`boulder_puzzle_solver`).
- **Strategic Flexibility:** Fixating on a single, stalled objective is inefficient. If multiple paths are available, and one is blocked by a difficult puzzle, exploring the alternate path is a better strategy than repeated failed attempts.
- **Tool Reliability:** A tool that produces an incorrect or impossible result is a critical failure. Tool maintenance and debugging must take precedence over any other gameplay action to ensure a reliable toolchain. The `ignored_object_types` logic in the pathfinder was a flawed shortcut that led to invalid paths; treating all NPCs as impassable is the correct approach.

# VI. Future Tool/Agent Ideas
- **`puzzle_master_agent`:** An agent to automate the entire puzzle-solving workflow: identify puzzle type, call the correct data extractor, call the solver, and parse the solution.

# VII. Victory Road Progression (Summary)
- **Multi-floor Puzzles:** The puzzles in Victory Road often require elements from multiple floors (e.g., pushing a boulder through a hole from 3F to solve a puzzle on 2F).
- **Solved Puzzles:**
  - **3F:** Pushed boulder from (14, 13) into hole at (14, 15). Pushed boulder from (18, 2) onto switch at (4, 6).
  - **2F:** Used boulder from 3F (landed at (5, 15)) and pushed it onto switch at (2, 17) to clear the main progression barrier. Another puzzle for an optional item remains.
- **Current Puzzle (1F):** I am in the western section, where the path to the exit is blocked by a local puzzle (boulder at (3, 11), switch at (3, 10)). The eastern puzzle (boulder at (15, 3), switch at (18, 14)) is on a separate, currently inaccessible landmass.
- **Tool Maintenance is Priority One:** A tool that produces an incorrect or impossible result is a critical failure. Tool maintenance and debugging must take absolute precedence over any other gameplay action to ensure a reliable toolchain. I must not attempt to work around a broken tool; I must fix it immediately.