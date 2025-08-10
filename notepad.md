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
- **Strength Push Mechanics:** The push is executed from an adjacent tile. Pushing a boulder moves the player into the boulder's previous space.

## A. Tile Mechanics (Advanced/Uncommon)
- `cleared_boulder_barrier`: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground` and can function as a one-way ramp up.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `hole`: Warps the player (or a boulder) to the floor below.

# IV. Methodology & Lessons Learned
- **Hypothesis-Driven Approach:** I must form a single, testable hypothesis, document it, test it, and record the conclusion.
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds. I must be more meticulous in my debugging process.
- **Puzzle Hypothesis Testing:** Before attempting complex puzzles, I will use `landmass_analyzer` to test connectivity. However, if the tool's output conflicts with a system validation check (e.g., 'Dead End Area Mismatch'), I must trust the validation check and conclude my tool is flawed or I've misinterpreted the situation. The immediate priority becomes debugging the tool or re-evaluating the map from a new perspective, rather than blindly trusting the faulty analysis.
- **Judicious Agent Use:** I must exercise my own judgment for simple, obvious situations (like trivial wild battles) and avoid calling agents unnecessarily. The agent is a tool for complex strategic analysis, not a replacement for basic game sense.
- **Verify All Exits:** Before concluding I am trapped or soft-locked, I must use my pathfinding tool to test routes to ALL available exits (ladders, warps, map connections) on the current map. A path being blocked to one objective does not mean all paths are blocked.

# V. Tool Development Notes
- **Boulder Puzzle Solver Tool:** A specialized tool that can analyze the map and plan the correct sequence of boulder pushes would be highly valuable for complex puzzles like those in Victory Road. This should be prioritized for development.

# VI. Future Improvements & Data Gathering
- **Type Chart Granularity:** The current type chart sometimes conflates single and dual-type effectiveness (e.g., Ground vs Rock/Ground). I need to be more diligent in observing and recording matchups against single-type Pokémon to build a more precise and reliable chart.

# VII. Agent & Tool Ideas
- **Goal Prioritizer Agent:** An agent that could take my current state (location, party, goals) and suggest the most logical next objective. Could be useful in more open-ended sections of the game.
- **Puzzle Analyzer Agent:** An agent that could take a description of a puzzle (e.g., number of boulders, switches, barriers) and suggest a high-level strategy or identify potential deadlocks.

# VIII. Puzzle Solving Log
## Victory Road 1F - West Boulder Puzzle
- **Hypothesis #1:** Pushing the boulder at (3, 11) north onto the switch at (3, 10) will clear a path forward.
- **Test:** Move to (3, 12) and push the boulder up.