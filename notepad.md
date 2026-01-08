# Tile Mechanics
- FLOOR: Walkable.
- WALL: Impassable.
- VOID: Impassable.
- PIT: Fall to 1F. Boulders fill gaps.
- LADDER: Move between floors.
- BOULDER: Pushable with Strength.
- NPCs: Walls.

# Game Mechanics & Systems
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Current Boulder Positions: Boulder 6 (3, 3), Boulder 7 (6, 1), Boulder 8 (8, 14).
- Strategy: Solve boulders manually or with `solve_gym_puzzle`.
- Current Status: Strength reset after falling. Facing Boulder 7 at (6, 1) from (5, 1).

# Pokemon & Party Information
## Training Session (Route 45)
- Start: Turn #33584.
- Goal: Kimchi (Lv33) and Xenon (Haunter, Lv36) to Lv40.
- Method: Kimchi holds Exp. Share. Lead Xenon.

# Exploration Strategy
- Boulder 7 (6, 1) Plan: Push Right to (7, 1), then maneuver to push into (8, 3).
- Boulder 6 (3, 3) Plan: Use ladder at (1, 7) from 1F to reach the left side.

# Obstacles & Solutions
- Accessing Route 45 East: Use Column 39 corridor in Blackthorn City. Entrance at (39, 8).
- Gym Navigation: Row 1 and Ladder (1, 7) are key connections.
- WARP_CARPET_DOWN: Standard exit warp.
- Blackthorn Gym Pit Shifts:
  - 2F (8, 3) -> 1F (7, 6)
  - 2F (2, 5) -> 1F (2, 6)
  - 2F (8, 7) -> 1F (7, 7)