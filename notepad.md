# Ice Path Strategy
- **Current Action:** Sliding North in West Ice Room.
- **Goal:** Reach the northern floor island at (16-21, 8-9).
- **Path History:**
  - Entered at (15, 14), slid North to (15, 12).
  - Slid Left from (15, 12) to (9, 12).
  - **NOW:** Sliding North from (9, 12) -> Target (9, 8).
- **Hypothesis:** Row 7 is a wall, stopping me at (9, 8). From there, I can slide East to the floor at (16, 8).
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Entrance & Ice Room (Current Location).
- **North-West:** Unexplored Floor Island?
- **Center:** Hub.
- **East:** Winding corridors.