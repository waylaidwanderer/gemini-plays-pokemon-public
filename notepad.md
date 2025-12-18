# Johto Journey: Gem's Log

## Tile Mechanics
- FLOOR: Traversable. Verified.
- WALL / FLOOR_UP_WALL: Impassable. Verified.
- TALL_GRASS: Traversable; wild encounters. Verified.
- LEDGE_HOP_DOWN: One-way South. Verified.
- LEDGE_HOP_RIGHT: One-way East. Verified.
- COUNTER: Impassable. Face to interact. Verified.
- HEADBUTT_TREE / CUT_TREE: Impassable. Verified.
- WARP_CARPET: Exit map. Verified.
- LADDER / DOOR / CAVE: Warp. Triggered immediately upon entering the tile. Verified.
- PC / BOOKSHELF / RADIO: Interactable objects. Verified.
- WATER / ROCK / INCENSE_BURNER: Impassable. Verified.

## Primary Goal Strategy: Defeat Falkner (Violet City)
- **Team Composition:**
  - Calcifer (Quilava): Lv14. Primary powerhouse.
  - ROCKY (Onix): Lv5. Counter for Falkner. Traded Pokemon; obedience depends on Badges.
  - GNEISS (Geodude): Lv4. Counter for Falkner.
- **Plan:**
  1. Complete Sprout Tower (Obtain HM05 Flash). ✅
  2. Heal at Pokemon Center. ✅
  3. Train Rocky/Gneiss to Lv11+ (Gneiss learns Rock Throw).
  4. Defeat Gym Leader Falkner.

## Pokemon Growth Mechanics
- **Medium Slow Growth Rate:** Pokémon in this group (like Cyndaquil/Quilava) require more EXP as they reach higher levels. Level-ups feel slower but stats scale better later. Verified.
- **Obedience:** Traded Pokémon or high-level Pokémon may not obey without the appropriate Gym Badges. Verified (NPC info).

## Defeated Trainers
- Route 30: Bug Catcher Don.
- Route 31: Bug Catcher Wade.
- Sprout Tower: Sage Chow (1F), Sage Nico (2F), Sage Edmond (2F), Sage Jin (3F), Sage Neal (3F), Sage Troy (3F), Sage Li (Elder) (3F).

## NPC Archive (Active/Relevant)
- New Bark: ELM, OFFICER, MOM.
- Route 30/31: MR. POKEMON, OAK.
- Violet City: KYLE (Trade), EARL (Spinning Master) at (25, 14).
- Sprout Tower: Sage at (7, 4) (HM info).
- Violet Pokecenter: Nurse Joy (3, 1), Gentleman (1, 4), Gameboy Kid (7, 6), Youngster (8, 1) (Obedience info).

## Lessons Learned
- **Object Collision:** NPCs and items are walls. Navigate around them.
- **Battle Menus:** Selecting NO for switching is faster if current Pokemon is fine.
- **Level Requirements:** Cyndaquil learns Ember at Lv12 and evolves into Quilava at Lv14 in Crystal.
- **Tool Hygiene:** Always provide full moveset and move data to `battle_strategist_v2`.
- **Scripted NPC Blockage:** During scripted events, NPCs can temporarily block paths. Wait for the event to conclude.

## Area Mechanics: Sprout Tower
- HM Flash: Received from Sage Li. Requires Zephyr Badge to use.

## Timestamps & Major Milestones
- Started Academy Turn 1167.
- Entered Sprout Tower Turn 1213.
- Calcifer evolved into QUILAVA Turn 1421.
- Received HM05 FLASH Turn 1422.
- Sprout Tower Complete Turn 1434.
- Team Healed at Violet Pokecenter Turn 1442.