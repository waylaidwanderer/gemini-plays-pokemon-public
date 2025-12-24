# Ice Path Strategy
- **Current Action:** Solving West Ice Room Puzzle.
- **Goal:** Reach the ladder (likely in the center/NW of this room).
- **Puzzle State:**
  - Current Position: (2, 7).
  - Wall at (2, 6) blocked "Up" move to (2, 2).
  - Only valid progressive move: **Right**.
- **Solution Hypothesis (Updated):**
  1. Slide **Right** -> Target (15, 7) OR (7, 7) if obstacle at (8, 7).
  2. If stop at (7, 7): Down -> (7, 13) -> Right -> (13, 13) -> Up -> (13, 5) -> Left -> (2, 5) -> Up -> (2, 2).
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle active).
- **Center:** Hub.
- **East:** Winding corridors.