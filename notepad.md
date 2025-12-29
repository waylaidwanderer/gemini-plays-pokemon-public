# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Warp for player (to 1F), destination for boulders.
- LADDER: Warp between floors.
- Strength: Active (Turn 30009). Required to push boulders.

# Blackthorn Gym 2F State
- Boulders: B6 (3, 5), B7 (6, 1), B8 (8, 14).
- Pits: (2, 5), (8, 3), (8, 7).
- Crossing Points:
  - Row 1: Gap in Column 2, but Cody (NPC) blocks Column 4.
  - Row 9: Gap in Column 2 at (2, 9).
  - Row 11: Gap in Column 4, but Fran (NPC) is there.
  - Rows 13-17: Gaps in Column 4, but Column 2 is a WALL.

# Strategy
- Goal: Drop all three boulders into pits.
- Current Status: B8 pushed from (8, 15) to (8, 14).
- Plan:
  1. Move to (8, 15) to get behind B8.
  2. Run solve_blackthorn_boulders from (8, 15).
  3. Execute sequence.

# Failed Hypotheses
- Row 13 crossing from (1, 13) to (3, 13) failed: (2, 13) is a WALL.
- Column 4 is a solid wall from Row 2-12, isolating Column 3 from the right.