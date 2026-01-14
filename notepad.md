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
- Status: At (23, 16). Starting 'Island Bypass' route.
- Attempt 1 (Triple Gap Loop): Hallucinated/Incorrect. Gaps at (26, 10) and (23, 15) only lead to a sealed middle pocket.
- Attempt 2 (Island Bypass): Verified via Mental Map and run_code pathfinding. Starting now.