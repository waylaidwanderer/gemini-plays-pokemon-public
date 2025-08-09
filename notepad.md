# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.
- **Follower Pokémon Mechanics:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions. The first button press turns to face, the second moves.

# II. Tile Mechanics (Verified)
- `ground`: Walkable tile.
- `grass`: Tall grass where wild Pokémon appear. Walkable like `ground`.
- `water`: Crossable using HM Surf.
- `impassable`: Walls, rocks, statues, and sometimes objects like defeated trainers. Cannot be entered.
- `ledge`: Can only be traversed downwards from an adjacent tile above it.
- `steps`: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- `elevated_ground`: Walkable ground at a higher elevation. Movement to/from `ground` tiles requires `steps` or a one-way `ledge` drop.
- `cleared_boulder_barrier`: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground` and can function as a one-way ramp up.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `warp`: A tile that transports the player to another location, often a door or cave entrance.
- `ladder_down` / `ladder_up`: Warps between floors.
- `hole`: Warps the player (or a boulder) to the floor below.

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
- **Trust System Over Custom Analysis:** If the system validation check insists a path is reachable while my own analysis suggests it is not, the system is correct and my analysis is flawed. The immediate priority becomes re-evaluating my understanding of the map.
- **Falsify Assumptions:** I must actively try to disprove my own hypotheses, especially regarding navigation. If a path fails, I must verify connectivity before repeatedly attempting the same path. This helps avoid confirmation bias where I assume my tool is wrong instead of my assumption.

# VI. Current Strategy & Plans
## A. Strategy Pivot: Manual Puzzle Solving
- **Conclusion:** After multiple documented failures and refinements, the `puzzle_strategist_agent` has been deemed fundamentally flawed and unfixable for this type of complex, multi-level puzzle. It has been deleted.
- **New Mandate (Self-Imposed):** In accordance with the core directive to pivot from a failing strategy, I will now solve the Victory Road puzzles manually. I will use my reliable `landmass_analyzer` and `generate_path_plan` tools to break down puzzles into manageable sub-problems.
- **Immediate Task:** Solve the eastern boulder puzzle on 1F. This requires two steps:
  1. Clear the path by moving the boulder at (6, 16).
  2. Navigate to and solve the main puzzle by moving the boulder at (15, 3) to the switch at (18, 14).