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
- **Pathfinding Verification:** When `pathfinder` reports no path, it is a strong indicator of a genuine barrier, not a tool bug. The `landmass_analyzer` tool should be used to confirm physical connectivity before assuming the pathfinder is flawed.
- **Agent Limitations:** The `puzzle_strategist_agent` cannot inherently understand disconnected map sections. It must be given explicit `analysis_bounds` to focus on a specific, connected area.

## B. Future Tool/Agent Ideas
- **`multi_map_navigation_strategist`:** An agent that could analyze `landmass_analyzer` output to determine if a multi-floor detour is necessary to reach a target on a different landmass.

# V. Current Objective: Solve Victory Road 3F Puzzle
- **Current Hypothesis:** The map is divided into two sections. To proceed, I must first solve the western boulder puzzle (switch at (4, 6)) to open the barrier at (8, 11). This requires navigating to the western section via a detour through Victory Road 2F.
- **Puzzle State:** The western switch is at (4, 6) and the boulder is at (14, 13). The eastern puzzle involves a hole at (24, 16) and is likely the solution for the 2F puzzle.

# VI. Archived & Falsified Hypotheses
- **Victory Road 3F Puzzle:** Attempted a solution from `puzzle_strategist_agent` which proved to be flawed, resulting in an unsolvable puzzle state. Confirmed unsolvable by the corrected agent, necessitating a retreat to reset the puzzle.