# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- Objective: Reach (14, 10) on the northern coast.
- Current Route: The X=11/13 Weave.
  1. Surf at (11, 26) and land at (11, 21).
  2. Walk North along Column 11 to (11, 14).
  3. Walk East to (13, 14) and North to (13, 12) (via Gap at Row 13).
  4. Walk East to (14, 12) and North to (14, 10).
- Mechanic Verification (Priority):
  - Hypothesis: FLOOR_UP_WALL (Terrace) allows horizontal movement.
  - Test: Walk onto (12, 50) from (12, 51), then move West to (11, 50).
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable.
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