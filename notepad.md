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
  - ROCKY (Onix) & GNEISS (Geodude): Primary counters for Falkner's Flying-type Pokémon.
- **Plan:**
  1. Complete Sprout Tower (Obtain HM05 Flash). ✅
  2. Collect remaining items in Tower. ✅
  3. Explore remaining unseen tiles on 3F.
  4. Defeat Gym Leader Falkner.

## Pokemon Growth Mechanics
- **Medium Slow Growth Rate:** Pokémon in this group (like Cyndaquil/Quilava) require more EXP as they reach higher levels. Level-ups feel slower but stats scale better later. Verified.

## Defeated Trainers
- Route 30: Bug Catcher Don.
- Route 31: Bug Catcher Wade.
- Sprout Tower:
  - Sage Chow (1F).
  - Sage Nico (2F).
  - Sage Edmond (2F).
  - Sage Jin (3F) at (8, 13).
  - Sage Neal (3F) at (11, 11).
  - Sage Troy (3F) at (8, 9).
  - Sage Li (Elder) (3F) at (10, 2).

## NPC Archive (Active/Relevant)
- New Bark: ELM, OFFICER, MOM.
- Route 30/31: MR. POKEMON, OAK.
- Violet City: KYLE (Trade), Pokefan M, EARL (Spinning Master) at (25, 14).
- Sprout Tower: Sage at (7, 4) (HM info).

## Lessons Learned
- **Object Collision:** NPCs and items are walls. Navigate around them.
- **Battle Menus:** Selecting NO for switching is faster if current Pokemon is fine.
- **Level Requirements:** Cyndaquil learns Ember at Lv12 and evolves into Quilava at Lv14 in Crystal.
- **Tool Hygiene:** Always provide full moveset and move data to `battle_strategist_v2`.
- **Scripted NPC Blockage:** During scripted events, NPCs can temporarily block paths. Wait for the event to conclude.

## Area Mechanics: Sprout Tower
- Ghosts: Immune to Normal moves. Use Ember.
- Central pillar: Giant Bellsprout.
- HM Flash: At the top. Received from Sage Li. Requires Zephyr Badge to use.

## Timestamps & Progress
- Started Academy Turn 1167.
- Entered Tower Turn 1213.
- Sprout Tower 3F (Turn 1429):
  - Defeated all Sages (Jin, Neal, Troy, Elder Li).
  - Calcifer evolved into QUILAVA at Lv14.
  - Received HM05 FLASH from Sage Li.
  - Potion collected at (6, 14).
  - Escape Rope collected at (14, 1).
  - 3F fully explored.
- Violet City (Turn 1436):
  - Used Escape Rope to exit Sprout Tower.
  - Arrived at Pokemon Center door.
## Strategy: Exiting Sprout Tower
- **Method:** Use Escape Rope for efficiency.
- **Reasoning:** Instantly exits the dungeon, saving turns and avoiding potential wild encounters while backtracking.
- **Next Steps:** Heal at Pokemon Center, then head to Violet Gym.
- **Gym Strategy:** Lead with Gneiss (Geodude) or Rocky (Onix) to counter Flying types and gain EXP.