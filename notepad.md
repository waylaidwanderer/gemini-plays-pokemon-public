# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- Objective: Reach (14, 10) via land to bypass buoy and wall barriers.
- Execution Plan (The X=11 Corridor):
  1. Use SURF at (11, 26) to cross Row 22-25 water; land at (11, 21).
  2. Walk North along X=11 to (11, 12).
  3. Walk East to (14, 12), then North to (14, 10).

# Mechanic Verification
- Hypothesis: FLOOR_UP_WALL (Terrace) allows horizontal movement.
- Test: Walk onto (4, 20) from (4, 21), then move West to (3, 20).

# Tile Mechanics (Verified)
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Blocks North.
- FLOOR_UP_WALL: Terrace. Walk ONTO from south to climb. Blocks South from North.
- ROCK (Object): Impassable until cleared with ROCK SMASH.

# Map Markers Reference
- (12, 28): 🏄 Surf spot to inner sea
- (11, 33): 🏝️ Grand Loop Landing Spot
- (8, 13): 📍 Northern Gap (X=8)
- (15, 37): 🏠 Lugia Speech House
- (15, 47): 💊 Pharmacy (SecretPotion)
- (17, 33): 👤 Pokefan M (Rock Smash)
- (23, 43): 🏥 Pokemon Center
- (8, 43): 🥊 Cianwood Gym