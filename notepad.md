# Tile Mechanics
- FLOOR: Standard walkable ground. Verified.
- TALL_GRASS: Walkable, may trigger wild battles. Verified.
- WATER: Traversable only while Surfing. 
- WALL / BUOY: Impassable.
- FLOOR_UP_WALL: Impassable from the NORTH. Verified.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH. Verified.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable (becomes FLOOR when cut). Verified.
- FRUIT_TREE: Impassable. Interact to obtain Apricorns. Verified.
- CAVE / WARP_CARPET: Warp to another map.
- COUNTER: Impassable. Used to interact with NPCs.

# Suicune Quest
- Status: 16 Badges, Clear Bell in inventory.
- Start Turn (Route 42 Grove): 47288 (Failed), Re-attempt 1: 47418 (Failed - missed trigger?), Re-attempt 2 (Verify Cianwood): 47450.
- Sighting Progress (Sequential):
    1. Burned Tower (DONE)
    2. Cianwood City (VERIFYING - Sighting and Eusine battle required)
    3. Route 42 (Middle Grove) - PENDING (Requires Cianwood event first)
    4. Route 25 (Kanto, near Bill's House) - LOCKED
- Strategy:
    - Sighting order is strictly linear: Burned Tower -> Cianwood -> Route 42 -> Route 25 -> Tin Tower.
    - Suicune stays in the Route 42 grove until approached.
- Backtracking Plan (HOW):
    - Fly to Ecruteak City.
    - Head East through the gatehouse to Route 42.
    - Use Cut on the tree at (24, 13) to enter the grove.
    - Approach the center of the grove (approx. (28, 15)) to trigger Suicune fleeing.
- General Lessons:
    - Route 36 is NOT a Suicune sighting location in Pokemon Crystal.
    - Red is NOT defeated (Team levels Lv44-64). Victory over Red requires higher levels.
    - Fly Tool: 'fly_list_navigator_v3_fixed' calibrated for Johto (Up increases index).

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

# Suicune Quest - Cianwood Verification
- Turn 47472 (Start): Expert advisor confirms Cianwood is the next sighting. Previous markers (Done/Confirmed) are likely incorrect.
- Land Route Discovery: (11, 26) is on an eastern peninsula. To reach the north beach (7, 4), one must travel south to Row 51, cross west to Col 4, then north to (2, 46) and follow the west path (X=2) north.
- Plan:
    1. Navigate to (2, 46) via the southern detour (Row 51).
    2. Follow the west path (X=2) all the way north to the beach.
    3. Trigger Suicune event and Eusine battle.
- Observation: (9, 18) is a dead-end pocket blocked by rocks and one-way walls.