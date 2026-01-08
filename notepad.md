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
2. Step 1: Solve B8 (8, 14) -> P3 (8, 7).
   - Hypothesis: Must use column 9 or column 7 gaps.
   - Verification needed: Check if (9, 13) or (9, 12) are actually traversable despite 'WALL' label.
3. Step 2: Solve B7 (6, 1) -> P1 (8, 3).
4. Step 3: Solve B6 (3, 3) -> P2 (2, 5).

## Tile Mechanics (2F)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Target for boulders; player falls to 1F.
- LADDER: Warp to 1F; resets boulder positions.
- NPC: Impassable (WALL).

## Lessons Learned
- Boulder Trap: (8, 10) is a trap because (8, 9) and (7, 10) are walls.
- Strength: Must be reactivated after changing maps or resetting.
- Visuals: The 'checkerboard' walls at (7, 10-15) are a mix of WALL and FLOOR.