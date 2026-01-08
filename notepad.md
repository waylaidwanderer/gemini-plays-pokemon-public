# Blackthorn Gym 2F Puzzle
## Current Boulder Positions (Reset)
- B6 (ID 6): (3, 3)
- B7 (ID 7): (6, 1)
- B8 (ID 8): (8, 14)

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Strategic Plan
1. Reset performed at Turn 35073.
2. Audit Column 9 and Column 7 for gaps:
   - Test (9, 13) from (8, 13).
   - Test (7, 14) from (7, 13).
   - Test (7, 15) from (6, 15).
3. If a gap is found, map a new path for B8.
4. If no gaps, B8 must be pushed into the center via (4, 13) gap.

## Tile Mechanics (2F)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Target for boulders; player falls to 1F.
- LADDER: Warp to 1F; resets boulder positions.
- NPC: Impassable (WALL).

## Lessons Learned
- Boulder Trap: (8, 10) is a dead end because (8, 9) and (7, 10) are walls.
- Strength: Must be reactivated after changing maps or resetting.
- Visuals: Visual inspection is unreliable; trust movement tests.
- Resetting: Use the ladder at (7, 9) or (1, 7) if a boulder gets stuck.