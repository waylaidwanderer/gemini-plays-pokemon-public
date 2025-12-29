# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable.
- PIT: Player falls to 1F.
- LADDER: Warp between floors. Resets boulder positions.

# Blackthorn Gym 2F Puzzle Analysis
- Boulders: B6 (3, 4), B7 (6, 1), B8 (8, 11).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11).

# Strategy
1. Push Boulder 8 north toward Pit P3 (8, 7).
2. Solve B7 and B6.

# Verification Status
- (8, 10): FLOOR in XML.
- (7, 11): WALL in XML.
- (2, 2): FLOOR in XML.