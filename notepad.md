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
- Strategy: The Western Gap Route (Turn 48392).
- Step 1: Surf North to (19, 26).
- Step 2: Surf West through Gap 3 at (18, 26) to (17, 26).
- Step 3: Surf North to (17, 20).
- Step 4: Surf West through Gap 5 at (16, 20) to (15, 20).
- Step 5: Surf North to (15, 12) and land at (15, 11).
- Step 6: Locate Suicune on the plateau (hypothesized near 14, 10).

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder for current map. Supports LAND and WATER mediums.
- menu_navigator_v2_fixed: Navigates menus using button sequences. Needs index/button strings.