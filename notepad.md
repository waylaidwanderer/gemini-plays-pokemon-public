# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- City Logic: Vertical walls partition the city. Gaps exist at (11, 33), (8, 33), (5, 34-37), and (8/13, 13).
- Mechanic Verification:
  1. Hypothesis: FLOOR_UP_WALL tiles allow horizontal movement (East/West).
  2. Test: Walk onto (6, 34) from (6, 35), then move West to (5, 34).
- Execution Plan (The Grand Loop):
  1. Land at (11, 26).
  2. Walk to (11, 33).
  3. Walk West to (6, 33).
  4. Walk South to (6, 35), then North onto (6, 34) (Terrace).
  5. Walk West to (2, 34) (Western Corridor).
  6. Walk North to (2, 12), then East to (14, 12).
  7. Walk North to (14, 10) for Suicune.
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
- (6, 34): 🧗 Terrace Gap (Verification Target)
- (11, 33): 🏝️ Grand Loop Landing Spot
- (8, 13): 📍 Northern Gap (X=8)