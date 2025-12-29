# Tile Mechanics (Global)
- FLOOR: Passable.
- WALL: Impassable.
- PIT: Player falls to 1F.
- LADDER: Warp between floors. Resets boulder positions.

# Blackthorn Gym 2F Puzzle Analysis
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 11).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11).

# Strategy: Solve Boulders
1. Use run_code to perform a full map scan of tile types.
2. Identify which 'silver block' tiles are actually FLOOR in the XML.
3. Formulate a push sequence based on verified traversable tiles.

# Verification Status
- (7, 11): WALL in XML.
- (2, 2): FLOOR in XML.
- (6, 10): FLOOR in XML.
- (7, 12): FLOOR in XML.
- (7, 13): FLOOR in XML.
- (8, 10): FLOOR in XML.
- (8, 9): WALL in XML.
- (8, 8): WALL in XML.
- (7, 10): WALL in XML.
- (6, 0): WALL in XML.