# Strategy: Trigger Suicune Sighting (Started: Turn 51131, Turn 51332 - Refined Plan)
- City Logic: Vertical walls and buoy barriers partition the city. No direct water path exists to the northern coast. Row 32 is a major horizontal highway.
- The Grand Loop (Execution Plan):
  1. Surf to (24, 32) and land at (23, 32).
  2. Walk West along Row 32 to (2, 32).
  3. Walk North through the Western Corridor (X=2) to Row 14.
  4. Walk East to (8, 14), then North to (8, 10).
  5. Walk East to (14, 10) for the Suicune sighting.

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