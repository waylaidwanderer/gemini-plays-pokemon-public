# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- Execution Plan (The Great Outer Sea Bypass):
  1. Surf North along Column 28 to Row 6.
  2. Hypothesis: There is a gap in the buoy ring at Column 26 (Rows 1-5). Test: Attempt to move West at Row 3.
  3. Hypothesis: There is a gap in the second buoy ring at Column 22 (Rows 6-8). Test: Attempt to move West at Row 8 if step 2 succeeds.
  4. If gaps exist: Surf West to (18, 11) and land at (16, 11).
  5. Walk West to (14, 11) and North to (14, 10).
- Battle Prep: Lead Calcifer (Lv64 Typhlosion).

# Tile Mechanics
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Requires SURF.
- LEDGE_HOP_DOWN: One-way (South). Blocks North.
- FLOOR_UP_WALL: Terrace. Walk ONTO from climb side to climb. Conclusion: Blocks jumping down from the north (Acts as wall). Allows horizontal movement while elevated.
- BREAKABLE ROCK: Requires ROCK SMASH.