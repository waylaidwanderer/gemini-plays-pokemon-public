# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable. (Visual confirmation: pillars at (7, 10), (7, 11), etc. are solid walls).
- PIT: Warp to same coordinates on 1F. Can be filled by pushing a boulder into it.
- LADDER: Two-way warp between floors. Located at (1, 7) and (7, 9).
- BOULDER: Pushable object requiring STRENGTH. Acts as a wall for movement.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Original Boulder Positions: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Puzzle Status [Turn 34262]: Boulder 8 was soft-locked at (8, 10). Arrived on 1F via ladder at (7, 9) to reset. Returning to 2F.

# Puzzle Reset Strategy
- To reset boulder positions, leave the map (via ladder or pit) and return.
- Current Reset Path: Exit via ladder at (7, 9).

# Pokemon & Party Information
## Strategy for Gym Leader Clair
- Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Tactical Plan: Lead Calcifer (Typhlosion, Lv49). Use `battle_advisor_v2`.

# Obstacles & Solutions
- Gym Navigation: Ladders (1,7) and (7,9) connect to 1F. Crossing at (4,13) connects Left/Right sides on 2F.
- Blackthorn Gym Pit Shifts:
  - 2F (8, 3) -> 1F (7, 6)
  - 2F (2, 5) -> 1F (2, 6)
  - 2F (8, 7) -> 1F (7, 7)