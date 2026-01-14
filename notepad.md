# PC Storage (Box 1)
- DAPXWW (LARVITAR): Lv20
- GLAIVE (SCYTHER): Lv14
- SELKIE (SEEL): Lv24
- DELTA (MANTINE): Lv20
- RANGOON (KRABBY): Lv22
- NOMURA (TENTACOOL): Lv17
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- Ouroboros (DRATINI): Lv15
- AAAAAAAAAA (SPINARAK): Lv13
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard walkable ground. Verified at (25, 5) and (29, 4) in Cherrygrove.
- WATER: Traversable only via Surf.
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- HEADBUTT_TREE: Special tree that can be interacted with using Headbutt.
- DOOR: Warp point to an interior.
- FLOOR_UP_WALL: Represents a ledge face. Impassable from ALL directions.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH.
- (11, 14): Dead End Pocket in Cianwood. Wall at (11, 13) and (12, 14) blocks access to the north plateau.
- (11, 15): Gap in the city wall (Y=15) in Cianwood. Accesses the beach area but not the plateau. Verified in Turn 47337.

# Fly Navigation (City Grid Theory)
- The Fly map uses a discrete city-to-city grid, NOT a tile-by-tile coordinate system.
- One directional press = One city jump.
- East-West City Order (X-axis):
  - Cianwood (0)
  - Olivine (1)
  - Goldenrod (2)
  - Ecruteak (3)
  - Violet (4)
  - Cherrygrove (5)
  - New Bark (6)
- North-South City Order (Y-axis):
  - Lake of Rage (0)
  - Mahogany (1)
  - Blackthorn (2)
  - ... (Needs verification)
- Navigation from New Bark (6) to Cianwood (0): 6 Lefts. (Analyst suggests 5, testing both).
- Failed Fly attempts: 58 (Reason: Used tile-based coordinate math instead of city-based grid).
- Current Plan: Move to (25, 5) -> Open Fly map -> Test city-by-city movement.
- Timestamp: Turn 48013. Quest started Turn 47680.

# Quest Strategies
## Suicune: 'The Great Spiral' (The Only Real Path)
- Fact: The northern plateau is walled off from the south and west. The buoy maze is the only intended entrance.
- Shortcut Hypothesis: Suicune (7, 4) reachable via beach at X=2. Requires verification of north/south wall at Y=10-20.
- Route:
    1. Fly to Cianwood.
    2. Land at (15, 44) (Center) or (23, 44) (South).
    3. Walk to beach at X=2.
    4. Walk North to Suicune at (7, 4).
- Preparation: Lead with XENON (Haunter). Use SUPER REPEL.

# Reflection Turn 48000
- Deferrals: None.
- Automation: fly_to_city_stable refined with sleeps.
- Strategy: Pivoting to City Grid theory for Fly navigation.
- Lessons: Fly map navigation is city-based, not tile-based.
- Root Hypothesis Check: Fly to Cianwood is valid; execution failed due to coordinate misunderstanding.
- Bias Check: Abandoned tool too early; now refining it with correct logic.