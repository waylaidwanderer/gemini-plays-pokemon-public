# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- Objective: Reach (14, 10) on the northern coast.
- The Grand Loop (Execution Plan):
  1. Walk South to (11, 51) via the gap at (11, 50).
  2. Walk West along the Row 51 Highway to (2, 51).
  3. Walk North through the Western Corridor (Column 2) to (2, 12).
  4. Walk East along the Row 12 Highway to (14, 12).
  5. Walk North to (14, 10) to trigger Suicune.
- Mechanic Verification (Priority):
  - Hypothesis: FLOOR_UP_WALL (Terrace) allows horizontal movement while elevated.
  - Test: Walk onto (12, 50) from (12, 51), then attempt to move West to (11, 50).
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Requires SURF.
- LEDGE_HOP_DOWN: One-way (South). Blocks North.
- FLOOR_UP_WALL: Terrace. Walk ONTO from South to climb. Blocks South from North. Hypothesis: Allows horizontal movement.

# Map Markers (Key Points)
- (14, 10): 🎯 Suicune Sighting Spot
- (11, 33): 🏝️ Grand Loop Landing Spot
- (8, 13): 📍 Northern Gap (X=8)
- (15, 37): 🏠 Lugia Speech House
- (15, 47): 💊 Pharmacy (SecretPotion)
- (17, 33): 👤 Pokefan M (Rock Smash)
- (23, 43): 🏥 Pokemon Center
- (8, 43): 🥊 Cianwood Gym