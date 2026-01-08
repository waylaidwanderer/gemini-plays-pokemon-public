# Blackthorn Gym (Puzzle Progress)
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14) [Current Positions].
- Reset Mechanic: Ladders (1, 7) and (7, 9) reset 2F boulders.
- Push Mechanic: Player stays in tile after push.
- Status: Strength is ACTIVE. B6 is at (3, 3).

# Verified Obstacles (2F)
- (4, 1): Cody. Impassable.
- (4, 11): Fran. Impassable.
- (4, 3), (4, 5), (4, 12): WALL. Impassable.
- (5, 10), (5, 12), (6, 2), (6, 3), (6, 6): WALL. Impassable.
- (7, 10), (7, 11), (7, 14), (7, 15): WALL. Impassable.
- (8, 4), (8, 8), (8, 9): WALL. Impassable.
- (9, 2), (9, 4), (9, 12-17): WALL. Impassable.

# Verified Connections (2F)
- (4, 13): FLOOR (gap).
- (6, 8) <-> (5, 8): FLOOR (gap).

# Strategy: Blackthorn Gym 2F
- Step 1: Push B6 (3, 3) to P2 (2, 5).
- Step 2: Push B7 (6, 1) to P3 (8, 7).
- Step 3: Push B8 (8, 14) to P1 (8, 3) via Col 9.

# Resource Locations
- Route 45: Good training spot for Haunter.

# Puzzle Analysis (2F)
- B6 is trapped in the top-left area (Cols 0-3, Rows 0-7) by Row 8 WALLs and Col 4 WALLs/NPCs.
- P2 (2, 5) is also in the top-left area.
- Hypothesis: B6 must go into P2. This requires pushing B6 LEFT from Col 3.
- Obstacle: Column 4 is almost entirely WALLs/NPCs.
- Test: Check if Cody (4, 1) is passable after defeat. If so, B6 can be pushed from (3, 1) to (2, 1).
- Alternative: B7 or B8 crosses to the left side at (4, 13) FLOOR to reach P2.
- Current B6 Position: (3, 3).