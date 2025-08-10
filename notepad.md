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
  - Ground > Fire, Electric, Rock, Ground (Confirmed super-effective vs Rock/Ground types)
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
- **Puzzle Hypothesis Testing:** Before attempting complex puzzles, I will use `landmass_analyzer` to test connectivity. If the tool's output conflicts with a system validation check, I must trust the validation check and conclude my tool is flawed or I've misinterpreted the situation. The immediate priority becomes debugging the tool or re-evaluating the map from a new perspective.
- **Judicious Agent Use:** I must exercise my own judgment for simple, obvious situations and avoid calling agents unnecessarily. The agent is a tool for complex strategic analysis, not a replacement for basic game sense.
- **Verify All Exits:** Before concluding I am trapped or soft-locked, I must use my pathfinding tool to test routes to ALL available exits (ladders, warps, map connections) on the current map.
- **Pre-emptive Path Planning:** For boulder puzzles, I must use my `generate_path_plan` tool to verify the entire sequence of pushes *before* I start moving anything to avoid soft-locking myself.
- **Mindful Gameplay:** I must be more vigilant in basic gameplay checks, as the failure to activate Strength caused a significant and unnecessary delay.

# V. Tool Development Notes & Ideas
- **Goal Prioritizer Agent:** An agent that could take my current state (location, party, goals) and suggest the most logical next objective.
- **Puzzle Analyzer Agent:** An agent that could take a description of a puzzle and suggest a high-level strategy or identify potential deadlocks.
- **Boulder Puzzle Solver Agent:** An agent that takes the output of the `boulder_puzzle_solver` tool and generates a step-by-step push plan.

# VI. Future Improvements & Data Gathering
- **Type Chart Granularity:** The current type chart sometimes conflates single and dual-type effectiveness (e.g., Ground vs Rock/Ground). I need to be more diligent in observing and recording matchups against single-type Pokémon to build a more precise and reliable chart.

# VII. Puzzle Solving Log
## Victory Road 1F - West Boulder Puzzle
- **Hypothesis #1:** Pushing the boulder at (3, 11) north onto the switch at (3, 10) will clear a path forward.
- **Test:** Moved to (3, 12) and pushed the boulder up.
- **Conclusion:** **FAILED.** The tile at (3, 10) is not a switch. The boulder is now blocking the path to the ladder. The puzzle must be reset.

## Victory Road 1F - Main Puzzle
- **Hypothesis #2:** Pushing the boulder at (6, 17) to the switch at (18, 14) will clear the barrier at (10, 13).
- **Test:** Pushed the boulder from (6, 17) eastward towards the switch.
- **Conclusion:** **FAILED.** Pushed the boulder into a corner at (17, 15), soft-locking the area. The puzzle must be reset.