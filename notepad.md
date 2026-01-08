# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34763
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 14).
- Status: Strength ACTIVE.

# Puzzle Analysis (2F)
- Hypothesis: Boulders must cross the gym via Row 1 (Cody gap) or Row 13 (South gap).
- Crossing 1: Row 1 (0,1) <-> (9,1). Requires Cody (4, 1) to be passable.
- Crossing 2: Row 13 (0,13) <-> (8,13). Requires (2, 13) and (4, 13) to be passable.
- B7 (6, 1) -> P1 (8, 3). (Confirmed viable).
- B8 (8, 14) -> P2 (2, 5). (Requires Row 13 crossing).
- B6 (3, 3) -> P3 (8, 7). (Requires Row 1 or Row 13 crossing).

# Strategy: Blackthorn Gym 2F
- Step 1: Verify Cody (4, 1) collision.
- Step 2: Verify Row 13 crossing at (2, 13).
- Step 3: Execute BFS with verified crossing points.

# Tile Mechanics (2F)
- WALL: (4, 0, 2-10, 12), (2, 8), (3, 8), (4, 8), (8, 8, 9), (7, 10, 11, 14, 15), (9, 12-17).
- GAP: (4, 1) and (4, 13-17) are passable.
- LADDER: Walkable for player, impassable for boulders.
- PIT: Target for boulders, warp for player.