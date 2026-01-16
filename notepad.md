# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- City Logic: Vertical walls partition the city. Gaps exist at X=9 (Row 33), X=5 (Row 34-37), X=8 (Row 13), and X=13 (Row 13).
- Mechanic Verification:
  1. Hypothesis: FLOOR_UP_WALL tiles allow horizontal movement (East/West).
  2. Test: Walk onto (6, 34) from (6, 35), then move West to (5, 34).
- Execution Plan (The Grand Loop):
  1. Walk to (9, 33) (Gap at X=9).
  2. Walk West to (6, 33), then South to (6, 35).
  3. Walk North onto (6, 34) and West to (5, 34) (Gap at X=5).
  4. Walk West to (2, 34) (Western Corridor).
  5. Walk North to (2, 14), then East to (8, 14).
  6. Walk North through the gap at (8, 13) to (8, 12).
  7. Walk East along Row 12 to (14, 12), then North to (14, 10).
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM ledge to tile below.
- FLOOR_UP_WALL: Terrace/Slope. Walk ONTO from south to climb. Hypothesis: Allows horizontal movement.
- ROCK (Object): Impassable until cleared with ROCK SMASH.