# Blackthorn Gym 2F Puzzle
## Current Boulder Positions (Reset)
- B6 (ID 6): (3, 2) [Marker]
- B7 (ID 7): (6, 1) [Marker]
- B8 (ID 8): (8, 14) [Verified]

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Strategic Plan
1. Activate Strength (Turn 35084).
2. Verify B6 and B7 positions.
3. Use solve_boulders_v2 to find the full solution.
4. Execute push sequence.

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