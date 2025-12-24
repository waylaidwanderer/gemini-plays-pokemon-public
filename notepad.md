# Ice Path Strategy
- **Current Action:** Solving West Ice Room Puzzle.
- **Goal:** Reach the ladder (likely in the center/NW of this room).
- **Puzzle State:**
  - Current Position: (15, 7).
  - Previous Path: (2, 7) -> Right -> (15, 7).
  - **Plan:** Slide Down -> (15, 10).
  - Then Left -> (5, 10).
  - Then Down -> (5, 13).
  - Then Right -> (15, 13).
  - Then Up -> (15, 12).
  - Then Left -> (9, 12).
  - Then Up -> (9, 2).
  - Then Left -> (2, 2).
  - Then Down -> (2, 13).
  - Then Right -> (15, 13).
  - **Goal Node:** Reach (11, 8) to slide Right to exit (16, 8).
  - **Problem:** Need to find path to (11, 2) to slide Down to (11, 8).
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle active).
- **Center:** Hub.
- **East:** Winding corridors.