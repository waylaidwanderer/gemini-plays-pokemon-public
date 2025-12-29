# Blackthorn Gym Boulder Puzzle
- Puzzle Start: Turn 30123
- Current Turn: 30249
- Boulders (Verified): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.
- Strength: Active.

# Strategy: Systematic Execution
1. Use boulder_pathfinder_v2 to find the mathematically valid push sequence.
2. Execute the solution strictly following the path.

# Verified Map Constraints (XML)
- Row 0: All WALL.
- (8, 9), (8, 8): WALL.
- (7, 11), (7, 10), (7, 14), (7, 15): WALL.
- (9, 12), (9, 13), (9, 14), (9, 15), (9, 16), (9, 17): WALL.
- (2, 2), (6, 10), (7, 12), (7, 13): FLOOR.