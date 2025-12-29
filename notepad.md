# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Warp for player (to 1F), destination for boulders.
- LADDER: Warp between floors.
- Strength: Active (Turn 30009). Required to push boulders.

# Blackthorn Gym 2F State
- Boulders: B6 (3, 5), B7 (6, 1), B8 (8, 12).
- Pits: (2, 5), (8, 3), (8, 7).
- Crossing Points:
  - Row 1: Gap in Column 2, but Cody (NPC) blocks Column 4.
  - Row 9: Gap in Column 2 at (2, 9).
  - Row 11: Gap in Column 4, but Fran (NPC) is there.
  - Row 13: Crossing Column 4, but Column 2 is a WALL.

# Strategy
- Goal: Drop all three boulders into pits.
- Current Status: B8 is at (8, 12). Player at (8, 13). Strength active.
- Plan:
  1. Clear "Boulders may now be moved!" text.
  2. Push B8 UP to (8, 11).
  3. Test if (9, 13) or (8, 9) are passable.
- B8 Path Hypothesis: (8, 12) -> (8, 11) -> (8, 10).
  - If (8, 9) is a wall, B8 is stuck unless Column 9 or 7 is accessible.