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
    3. Route 42 (Middle Grove) - TRIGGER ATTEMPTED (Full grid sweep Turn 47324)
    4. Route 36 (Violet City North) - PENDING
    5. Kanto Route 14 (East of Fuchsia) - SIGHTING LOCKED
    6. Kanto Route 25 (Cerulean Cape) - SIGHTING LOCKED
- Strategy:
    - Verify sightings sequentially. Johto: Burned Tower -> Cianwood -> Route 42 -> Route 36.
    - If a Johto sighting is skipped, later sightings (including Kanto and Tin Tower) are blocked.
- Current Plan:
    - Re-entering Route 42 from Ecruteak gatehouse at (35, 27).
    - Use Cut on tree at (24, 13) to reach the grove.
    - Approach the center of the grove to trigger Suicune.
- Hypothesis Log (Route 42):
    - H1: Trigger is a specific tile within the grove boundary. (Tested with 'suicune_sweep_v2', Failed Turn 47324).
    - H2: Missing prerequisite sighting. (Cianwood confirmed DONE Turn 47347).
    - H3: Route 36 sighting must occur before Route 42. (Pending test if re-entry fails).
    - H4: Sighting sequence is strictly linear. (Confirmed by expert).

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