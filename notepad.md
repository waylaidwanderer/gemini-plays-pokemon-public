# Strategy: Trigger Suicune Sighting (Started: Turn 51131, Turn 51369 - Resumed)
- City Logic: Vertical walls partition the city into corridors. Gaps in the walls exist at (5, 34-37), (8, 13), and (13, 13). Row 15 is clear at (0-2, 15) and (11, 15).
- The Western Gap Route (Execution Plan):
  1. Walk West to (6, 21), then South to (6, 35).
  2. Walk West to (2, 35) (Gap in X=5 wall).
  3. Walk North through the Western Corridor (X=2) to (2, 14).
  4. Walk East to (8, 14), then North to (8, 12) (Gap in Row 13).
  5. Walk East along Row 12 to (14, 12), then North to (14, 10) for Suicune.
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics & Verification
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM the ledge tile to the tile below it.
- FLOOR_UP_WALL (Terrace): Walk ONTO from the south (climb up). Hypothesis: Allows horizontal (East/West) movement while on the elevated tier. Blocked from the North.
- ROCK (Object): Impassable until cleared with ROCK SMASH. Rocks respawn upon map re-entry or Fly.

# Map Markers (Summary)
- Suicune Sighting: (14, 10)
- Surf Shore: (12, 28)
- Breakable Rocks: (8, 16), (9, 17), (10, 27), (4, 19)
- Key Buildings: Seer (5, 17), Studio (9, 31), Pharmacy (15, 47), Gym (8, 43)