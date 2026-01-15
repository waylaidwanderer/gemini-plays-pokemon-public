# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard ground.
- WATER: Surf required.
- BUOY: Impassable water.
- WALL: Impassable ground/object.
- FLOOR_UP_WALL: Impassable ledge face. Effectively a WALL.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Goal Tracking: Capture Suicune
- Start Turn: 48227
- Start Time: Wednesday, 3:37 PM (Turn 48250)
- Strategy: The City Center Maze Bypass (Turn 48351).
- Step 1: Land at (27, 44) and walk to (12, 44).
- Step 2: Walk North to (12, 33) and West to (6, 33). (Bypasses Column 9 wall)
- Step 3: Walk South to (6, 37) and West to (2, 37). (Bypasses Column 5 wall)
- Step 4: Walk North along Column 2 to (2, 12). (Bypasses Row 15 wall)
- Step 5: Walk East along Row 12 to (14, 12) and North to (14, 10).

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder for current map.