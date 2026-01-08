# Blackthorn Gym 2F Puzzle
- Puzzle Started: Turn 35022
- Status: Strength ACTIVE (Turn 35113)

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Target for boulders; player falls to 1F. Boulders fill them to create paths on 1F.
- LADDER: Warp to 1F. Resets boulder positions on 2F.
- NPCs act as walls.

## Current Boulder Positions
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Strategic Plan
1. Fix solve_boulders_v2 to handle Blackthorn Gym 2F correctly.
2. Verify if (7, 11) is FLOOR by attempting to move Up from (7, 12).
3. If (7, 11) is FLOOR, use solve_boulders_v2 to find the push sequence.
4. Execute the sequence.

## Lessons Learned
- Visuals are deceptive; trust the 'type' attribute in the Game State.
- Strength must be reactivated after changing floors.
- Boulder Reset: Boulders reset to starting positions when changing maps via ladder.