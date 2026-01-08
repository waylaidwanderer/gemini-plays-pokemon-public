# Blackthorn Gym 2F Puzzle
- Puzzle Started: Turn 35022
- Status: Strength ACTIVE (Turn 35084)

## Tile Mechanics (BlackthornGym2F)
- FLOOR (Type: FLOOR): Traversable.
- WALL (Type: WALL): Impassable.
- PIT (Type: PIT): Warp to 1F. Boulders fill them to create paths on 1F.
- LADDER (Type: LADDER): Warp to 1F. Resets boulder positions.
- NPCs act as walls.

## Expected Boulder Positions (Reset)
- B6 (ID 6): (3, 2)
- B7 (ID 7): (6, 1)
- B8 (ID 8): (8, 14)

## Pits (Targets)
- P1: (8, 3)
- P2: (2, 5)
- P3: (8, 7)

## Strategic Plan
1. Reset the room using the ladder at (7, 9).
2. Verify boulder positions.
3. Use solve_boulders_v2 to find the sequence of pushes from the reset state.

## Lessons Learned
- Visuals are deceptive; trust the 'type' attribute in the Game State.
- Strength must be reactivated after changing floors.
- (8, 10) is a dead end for boulders because (8, 9), (7, 10), and (9, 10) are walls or inaccessible.