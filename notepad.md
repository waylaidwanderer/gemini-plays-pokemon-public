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

# Strategic Plan: The Great Band Bypass (Turn 48250)
- Goal: Reach Suicune sighting spot at (14, 10).
- Problem: The city is divided into horizontal bands by long WALL/FLOOR_UP_WALL ledges at Row 15, Row 46, and Row 50. My target (14, 10) is in Band 1 (North), but Column 5 is a WALL (Row 40-45) preventing Westward access within Band 1.
- Solution: Surf South along the East coast to Row 51 (Band 3), walk West to Column 2 (West Beach), then walk North along the clear West Beach corridor to Row 14.
- Step 1: Walk to (26, 44) and use Surf to enter the water at (27, 44). (Complete)
- Step 2: Surf South along Route 41 coast to (0, 51). (In Progress)
- Step 3: Surf West back into Cianwood at (29, 51) (Band 3 landing), then walk West to (2, 51).
- Step 4: Walk North to (2, 12).
- Step 5: Walk East to (14, 12) -> (14, 10).
- Status: At Route 41 (0, 44). Surfing. Repel active.

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