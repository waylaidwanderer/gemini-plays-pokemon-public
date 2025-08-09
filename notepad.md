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

## Solved Puzzles (Victory Road)
- **3F to 2F:** Pushed boulder from (14, 13) into hole at (14, 15).
- **2F Main Barrier:** Used boulder from 3F (landed at (5, 15)) and pushed it onto switch at (2, 17).
- **3F Main Barrier:** Pushed boulder from (23, 2) to switch at (4, 6).
- **1F Boulder Puzzle:** Pushed boulder from (3, 11) to switch at (3, 10).

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
- **Tool Reliability & Immediate Action:** A tool that produces an incorrect or impossible result is a critical failure. I MUST fix it immediately with `define_tool` instead of deferring the task or attempting workarounds.
- **Agent & Tool Limitations:** The `landmass_analyzer` ignores boulders by design to check theoretical terrain connectivity. Its output does not account for the current puzzle state.
- **Hallucination & Verification:** I must be vigilant against hallucinating game elements (e.g., a non-existent fourth boulder). All strategic elements must be verified against the map data before forming a hypothesis.

# VI. Tool Development Status
- **`pathfinder`:** Currently UNRELIABLE. This tool has repeatedly failed to find valid paths on multi-level maps due to flawed elevation and traversal logic. It requires a fundamental rebuild or a completely new approach. Do not trust its output.
- **`boulder_puzzle_solver`:** UNTESTED. Its internal player reachability check may have inherited the same flawed traversal logic from the old `pathfinder`, causing it to generate impossible solutions or fail to find solutions that exist. This tool requires testing and refinement at the next opportunity.
- **`battle_strategist_agent`:** RELIABLE. Consistently provides sound, turn-by-turn battle advice.

# VII. Future Development & Testing
- **Tool Idea:** Create a `long_range_planner` tool that can break down a long-distance navigation goal into a sequence of pathfinder calls with different movement modes.
- **Hypothesis to Test:** After crossing the next water section on Route 23, I must use the `landmass_analyzer` to confirm that the new landmass connects all the way to the Victory Road entrance at (5, 32).