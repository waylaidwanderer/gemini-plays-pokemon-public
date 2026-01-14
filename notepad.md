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
- FLOOR_UP_WALL: Impassable from the NORTH. Verified at (16, 10) and (4, 30).
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH. Verified at (10, 15).
- COUNTER: Impassable.

# Suicune Quest Strategy: 'The Grand Loop'
- Goal: Reach Suicune sighting area at (7, 4).
- Problem: The city is divided by vertical walls and one-way barriers (FLOOR_UP_WALL). Direct access to the west coast from (6, 33) is blocked.
- Pathing Logic:
    1. Move East to (12, 33) to clear the X=9 wall.
    2. Move South to Row 44 to find the gap in the X=11 wall.
    3. Move West to (9, 44) to cross into the central strip.
    4. Move South to Row 48 to find the gap in the X=7/5 walls.
    5. Move West to (2, 48) to reach the far west coastal corridor.
    6. Walk North along X=2 to Row 14.
    7. Move East to (7, 14), then North to the sighting area at (7, 4).
- Battle Strategy: Lead with XENON (Haunter) for Hypnosis. Be ready for Eusine.
- Status: Moving to (12, 33).