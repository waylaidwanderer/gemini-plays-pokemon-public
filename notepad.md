# PC Storage (Box 1)
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard walkable ground.
- WATER: Traversable only via Surf.
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- HEADBUTT_TREE: Special tree for Headbutt.
- DOOR: Warp point.
- FLOOR_UP_WALL: Ledge face. Impassable from all directions.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Suicune Capture Strategy
- Lead: XENON (Haunter, Lv44).
- Move 1: Hypnosis (Sleep).
- Move 2: Night Shade (44 dmg). Suicune has ~120 HP. Use twice for Red health.
- Item: Ultra Balls (32).
- Note: Suicune is Water type. Calcifer (Fire) is vulnerable. GORP (Snorlax) is a good tank.

# Strategic Plans: Locate Suicune
- Start Turn: 47680
- Goal: Reach (7, 4) on north plateau.
- Primary Route: 'Beach Shortcut' (X=2).
  - Step 1: Reach West Beach at (2, 51) via southern city corridor.
  - Step 2: Walk North along X=2.
  - Verification: Check for blockage at Y=10 (Seen FLOOR_UP_WALL tiles).
- Backup Route: 'Great Spiral' buoy maze via (27, 30).
- Turn Limit for Shortcut: 48150.

# Lessons Learned
- Fly Navigation: Johto Fly menu is a linear list scrolled with Up/Down, not a 2D grid.
- Exploration: (11, 15) and (11, 14) are confirmed dead-end pockets. Marker 🚫 placed.
- Navigation: (21, 46) and (18, 50) are solid cliffs (FLOOR_UP_WALL). Marker 📍 placed.
- Pathing: To reach the southern corridor from the city center, use the gap at X=20-21.
- Turn 48109: Row 35 plan blocked by (6, 34) FLOOR_UP_WALL.
- New Plan: Use Row 47 crossover to reach the southern corridor (Row 51).
- Route: (10, 35) -> (12, 35) -> (12, 47) -> (10, 47) -> (10, 51) -> (4, 51) -> (2, 51).
- Step 1: Reach (4, 51).
- Status: XENON leading, Ultra Balls ready.
- Goal: Reach (2, 14) to enter the north plateau.