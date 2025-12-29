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
  1. Clear "Boulders may now be moved!" text with multiple A presses.
  2. Test tile passability for (9, 13), (6, 0), and (4, 5) to find the "fake" wall.
  3. Once the grid is verified, solve the puzzle.
- B8 Path Hypothesis: (8, 12) -> (8, 11) -> (8, 10).
  - If (8, 9) is a wall, B8 is stuck unless Column 9 or 7 is accessible.
- Verification: I am in a dialogue loop because I'm pressing A while facing the boulder. I must clear the text and then move away or push.