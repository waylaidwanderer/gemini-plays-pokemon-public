# Blackthorn Gym 2F Puzzle
## Current Boulder Positions (Post-Reset)
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Verified Path for B8 (8, 14) to P3 (8, 7)
1. Push B8 Up to (8, 13). Player at (8, 15).
2. Push B8 Up to (8, 12). Player at (8, 14).
3. Push B8 Up to (8, 11). Player at (8, 13).
4. Push B8 Up to (8, 10). Player at (8, 12).
5. Push B8 Left to (7, 10). Player at (9, 10).
6. Push B8 Left to (6, 10). Player at (8, 10).
7. Push B8 Up to (6, 9). Player at (6, 11).
8. Push B8 Up to (6, 8). Player at (6, 10).
9. Push B8 Up to (6, 7). Player at (6, 9).
10. Push B8 Right to (7, 7). Player at (5, 7).
11. Push B8 Right to (8, 7) (PIT). Player at (6, 7).

## Tile Mechanics (2F)
- FLOOR: Traversable. (7, 10), (7, 12), (7, 13) are verified FLOOR.
- WALL: Impassable. (8, 9), (7, 11), (7, 14), (7, 15) are verified WALL.
- PIT: Target for boulders; player falls to 1F. Moving a boulder onto this tile removes the boulder and fills the hole on 1F.
- LADDER: Warp to 1F; resets boulder positions.
- NPC: Impassable (WALL).

## Lessons Learned
- Step 1 for B8 in previous plan was impossible because (9, 14) is a WALL.
- Visual inspection of walls is unreliable; must test with player movement or use Game State.
- Checkerboard walls: (7, 10) FLOOR, (7, 11) WALL, (7, 12) FLOOR, (7, 13) FLOOR.