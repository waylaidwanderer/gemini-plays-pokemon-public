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
- Current Plan: Surf through the gap at (23, 15), then head north to Row 8 and west to the north beach (7, 4).
- Verification (Turn 47549): Eastern water channel has a confirmed gap at (23, 15) in the buoy wall. Column 22 also has a gap at Row 8. This bypasses all land barriers.
- Goal: Reach (7, 4) to trigger Suicune sighting and battle Eusine.
- Sighting 1: Burned Tower (DONE)
- Battle Strategy: Use XENON (Haunter) for Hypnosis. Chip HP with fixed damage moves if needed.

# Lessons Learned
- (23, 46) is a FLOOR_UP_WALL, not a ledge. The 'Ledge' marker was a hallucination.
- Southern detours are blocked by one-way walls at Row 50.
- Northern land route is blocked by Row 15 wall.
- Eastern water channel has gaps in buoy walls at (23, 15) and (21, 9).