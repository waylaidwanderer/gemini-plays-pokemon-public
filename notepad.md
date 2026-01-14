# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard ground.
- WATER: Surf required.
- BUOY: Impassable water.
- WALL: Impassable ground/object.
- FLOOR_UP_WALL: Impassable ledge face (blocks movement towards the "up" direction, usually South to North or North to South depending on map). Effectively a WALL that cannot be jumped over in either direction.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Goal Tracking: Capture Suicune
- Start Turn: 48227
- Start Time: Wednesday, 3:37 PM (Turn 48250)
- Attempts: 1 (Current)
- Strategy: The Great Band Bypass (Turn 48250).

# Strategic Plan: The Eastern Sea Bypass (Turn 48269)
- Goal: Reach Suicune sighting spot at (14, 10).
- Problem: Cianwood is tiered with horizontal walls.
- Solution: Surf North through Route 41 (East of Cianwood) to bypass land walls.
- Step 1: Surf to (11, 49) and head North to (11, 46).
- Step 2: Surf West to (9, 46) and head North to (9, 12).
- Step 3: Surf West into Cianwood at (29, 12).
- Step 4: Land at (18, 12) and walk to (14, 10).
- Status: At Route 41 (8, 49). Surfing. Repel active.

# Verified Landmarks
- West Beach Corridor: Column X=2 - Clear path from Row 51 to Row 14 (passes Row 15 wall).
- Suicune Spot: (14, 10).
- Band 1 (North): Rows 0-45.
- Band 2 (Middle): Rows 47-49.
- Band 3 (South): Rows 51-53.
- Ledge 1: Row 15 (X=3-17) WALL.
- Ledge 2: Row 46 (X=21-28) FLOOR_UP_WALL, (X=6) FLOOR_UP_WALL. (X=29) WALL.
- Ledge 3: Row 50 (X=12-19) FLOOR_UP_WALL.
- Water Bypass: Route 41 (Column 0) is clear of Cianwood's Row 46/50 obstacles.

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder. Handles LAND vs WATER medium consistency. Treats unseen tiles as traversable within the starting medium. Handles LEDGE_HOP_DOWN as one-way (dy=1).
- route_analyst (Agent): Expert in map connectivity and elevation analysis.