# Tile Mechanics
- FLOOR: Passable.
- WALL: Impassable silver blocks. Tested at (4,5), (9,13), (2,13), (3,0) - all solid.
- PIT: Boulder destination. Forms bridge on 1F.
- LADDER: Map transition. Deactivates Strength.
- Strength: Reactivating at (3,4) on Turn 30085.

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1). Verify B8.
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both defeated.

# Strategy
- Puzzle Start Turn: 29931.
- Goal: Drop B6 and B7 into pits.
- Plan:
  1. Activate Strength.
  2. Verify B8 status.
  3. Use optimized BFS solver to find the push sequence.