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
- Turn 48106: Direct path to West Beach (2, 51) is blocked by terraces.
- New Plan: Use the Row 35 corridor.
- Step 1: (18, 45) -> (20, 45) -> (20, 35).
- Step 2: (20, 35) -> (10, 35) -> (10, 33) -> (6, 33) -> (6, 35).
- Step 3: (6, 35) -> (2, 35) -> (2, 14).
- Status: XENON leading, Ultra Balls ready.
- Goal: Reach (2, 14) to enter the north plateau.