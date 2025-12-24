# Ice Path Strategy
- **Current Action:** Solving West Ice Room Puzzle.
- **Goal:** Reach the ladder (likely in the center/NW of this room).
- **Puzzle State:**
  - Located at (15, 5).
  - Valid moves: Up (backtrack), Left.
  - **Plan:** Slide Left -> Stop at (13, 5) (Wall at 12, 5).
  - **Next:** From (13, 5), choose Down or Up.
- **Observations:**
  - Walls/Rocks act as stops: (12, 5), (15, 6), (11, 9).
  - (12, 5) is the rock I'm aiming for now.
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle active).
- **Center:** Hub.
- **East:** Winding corridors.