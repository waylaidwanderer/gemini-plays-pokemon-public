# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable.
- PIT: Player falls to 1F. Boulders falling in create bridges on 1F.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.

# Blackthorn Gym 2F Puzzle Analysis
- Boulders (Initial): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).
- Strength: Inactive (Turn 30193). Reset by ladder.

# Strategy: Solve Boulders
1. Reset floor to return all boulders to initial positions.
2. Reactivate Strength on Boulder 8 at (8, 14).
3. Push Boulder 8 north to (8, 12).
4. Analyze paths from (8, 12) to avoid the corner at (8, 10).
5. Target Pits: B8 -> P3 (8, 7), B7 -> P2 (8, 3), B6 -> P1 (2, 5).

# Verification Status
- (8, 9), (8, 8), (7, 10), (7, 11): Verified REAL WALLS.
- (2, 2), (6, 10), (7, 12): Verified FLOOR.