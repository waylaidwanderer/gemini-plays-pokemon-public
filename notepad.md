# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable (statues, pillars, rocks).
- PIT: Warp to same coordinates on 1F. Filled by pushing a boulder into it.
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- BOULDER: Pushable object. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Start Turn: 34112 (Exploration), 34370 (Puzzle Implementation)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): P0 (2, 5), P1 (8, 3), P2 (8, 7).
- Mechanics: Pushing a boulder moves it one tile. The player STAYS in their original tile. Verified in Turns 34280, 34303, 34406, and 34432.
- Reset: Leaving the floor (via ladder or pit) resets all boulder positions. Strength must be reactivated (A to interact, B to close message, then walk into boulder).

## Original Boulder Positions (2F)
- Boulder 6: (3, 3)
- Boulder 7: (6, 1)
- Boulder 8: (8, 14)

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36).
- Gym Leader Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Strategy for Training (Route 45): Grind wild encounters in tall grass until Xenon and Kimchi reach Lv40. Focus on high-experience targets like Donphan and Gligar. Use Max Repel to skip low-level encounters if necessary.

# Obstacles & Solutions
- Blackthorn Gym Pit Shifts (2F -> 1F):
  - (8, 3) -> (7, 6)
  - (2, 5) -> (2, 6)
  - (8, 7) -> (7, 7)

# Lessons Learned
- Puzzle Mechanics: Always verify if the player moves or stays put after a push. In Blackthorn Gym, the player STAYS in their original tile. Verified in Turns 34280, 34303, 34406, and 34435.
- Map Analysis: Check for walls along the entire path of a boulder, not just the starting point. Boulder 8 at (8, 14) is blocked from a straight-up path to (8, 7) by walls at (8, 9).
- Tool Hygiene: If a solver tool returns an empty list or "No solution", verify the map XML data and the solver's logic immediately.