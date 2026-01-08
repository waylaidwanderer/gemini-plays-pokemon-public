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
- Mechanics: Pushing a boulder moves it one tile. The player STAYS in their original position. Verified in Turns 34280 and 34303. Boulders cannot be pushed into NPCs.
- Reset: Leaving the floor (via ladder or pit) and returning resets all boulder positions to their original coordinates.

# Strategy & Progress
- Lead Pokémon: Calcifer (Typhlosion, Lv49).
- Gym Leader Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Strategy for Training (Route 45): Grind wild encounters in tall grass until Xenon and Kimchi reach Lv40. Use Max Repel to avoid weak encounters if needed.

# Obstacles & Solutions
- Blackthorn Gym Pit Shifts (2F -> 1F):
  - (8, 3) -> (7, 6)
  - (2, 5) -> (2, 6)
  - (8, 7) -> (7, 7)

# Puzzle Testing Log
- Turn 34358: Testing walkability of (9, 17). If walkable, B8 can be pushed from Column 8 to the Column 6 artery via Row 17.
- Verified WALLS: (4,3), (4,4), (4,5), (5,0), (6,3), (7,11), (9,13).
- Cody (4, 1) is a solid obstacle for boulders.