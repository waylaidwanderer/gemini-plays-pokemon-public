# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable. Statues and pillars are solid.
- PIT: Warp to same coordinates on 1F. Filled by pushing a boulder into it.
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- BOULDER: Pushable object. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): P0 (2, 5), P1 (8, 3), P2 (8, 7).
- Original Boulder Positions: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Mechanics: Pushing a boulder moves it one tile. The player MOVES into the boulder's previous position. Boulders cannot be pushed into NPCs.
- Reset: Leaving the floor (via ladder or pit) and returning resets all boulder positions to their original coordinates.

# Strategy & Progress
- Lead Pokémon: Calcifer (Typhlosion, Lv49).
- Gym Leader Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Current Task: Solving the puzzle using the refined solver tool from the reset state.

# Obstacles & Solutions
- Blackthorn Gym Pit Shifts (2F -> 1F):
  - (8, 3) -> (7, 6)
  - (2, 5) -> (2, 6)
  - (8, 7) -> (7, 7)