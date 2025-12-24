# Ice Path Strategy
- **Current Action:** Executing Return Path to East Hub.
- **Goal:** Explore East Floor Area (x>20) for Ladder to B1F.
- **Reasoning:**
  - West Floor Area (x<10) connects only to Entrance (Route 44).
  - South-West Area (Row 22+, x<15) is blocked from the North.
  - East Floor Area (x>20) was partially seen but not explored.
- **Path Plan:**
  1. Walk to (13, 17). [DONE]
  2. From (13, 17), Slide Right -> Stop at (15, 17). [DONE]
  3. From (15, 17), Slide Down -> Stop at (15, 21). [NEXT]
  4. Slide Right -> Stop at (19, 21).
  5. Slide Down -> Stop at (19, 23).
  6. Slide Right -> Arrive at (20, 23) [Hub].
  7. Explore East.

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision or landing on non-ice.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls from above (and likely below).
- **Map Structure:** 
  - West: Entrance (Route 44).
  - Center: Ice Maze.
  - East: Progression?

# Items
- Item Balls at (32, 23), (35, 9), (31, 7) [Far East - Behind Wall at x=31].