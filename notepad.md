# Blackthorn Gym 2F Puzzle
- Status: Strength ACTIVE (Turn 35113)

## Tile Mechanics (BlackthornGym2F)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Target for boulders. (8,3), (2,5), (8,7).
- LADDER: Warp to 1F. Resets boulders.
- NPCs: Act as walls.

## Current Boulder Positions
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

## Strategic Plan
1. Trust Game State collision types (WALL, FLOOR) as absolute truth.
2. Use run_code to solve for each boulder individually to identify specific reachability bottlenecks.
3. Verify player reachability to the right side of B8 at (9, 11) and (9, 10).
4. Execute the resulting sequence.

## Lessons Learned
- Trust Game State: Collision types in Game State are the absolute truth.
- Strength: Reactivate after floor changes.
- Boulder Reset: Boulders reset to starting positions when changing maps via ladder.
- Reachability: The player can cross between the left and right sides via gaps at Y=1 and Y=13.