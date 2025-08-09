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
- **Analysis:** My previous hypotheses were flawed. Hypothesis #2 (Eastern Boulder) is impossible due to circular logic (the path to the boulder is blocked by the barrier it's supposed to open). Hypothesis #1 (Western Boulder) was incorrectly dismissed as a "dead end." The path it opens to 2F is likely the next step in a multi-floor solution.
- **Hypothesis (Attempt #3):** The puzzle requires actions on multiple floors. Pushing the western boulder at (3, 11) south to (3, 10) grants access to the ladder to 2F. An action on 2F will then open the main barrier at (10, 13) on 1F.
- **Test Plan:**
    1. Navigate to (3, 12).
    2. Push the boulder at (3, 11) south to (3, 10).
    3. Navigate to the ladder at (2, 2) and ascend to Victory Road 2F.
    4. Explore 2F for a mechanism (e.g., a new boulder/hole puzzle) that affects the 1F barrier.

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

# VI. Tool Development Status
- **`pathfinder`:** RELIABLE. The tool's logic is sound. Previous failures were due to a misunderstanding of the game state (blocked paths), not a bug in the code.
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