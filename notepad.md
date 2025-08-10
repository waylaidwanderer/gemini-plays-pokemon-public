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
- **Puzzle Hypothesis Testing:** Before attempting complex puzzles, I will use `landmass_analyzer` and `boulder_puzzle_solver` to test connectivity and puzzle state. If the tool's output conflicts with reality, I must trust reality and conclude my tool is flawed. The immediate priority becomes debugging the tool.
- **Judicious Agent Use:** I must exercise my own judgment for simple, obvious situations and avoid calling agents unnecessarily. The agent is a tool for complex strategic analysis, not a replacement for basic game sense.
- **Verify All Exits:** Before concluding I am trapped or soft-locked, I must use my pathfinding tool to test routes to ALL available exits (ladders, warps, map connections) on the current map.
- **Pre-emptive Path Planning:** For boulder puzzles, I must use my pathfinding and puzzle analysis tools to verify the entire sequence of pushes *before* I start moving anything to avoid soft-locking myself.
- **Mindful Gameplay:** I must be more vigilant in basic gameplay checks, as the failure to activate Strength caused a significant and unnecessary delay.

# V. Agent & Tool Development
- **Goal Prioritizer Agent:** An agent that could take my current state (location, party, goals) and suggest the most logical next objective.
- **Puzzle Analyzer Agent:** An agent that could take a description of a puzzle and suggest a high-level strategy or identify potential deadlocks.

# VI. Puzzle Solving Log
## Victory Road 1F - East Boulder Puzzle
- **Hypothesis #1 (FAILED):** The boulder at (6, 16) can be pushed to the switch at (18, 14).
  - **Test:** Attempted to generate a path for the player to execute the boulder push sequence.
  - **Conclusion:** FAILED. The path requires the player to stand on a tile that is impassable, making the push sequence impossible. This boulder is not the solution for this switch.
- **Hypothesis #2 (VIABLE):** The boulder at (3, 11) can be pushed to the switch at (18, 14).
  - **Test:** Used `generate_path_plan` to simulate the boulder's movement path, ignoring other boulders as obstacles.
  - **Conclusion:** CONFIRMED. A valid path exists for this boulder to reach the switch.
- **Hypothesis #3 (FAILED):** The boulder at (15, 3) can be pushed to the switch at (18, 14).
  - **Test:** Used `generate_path_plan` to simulate the boulder's movement path.
  - **Conclusion:** FAILED. No path exists for this boulder to reach the switch.