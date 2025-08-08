# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.

## A. Tile Mechanics (Verified)
- **`impassable`**: Walls, rocks. Cannot be entered.
- **`ground`**: Walkable tile.
- **`water`**: Crossable using HM Surf.
- **`elevated_ground`**: Walkable ground at a higher elevation. Cannot be stepped up to or down from `ground` tiles directly.
- **`steps`**: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- **`ladder_down` / `ladder_up`**: Warps between floors.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable barrier linked to a boulder switch.
- **`cleared_boulder_barrier`**: A tile that becomes traversable after a boulder switch is activated.
- **`hole`**: Warps the player (or a boulder) to the floor below.
- **`ledge`**: Can only be traversed downwards.

## B. Follower Pokémon Mechanics
- **Pikachu Position Swap:** When moving onto a tile occupied by Pikachu, the player and Pikachu appear to swap positions.

# II. Puzzles & Navigation

## A. Puzzle Mechanics
- **Reset Condition:** Boulder puzzles reset upon leaving and re-entering a map or using ladders between floors.
- **Boulder/Item Interaction:** Pushing a boulder onto an item collects the item and moves the boulder into that space.

# III. Battle Intelligence
## A. Type Effectiveness Chart (OBSERVATION-ONLY)
- **Super Effective (2x damage):**
  - Electric > Flying
  - Water > Rock/Ground
  - Ground > Rock/Ground
- **Not Very Effective (0.5x damage):**
  - Normal !> Rock/Ground
- **Immune (0x damage):**
  - Ground immune to Electric

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Body Slam:** Can cause paralysis.

# IV. Methodology & Lessons Learned
## A. Tool Usage & Debugging
- **Revised Tool Failure Protocol:** If any tool fails (especially `pathfinder`): 1. Use `landmass_analyzer` to confirm physical connectivity. 2. If a path exists, add verbose logging to the failing tool. 3. Re-run the tool to generate a detailed log. 4. Analyze the log myself to identify the root cause. I am forbidden from using an agent for tool debugging.
- **Landmass Analyzer Limitations:** The `landmass_analyzer` tool now correctly accounts for boulders as obstacles, but it still does not understand one-way traversal tiles like ledges or `cleared_boulder_barrier` ramps.
- **Surfing Navigation:** The `pathfinder` tool requires `movement_mode='surfing'` to navigate over water.

# V. Current Puzzle Plan (Victory Road 3F)
- **Objective:** Get a boulder to the switch at (4, 6) to open the barrier at (8, 11).
- **Attempt 1 (Failed):** Followed a plan from `puzzle_strategist_agent` to move the boulder from (14, 13). The plan was flawed as it required moving through an impassable tile. This resulted in pushing the boulder to (14, 14), making the puzzle's current state unsolvable.
- **Plan:** Retreat from Victory Road 3F to reset the puzzle and heal my party. Then, re-attempt with a corrected agent.

# VI. Archived & Falsified Hypotheses
- [Previous hypotheses removed for clarity as per Overwatch critique.]

# VII. Self-Reflection Insights (Turn 126679)
- **Potential Confirmation Bias:** I may be overly focused on the boulder puzzles as the only path forward on Victory Road 3F. I have been neglecting the unvisited warp at (27, 9).
- **Contingency Plan:** If my current hypothesis about the multi-floor boulder puzzle proves false or gets stuck, my next action will be to investigate the warp at (27, 9) as a potential alternative route.