# Blackthorn Gym Puzzle
- Status: Strength ACTIVE (Turn 35113)

## Tile Mechanics
- FLOOR: Traversable. Collision type is absolute truth.
- WALL: Impassable. Trust Game State 'type' attribute.
- PIT (2F): Warp to 1F. Boulders fill them to create paths on 1F.
- LADDER: Warp between floors. Resets boulders on 2F.
- NPCs: Act as walls.

## Correct Boulder Positions (2F Reset State)
- B6 (ID 6): (3, 3) [Verified]
- B7 (ID 7): (6, 1) [Verified]
- B8 (ID 8): (8, 14) [Verified]

## Pits (2F Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Strategic Plan
1. Finish talking to Clair on 1F.
2. Re-run solve_boulders_v2 with the correct reset coordinates: B6(3,3), B7(6,1), B8(8,14).
3. If still 'No solution', investigate player reachability to the tiles needed for pushes.
4. Execute the sequence.

## Lessons Learned
- Trust Game State: 'WALL' and 'FLOOR' labels are the source of truth.
- B6 reset position is (3, 3), not (3, 2).
- Strength: Reactivate after floor changes.
- Reachability: The player can reach Clair on 1F by walking around the right edge (Column 9).