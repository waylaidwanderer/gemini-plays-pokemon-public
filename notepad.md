# Strategy: Trigger Suicune Sighting (Started: Turn 51131, Turn 51331 - Refined Plan)
- City Logic: Vertical walls and buoy barriers partition the city. No direct water path exists to the northern coast.
- The Grand Loop (Execution Plan):
  1. Surf to (24, 32) and land at (23, 32).
  2. Walk West to (12, 32), then North to (12, 35).
  3. Walk West to (2, 35) (through gap in X=5 wall).
  4. Walk North to (2, 14) (through the Western Corridor).
  5. Walk East to (8, 14), then North to (8, 10).
  6. Walk East to (14, 10) for the Suicune sighting.

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