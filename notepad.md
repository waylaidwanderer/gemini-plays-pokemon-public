# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable. (0,0)-(9,0), (4,2)-(4,10), (6,2)-(6,6), (9,13) verified.
- VOID: Impassable.
- PIT: Warp to same coords on 1F. Boulders fill gaps on 1F. Player must fall into them to warp.
- LADDER: Two-way warp between floors. (1,7) and (7,9) on 2F.
- BOULDER: Impassable. Pushable with Strength.
- NPCs: Impassable walls. Cody (4,1) persists after defeat.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Original Boulder Positions: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Strategy: Use BFS to find the exact sequence.

# Pokemon & Party Information
## Training Session (Route 45)
- Goal: Kimchi (Lv33) and Xenon (Haunter, Lv36) to Lv40.
- Method: Kimchi holds Exp. Share. Lead Xenon.

# Obstacles & Solutions
- Accessing Route 45 East: Use Column 39 corridor in Blackthorn City. Entrance at (39, 8).
- Gym Navigation: Ladders (1,7) and (7,9) connect to 1F. Crossing at (4,13) connects Left/Right sides on 2F.
- Blackthorn Gym Pit Shifts:
  - 2F (8, 3) -> 1F (7, 6)
  - 2F (2, 5) -> 1F (2, 6)
  - 2F (8, 7) -> 1F (7, 7)