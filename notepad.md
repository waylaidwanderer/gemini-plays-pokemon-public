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
- FLOOR: Standard walkable ground. Verified in Cherrygrove.
- WATER: Traversable only via Surf.
- BUOY: Impassable water obstacle.
- WALL: Impassable obstacle.
- HEADBUTT_TREE: Special tree that can be interacted with using Headbutt.
- DOOR: Warp point to an interior.
- FLOOR_UP_WALL: Represents a ledge face. Impassable from ALL directions.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH.
- (11, 14): Dead End Pocket in Cianwood. Wall at (11, 13) and (12, 14) blocks access to the north plateau.
- (11, 15): Gap in the city wall (Y=15) in Cianwood. Accesses the beach area but not the plateau. (Needs re-verification).

# Fly Navigation (Testing Phase)
- Map: Town Map (Fly).
- Hypothesis: 1 directional tap = 1 coordinate unit (Tile on Town Map grid).
- Target: Cianwood (0, 9).
- Start: New Bark (14, 10).
- Displacement: 14 units West, 1 unit North.
- Failed Fly attempts: 59.
- Current Test: Press B to clear UI, then 15 Left taps to check for destination name change.

# Quest Strategies
## Suicune: 'The Great Spiral'
- Fact: The northern plateau is walled off from the south and west. The buoy maze is the only intended entrance.
- Shortcut Hypothesis: Suicune (7, 4) reachable via beach at X=2. Requires verification of north/south wall at Y=10-20.
- Route: Fly to Cianwood -> Walk to beach at X=2 -> Walk North to Suicune at (7, 4).
- Preparation: Lead with XENON (Haunter). Use SUPER REPEL.
- Capture Strategy: Use XENON's Hypnosis to sleep Suicune. Lower HP with GORP's Body Slam (careful not to KO) or Night Shade. Throw Ultra Balls.