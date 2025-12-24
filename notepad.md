# Ice Path Strategy
- **Current Action:** Collecting Item & Backtracking.
- **Goal:** Find Ladder to B1F.
- **Status:** East Ice Puzzle SOLVED. Item at (31, 7) retrieved.
- **Observation:** This path is a dead end for the item. The Ladder is likely South of (28, 19).
- **Backtrack Plan:**
  1. Slide **Left** -> (22, 7).
  2. Slide **Up** -> (22, 6).
  3. Slide **Right** -> (25, 6).
  4. Slide **Down** -> (25, 9).
  5. Slide **Right** -> (28, 9).
  6. Slide **Up** -> (28, 6).
  7. Slide **Right** -> (29, 6).
  8. Slide **Down** -> (29, 8).
  9. Slide **Left** -> (23, 8).
  10. Slide **Down** -> (23, 9).
  11. Slide **Left** -> (21, 9) [Exit to Floor].
- **Next:** Walk to (28, 19) and explore South.
- **Items:** Item Balls at (32, 23), (35, 9) [Inaccessible from here], (31, 7) [Collected].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle solved).
- **Center:** Hub.
- **East:** Winding corridors & East Ice Puzzle (Solved).

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle active).
- **Center:** Hub.
- **East:** Winding corridors.