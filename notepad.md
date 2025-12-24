# Ice Path Strategy
- **Current Action:** Exploring West Ice Room.
- **Goal:** Solve the ice puzzle to find the Ladder to B1F.
- **Path History:**
  - Entered at (15, 14), slid North to (15, 12).
  - Sliding Left from (15, 12) -> Target (9, 12).
- **Hypothesis:** The "stop" points (rocks/walls) in the North-West (x=9-11, y<12) are key to navigating to the ladder.
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Entrance & Ice Room (Current Location).
- **Center:** Hub.
- **East:** Winding corridors.