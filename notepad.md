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
- Current Status: B8 is at (8, 12). Player at (8, 13).
- Plan:
  1. Confirm Strength is active by interacting with B8.
  2. Push B8 UP to (8, 10) or LEFT to (7, 12) if possible.
  3. Run a focused BFS for B8 to Pit (8, 7).
- B8 Path Hypothesis: (8, 12) -> (8, 10) -> (9, 10) -> (9, 7) -> (8, 7) PIT.
  - Test: Can I push B8 right at (8, 10)? (Player needs to be at (7, 10) WALL).
  - Test: Can I push B8 down at (9, 6)? (Player needs to be at (9, 5) FLOOR).