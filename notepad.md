# Strategy: Trigger Suicune Sighting (Started: Turn 51131, Turn 51301 - Resumed)
- City Logic: Vertical walls divide the city. The Western Corridor (X=0-2) is the main land route to the north, but requires a long detour to Row 51 or using Surf to bypass walls.
- Execution Plan:
  1. Walk South to (12, 44).
  2. Walk West to (6, 44), then North to (6, 42).
  3. Walk West to (4, 42), then South to (4, 44).
  4. Walk West to (2, 44), then North to (2, 12).
  5. Walk East to (14, 12), then North to (14, 10) for the Suicune sighting.

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM ledge to tile below.
- FLOOR_UP_WALL: One-way passage (North only). Walk ONTO from south or walk North from it.
- ROCK (Object): Impassable until cleared with ROCK SMASH.

# Game Systems
## Menu Navigation
- Start Menu: 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. PLAYER, 6. SAVE, 7. OPTION, 8. EXIT.
- Party Menu: 1-6. Pokemon, 7. CANCEL.
- Navigation: Pressing Up from the first item wraps to the last item.

# Discoveries
- Tully has an item for me on Route 42.
- Smashed Rocks: (5, 29), (4, 25).
- Suicune sighting spot: (14, 10).