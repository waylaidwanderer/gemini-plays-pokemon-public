# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard walkable ground.
- WATER: Traversable only via Surf.
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- DOOR: Warp point.
- FLOOR_UP_WALL: Ledge face. Impassable from all directions.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Suicune Capture Strategy
- Lead: XENON (Haunter, Lv44).
- Move 1: Hypnosis (Sleep). Accuracy is key.
- Move 2: Night Shade (44 dmg). Suicune (Lv40) has ~120 HP. Use twice for Red health.
- Move 3: Dream Eater (100 power). Only works if Suicune is asleep.
- Item: Ultra Balls (32).
- Backup: GORP (Snorlax) as a tank. Calcifer (Typhlosion) is risky due to type disadvantage.

# Strategic Plan: The Great Spiral (Refined)
- Start Turn: 48151.
- Step 1: Walk to East Coast Surf Point (19, 30). (Done)
- Step 2: Surf to Outer Channel (X=27) and enter Gap 1 at (26, 10). (Done)
- Step 3: Navigate Middle Ring to Gap 2 at (22, 16). (Done)
- Step 4: Navigate to Gap 3 at (19, 14). (In Progress)
- Route: (22, 16) -> (27, 16) -> (27, 8) -> (19, 8) -> (19, 14).
- Step 5: Navigate to Landing Point at (16, 13) and land.
- Step 6: Walk to Sighting Spot at (14, 10).
- Status: XENON leading, Ultra Balls ready.

# Lessons Learned
- Fly Navigation: Johto Fly menu is a linear list scrolled with Up/Down, not a 2D grid.
- Exploration: (11, 15) and (11, 14) are dead-end pockets blocked by walls at Row 14/15.
- Pathing: Cianwood city center is elevated; use the West Beach (X=2) or East Coast Surf for navigation to the North Plateau.
- Pathing Failure: Attempting to walk from city center to West Beach (X=2) failed due to undetected FLOOR_UP_WALL tiles at Row 34/48.
- Navigation: The "Beach Express" (X=2) corridor is not reachable from the city center.
- Turn 48162: At (22, 16). find_path_v4 failed due to medium check on unseen tiles. Fixing tool with robust medium and ledge logic.
- Turn 48165: At (27, 16). Navigation to Gap 1 (26, 10). Testing Row 0 shortcut hypothesis.