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

## Strategic Insights
- Gap at (7, 13): B8 at (8, 13) can be pushed Left into the center area.
- Gap at (4, 13): Allows movement between the left and right sides of the gym.
- Strength Status: ACTIVE (Turn 35063).

## Lessons Learned
- (7, 10) and (7, 11) are definitely WALLS.
- (8, 9) is a WALL.
- Visuals are deceptive; trust the 'type' attribute and movement tests.
- Strength must be reactivated after changing floors.