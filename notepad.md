# Strategy: Trigger Suicune Sighting (Started: Turn 51131, Turn 51359 - Resumed)
- City Logic: Vertical walls partition the city. Gaps exist at X=8 (Row 13) and X=13 (Row 13).
- The Center Shortcut (Execution Plan):
  1. Land at (11, 20).
  2. Walk South to (11, 25), then West to (4, 25).
  3. Walk North to (4, 21), then West to (2, 21).
  4. Walk North to (2, 14) (Western Corridor).
  5. Walk East to (8, 14), then North to (8, 12) (Gap at X=8).
  6. Walk East to (14, 12), then North to (14, 10) for Suicune.
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM ledge to tile below.
- FLOOR_UP_WALL: One-way passage (North only). Walk ONTO from south or walk North from it.
- ROCK (Object): Impassable until cleared with ROCK SMASH.

# Discoveries
- Smashed Rocks: (5, 29), (4, 25).
- Suicune sighting spot: (14, 10).
- Respawned Rocks: (8, 16), (9, 17), (10, 27).