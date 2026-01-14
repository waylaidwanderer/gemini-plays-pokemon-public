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
- FLOOR_UP_WALL: Blocks entry from the NORTH (tested at (19, 50)). One-way barrier.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH. Verified at (10, 15).
- COUNTER: Impassable.

# Suicune Quest
- Start Turn (Cianwood Re-attempt): 47450
- Status: Sighting 2 (Cianwood North Beach) in progress.
- Land Route Discovery (Turn 47541): The only way to reach the north beach (7, 4) is via the west corridor (X=2). To reach it from the center, one must go south to Row 51 via the gap at (21, 50), then west to X=2, then all the way north.
- Plan:
    1. Navigate to (21, 51) via (27, 45) and (27, 47) loop.
    2. Follow Row 51 west to (2, 51).
    3. Follow X=2 corridor north to (2, 4).
    4. Trigger Suicune sighting at (7, 4).
- Sighting 1: Burned Tower (DONE)
- Battle Strategy: Use XENON (Haunter) for Hypnosis. Chip HP with fixed damage moves if needed.

# Lessons Learned
- (23, 46) is a FLOOR_UP_WALL, not a ledge. The 'Ledge' marker was a hallucination.
- Southern detours are blocked by one-way walls at Row 50.
- Northern land route is blocked by Row 15 wall.
- Eastern water channel has gaps in buoy walls at (23, 15) and (21, 9).