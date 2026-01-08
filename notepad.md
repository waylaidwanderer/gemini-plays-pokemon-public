# Blackthorn Gym 2F Puzzle
- Puzzle Started: Turn 35022
- Status: Strength ACTIVE (Turn 35113)

## Tile Mechanics (BlackthornGym2F)
- FLOOR: Traversable.
- WALL: Impassable. (7,10), (7,11), (7,14), (8,9), (9,12), (9,13) are confirmed WALLS.
- PIT: Target for boulders. (8,3), (2,5), (8,7).
- LADDER: Warp to 1F. Resets boulders.
- NPCs act as walls. Testing Fran at (4,11).

## Current Boulder Positions
- B6 (ID 6): (3, 2) [Marker]
- B7 (ID 7): (6, 1) [Marker]
- B8 (ID 8): (8, 14) [Verified]

## Strategic Plan
1. Test if Fran at (4,11) is a solid obstacle.
2. Verify B6 at (3,2) and B7 at (6,1) after reset.
3. Run BFS solver with ALL verified data.
4. Execute push sequence.

## Lessons Learned
- Visuals are deceptive; trust the 'type' attribute in the Game State.
- Strength must be reactivated after changing floors.
- Boulder Reset: Boulders reset to starting positions when changing maps via ladder.