# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard ground.
- WATER: Surf required.
- BUOY: Impassable water.
- WALL: Impassable ground/object.
- FLOOR_UP_WALL: Impassable ledge face.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Suicune Capture Strategy
- Lead: XENON (Haunter, Lv44).
- Move 1: Hypnosis (Sleep).
- Move 2: Night Shade (Fixed 44 dmg). Suicune (Lv40) has ~120 HP. Use 2-3 times.
- Move 3: Dream Eater (100 power). Only if asleep.
- Item: Ultra Balls (32).
- Backup: GORP (Snorlax) for tanking.

# Strategic Plan: The West Beach Sprint (Turn 48227)
- Goal: Reach Suicune sighting spot at (14, 10).
- Problem: Buoy maze is complex; city center is tiered.
- Solution: Verified land route via gaps at (12, 44) and (5, 35).
- Step 1: Walk to (12, 44). (In Progress)
- Step 2: Walk to (12, 35) -> (5, 35).
- Step 3: Walk West to West Beach at (2, 35).
- Step 4: Walk North along X=2 to Row 10.
- Step 5: Walk East along Row 10 to (14, 10).
- Status: At (19, 30). Repel active.

# Verified Landmarks
- Land Gap 1: (12, 44) - Clear north-south passage between Tier 1 and Tier 2.
- Land Gap 2: (5, 35) - Clear east-west passage to West Beach.
- West Beach Corridor: Column X=2 - Clear path from Row 51 to Row 10.
- Dead Ends: Great Spiral (Nautical maze), Row 15 wall (X=3-17).

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder. Handles LAND vs WATER medium consistency. Treats unseen tiles as traversable within the starting medium. Handles LEDGE_HOP_DOWN as one-way (dy=1).
- route_analyst (Agent): Expert in map connectivity and elevation analysis.