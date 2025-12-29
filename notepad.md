# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Warp for player (to 1F), destination for boulders.
- LADDER: Warp between floors. Transfers between 1F and 2F.
- Strength: Active (Turn 30009). Required to push boulders. Reactivate by interacting with a boulder if it fails.

# Blackthorn Gym 2F State
- Boulders (Current):
  - B6: (3, 5)
  - B7: (6, 1)
  - B8: (8, 12)
- Pits: (2, 5), (8, 3), (8, 7).
- Crossing Points:
  - Row 1: Gap in Column 2, but Cody (NPC) blocks Column 4.
  - Row 9: Gap in Column 2 at (2, 9).
  - Row 11: Gap in Column 4, but Fran (NPC) is there.
  - Row 13: Crossing Column 4, but Column 2 is a WALL. (8, 13) to (7, 13) is open.

# Strategy: Boulder Puzzle
- Goal: Drop all three boulders into pits to bridge gaps on 1F.
- Phase 1: Return to 2F and test (2, 13) passability.
  - Hypothesis: (2, 13) is a fake wall on 2F.
  - Test: Push B6 to (3, 13), then try to push it to (2, 13).
- Phase 2: Solve B7 and B8 using confirmed paths.
  - B7: (6, 1) -> (7, 1) -> (7, 3) -> (8, 3) Pit.
  - B8: (8, 12) -> (8, 10) -> (9, 10) -> (9, 7) -> (8, 7) Pit.