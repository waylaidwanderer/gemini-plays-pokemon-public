# Ice Path Strategy
- **Current State:** At (25, 19).
- **Discovery:** The East Corridor is not a dead end but a maze. The `FLOOR_UP_WALL` at (25, 18) blocks direct North travel, forcing a detour Right to x=28.
- **Goal:** Reach the Northern Ice Room via the East Maze.
- **Route:**
  1. Move **Right** to (28, 19), then **Up** to (28, 18).
  2. Move **North** to (29, 12).
  3. Turn **West** at Row 12/13 to access the central area (e.g., 27, 13 -> 27, 14 -> 21, 14).
  4. Follow the path to the Hidden Floor at (18, 14).

# Map Structure
- **SE Floor:** Entrance to East Maze.
- **East Maze (x=25-30):** Connects to North via winding path.
- **North Room:** Accessible from East Maze.