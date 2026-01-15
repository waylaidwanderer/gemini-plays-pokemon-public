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
- Strategy: The Great Buoy Loop (Turn #48403).
- Step 1: Use Super Repel.
- Step 2: Move East to (27, 16).
- Step 3: Move North to (27, 10).
- Step 4: Move West through Gap 1 at (26, 10) to (21, 10).
- Step 5: Move North to (21, 8).
- Step 6: Move West to (18, 8).
- Step 7: Move South to (18, 11).
- Step 8: Land on the plateau and locate Suicune (hypothesized near 14, 10).

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder for current map. Supports LAND and WATER mediums.
- menu_navigator_v2_fixed: Navigates menus using button sequences. Needs index/button strings.