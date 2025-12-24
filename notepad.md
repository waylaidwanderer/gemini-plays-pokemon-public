# Ice Path Strategy
- **Current Action:** Solving West Ice Room Puzzle.
- **Goal:** Reach the ladder (likely in the center/NW of this room).
- **Puzzle State:**
  - Located at Top-Right corner (15, 2).
  - Only valid move is South.
  - **Plan:** Slide South -> Stop at (15, 5) (Wall at 15, 6).
  - **Next:** Likely slide Left from (15, 5) towards the center.
- **Observations:**
  - Walls/Rocks act as stops: (12, 5), (15, 6), (11, 9).
  - Ladder might be on the floor island seen at row 8-9 (x=16+). Wait, that's outside the ice rink.
  - There might be a ladder *inside* the ice area or a path leading to one.
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Ice Room (Puzzle active).
- **Center:** Hub.
- **East:** Winding corridors.