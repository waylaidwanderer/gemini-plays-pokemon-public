# Ice Path Strategy
- **Current Action:** Solving East Ice Puzzle.
- **Goal:** Reach the East side (Ladder/Items) at (30, 7).
- **Location:** At (22, 6).
- **Solution Path Verified (5 Steps):**
  1. Start (21, 9). Slide **Right** -> (23, 9) [DONE].
  2. Slide **Up** -> (23, 6) [Hit Wall at 23, 5]. [DONE]
  3. Slide **Left** -> (22, 6) [Hit Wall at 21, 6]. [DONE]
  4. Slide **Down** -> (22, 7) [Hit Wall at 22, 8]. [NEXT]
  5. Slide **Right** -> (30, 7) [Land on Floor].
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle active).
- **Center:** Hub.
- **East:** Winding corridors.