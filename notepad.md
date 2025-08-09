# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.

# II. Tile Mechanics (Verified)
- `ground`: Walkable tile.
- `grass`: Tall grass where wild Pokémon appear. Walkable like `ground`.
- `elevated_ground`: Walkable ground at a higher elevation. Movement to/from `ground` tiles requires `steps` or a one-way `ledge` drop.
- **One-Way Drop:** It is possible to drop down from an `elevated_ground` tile to an adjacent `ground` tile.
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
  - Electric > Flying, Water, Rock/Ground
  - Water > Rock/Ground, Fire
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
- **Trust System Over Tools:** If the system validation check insists a path is reachable while my tools (`pathfinder`, `landmass_analyzer`) say it is not, the system is correct and my tools are flawed. The immediate priority becomes debugging the tool, not continuing to test hypotheses based on the tool's flawed output.

# VI. Current Strategy & Plans
## Victory Road 1F Navigation
- **Goal:** Reach the ladder to Victory Road 2F at (2, 2).
- **Status:** The direct path is blocked by a boulder barrier at (10, 13). The western boulder puzzle is solved.
- **Eastern Boulder Puzzle - FAILED ATTEMPT 1:**
  - **Conclusion:** My previous plan was flawed. I pushed the boulder to (17, 14), but the tile required to push it onto the switch at (18, 14) is (16, 14), which is an impassable wall. The boulder is now in an unsolvable position.
  - **New Plan:**
    1. Reset the puzzle by leaving and re-entering Victory Road 1F via the entrance warp at (9, 18).
    2. Re-approach the eastern puzzle with the boulder reset to its original position of (11, 15).
    3. Devise a new solution that accounts for the impassable tile at (16, 14).

# VII. Future Development Ideas
- **puzzle_strategist_agent:** Recreate an agent to solve complex boulder puzzles. It would take the map state (boulders, switches, player position, target) and output an optimal sequence of pushes and movements. This would automate the most complex part of navigating puzzle-heavy areas like Victory Road.