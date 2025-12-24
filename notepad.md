# Ice Path Strategy
- **Current Action:** Backtracking from East Floor.
- **Goal:** Find Ladder to B1F.
- **Status:** Found **HM07 (Waterfall)** at (31, 7).
- **Backtrack Plan (Active):**
  1. Slide **Left** -> (22, 7) [Hit Wall at 21, 7]. [DONE]
  2. Slide **Up** -> (22, 6) [Hit Wall at 22, 5]. [DONE]
  3. Slide **Right** -> (25, 6) [Hit Wall at 26, 6]. [DONE]
  4. Slide **Down** -> (25, 9) [Hit Wall at 25, 10]. [DONE]
  5. Slide **Right** -> (28, 9) [Hit Wall at 29, 9]. [DONE]
  6. Slide **Up** -> (28, 6) [Hit Wall at 28, 5]. [DONE]
  7. Slide **Right** -> (29, 6) [Hit Wall at 30, 6]. [DONE]
  8. Slide **Down** -> (29, 8) [Hit Wall at 29, 9]. [DONE]
  9. Slide **Left** -> (23, 8) [Hit Wall at 22, 8]. [DONE]
  10. Slide **Down** -> (23, 9) [Hit Wall at 23, 10]. [NEXT]
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