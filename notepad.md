# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable silver blocks. 
- PIT: Player falls to 1F. Boulders falling in create bridges on 1F.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.

# Blackthorn Gym 2F Puzzle Analysis
- Start Turn: 30151
- Boulders: B6 (3, 4), B7 (6, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs (Solid): Cody (4, 1), Fran (4, 11).
- Problem: All boulders appear to be trapped in corridors by silver blocks.
- Hypothesis: Some silver blocks (WALL tiles) are actually FLOOR.

# Investigation Log: Wall Testing
- (6, 0): REAL WALL (Turn 30157).
- (7, 11): REAL WALL (Turn 30160).
- (8, 9): REAL WALL (Turn 30140).
- (7, 10): REAL WALL (Turn 30143).
- (5, 12): REAL WALL (Turn 30163).
- (4, 2): Testing now.

# Strategy: Systematic Fake Wall Search
1. Walk into every adjacent silver block to identify floor tiles.
2. Focus on Column 4 and Column 2 as they block most lateral pushes.
3. Update solver once a fake wall is found.

# Progress Log
- Turn 30176: Pushed B6 to (3, 4). Strength is active.