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
  - Calcifer (Cyndaquil): Target Lv12 for Ember to handle Sprout Tower and potentially Falkner's Pidgey.
  - ROCKY (Onix) & GNEISS (Geodude): Primary counters for Falkner's Flying-type Pokémon.
- **Plan:**
  1. Complete Sprout Tower to obtain HM05 Flash and train the team.
  2. Ensure Rocky and Gneiss are healthy for the Gym battle.
  3. Use Rock-types to soak up Normal/Flying hits.

## Pokemon Growth Mechanics
- **Medium Slow Growth Rate:** Pokémon in this group (like Cyndaquil) require more EXP as they reach higher levels. Level-ups feel slower but stats scale better later. Verified.

## Defeated Trainers
- Route 30: Bug Catcher Don.
- Route 31: Bug Catcher Wade.
- Sprout Tower:
  - Sage Chow (1F).
  - Sage Nico (2F).
  - Sage Edmond (2F).
  - Sage Jin (ID 1) at (8, 13).
  - Sage Neal (ID 4) at (11, 11).
  - Sage Troy (ID 2) at (8, 9).

## NPC Archive (Active/Relevant)
- New Bark: ELM, OFFICER, MOM.
- Route 30/31: MR. POKEMON, OAK.
- Violet City: KYLE (Trade), Pokefan M, EARL (Spinning Master) at (25, 14).
- Sprout Tower: Sage at (7, 4) (HM info), Sage Li (ID 3) (At top).

## Lessons Learned
- **Object Collision:** NPCs and items are walls. Navigate around them.
- **Battle Menus:** Selecting NO for switching is faster if current Pokemon is fine.
- **Level Requirements:** Cyndaquil learns Ember at Lv12 in Crystal.
- **Tool Hygiene:** Always provide full moveset data to `battle_strategist_v2`.
- **Scripted NPC Blockage:** During scripted events, NPCs can temporarily block paths. Wait for the event to conclude.

## Area Mechanics: Sprout Tower
- Ghosts: Immune to Normal moves. Use Ember.
- Central pillar: Giant Bellsprout.
- HM Flash: At the top.

## Timestamps & Progress
- Started Academy Turn 1167.
- Entered Tower Turn 1213.
- Sprout Tower 3F (Turn 1416):
  - Battling Sage Li's Hoothoot (Lv 10) at (10, 2).
  - Potion collected at (6, 14).
  - Calcifer is Lv13.
  - Calcifer needs 166 EXP for Lv14. Verified with tool.