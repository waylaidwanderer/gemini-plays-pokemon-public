# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- Objective: Reach (14, 10) via land to bypass buoy and wall barriers.
- Strategic Route (The Grand Loop):
  1. Land at (11, 26).
  2. Walk South to (11, 51) (Highway).
  3. Walk West to (2, 51) (Western Corridor).
  4. Walk North to Row 14.
  5. Walk East to (8, 14), then North through gap at (8, 13).
  6. Walk East to (14, 12), then North to (14, 10).

# Mechanic Verification (Higher Priority than Navigation)
- Hypothesis 1: FLOOR_UP_WALL tiles allow horizontal movement (East/West).
- Hypothesis 2: FLOOR_UP_WALL tiles block movement from the North (cannot walk South onto them).
- Test Plan: Once at Row 46 or 50, attempt horizontal movement. Attempt to walk South onto a terrace from the North.

# Tile Mechanics (Verified)
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM ledge to tile below. Blocks North movement.
- FLOOR_UP_WALL: Terrace/Slope. Walk ONTO from south to climb. Blocks Down movement from North.

# Map Markers Reference
- (12, 28): 🏄 Surf spot to inner sea
- (14, 10): 🎯 Suicune Sighting Spot
- (11, 33): 🏝️ Grand Loop Landing Spot
- (8, 13): 📍 Northern Gap (X=8)
- (15, 37): 🏠 Lugia Speech House
- (15, 47): 💊 Pharmacy (SecretPotion source)
- (17, 33): 👤 Pokefan M (Rock Smash source)
- (23, 43): 🏥 Pokemon Center
- (8, 43): 🥊 Cianwood Gym
- (4, 19): 🪨 Breakable Rock (4, 19)
- (8, 16): 🪨 Breakable Rock (8, 16)
- (9, 17): 🪨 Breakable Rock (9, 17)
- (10, 27): 🪨 Breakable Rock (10, 27)