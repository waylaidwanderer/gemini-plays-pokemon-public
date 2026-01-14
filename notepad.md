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
- Start Turn: 47680
- Lead: XENON (Haunter, Lv44).
- Move 1: Hypnosis (Sleep).
- Move 2: Night Shade (44 dmg). Suicune has ~120 HP. Use twice for Red health.
- Item: Ultra Balls (32).
- Note: Suicune is Water type. Calcifer (Fire) is vulnerable. GORP (Snorlax) is a good tank.

# Strategic Plans: Locate Suicune
## The 'Beach Shortcut'
- Hypothesis: The northern plateau (Suicune at 7, 4) is reachable by walking North along the West beach at X=2.
- Route: 
  1. Navigate to the southern corridor (Y >= 48).
  2. Walk West through gaps in the internal walls to reach the beach at X=2.
  3. Walk North along the sand (X=2) to Y=4.
- Status: Testing. Turn Limit: 48150.

## The Great Spiral (Backup Plan)
- Entrance: (27, 44).
- Route: Lane 1 (N) -> Lane 2 (S) -> Lane 3 (S) -> Lane 4 (N) -> Lane 5 (N) -> Land at (14, 10).
- Requirements: Surf, Super Repel.

# Lessons Learned
- Fly Navigation: The Johto Fly menu is a linear list scrolled with Up/Down, not a 2D grid.
- Exploration: (11, 15) and (11, 14) are confirmed dead-end pockets.
- Navigation: (21, 46) is a solid cliff (FLOOR_UP_WALL), not a jumpable ledge. Use X=18 gap to go South.