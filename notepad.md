# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- The Grand Loop & Mechanic Test (Execution Plan):
  1. Walk North to (12, 47), then West to (8, 47).
  2. Walk South to (8, 48), then West to (6, 48).
  3. Walk South to (6, 51) (Highway), then East to (12, 51).
  4. Mechanic Test: Walk North onto terrace at (12, 50), then try moving West to (11, 50).
  5. If horizontal works: Walk West along terraces to (2, 50), then North to (2, 14).
  6. If not: Walk West along Row 51 to (2, 51), then North through Western Corridor to (2, 14).
  7. Walk East along Row 14 to (8, 14), then North through gap at (8, 13) to (8, 12).
  8. Walk East along Row 12 Highway to (14, 12), then North to (14, 10).
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable.
- WATER: Requires SURF.
- LEDGE_HOP_DOWN: One-way (South). Blocks North.
- FLOOR_UP_WALL: Terrace. Walk ONTO from South to climb. Blocks South from North. Hypothesis: Allows horizontal movement while elevated.
- ROCK (Object): Impassable until cleared with ROCK SMASH.