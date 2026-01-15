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
- Strategy: The Great Buoy Loop (Turn 48381).
- Step 1: Use Super Repel.
- Step 2: Surf North at X=27 to (27, 16).
- Step 3: Surf West through Gap 2 at (22, 16) to (21, 16).
- Step 4: Surf North to (21, 14), then West through Gap 4 at (19, 14) to (18, 14).
- Step 5: Surf North to (18, 11), then West to land at (16, 11).
- Step 6: Walk to Suicune at (14, 10).

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder for current map.