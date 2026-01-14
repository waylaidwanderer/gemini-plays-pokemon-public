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

# Fly Navigation (Grid Step Theory)
- Map: Town Map (Fly).
- Rule: 7 directional taps = 1 coordinate unit.
- Evidence: 14 taps moved cursor from New Bark (14, 10) to Cherrygrove (12, 10).
- Target: Cianwood (0, 9).
- Math: 14 units West (98 taps), 1 unit North (7 taps).
- Progress: 1/98 Lefts.
- Failed Fly attempts: 58.
- Timestamp: Turn 48031. Quest started Turn 47680.

# Quest Strategies
## Suicune: 'The Great Spiral' (The Only Real Path)
- Fact: The northern plateau is walled off from the south and west. The buoy maze is the only intended entrance.
- Shortcut Hypothesis: Suicune (7, 4) reachable via beach at X=2. Gap at Y=33/35 needs re-verification in Cianwood.
- Route: Fly to Cianwood -> Walk to beach at X=2 -> Walk North to Suicune at (7, 4).
- Preparation: Lead with XENON (Haunter). Use SUPER REPEL.
- Capture Strategy: Use XENON's Hypnosis to sleep Suicune. Lower HP with GORP's Body Slam (careful not to KO) or Night Shade. Throw Ultra Balls.

# Reflection Turn 48031
- Strategy: Moving Fly cursor in manual chunks of 24 taps (48 buttons total including sleeps) to stay under the 50-button limit.
- Lessons: Fly map navigation is based on a sub-grid (7 taps/unit). 1 tap moves the cursor visually but doesn't change city text until the unit threshold is met.
- Root Hypothesis Check: Fly to Cianwood is valid; execution failed due to coordinate scaling misunderstanding.
- Verification: Analyst claims 1 tap = 1 city, but observation proves 1 tap < 1 city. Trusting observation.