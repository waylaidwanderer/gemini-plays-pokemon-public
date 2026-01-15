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
- Strategy: The Southern Corridor Cross (Turn #48415).
- Step 1: Walk South to (19, 51).
- Step 2: Walk West through the corridor at Row 51 to (4, 51).
- Step 3: Walk North to (4, 50), then West to (2, 50) (West Beach).
- Step 4: Walk North along the beach to Row 10.
- Step 5: Walk East to trigger Suicune sighting (hypothesized near 14, 10).

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder for current map. Supports LAND and WATER mediums.
- menu_navigator_v2_fixed: Navigates menus using button sequences. Needs index/button strings.