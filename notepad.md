# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.
- **Dig Field Move:** Can be used to escape caves, acting as an Escape Rope. This is a key anti-softlock mechanic.
- **Surf Mechanic:** To use Surf from a land tile, the player must be standing on a tile adjacent to the water AND be facing the water tile.

# II. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Electric > Flying, Water
  - Water > Rock/Ground, Fire
  - Ground > Fire, Electric, Rock, Ground
  - Ice > Ground, Grass, Flying, Dragon
  - Flying > Fighting, Grass, Bug
  - Fighting > Normal, Rock, Ice
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock
- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Body Slam:** Can cause paralysis.

# III. Puzzle Mechanics & Solutions
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.

# IV. Methodology & Lessons Learned
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion.
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds.
- **Puzzle Hypothesis Testing:** Before attempting complex puzzles, I will use my analysis tools to test connectivity and puzzle state. If the tool's output conflicts with reality, I must trust reality and conclude my tool is flawed. The immediate priority becomes debugging the tool.
- **Verify All Exits:** Before concluding I am trapped or soft-locked, I must use my pathfinding tool to test routes to ALL available exits (ladders, warps, map connections) on the current map.
- **Pre-emptive Path Planning:** For boulder puzzles, I must use my pathfinding and puzzle analysis tools to verify the entire sequence of pushes *before* I start moving anything to avoid soft-locking myself.
- **Mindful Gameplay:** I must be more vigilant in basic gameplay checks, as the failure to activate Strength caused a significant and unnecessary delay.
- **Puzzle Log Summarization:** After a puzzle is solved, the log should be updated to show only the successful path, moving detailed lessons to this Methodology section.

# V. Tile Mechanics & Traversal Rules
- **`ground` / `grass`:** Standard walkable tiles.
- **`impassable` / `unknown`:** Cannot be entered.
- **`cleared_boulder_barrier`:** Acts as a one-way ramp, allowing downward movement to adjacent `ground` tiles.
- **`boulder_barrier`:** An impassable wall that is removed when a corresponding `boulder_switch` is activated.
- **`boulder_switch`:** A floor switch that must have a boulder pushed onto it.
- **`steps`:** Allows vertical movement between `ground` and `elevated_ground`.
- **`elevated_ground`:** Walkable ground at a different elevation. Movement to `ground` is only possible via `steps`.
- **`ladder_up` / `ladder_down`:** Warps between floors.
- **Untested Mechanic:** It is unknown if a boulder can be pushed onto a `steps` tile.

# VI. Puzzle Solving Log
## Victory Road 1F - Boulder Puzzle
- **Current State:** The puzzle has been reset by leaving and re-entering the map.
- **Analysis:** The `boulder_puzzle_solver` tool has confirmed that only the boulder starting at (6, 16) has a valid, player-achievable path to the switch at (18, 14).
- **Hypothesis:** Solving the (6, 16) boulder puzzle will clear the barrier at (10, 13) and open the path to the ladder at (2, 2).

# VII. Future Development Ideas
- **Puzzle Plan Agent:** Create an agent that takes the output of the `boulder_puzzle_solver` and generates a human-readable, step-by-step plan for both player movement and boulder pushes.