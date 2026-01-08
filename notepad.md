# Blackthorn Gym 2F Puzzle
- Puzzle Started: Turn 35022
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
1. Run deep BFS diagnostic to identify which NPC or wall is the bottleneck (using run_code).
2. Verify if Trainers (Cody, Fran, Lola, Paul) move or can be bypassed.
3. Execute the resulting push sequence once a valid path is found.

## Lessons Learned
- Trust Game State: 'WALL' and 'FLOOR' labels are the source of truth; do not hunt for 'fake' tiles.
- Boulder Reset: Changing maps via ladder resets all boulders to starting positions.
- Reachability: The player can cross between the left and right sides via gaps at Y=1 and Y=13.