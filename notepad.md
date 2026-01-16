# Strategy: Trigger Suicune Sighting (Started: Turn 51131, Turn #51366 - Resumed)
- City Logic: Vertical walls partition the city into corridors. Row 51 is the primary horizontal highway.
- The Grand Loop (Execution Plan):
  1. Walk South to (11, 51) (Gap in Row 50 terrace).
  2. Walk West along Row 51 to (2, 51) (Western Corridor).
  3. Walk North through the Western Corridor to (2, 14).
  4. Walk East to (8, 14), then North to (8, 12) (Gap in Row 13).
  5. Walk East to (14, 12), then North to (14, 10) for Suicune.
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics & Verification
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM the ledge tile to the tile below it.
- FLOOR_UP_WALL (Terrace): Walk ONTO from the south (climb up). Allows horizontal (East/West) movement while on the elevated tier. Blocked from the North.
- ROCK (Object): Impassable until cleared with ROCK SMASH. Rocks respawn upon map re-entry or Fly.

# Map Layout Notes
- Western Corridor (X=0-2): Primary land route to the north, accessible via Row 51 highway.
- Southern Highway: Row 51 connects all land corridors.
- Row 13 & 15 Walls: Major land barriers partitioning the city. Gaps exist at X=8 (Row 13) and X=13 (Row 13).

# Map Markers (Summary)
- Suicune Sighting: (14, 10)
- Surf Shore: (12, 28)
- Breakable Rocks: (8, 16), (9, 17), (10, 27), (4, 19)
- Key Buildings: Seer (5, 17), Studio (9, 31), Pharmacy (15, 47), Gym (8, 43)