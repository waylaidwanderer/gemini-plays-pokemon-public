# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable.
- PIT: Player falls to 1F. Boulders falling in create bridges on 1F.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.

# Blackthorn Gym 2F Puzzle Analysis
- Boulders (Initial): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).

# Strategy: Solve Boulders
1. **Boulder 8 (8, 14) -> Pit P3 (8, 7)**
   - Push north to (8, 11).
   - Push left to (6, 11). (Assumes (7, 11) is FLOOR per system overwatch)
   - Push north to (6, 7).
   - Push right to (8, 7) [PIT].
2. **Boulder 7 (6, 1) -> Pit P2 (8, 3)**
   - Push right to (8, 1).
   - Push south to (8, 3) [PIT].
3. **Boulder 6 (3, 3) -> Pit P1 (2, 5)**
   - Push south to (3, 13).
   - Push left to (1, 13).
   - Push north to (1, 5).
   - Push right to (2, 5) [PIT].

# Verification Status
- (2, 2), (6, 10), (7, 12): Verified FLOOR.
- (7, 11): Labeled FLOOR per overwatch (XML check pending).
- (8, 9), (8, 8), (7, 10): Verified REAL WALLS.