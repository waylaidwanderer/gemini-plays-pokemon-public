# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable.
- PIT: Player falls to 1F. Boulders falling in create bridges on 1F.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.

# Blackthorn Gym 2F Puzzle Analysis
- Boulders: B6 (3, 4), B7 (6, 1), B8 (8, 13).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).

# Strategy: Solve Boulders
1. Use run_code solver results to push boulders into pits.
2. Current Focus: Boulder 8 toward P3 (8, 7).

# Verification Status
- (2, 2): Verified FLOOR (looks like silver block).
- (7, 11): Checking XML type via run_code.