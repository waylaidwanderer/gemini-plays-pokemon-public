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

# Strategy: Decisive Action Phase
1. Reset floor via ladder (Done Turn 30224).
2. Reactivate Strength.
3. Use specialized solver (boulder_pathfinder_v2) to find the exact push sequence.
4. Execute pushes based on confirmed FLOOR paths in XML.
5. Goal: Fill all three pits.