# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard ground. Traversable.
- WATER: Surf required. Traversable.
- BUOY: Impassable water obstacle.
- WALL: Impassable ground/object.
- FLOOR_UP_WALL: Impassable ledge face. Acts as a solid wall from all directions.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Goal Tracking: Capture Suicune
- Start Turn: 48227
- Start Time: Wednesday, 3:37 PM (Turn 48250)
- Strategy: The Great Buoy Loop (Turn 48397).
- Step 1: Move East along Row 26 to (27, 26).
- Step 2: Move North to (27, 16).
- Step 3: Move West through Gap 2 at (22, 16) to (20, 16).
- Step 4: Move North to (20, 14).
- Step 5: Move West through Gap 4 at (19, 14) to (18, 14).
- Step 6: Move North to (18, 11).
- Step 7: Land on the plateau and locate Suicune (hypothesized near 14, 10).

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder for current map. Supports LAND and WATER mediums.
- menu_navigator_v2_fixed: Navigates menus using button sequences. Needs index/button strings.