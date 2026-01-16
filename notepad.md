# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- City Logic: Vertical walls partition the city into corridors. The inner sea is a dead end due to buoy barriers. Land gaps exist at (11, 33), (8, 33), (5, 34-37), and (8/13, 13).
- Mechanic Verification:
  - Hypothesis: FLOOR_UP_WALL tiles allow horizontal movement (East/West).
  - Test: Walk onto (6, 34) from (6, 35), then try moving West to (5, 34).
- The Grand Loop (Execution Plan):
  1. Surf South to (11, 32) and land at (11, 33).
  2. Walk West to (8, 33) (Gap), then to (6, 33).
  3. Walk South to (6, 35), then North onto (6, 34) (Terrace).
  4. Walk West to (2, 34) (Western Corridor).
  5. Walk North to (2, 12), then East to (14, 12).
  6. Walk North to (14, 10) for Suicune.
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM ledge to tile below.
- FLOOR_UP_WALL: Terrace/Slope. Walk ONTO from south to climb. Hypothesis: Allows horizontal movement. Blocked from North.
- ROCK (Object): Impassable until cleared with ROCK SMASH.

# Map Markers (Refined)
- (12, 28): 🏄 Surf spot to inner sea
- (14, 10): 🎯 Suicune Sighting Spot
- (6, 34): 🧗 Terrace Gap (Verification Target)
- (5, 35): 📍 Western Gap (X=5)
- (8, 13): 📍 Northern Gap (X=8)
- (11, 33): 🏝️ Grand Loop Landing Spot