# Blackthorn Gym 2F Puzzle
- Status: Strength ACTIVE (Turn 35113)

## Tile Mechanics (BlackthornGym2F)
- FLOOR: Traversable. Collision type is absolute truth.
- WALL: Impassable. Trust Game State 'type' attribute.
- PIT: Target for boulders. (8,3), (2,5), (8,7).
- LADDER: Warp to 1F. Resets boulders.
- NPCs: Currently at (4,1), (4,11), (9,2), (1,15). They act as solid obstacles.

## Current Boulder Positions
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

## Strategic Plan
1. Talk to Fran at (4, 11) to see if she moves or is non-solid.
2. Talk to Cody at (4, 1) to see if he moves.
3. If trainers are solid, re-examine the central wall (Column 4) for hidden gaps.
4. Use solve_boulders_v2 once reachability is confirmed.

## Lessons Learned
- Trust Game State: 'WALL' and 'FLOOR' labels are the source of truth; do not hunt for 'fake' tiles.
- Boulder Reset: Changing maps via ladder resets all boulders to starting positions.
- Reachability: The player can cross between the left and right sides via gaps at Y=1 and Y=13.