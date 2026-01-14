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

# Strategic Plan: The Southern Corridor Sprint (Turn 48205)
- Goal: Trigger Suicune sighting at (14, 10).
- Step 1: Land at (19, 30). (Done)
- Step 2: Walk to (21, 49).
- Step 3: Walk to (21, 51) via (21, 50).
- Step 4: Walk West to (4, 51).
- Step 5: Walk North to (4, 35).
- Step 6: Walk West to (2, 35).
- Step 7: Walk North to (2, 12).
- Step 8: Walk East to (14, 12) -> North to (14, 10).
- Status: Clearing Surf text at (19, 30).

# Lessons Learned
- Pathing: Cianwood is a fortress of plateaus. Row 51 is a low-level corridor connecting the east and west beaches.
- Navigation: Vertical cliffs (FLOOR_UP_WALL) block most north-south land movement. X=2 and X=4 are key corridors.
- Tool Maintenance: find_path_v4 refined for medium consistency and unseen tile handling.