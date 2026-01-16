# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- City Logic: Vertical walls partition the city. Row 51 is a horizontal highway connecting all corridors. Gaps in the Row 50 terraces exist at X=11 and X=20.
- Execution Plan (The Grand Loop):
  1. Walk South to (11, 51) (Gap at Row 50).
  2. Walk West along Row 51 to (2, 51) (Western Corridor).
  3. Walk North through the Western Corridor to Row 12.
  4. Walk East along Row 12 to (14, 12), then North to (14, 10).
- Mechanic Verification:
  - Hypothesis: FLOOR_UP_WALL tiles allow horizontal movement (East/West).
  - Test: Once on a terrace (e.g., Row 46 or 50), try moving Left/Right.

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM ledge to tile below.
- FLOOR_UP_WALL: Terrace/Slope. Walk ONTO from south to climb. Allows horizontal movement. Blocked from North.
- ROCK (Object): Impassable until cleared with ROCK SMASH.

# Map Markers (Key Points)
- (12, 28): 🏄 Surf spot to inner sea
- (6, 34): 🧗 Terrace Gap (Verification Target)
- (11, 33): 🏝️ Grand Loop Landing Spot
- (8, 13): 📍 Northern Gap (X=8)