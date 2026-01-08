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
1. Use 1F ladders to re-examine reachability to different sections of 2F.
2. Verify if there is a third ladder on 1F leading to a restricted area on 2F.
3. Stop 'wall auditing' and trust Game State data.
4. Once reachability is understood, use solve_boulders_v2.

## Lessons Learned
- Trust Game State: 'WALL' and 'FLOOR' labels are the source of truth.
- Boulder Reset: Changing maps via ladder resets all boulders.
- Reachability: Current analysis suggests B8 (8,14) is blocked from all pits on 2F. Investigation on 1F required.