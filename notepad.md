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
- Strategy: The Inland Gap Crossing (Turn #48418).
- Step 1: Walk to (10, 33) (Gap in the X=9 Wall).
- Step 2: Walk West to (8, 33) (Entering the Middle Strip).
- Step 3: Walk to (6, 35) and then West to (2, 35) (Gap in the X=5 Wall, Entering West Beach).
- Step 4: Walk North along West Beach (X=2) to Row 11.
- Step 5: Walk East to (14, 11) and then North to Suicune at (14, 10).
- Hypothesized sighting spot: (14, 10). Verified that Row 12 is clear of vertical walls.

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder for current map. Supports LAND and WATER mediums.
- menu_navigator_v2_fixed: Navigates menus using button sequences. Needs index/button strings.