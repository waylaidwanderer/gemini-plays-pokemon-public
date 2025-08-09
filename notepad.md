# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.

# II. Tile Mechanics (Verified)
- `ground`: Walkable tile.
- `grass`: Tall grass where wild Pokémon appear. Walkable like `ground`.
- `elevated_ground`: Walkable ground at a higher elevation. Movement to/from `ground` tiles requires `steps` or a one-way drop.
- `cleared_boulder_barrier`: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground`.
- `steps`: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- `ledge`: Can only be traversed downwards.
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

## Solved Puzzles (Victory Road)
- **3F to 2F:** Pushed boulder from (14, 13) into hole at (14, 15).
- **2F Main Barrier:** Used boulder from 3F (landed at (5, 15)) and pushed it onto switch at (2, 17).
- **3F Main Barrier:** Pushed boulder from (23, 2) to switch at (4, 6).
- **2F Western Barrier:** The switch at (2, 17) is empty, but the barrier is already cleared. This puzzle is solved.

## Current Puzzle: Victory Road 1F
- **Key Insight (The True Path):** The `landmass_analyzer` has confirmed that the entire floor is one interconnected landmass. The path to the ladder at (2, 2) is possible from my current location. My `pathfinder` tool's logic is flawed.
- **Hypothesis:** The path involves using the steps at (6, 14) or (8, 8) to navigate between ground and elevated platforms.
- **Current Plan:**
    1. Fix the `pathfinder` tool by replacing its faulty traversal logic with the simpler, proven logic from the `landmass_analyzer`.
    2. Use the repaired tool to find the correct path to the ladder at (2, 2).

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
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task. My highest priority is maintaining the integrity of my tools.
- **Agent & Tool Limitations:**
    - The `landmass_analyzer` ignores boulders by design to check theoretical terrain connectivity. Its output does not account for the current puzzle state and should not be misinterpreted as a guarantee of a currently open path.
- **Hallucination & Verification:** I must be vigilant against hallucinating game elements. I previously based my strategy on a non-existent fourth boulder, a major error that drove my strategy for a significant period. All strategic elements must be verified against the map data before forming a hypothesis.

# VI. Tool Development & Refinement
- **`pathfinder` Status:** The tool is now fully functional. Critical bugs related to elevation changes, one-way drops, defeated trainers, and ledge traversal have been resolved. It can now reliably navigate complex multi-level maps.
- **`boulder_puzzle_solver` Status:** This tool is likely still unreliable. Its internal player reachability check may have inherited the same flawed traversal logic from the old `pathfinder`, causing it to generate impossible solutions or fail to find solutions that exist. This tool requires testing and refinement.

# VII. Future Development & Testing
- **Tool Idea:** Create a `long_range_planner` tool that can break down a long-distance navigation goal into a sequence of pathfinder calls with different movement modes (e.g., walking, then surfing, then walking again).
- **Hypothesis to Test:** After crossing the next water section on Route 23, I must use the `landmass_analyzer` to confirm that the new landmass connects all the way to the Victory Road entrance at (5, 32).