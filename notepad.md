# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable.
- PIT: Player falls to 1F.
- LADDER: Warp between floors. Resets boulder positions.

# Blackthorn Gym 2F Puzzle Analysis
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11).

# Strategy: Solve B7
1. Navigate to (5, 1) via the central corridor.
2. Attempt to push Boulder 7 (6, 1) to the right.
3. Test if Row 0 contains any hidden floor tiles by attempting to move north from Row 1.

# Verification Status
- (7, 11), (7, 10), (8, 9), (8, 8), (6, 0): Verified REAL WALLS.
- (2, 2), (6, 10), (7, 12), (7, 13): Verified FLOOR.