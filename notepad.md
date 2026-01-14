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

- Status: At (25, 5) in Cherrygrove; Fly map open. Cursor on New Bark Town (14, 10).
- Fly Map Rule: 7 directional taps = 1 unit of distance. (Verified: 14 taps = 2 units from New Bark to Cherrygrove).
- Flight Plan: Move cursor 14 units West (98 taps) and 1 unit North (7 taps) from New Bark to reach Cianwood (0, 9).
- Progress: 0/98 Lefts (Previous Turn 48021 taps failed to register due to lack of sleeps).
- Current Action: Sending 25 Lefts with 200ms sleeps. (Chunk 1/4).
- Timestamp: Turn 48022. Quest started Turn 47680.

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