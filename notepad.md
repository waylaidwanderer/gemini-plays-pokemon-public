# I. Core Gameplay & World Rules
- **Poison Damage:** Poisoned Pokémon in the party lose 1 HP every four steps taken outside of battle.
- **Fainted Pokémon can use HMs:** Confirmed that a fainted Pokémon can be selected to use a field move like Strength.

## A. Tile Mechanics (Verified)
- **`impassable`**: Walls, rocks. Cannot be entered.
- **`ground`**: Walkable tile.
- **`water`**: Crossable using HM Surf.
- **`elevated_ground`**: Walkable ground at a higher elevation. One-way drops to adjacent `ground` tiles below are possible.
- **`steps`**: Connects `ground` and `elevated_ground` tiles, allowing vertical movement between them.
- **`ladder_down` / `ladder_up`**: Warps between floors.
- **`boulder_switch`**: Floor switch for boulders.
- **`boulder_barrier`**: Impassable barrier linked to a boulder switch.
- **`cleared_boulder_barrier`**: A tile that becomes traversable after a boulder switch is activated. Acts like `elevated_ground`.
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
  - Flying immune to Ground

## B. Strategic Notes & Mechanics
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Struggle Mechanic:** Used automatically only when a Pokémon is out of PP for ALL moves.
- **Full Heal:** Cures status conditions only, does not restore HP.
- **Body Slam:** Can cause paralysis.

# IV. Methodology & Lessons Learned
## A. Tool Usage & Debugging
- **Revised Tool Failure Protocol:** If any tool fails (especially `pathfinder`): 1. Use `landmass_analyzer` to confirm physical connectivity. 2. If a path exists, add verbose logging to the failing tool. 3. Re-run the tool to generate a detailed log. 4. Analyze the log myself to identify the root cause. I am forbidden from using an agent for tool debugging.
- **Landmass Analyzer Limitations:** The `landmass_analyzer` tool does not understand one-way traversal tiles like ledges or elevation drops.
- **Surfing Navigation:** The `pathfinder` tool requires `movement_mode='surfing'` to navigate over water.

# V. Current Objective: Solve Victory Road 2F Puzzle
- **CRITICAL FAILURE:** My `pathfinder` tool is critically bugged and has failed repeatedly, preventing progress. I have been stuck in a failure loop trying to fix it.
- **MANDATORY NEXT STEP:** My absolute highest priority is to fix the `pathfinder` tool. The latest attempt involves a complete overhaul of the traversal logic to a 'default-deny' system.
- **Puzzle State:** Once the tool is fixed, the objective is to solve the puzzle. The empty switch is at (10, 17). Available boulders are at (5, 15) and (6, 6).

# VI. Archived & Falsified Hypotheses
- **Victory Road 3F Puzzle:** Attempted a solution from `puzzle_strategist_agent` which proved to be flawed, resulting in an unsolvable puzzle state. Confirmed unsolvable by the corrected agent, necessitating a retreat to reset the puzzle.

# VII. Self-Reflection Insights (Turn 126679)
- **Potential Confirmation Bias:** I may be overly focused on the boulder puzzles as the only path forward. I have been neglecting other potential routes, like the unvisited warp at (27, 9) on Victory Road 3F.
- **Contingency Plan:** If I get stuck on a puzzle, my next action will be to investigate alternative routes like unvisited warps.