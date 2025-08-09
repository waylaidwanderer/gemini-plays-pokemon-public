# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.

# II. Tile Mechanics (Verified)
- `ground`: Walkable tile.
- `grass`: Tall grass where wild Pokémon appear. Walkable like `ground`.
- `elevated_ground`: Walkable ground at a higher elevation. Movement to/from `ground` tiles requires `steps` or a one-way `ledge` drop.
- `cleared_boulder_barrier`: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground` and can function as a one-way ramp up.
- `steps`: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- `ledge`: Can only be traversed downwards from an adjacent tile above it.
- `water`: Crossable using HM Surf.
- `impassable`: Walls, rocks, and sometimes objects like defeated trainers. Cannot be entered.
- `ladder_down` / `ladder_up`: Warps between floors.
- `hole`: Warps the player (or a boulder) to the floor below.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `warp`: A tile that transports the player to another location, often a door or cave entrance.

# III. Puzzle Mechanics & Solutions
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Strength Push Mechanics:** The push is executed from an adjacent tile, and only the boulder moves.

## Current Puzzle: Victory Road 1F
- **Hypothesis 1 (Failed):** Pushing the boulder at (15, 3) onto the switch at (18, 14) will clear the barrier at (10, 13).
  - **Conclusion:** This requires accessing the eastern elevated platform, which is currently blocked.
- **Hypothesis 2 (Failed):** The boulder at (3, 10) can be pushed UP to clear a path.
  - **Conclusion:** The tile at (3, 9) is impassable, blocking the push.
- **Current Hypothesis:** The only way forward is to ascend to 2F via the ladder at (2, 2) and find a path that loops back down to the eastern side of 1F.

# IV. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Electric > Flying, Water
  - Water > Rock/Ground
  - Ground > Rock/Ground, Fire, Electric, Rock
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock/Ground, Rock
- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Body Slam:** Can cause paralysis.

# V. Methodology & Lessons Learned
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion. This avoids chaotic, assumption-driven actions.
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds. This is a non-negotiable directive.
- **Trust Tool Failures:** A tool reporting 'no path found' is a strong indicator that my hypothesis about the path is wrong. I must use this to falsify my own beliefs and avoid confirmation bias, rather than immediately assuming the tool is broken. 
- **New Rule:** If `pathfinder` reports 'No path found', my first action MUST be to run `landmass_analyzer` to verify connectivity before attempting any debugging. This is to combat confirmation bias.

# VI. Tool Development Status
- **`pathfinder`:** **CRITICALLY FAILED & ABANDONED.** Multiple complete overhauls of the neighbor-finding logic have failed to produce a working tool. It is fundamentally broken and MUST NOT be used for navigation. All future pathing will be done manually until a full, systematic debugging effort can be undertaken. Relying on this tool is a waste of turns.
- **`battle_strategist_agent`:** RELIABLE. Consistently provides sound, turn-by-turn battle advice.

# VII. Future Development & Testing
- **Agent Idea: `puzzle_strategist_agent`**
  - **Purpose:** Provide optimal push sequences for boulder puzzles.
  - **Function:** Takes a grid layout, player position, boulder positions, and target switch position as input. It would output a sequence of moves to solve the puzzle.
- **Tool Idea: `puzzle_input_generator`**
  - **Purpose:** Automate the repetitive task of parsing the map XML to gather all necessary data for the `puzzle_strategist_agent`.