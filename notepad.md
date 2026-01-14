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

- Status: At (25, 5) in Cherrygrove; Fly map open. Cursor on New Bark Town (Tile X=14, Y=10).
- Verified Fly Map Math: 7 taps = 1 Tile unit.
- Evidence: 14 taps moved cursor from New Bark (X=14) to Cherrygrove (X=12) in Turn 47978.
- Target: Cianwood City (Tile X=0, Y=9).
- Total Distance: 14 tiles West (98 taps), 1 tile North (7 taps).
- Progress: 1/98 Left taps sent.
- Flight Plan: Send 49 Left taps this turn (reaching 50/98).
- Timestamp: Turn 48023. Quest started Turn 47680.

# Quest Strategies
## Suicune: 'The Great Spiral' (The Only Real Path)
- Fact: The northern plateau is walled off from the south and west. The buoy maze is the only intended entrance.
- Shortcut Hypothesis: Suicune (7, 4) reachable via beach at X=2. Gap at Y=33/35 needs re-verification in Cianwood.
- Route: Fly to Cianwood -> Walk to beach at X=2 -> Walk North to Suicune at (7, 4).
- Preparation: Lead with XENON (Haunter). Use SUPER REPEL.

# Reflection Turn 48000
- Deferrals: None.
- Automation: fly_to_city_stable refined with sleeps.
- Strategy: Pivoting to City Grid theory for Fly navigation.
- Lessons: Fly map navigation is city-based, not tile-based.
- Root Hypothesis Check: Fly to Cianwood is valid; execution failed due to coordinate misunderstanding.
- Bias Check: Abandoned tool too early; now refining it with correct logic.