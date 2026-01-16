# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- City Logic: Vertical walls partition the city. Row 51 is the only continuous horizontal highway. Gaps in the Row 50 terraces exist at X=11 and X=20.
- The Grand Loop (Execution Plan):
  1. Surf South to (11, 26) and land.
  2. Walk South to (11, 51) (Gap in Row 50 terrace).
  3. Walk West along Row 51 to (2, 51) (Western Corridor).
  4. Walk North through the Western Corridor to (2, 14).
  5. Walk East to (8, 14), then North to (8, 12) (Gap in Row 13).
  6. Walk East along Row 12 to (14, 12), then North to (14, 10) for Suicune.
- Mechanic Verification:
  - Terrace (FLOOR_UP_WALL): Test horizontal movement at (6, 46) or (6, 34).
  - Ledge (LEDGE_HOP_DOWN): Jump Down from (10, 15) to confirm blockage from North.
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM ledge to tile below.
- FLOOR_UP_WALL: Terrace/Slope. Walk ONTO from south to climb. Hypothesis: Allows horizontal movement. Blocked from North.
- ROCK (Object): Impassable until cleared with ROCK SMASH.

# Map Markers (Key Points)
- (12, 28): 🏄 Surf spot to inner sea
- (14, 10): 🎯 Suicune Sighting Spot
- (6, 34): 🧗 Terrace Gap (Verification Target)
- (11, 50): 📍 Southern Gap (Row 50)
- (8, 13): 📍 Northern Gap (Row 13)