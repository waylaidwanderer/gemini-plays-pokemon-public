# Tile Mechanics
- FLOOR: Standard walkable ground. Verified traversable.
- TALL_GRASS: Walkable, may trigger wild battles. Verified.
- WATER: Traversable only while Surfing. 
- WALL / BUOY: Impassable.
- FLOOR_UP_WALL: Impassable from the NORTH (e.g., (6, 46)). Verified.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH. Impassable from the SOUTH. Verified.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable (becomes FLOOR when cut). Verified regrows on map exit.
- FRUIT_TREE: Impassable. Interact to obtain Apricorns. Verified.
- CAVE / WARP_CARPET: Warp to another map (e.g. Mt. Mortar, Gatehouse).
- COUNTER: Impassable. Used to interact with NPCs from an adjacent tile.

# Suicune Quest
- Status: 16 Badges, Clear Bell in inventory, Red Defeated (Turn 44000).
- Start Turn (Route 42 Grove): 47288.
- Sighting Progress:
    1. Burned Tower (DONE)
    2. Cianwood City (DONE - Confirmed Turn 47347)
    3. Route 42 (Middle Grove) - TRIGGER ATTEMPTED (Swept Turn 47324, re-entered Turn 47365. Empty.)
    4. Route 36 (Violet City North) - IN PROGRESS (Checking (11, 9) area)
    5. Kanto Route 14 (East of Fuchsia) - SIGHTING LOCKED
    6. Kanto Route 25 (Cerulean Cape) - SIGHTING LOCKED
- Strategy:
    - Verify sightings sequentially. Johto: Burned Tower -> Cianwood -> Route 42 -> Route 36.
    - If a Johto sighting is skipped, later sightings (including Kanto and Tin Tower) are blocked.
- Hypothesis Log:
    - H1: Trigger tile missed in grove. (Tested with full sweep).
    - H2: Missing prerequisite sighting. (Cianwood DONE, checking Route 36).
    - H3: Sighting sequence is strictly linear. (Confirmed by expert).
- General Lessons:
    - Menu Navigation: Verify cursor position before issuing long 'menu_navigator' sequences to avoid wrapping or selecting wrong options.
    - Fly Tool: 'fly_list_navigator_v3_fixed' is now calibrated for Johto (Up increases index).

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