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
- `pathfinder`: **REPAIRED & VERIFIED.** The tool's logic has been proven correct. Previous failures were due to user error (hallucinated coordinates) and misunderstanding the map's disconnected layout. The tool is now considered reliable.

# VII. Agent Development Status
- `battle_strategist_agent`: **REFINED & VERIFIED.** The system prompt has been updated to be more conservative in its damage calculations. It now correctly identifies safe and efficient battle actions.

# VIII. Tool Development Plan
- **Boulder Puzzle Solver:** Plan to create a new agent/tool combo to solve boulder puzzles.
  - **`puzzle_input_generator` (Tool):** A tool that parses the `map_xml_string` to extract player position, boulder locations, switch locations, and the grid layout, formatting it into a JSON object.
  - **`puzzle_strategist_agent` (Agent):** An agent that takes the formatted JSON from the generator and returns a sequence of moves to solve the puzzle.

# IX. Current Puzzle Plan
## Victory Road 1F - Main Puzzle
- **Hypothesis 3 (Failed):** The switch at (3, 10) opened a different, previously unseen path.
  - **Test:** Explored the western elevated platform after activating the switch.
  - **Conclusion:** Failed. No new paths opened. The western puzzle appears to be self-contained.
- **Hypothesis 4 (Current):** The eastern boulder puzzle is independent and must be solved to proceed. I need to get onto the eastern platform to assess how to push the boulder at (15, 3) to the switch at (18, 14).