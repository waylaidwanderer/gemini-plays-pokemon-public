# Ice Path Strategy
- **Current Action:** Sliding East in West Ice Room.
- **Goal:** Explore NE corner of the room (x>14, y<10).
- **Path History:**
  - Slid North from (9, 12) -> Overshot (9, 8) (Row 7 was not a wall).
  - Stopped at (9, 2) (Wall at Row 1).
  - **NOW:** Sliding Right from (9, 2).
- **Hypothesis:** I will hit a wall on the East side of this room, allowing me to slide Down/South towards the center.
- **Observations:**
  - (11, 9) is a Wall/Rock.
  - (12, 5) is a Wall/Rock.
  - (11, 11) is likely a Wall/Rock (visually confirmed, map data says ICE).
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles are impassable walls.

# Map Structure
- **West:** Entrance & Ice Room (Current Location).
- **North-West:** Unexplored.
- **Center:** Hub.
- **East:** Winding corridors.