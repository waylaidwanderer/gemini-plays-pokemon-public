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
- FLOOR_UP_WALL: Ledge face. Impassable from all directions. (Critical for shortcut evaluation).
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Suicune Capture Strategy
- Lead: XENON (Haunter, Lv44).
- Move 1: Hypnosis (Sleep).
- Move 2: Night Shade (44 dmg). Suicune has ~120 HP. Use twice for Red health.
- Item: Ultra Balls (32).

# Strategic Plans: Locate Suicune
- Current Turn: 48094. Shortcut Turn Limit: 48150.
- Goal: Reach (7, 4) on north plateau.
- Primary Route: 'Beach Shortcut' (X=2).
  - Step 1: Reach West Beach at (2, 51) via southern city corridor.
  - Step 2: Walk North along X=2.
  - Verification: Check for blockage at Y=10 (Seen FLOOR_UP_WALL tiles).
- Backup Route: 'Great Spiral' buoy maze via (27, 30).

# Lessons Learned
- Fly Navigation: Johto Fly menu is a linear list (Up/Down), not 2D.
- Exploration: (11, 15) and (11, 14) are confirmed dead-end pockets. Marker 🚫 placed.
- Navigation: (21, 46) is a solid cliff (FLOOR_UP_WALL), not a jumpable ledge. Marker 📍 placed.