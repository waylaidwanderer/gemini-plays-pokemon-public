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

# Current Strategy: The Great Spiral (Turn 48203)
- Goal: Trigger Suicune sighting at (14, 10).
- Step 1: Surf from (19, 30) to Outer Channel (X=27).
- Step 2: Navigate Buoy Maze Gaps:
  - Gap 1: (26, 10)
  - Gap 2: (22, 16)
  - Gap 3: (19, 14)
- Step 3: Land on North Plateau at (16, 11-14).
- Step 4: Walk to (14, 10).
- Status: At Surf Point (19, 30). Repel active.

# Lessons Learned
- Pathing: Cianwood is a fortress of plateaus. Land routes to the North Plateau are blocked by vertical cliffs.
- Navigation: The Great Spiral is the only verified nautical path.
- Tool Maintenance: find_path_v4 refined for medium consistency and unseen tile handling.