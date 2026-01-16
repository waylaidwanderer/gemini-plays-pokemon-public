# Strategy: Trigger Suicune Sighting (Started: Turn 51131, Turn 51364 - Resumed)
- City Logic: Vertical walls and buoy barriers partition the city. The Outer Sea (X=24+) is the only confirmed water route to the northern coast. Row 32 is a major horizontal highway.
- Execution Plan (The Outer Sea Highway):
  1. Walk to (23, 32) and face the water at (24, 32).
  2. Use SURF to enter the Outer Sea.
  3. Surf North to Row 21, then East to X=27 (clears buoy barriers).
  4. Surf North at X=27 to Row 8 (clears Row 9 buoy barrier).
  5. Surf West to X=14, then South to land at (14, 11).
  6. Walk to (14, 10) for Suicune.
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics & Verification
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF. Shorelines are adjacent FLOOR/WATER tiles.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM the ledge tile to the tile below it.
- FLOOR_UP_WALL (Terrace): Walk ONTO from the south (climb up). Hypothesis: Allows horizontal (East/West) movement while on the elevated tier. Blocked from the North.
- ROCK (Object): Impassable until cleared with ROCK SMASH. Rocks respawn upon map re-entry or Fly.

# Map Layout Notes
- Western Corridor (X=0-2): Primary land route to the north, accessible via Row 51 highway.
- Column 14 Channel: The only confirmed water route bypassing internal city walls.
- Row 13 & 15 Walls: Major land barriers partitioning the city.
- Southern Highway: Row 51 connects all land corridors.

# Map Markers (Summary)
- Suicune Sighting: (14, 10)
- Surf Shore: (13, 19)
- Breakable Rocks: (8, 16), (9, 17), (10, 27), (4, 19)
- Key Buildings: Seer (5, 17), Studio (9, 31), Pharmacy (15, 47), Gym (8, 43)