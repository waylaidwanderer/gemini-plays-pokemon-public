# Strategic Plan: Mt. Silver & Red
- **Strategy (The HOW):**
    1. Explore the upper areas of SilverCaveRoom1 (Row 5 and above) to find the ladder to the next floor.
    2. Path: Head to the far-left corridor (X=0) via the bottom of the room (Row 34/35).
    3. Face Red at the peak.

# Progress Tracking
- Badges: 16/16.
- Mt. Silver Access: Unlocked.
- Task Started: Turn 43386. Goal: Reach (0, 34) to access the left corridor.

# Tile Mechanics (Global Reference)
- FLOOR: Walkable.
- WALL: Impassable.
- COUNTER: Blocks movement; interact from front.
- WATER: Requires Surf.
- TALL_GRASS: Wild encounters.
- DOOR/WARP: Map transitions.
- LEDGE_HOP_DOWN: One-way movement Down.
- LEDGE_HOP_RIGHT: One-way movement Right.
- FLOOR_UP_WALL: North edge is impassable. Cannot move North (Up) FROM the tile, or South (Down) ONTO the tile. Verified: (8, 20)->(8, 19) [Up] BLOCKED, (10, 33)->(10, 34) [Down] BLOCKED.

# Area Records: Silver Cave Room 1 (3_74)
- Entrance/Exit: (9, 33).
- Inventory: 19/20 slots used in Items pocket. 4/12 in Balls pocket.
- PC Box 1: 9/20.

# Party Status
- Calcifer (Lv64 Typhlosion) - Lead. Received Protein at Turn 43371.
- ICARUS (Lv19 Pidgeotto)
- XENON (Lv44 Haunter)
- KIMCHI (Lv51 Gloom)
- GORP (Lv50 Snorlax)
- GNEISS (Lv54 Graveler)

# Red Battle Strategy (Advisor Recommendations)
- Grind team to Lv 70+.
- Replace ICARUS (Lv19) with a high-level Water or Electric type (e.g., Suicune).
- Evolve KIMCHI (Gloom) using Sun Stone or Leaf Stone.
- Lead with GNEISS (Graveler) vs Pikachu (uses Earthquake).
- Teach GORP (Snorlax) Shadow Ball (TM02) vs Espeon.
- Use XENON (Haunter) for Curse vs Snorlax.

# Navigation Hypothesis: Left Corridor Access
- Observation: Currently at (8, 11). Row 11 is blocked by walls/ledges from accessing X=0.
- Hypothesis: Access to the far-left corridor (X=0) is only possible by walking along the bottom (Row 34 or 35).
- Test: Use find_path_v7_robust to reach (1, 35) from (8, 11).
- Conclusion: (In progress). Testing path via (3, 11) -> (0, 11).