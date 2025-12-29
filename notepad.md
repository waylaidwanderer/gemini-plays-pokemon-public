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
1. **Boulder 8 (8, 13) -> Pit P3 (8, 7)**
   - Goal: Fill the pit at (8, 7) to create a bridge on 1F.
   - Current: Pushing north from (8, 14) to (8, 13).
   - Next: Continue pushing north toward Row 10.
2. **Boulder 7 (6, 1) -> Pit P2 (8, 3)**
   - Goal: Fill the pit at (8, 3) to create a bridge on 1F.
   - Initial position is (6, 1).
3. **Boulder 6 (3, 3) -> Pit P1 (2, 5)**
   - Goal: Fill the pit at (2, 5) to create a bridge on 1F.
   - Initial position is (3, 3).

# Verification Status
- (2, 2): Verified FLOOR in XML.
- (6, 10): Verified FLOOR in XML.
- (7, 12): Verified FLOOR in XML.
- (7, 11): Verified WALL in XML and confirmed by collision.
- (8, 9): Verified WALL in XML.
- (8, 8): Verified WALL in XML.
- (7, 10): Verified WALL in XML.
- NPC Cody at (4, 1) and Fran at (4, 11) are solid obstacles.