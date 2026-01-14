# PC Storage (Box 1)
- DAPXWW (LARVITAR): Lv20
- GLAIVE (SCYTHER): Lv14
- SELKIE (SEEL): Lv24
- DELTA (MANTINE): Lv20
- RANGOON (KRABBY): Lv22
- NOMURA (TENTACOOL): Lv17
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- Ouroboros (DRATINI): Lv15 (ExtremeSpeed)
- AAAAAAAAAA (SPINARAK): Lv13
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Verified)
- FLOOR: Walkable.
- WALL / BUOY: Impassable.
- WATER: Traversable only via Surf.
- FLOOR_UP_WALL: Impassable from the NORTH.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH.
- COUNTER: Impassable.

# Suicune Quest Strategy: 'The Island Bypass'
- Goal: Reach Suicune at (7, 4).
- Fact: Northern water is isolated from southern/eastern water by buoy walls.
- Solution: Sail south to the land bridge at Y=30, walk across to the western channel, then sail north and land on the north beach.
- Route:
    1. From (23, 16), sail Down to (23, 30).
    2. Sail Left to (20, 30) and land at (19, 30).
    3. Walk West across the land bridge to (15, 30).
    4. Face Up and Surf into (15, 29).
    5. Sail North in the western channel to (15, 19).
    6. Sail West and land at (4, 19).
    7. Walk to (14, 10) and then (7, 4).
- Preparation: Lead with XENON (Haunter) for Hypnosis. Be ready for Eusine.
- Status: At (12, 30). Moving north along the western beach.
- Attempt 1 (Triple Gap Loop): Hallucinated/Incorrect. Gaps at (26, 10) and (23, 15) only lead to a sealed middle pocket.
- Attempt 2 (Island Bypass): Verified via Mental Map and run_code pathfinding. Currently walking north on the sand.
- Route:
    1. From (12, 30), walk north along the beach.
    2. Path found: (12, 30) -> (12, 29) -> (12, 28) -> (11, 28) -> (11, 27) -> (11, 26) -> (10, 26) -> (9, 26) -> (9, 25) -> (9, 24) -> (9, 23) -> (9, 22) -> (9, 21) -> (9, 20) -> (9, 19) -> (8, 19) -> (7, 19) -> (6, 19) -> (5, 19) -> (4, 19) -> (4, 20) -> (3, 20) -> (2, 20) -> (2, 19) -> (2, 18) -> (2, 17) -> (2, 16) -> (2, 15) -> (2, 14) -> (3, 14) -> (4, 14) -> (4, 13) -> (5, 13) -> (5, 12) -> (6, 12) -> (6, 11) -> (6, 10) -> (7, 10) -> (8, 10) -> (9, 10) -> (10, 10) -> (11, 10) -> (12, 10) -> (13, 10) -> (14, 10).
    3. Final approach: Walk to Suicune sighting area at (7, 4).
- Preparation: Lead with XENON (Haunter) for Hypnosis. Be ready for Eusine.