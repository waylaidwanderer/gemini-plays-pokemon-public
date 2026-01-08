# Blackthorn Gym 2F Puzzle
## Current Boulder Positions (Post-Reset)
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Tile Mechanics (2F)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Target for boulders; player falls to 1F. Moving a boulder onto this tile removes the boulder and fills the hole on 1F.
- LADDER: Warp to 1F; resets boulder positions.
- NPC: Impassable (WALL).

## Verified Path for B8 (8, 11) to P3 (8, 7)
1. Push B8 Up to (8, 10). Player at (8, 11).
2. Push B8 Right to (9, 10). Player at (8, 10).
3. Push B8 Up to (9, 9). Player at (9, 10).
4. Push B8 Up to (9, 8). Player at (9, 9).
5. Push B8 Up to (9, 7). Player at (9, 8).
6. Push B8 Left to (8, 7) (PIT). Player at (9, 7).

## Strategic Insights
- Gap at (9, 10): Allows B8 to bypass the wall at (8, 9).
- Strength Status: ACTIVE (Turn 35063).

## Lessons Learned
- (7, 10) and (7, 11) are definitely WALLS.
- (8, 9) is a WALL.
- Visuals are deceptive; trust the 'type' attribute and movement tests.
- Strength must be reactivated after changing floors.