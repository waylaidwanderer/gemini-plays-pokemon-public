# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable.
- PIT: Player falls to 1F. Boulders falling in create bridges on 1F.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.

# Blackthorn Gym 2F Puzzle Analysis
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 13).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).

# Strategy: Solve Boulders
1. Push Boulder 8 north from (8, 13) toward (8, 10).
2. At (8, 10), test if (7, 10) or (8, 9) are traversable FLOOR tiles.
3. Solve B7 and B6 once B8 is positioned.

# Verification Status
- (2, 2): Verified FLOOR in XML.
- (6, 10): Verified FLOOR in XML.
- (7, 12): Verified FLOOR in XML.
- (7, 11): Verified WALL in XML.
- (8, 9): Verified WALL in XML.
- (8, 8): Verified WALL in XML.
- (7, 10): Verified WALL in XML.
- NPC Cody at (4, 1) and Fran at (4, 11) are solid obstacles.