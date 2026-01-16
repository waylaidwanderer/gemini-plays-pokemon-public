# Strategy: Trigger Suicune Sighting (Started: Turn 51131, Turn 51318 - Refined Plan)
- Quest Start: Turn 51131.
- City Logic: Vertical walls divide the city. The Outer Sea (X=24+) is the most reliable route to the northern coast, bypassing internal barriers.
- Execution Plan:
  1. Surf North to (24, 21), then East to (27, 21) to clear the Row 15 buoy barrier.
  2. Surf North to (27, 8) to clear the Row 9 buoy barrier.
  3. Surf West to (14, 8), then South to (14, 11).
  4. Land at (14, 11) and walk to (14, 10) for the Suicune sighting.

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