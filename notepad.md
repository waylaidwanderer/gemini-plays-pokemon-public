# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- Execution Plan (The Verified Land Route):
  1. Clear Surf text (Land at 28, 38 surfing).
  2. Surf North to (28, 44) and land at (27, 44).
  3. Walk West along Row 44 to (6, 44).
  4. Walk South to (6, 47) and North to (6, 46) (Climb Terrace).
  5. Walk West to Column 2 (Western Corridor).
  6. Walk North along Column 2 to Row 12.
  7. Walk East along Row 12 to (14, 12) and North to (14, 10).
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Requires SURF.
- LEDGE_HOP_DOWN: One-way (South). Blocks North.
- FLOOR_UP_WALL: Terrace. Walk ONTO from climb side to climb. Conclusion: Blocks jumping down from the north (Acts as wall). Allows horizontal movement while elevated.
- BREAKABLE ROCK: Requires ROCK SMASH.