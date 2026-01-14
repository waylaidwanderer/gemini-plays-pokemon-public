# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard ground.
- WATER: Surf required.
- BUOY: Impassable water.
- WALL: Impassable ground/object.
- FLOOR_UP_WALL: Impassable ledge face (blocks movement towards the "up" direction, usually South to North or North to South depending on map). Observed: Blocks Southward movement at (12, 50).
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Strategic Plan: The Great Tiered Bypass (Turn 48242)
- Goal: Reach Suicune sighting spot at (14, 10).
- Problem: The city is tiered. Current pocket (X=11-13, Y=45-49) is blocked south by FLOOR_UP_WALL at (12, 50).
- Solution: Find a gap in the tier walls (Column 5/9/11) to reach the West Beach.
- Step 1: Walk to (8, 44) via (12, 47) and (8, 47).
- Step 2: Navigate to (2, 44) or (2, 51) by finding a gap in the Column 5/7/9 walls.
- Status: At (12, 49). Repel active. Start Turn: 48227.

# Verified Landmarks
- Land Gap 1: (12, 44) - North-south passage.
- West Beach Corridor: Column X=2 - Clear path from Row 51 to Row 14.
- Plateau Boundary: Row 15 WALL/LEDGE.
- Suicune Spot: (14, 10).
- Obstacle: (12, 50) FLOOR_UP_WALL blocks South.

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder. Handles LAND vs WATER medium consistency. Treats unseen tiles as traversable within the starting medium. Handles LEDGE_HOP_DOWN as one-way (dy=1).
- route_analyst (Agent): Expert in map connectivity and elevation analysis.