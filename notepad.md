# Blackthorn Gym 2F Puzzle
- Puzzle Started: Turn 35022 (Reset)
- Current Turn: 35096
- Status: Strength ACTIVE (Turn 35084)

## Current Boulder Positions
- B6 (ID 6): (3, 3)
- B7 (ID 7): (6, 1)
- B8 (ID 8): (8, 11)

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Strategic Plan
1. Audit walls in Column 7 and 9 to find the intended path for B8.
   - (9, 13): Verified WALL (Turn 35095).
   - (7, 14): Verified WALL (Turn 35096).
2. Use run_code to find a solution by testing single-wall removals in the right area.
3. Verify the discovered "fake" wall in-game.
4. Execute the verified push sequence.

## Tile Mechanics (2F)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Target for boulders; player falls to 1F.
- LADDER: Warp to 1F; resets boulder positions.
- NPC: Impassable (WALL).

## Lessons Learned
- Visuals: Visual inspection is unreliable; trust movement tests. (7, 10), (7, 11), (7, 14), (9, 13) are confirmed WALLS.
- Resetting: Use the ladder at (7, 9) or (1, 7) if a boulder gets stuck.
- Strength: Reactivate after floor changes.