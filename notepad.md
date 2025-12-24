# Ice Path Strategy
- **Current Action:** Solving West Ice Room Puzzle.
- **Goal:** Reach the ladder (likely in the center/NW of this room).
- **Solution Path Identified:**
  1. Start (13, 5). Slide **Down** -> (13, 13). [NEXT]
  2. Slide **Left** -> (2, 13).
  3. Slide **Up** -> (2, 2).
  4. Slide **Right** -> (6, 2).
  5. Slide **Down** -> (6, 10).
  6. Slide **Right** -> (15, 10).
  7. Slide **Up** -> (15, 7).
  8. Slide **Left** -> (8, 7) [Hypothesis: Rock at 7, 7].
  9. Slide **Down** -> (8, 11).
  10. Slide **Left** -> (7, 11).
  11. Slide **Up** -> (7, 8).
  12. Slide **Right** -> (16, 8) [EXIT].
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle active).
- **Center:** Hub.
- **East:** Winding corridors.