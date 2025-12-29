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
- Phase 1: Break interaction loops by moving away from boulders before planning.
- Phase 2: Use `solve_blackthorn_boulders` to calculate the sequence.
- Phase 3: Execute sequence precisely.

# Lessons Learned
- Dialogue Loops: Pressing A while facing a boulder triggers a "Boulders may now be moved!" prompt. If already active, it just loops. Move away or push immediately.
- Coordinate Precision: Always verify boulder positions against Game State (Map Objects) before planning. Hallucinating a 1-tile offset (e.g., 8,14 vs 8,13) causes navigation loops.
- Strength Activation: Interacting with a boulder is the fastest way to activate Strength.
- Map Layout: Column 4 and Column 2 are major wall barriers. Use Row 1, Row 9, and Row 13 for horizontal movement.