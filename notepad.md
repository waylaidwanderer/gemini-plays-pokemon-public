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

# Strategic Plan: The Great Spiral (Turn 48223)
- Goal: Trigger Suicune sighting at (14, 10).
- Trek Start: Turn 48203.
- Step 1: Reach Outer Channel at (27, 30). (Done)
- Step 2: Use Super Repel. (Done)
- Step 3: Navigate Buoy Maze Gaps:
  - Gap 1: (22, 16) - Outer to Inner Channel. (In Progress)
  - Gap 2: (19, 14) - Inner to Approach Channel.
  - Gap 3: (18, 14) - Clear X=18 buoy line.
  - Gap 4: (17, 11) - Clear X=17 wall (Hypothesized).
- Step 4: Land on North Plateau at (16, 11).
- Step 5: Walk to (14, 10).

# Verified Landmarks
- Gaps: (26, 10), (22, 16), (19, 14), (18, 14).
- Plateau Landing: (16, 11-14).
- Sighting Spot: (14, 10).
- Land Shortcut (Backup): Reach Row 51 via (20, 50), walk West to X=2, then North.

# Custom Tools (Technical Details)
- find_path_v4: BFS pathfinder. Handles LAND vs WATER medium consistency. Treats unseen tiles as traversable within the starting medium. Handles LEDGE_HOP_DOWN as one-way (dy=1).
- menu_navigator_v2_fixed: Sequence-based button presser for deep menu navigation.