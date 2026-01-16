# Strategy: Trigger Suicune Sighting (Started: Turn 51131)
- City Logic: Vertical walls partition the city into corridors. The inner sea channel at Column 14 is a clear, 1-tile wide water route to the northern coast. Internal buoy barriers block other water routes.
- Execution Plan (The Column 14 Surf Route):
  1. Walk to (13, 19) and face the water at (14, 19).
  2. Use SURF to enter the water channel.
  3. Surf North along Column 14 to Row 11.
  4. Land on the northern coast at (14, 11).
  5. Walk to (14, 10) to trigger the Suicune sighting event.
- Battle Prep: Lead Calcifer (Lv64 Typhlosion) for potential encounter with Eusine.

# Tile Mechanics & Verification
- FLOOR: Standard traversable tile.
- WALL / BUOY: Impassable collision.
- WATER: Traversable only while using SURF. Shorelines are adjacent FLOOR/WATER tiles.
- LEDGE_HOP_DOWN: One-way passage (South only). Jump FROM the ledge tile to the tile below it.
- FLOOR_UP_WALL (Terrace): Walk ONTO from the south (climb up). Hypothesis: Allows horizontal (East/West) movement while on the elevated tier. Blocked from the North.
- ROCK (Object): Impassable until cleared with ROCK SMASH. Rocks respawn upon map re-entry or Fly.

# Map Layout Notes
- Western Corridor (X=0-2): Primary land route to the north, accessible via Row 51 highway.
- Column 14 Channel: The only confirmed water route bypassing internal city walls.
- Row 13 & 15 Walls: Major land barriers partitioning the city.
- Southern Highway: Row 51 connects all land corridors.

# Map Markers (Summary)
- Suicune Sighting: (14, 10)
- Surf Shore: (13, 19)
- Breakable Rocks: (8, 16), (9, 17), (10, 27), (4, 19)
- Key Buildings: Seer (5, 17), Studio (9, 31), Pharmacy (15, 47), Gym (8, 43)