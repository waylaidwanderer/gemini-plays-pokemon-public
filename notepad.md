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

# Strategic Plan: The Great Spiral (Turn 48206)
- Goal: Trigger Suicune sighting at (14, 10).
- Step 1: Surf from (20, 30) to Outer Channel (X=27). (In Progress)
- Step 2: Use Super Repel.
- Step 3: Navigate Buoy Maze Gaps:
  - Gap 1: (26, 10)
  - Gap 2: (22, 16)
  - Gap 3: (19, 14)
- Step 4: Land on North Plateau at (16, 11).
- Step 5: Walk to (14, 10).
- Status: Surfing at (20, 30). Clearing text.

# Lessons Learned
- Pathing: Cianwood is a fortress of plateaus. Land routes to the North Plateau are blocked by vertical cliffs.
- Navigation: The Great Spiral is the only verified nautical path. Previous land route hypotheses failed due to impassable FLOOR_UP_WALL tiers.
- Tool Maintenance: find_path_v4 refined for medium consistency and unseen tile handling.