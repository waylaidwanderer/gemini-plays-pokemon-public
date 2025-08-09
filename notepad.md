# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.

# II. Tile Mechanics (Verified)
- `ground`: Walkable tile.
- `grass`: Tall grass where wild Pokémon appear. Walkable like `ground`.
- `elevated_ground`: Walkable ground at a higher elevation. Movement to/from `ground` tiles requires `steps` or a one-way `ledge` drop.
- `cleared_boulder_barrier`: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground`.
- `steps`: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- `ledge`: Can only be traversed downwards from an adjacent tile above it.
- `water`: Crossable using HM Surf.
- `impassable`: Walls, rocks. Cannot be entered.
- `ladder_down` / `ladder_up`: Warps between floors.
- `hole`: Warps the player (or a boulder) to the floor below.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `warp`: A tile that transports the player to another location, often a door or cave entrance.

# III. Puzzle Mechanics & Solutions
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.
- **Strength Push Mechanics:** When pushing a boulder, the player's character remains in place. The push is executed from an adjacent tile, and only the boulder moves.

## Current Puzzle: Victory Road 1F Main Barrier
- **Analysis (Correction):** My previous hypotheses were based on a hallucinated western boulder switch. The map data confirms there is only one switch on this floor, at (18, 14), which controls the single barrier at (10, 13). The most plausible boulder to use is the one located at (15, 3).
- **Hypothesis (Attempt #4):** Pushing the boulder from (15, 3) onto the switch at (18, 14) will clear the barrier at (10, 13), opening the path to the western side of the map and the ladder to 2F.
- **Test Plan:**
    1. Navigate to a position to push the boulder at (15, 3) south.
    2. Maneuver the boulder south and east until it rests on the switch at (18, 14).
    3. Verify that the barrier at (10, 13) has been cleared.
    4. Navigate through the now-open path to the ladder at (2, 2) and ascend to Victory Road 2F.

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
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds. This is a non-negotiable directive.
- **Agent & Tool Limitations:** The `landmass_analyzer` ignores boulders by design to check theoretical terrain connectivity. Its output does not account for the current puzzle state.
- **Hallucination & Verification:** I must be vigilant against hallucinating game elements or progress. All strategic elements must be verified against the map data before forming a hypothesis.
- **Trust Tool Failures:** A tool reporting 'no path found' is a strong indicator that my hypothesis about the path is wrong. I must use this to falsify my own beliefs and avoid confirmation bias, rather than immediately assuming the tool is broken. My failure on Victory Road 1F (Turns 129461-129485) was a direct result of ignoring this rule; I spent dozens of turns 'fixing' a correct tool because I refused to believe my navigation goal was on a separate landmass.

# VI. Tool Development Status
- **`pathfinder`:** RELIABLE. The tool's logic is sound. Recent failures were due to my own misinterpretation of the map layout (being on a disconnected platform), not a bug in the code. This was confirmed by re-reading the `landmass_analyzer` output.
- **`boulder_puzzle_solver`:** PASSED INITIAL TEST. The tool successfully provided a single-step solution to move a blocking boulder. Further testing on multi-step puzzles is required, but it is now considered provisionally reliable.
- **`battle_strategist_agent`:** RELIABLE. Consistently provides sound, turn-by-turn battle advice.

# VII. Future Development & Testing
- **Tool Idea: `long_range_planner`**
  - **Purpose:** Automate multi-map navigation.
  - **Function:** Takes a final destination (map ID and coordinates) as input. It would call the `pathfinder` to get to the first exit/warp, then upon arrival on the new map, call `pathfinder` again to the next warp, and so on, until the final destination is reached. This would streamline travel between distant cities or through complex multi-map dungeons.
- **Agent Idea: `multi_boulder_puzzle_agent`**
  - **Purpose:** Solve complex puzzles with multiple interacting boulders.
  - **Function:** Analyzes the map state (boulder positions, switch locations, barriers) and generates a full sequence of moves. This would be a high-level strategic agent, potentially calling the `boulder_puzzle_solver` tool for individual steps.
- **Hypothesis to Test:** After crossing the next water section on Route 23, I must use the `landmass_analyzer` to confirm that the new landmass connects all the way to the Victory Road entrance at (5, 32).