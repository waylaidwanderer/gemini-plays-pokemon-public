# Tile Mechanics
- FLOOR: Passable.
- WALL: Impassable silver blocks. Tested at (4,5), (9,13), (2,13), (3,0) - all solid.
- PIT: Boulder destination. Forms bridge on 1F.
- LADDER: Map transition. Deactivates Strength.
- Strength: Active (Turn 30085).

# Blackthorn Gym 2F State
- Boulders: B6 (3, 3), B7 (6, 1). B8 status unknown.
- Pits: (2, 5), (8, 3), (8, 7).
- NPCs: Cody (4, 1), Fran (4, 11). Both solid.
- Column 4: Solid wall/NPC from Row 0 to 12. Gap at Row 13.
- Column 2: Wall from Row 10 to 17.

# Strategy
- Goal: Drop all boulders into pits.
- Current Task: Verify B8 position at (8, 14).
- Plan:
  1. Navigate to (8, 14) via Row 13 crossing.
  2. If B8 is found, use it to fill (8, 7) or (8, 3).
  3. Re-run BFS solver with confirmed B8 position.