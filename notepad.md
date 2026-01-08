# Blackthorn Gym 2F Puzzle
- Puzzle Started: Turn 35022
- Status: Strength ACTIVE (Turn 35113)

## Tile Mechanics (BlackthornGym2F)
- FLOOR (Type: FLOOR): Traversable.
- WALL (Type: WALL): Impassable.
- PIT (Type: PIT): Warp to 1F. Boulders fill them to create paths on 1F.
- LADDER (Type: LADDER): Warp to 1F. Resets boulder positions.
- NPCs act as walls.

## Current Boulder Positions
- B6 (ID 6): (3, 2) [Unverified]
- B7 (ID 7): (6, 1) [Unverified]
- B8 (ID 8): (8, 14) [Verified]

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Strategic Plan
1. Navigate to (3, 2) and (6, 1) to verify B6 and B7 positions after reset.
2. Use solve_boulders_v2 with the verified positions and wall data.
3. Execute the resulting sequence of pushes.

## Lessons Learned
- Visuals are deceptive; trust the 'type' attribute in the Game State.
- Strength must be reactivated after changing floors.
- Boulder Reset: Boulders reset to starting positions when changing maps via ladder.