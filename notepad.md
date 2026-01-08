# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- VOID: Impassable.
- PIT: Warp to same coords on 1F. Boulders fill gaps on 1F. Player must fall into them to warp.
- LADDER: Two-way warp between floors. (1,7) and (7,9) on 2F.
- BOULDER: Impassable. Pushable with Strength.
- NPCs: Impassable. Some may disappear after defeat (e.g., Mike at 6,8).

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Start Turn: 34032.
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Original Boulder Positions: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Strategy: Use BFS to find the exact sequence. Manual attempts have failed due to complex wall collisions.
- Verification Status:
  - Row 0: (5,0), (8,0) are WALLs (Verified).
  - Column 9: (9,13) is a WALL (Verified).
  - Column 4: (4,2) to (4,10) are WALLs.
  - Column 6: (6,2), (6,3), (6,4), (6,6) are WALLs.
- Current Status: Strength active. Standing at (8,13). Moving to Left side via (4,13).

# Pokemon & Party Information
## Training Session (Route 45)
- Start Turn: 33584.
- Goal: Kimchi (Lv33) and Xenon (Haunter, Lv36) to Lv40.
- Method: Kimchi holds Exp. Share. Lead Xenon.

# Obstacles & Solutions
- Accessing Route 45 East: Use Column 39 corridor in Blackthorn City. Entrance at (39, 8).
- Gym Navigation: Ladders (1,7) and (7,9) connect the two sides of the gym.
- Blackthorn Gym Pit Shifts:
  - 2F (8, 3) -> 1F (7, 6)
  - 2F (2, 5) -> 1F (2, 6)
  - 2F (8, 7) -> 1F (7, 7)
- Boulder 8 Plan: (8,14) -> (6,14) -> (6,7) -> (8,7) PIT. Requires Stand at (9,14), (8,14), (6,15-8), (5,7), (6,7).