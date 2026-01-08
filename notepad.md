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
- Start Turn: 34032.
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Original Boulder Positions (Reset): Boulder 6 (3, 3), Boulder 7 (6, 1), Boulder 8 (8, 14).
- Strategy: Use manual steps or `gem_solve_gym_puzzle`.

# Pokemon & Party Information
## Training Session (Route 45)
- Start: Turn #33584.
- Goal: Kimchi (Lv33) and Xenon (Haunter, Lv36) to Lv40.
- Method: Kimchi holds Exp. Share. Lead Xenon.

# Manual Puzzle Plan
## Boulder 7 (6, 1) -> Pit (8, 3)
1. Push Right to (7, 1). [Done]
2. Stand at (6, 1), push Right to (8, 1).
3. Push Right to (9, 1).
4. Move to (9, 2), push Left to (8, 2).
5. Move to (8, 1), push Down to (8, 3) PIT.
Wait, Step 4/5: If Row 0 is blocked, I can't push Down from (8,1).
Hypothesis: Row 0 is WALKABLE, or my plan is flawed. Testing (5,0) was blocked.

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
- Plan: Solve B7 first.