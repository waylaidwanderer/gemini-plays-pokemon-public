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
- FLOOR_UP_WALL: Blocks NORTHWARD movement (entry from below, exit to above). SOUTHWARD entry is likely possible. Strategy: Use southern detour at Row 51 if water route is blocked.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH. Verified at (10, 15).
- COUNTER: Impassable.

# Suicune Quest
- Start Turn (Cianwood Re-attempt): 47450
- Sighting 1: Burned Tower (DONE)
- Sighting 2: Cianwood City (In Progress)
- Battle Strategy: Use XENON (Haunter) to inflict Hypnosis. Switch to a lower-level Pokemon if needed to chip HP, or use Night Shade for fixed damage.
- Current Status: Solution discovered! Southern detour via ledge at (23, 46) to reach Row 51, then west path (X=2) to north beach.

# Suicune Quest - Movement Test (Turn 47526)
- Hypothesis: FLOOR_UP_WALL tiles (like at (6, 46)) can be entered from the NORTH (moving SOUTH). This allows a southern detour to reach the west path (X=2).
- Test: Navigate to (6, 45) and attempt to move DOWN to (6, 46).
- Rationale: The northern part of the island is blocked by a wall at Row 15. The west path (X=2) is the only land route to the north beach.

# Water Route Discovery (Turn 47531)
- Buoy Wall Gaps:
    - Row 15: Gap at X=23.
    - Row 9: Gap at X=21 and X=27.
- Strategy: Surf from (21, 23) -> (23, 23) -> (23, 15) -> (21, 15) -> (21, 9) -> (7, 9) -> (7, 4).
- Advantage: Bypasses all land walls and one-way ledges.