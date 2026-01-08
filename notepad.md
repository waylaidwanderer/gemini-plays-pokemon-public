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
1. Navigate to (8, 13) via the gap at (4, 13) to confirm player reachability to the right side.
2. Run solve_boulders_v2 with the absolute truth from Game State.
3. Execute the resulting push sequence.

## Lessons Learned
- Trust Game State: Collision types (WALL, FLOOR) in Game State are the absolute truth.
- Strength: Reactivate after floor changes.
- Boulder Reset: Boulders reset when changing maps via ladder.