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
- Mechanics: Pushing a boulder moves it one tile. The player STAYS in their original position. Boulders cannot be pushed into NPCs, but the player can walk through them.
- Reset: Leaving the floor (via ladder or pit) and returning resets all boulder positions to their original coordinates.

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36).
- Gym Leader Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Strategy for Training (Route 45): Grind wild encounters in tall grass until Xenon and Kimchi reach Lv40. Focus on high-experience targets and use Max Repel to skip low-level encounters.

# Puzzle Testing Log
- Turn 34368: Testing if player can walk through NPCs (Fran at 4,11).
- Turn 34368: Testing if pillars at (8,9) and (8,8) are walkable.

# Obstacles & Solutions
- Blackthorn Gym Pit Shifts (2F -> 1F):
  - (8, 3) -> (7, 6)
  - (2, 5) -> (2, 6)
  - (8, 7) -> (7, 7)