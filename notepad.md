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
- Start: Turn #34032.
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Original Boulder Positions (Reset): Boulder 6 (3, 3), Boulder 7 (6, 1), Boulder 8 (8, 14).
- Strategy: Use manual steps.
- Current Status: Strength active. Moving to (8, 15) to push Boulder 8 Up.
- Puzzle Start Turn: 34032.

# Manual Puzzle Plan
## Boulder 7 (6, 1) -> Pit (8, 3)
1. Push Right to (7, 1), then Right to (8, 1), then Right to (9, 1).
2. Move to (9, 2), push Left. B7 to (8, 2).
3. Move to (8, 1), push Down. B7 to (8, 3) PIT.

## Boulder 8 (8, 14) -> Pit (8, 7)
1. Move to (8, 15), push Up. B8 to (8, 13).
2. Move to (9, 13), push Left. B8 to (7, 13).
3. Move to (8, 13), push Left. B8 to (6, 13).
4. Push Up all the way to (6, 7).
5. Move to (5, 7), push Right to (7, 7).
6. Move to (6, 7), push Right. B8 to (8, 7) PIT.

## Boulder 6 (3, 3) -> Pit (2, 5)
1. Reach left side via ladder at (1, 7).
2. Plan TBD once on-site.

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