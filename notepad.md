# Blackthorn Gym 2F Puzzle
- Puzzle Started: Turn 35022 (Reset)
- Current Turn: 35087
- Status: Strength ACTIVE (Turn 35084)

## Current Boulder Positions
- B6 (ID 6): (3, 2)
- B7 (ID 7): (6, 1)
- B8 (ID 8): (8, 12)

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Strategic Plan
1. Move to (8, 13) and push B8 Up to (8, 11).
2. Move to (8, 12) and then to the left side via (7, 12) and (6, 12).
3. Audit walls at (7, 11) and (7, 10) from the left side.
4. Once the map is fully verified, use solve_boulders_v2.

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