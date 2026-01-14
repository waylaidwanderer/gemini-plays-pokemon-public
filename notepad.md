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

# Strategic Plan: The North Beach Ramp (Turn 48234)
- Goal: Reach Suicune sighting spot at (14, 10).
- Problem: The city is tiered. Row 15 has a ledge/wall blocking direct access from the south.
- Solution: Use the West Beach Corridor (X=2) to bypass the main city walls, then use the Row 12 ramp to enter the plateau.
- Step 1: Walk to (12, 33) and head West to (2, 33).
- Step 2: Walk North along X=2 to (2, 12).
- Step 3: Walk East along Row 12 to (14, 12).
- Step 4: Walk North to (14, 10) to trigger Suicune.
- Status: At (12, 44). Repel active.

# Verified Landmarks
- West Beach Corridor: Column X=2 - Clear path from Row 51 to Row 14.
- North Beach Ramp: Row 12 (X=5-16) - Clear path across the plateau boundary.
- Plateau Boundary: Row 15 (X=3-9) WALL/LEDGE, Row 14 (X=9) WALL, Row 13 (X=9-12) WALL.
- Suicune Spot: (14, 10) on the elevated beach.

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder. Handles LAND vs WATER medium consistency. Treats unseen tiles as traversable within the starting medium. Handles LEDGE_HOP_DOWN as one-way (dy=1).
- route_analyst (Agent): Expert in map connectivity and elevation analysis.