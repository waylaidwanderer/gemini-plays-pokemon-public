# Tile Mechanics (Global)
- FLOOR: Passable. Standard movement.
- WALL: Impassable. (Includes 'SILVER BLOCKS')
- PIT: Player falls to 1F. Boulders create bridges on 1F.
- LADDER: Warp between floors. Resets boulder positions. Deactivates Strength.

# Blackthorn Gym 2F Puzzle Analysis
- Start Turn: 30123
- Boulders (Initial - Assumed): B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Pits: P1 (2, 5), P2 (8, 3), P3 (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11).

# Strategy: Visual Confirmation and Reactivation
1. Navigate to (5, 1) to confirm B7 at (6, 1).
2. Navigate to (3, 4) to confirm B6 at (3, 3).
3. Navigate to (8, 15) to confirm B8 at (8, 14).
4. Reactivate Strength on B8.
5. Use specialized solver to find the definitive path.