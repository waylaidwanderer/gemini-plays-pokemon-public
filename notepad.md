# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable. Statues and pillars are solid.
- PIT: Warp to same coordinates on 1F. Filled by pushing a boulder into it.
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- BOULDER: Pushable object. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Start Turn: 34112
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): P0 (2, 5), P1 (8, 3), P2 (8, 7).
- Mechanics: Pushing a boulder moves it one tile. The player STAYS in their original position. Verified in Turns 34280 and 34303. Boulders cannot be pushed into NPCs, and NPCs block the player's movement.
- Reset: Leaving the floor (via ladder or pit) and returning resets all boulder positions to their original coordinates. Strength must also be reactivated each time.

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

# Puzzle Testing Log
- Turn 34369: Confirmed Fran (4, 11) blocks player movement. NPCs act as walls.
- Turn 34359: Confirmed (9, 17) is a solid WALL.