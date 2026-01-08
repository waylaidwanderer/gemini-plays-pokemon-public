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

## Lessons Learned
- Corner Traps: Always check if the path *behind* or *adjacent* to a boulder's destination is blocked before pushing. (8, 10) is a trap because (8, 9) and (7, 10) are walls.
- Resetting: Use the ladder at (7, 9) or (1, 7) to reset the room if a boulder gets stuck.

## How to Solve Boulder Puzzle
- Goal: Push three boulders into pits to create a path on 1F.
- Step 1: Move B8 from (8, 14) to P3 (8, 7).
- Step 2: Move B7 from (6, 1) to P1 (8, 3).
- Step 3: Move B6 from (3, 3) to P2 (2, 5).