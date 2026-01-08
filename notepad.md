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
- Original Boulder Positions (Reset): Boulder 6 (3, 3), Boulder 7 (6, 1), Boulder 8 (8, 14).
- Strategy: Reactivate Strength at (8, 14), then use `solve_gym_puzzle` to determine the move sequence.
- Current Status: Strength reset after falling. Facing Right at (8, 13). Boulder 8 is at (8, 14).

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
- Observation: Column 8 is blocked by walls at (8, 8) and (8, 9). Boulder 8 cannot go Up Column 8.
- Observation: Column 5 is blocked by walls at (5, 10), (5, 12), (5, 16), (5, 17).
- Observation: Column 4 is a solid wall from (4, 2) to (4, 10).
- Plan: Reset room via ladder at (7, 9).