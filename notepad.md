# Blackthorn Gym 2F Puzzle
- Status: Strength ACTIVE (Turn 35113)

## Tile Mechanics (BlackthornGym2F)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Target for boulders. (8,3), (2,5), (8,7).
- LADDER: Warp to 1F. Resets boulders.
- NPCs: Act as walls.

## Confirmed Walls (Verified by movement)
- (7, 10), (7, 11), (7, 14), (8, 9), (9, 12), (9, 13).

## Current Boulder Positions
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

## Strategic Plan
1. Re-verify player reachability to the right side (Column 7-9) via the gap at (4, 13).
2. Use solve_boulders_v2 with the absolute truth from Game State (no 'fake wall' hunting).
3. If solve_boulders_v2 returns no buttons, investigate why the BFS is failing (e.g., player reachability to push tiles).

## Lessons Learned
- Trust Game State: Collision types (WALL, FLOOR) in Game State are the absolute truth.
- Strength: Reactivate after floor changes.
- Boulder Reset: Boulders reset when changing maps via ladder.