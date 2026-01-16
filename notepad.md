# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- Objective: Reach (14, 10) on the northern coast.
- The Grand Loop (Execution Plan):
  1. Walk to (12, 47) (Bypass wall at (11, 30)).
  2. Walk West to (6, 47) and North onto the terrace at (6, 46).
  3. Test horizontal movement: Walk West from (6, 46) to (2, 46).
  4. If successful, walk North through the Western Corridor (Column 2) to (2, 12).
  5. Walk East along the Row 12 Highway to (14, 12).
  6. Walk North to (14, 10) to trigger Suicune sighting.
- Mechanic Verification (Priority):
  - Hypothesis: FLOOR_UP_WALL (Terrace) allows horizontal movement.
  - Test: At (6, 46), attempt to move West to (5, 46).
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Requires SURF.
- LEDGE_HOP_DOWN: One-way (South). Blocks North.
- FLOOR_UP_WALL: Terrace. Walk ONTO from South to climb. Blocks South from North. Hypothesis: Allows horizontal movement.
- ROCK (Object): Impassable until cleared with ROCK SMASH.

# Map Markers (Key Points)
- (12, 28): 🏄 Surf spot to inner sea
- (11, 33): 🏝️ Grand Loop Landing Spot
- (8, 13): 📍 Northern Gap (X=8)
- (15, 37): 🏠 Lugia Speech House
- (15, 47): 💊 Pharmacy (SecretPotion)
- (17, 33): 👤 Pokefan M (Rock Smash)
- (23, 43): 🏥 Pokemon Center
- (8, 43): 🥊 Cianwood Gym