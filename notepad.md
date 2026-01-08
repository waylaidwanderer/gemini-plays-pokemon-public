# Blackthorn Gym 2F Puzzle
- Status: Strength ACTIVE (Turn 35113)

## Tile Mechanics (BlackthornGym2F)
- FLOOR: Traversable. Collision type is absolute truth.
- WALL: Impassable. Trust Game State 'type' attribute.
- PIT: Target for boulders. (8,3), (2,5), (8,7).
- LADDER: Warp to 1F. Resets boulders.
- NPCs: Currently at (4,1), (4,11), (9,2), (1,15). They act as solid obstacles.

## Current Boulder Positions (2F)
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

## Strategic Plan
1. Talk to Gym Leader Clair on 1F to see if she battles or provides a hint.
2. Re-examine 1F layout for clues about boulder-pit pairings.
3. Use solve_boulders_v2 with absolute truth from Game State once reachability is understood.

## Lessons Learned
- Trust Game State: 'WALL' and 'FLOOR' labels are the source of truth; visuals can be deceptive.
- Boulder Reset: Changing maps via ladder resets all boulders.
- Reachability: The player can reach Clair on 1F by walking around the right edge (Column 9).