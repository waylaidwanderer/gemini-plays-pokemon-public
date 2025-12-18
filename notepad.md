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

## Completed Areas
- **Route 30/31:** Defeated trainers, caught Geodude and Bellsprout.
- **Violet City:** Traded Bellsprout for Rocky (Onix).

## NPC Archive
- New Bark: ELM, OFFICER, MOM.
- Route 30/31: MR. POKEMON, OAK, WADE.
- Cherrygrove: GRAMPS, NURSE JOY, CLERK.
- Violet City: LASS (Tower info), KYLE (Trade), Pokefan M, EARL (Spinning Master) at (25, 14).
- Sprout Tower:
  - GRANNY: Lore.
  - Sage at (7, 4): Confirmed HM is at top.
  - Sage Chow: Defeated at (3, 2) on 1F.
  - Sage Nico: Defeated at (11, 3) on 2F.
  - Sage Edmond: Defeated at (5, 14) on 2F.
  - Sage at (6, 7) on 1F: Moving NPC.
  - Teacher at (9, 9) on 1F: Lore.

## Lessons Learned
- **Object Collision:** NPCs and items are walls. Navigate around them.
- **Battle Menus:** Selecting NO for switching is faster if current Pokemon is fine.
- **Level Requirements:** Cyndaquil learns Ember at Lv12 in Crystal.
- **Tool Hygiene:** Always provide full moveset data to `battle_strategist_v2`.

## Area Mechanics: Sprout Tower
- Ghosts: Immune to Normal moves. Use Ember.
- Central pillar: Giant Bellsprout.
- HM Flash: At the top.

## Timestamps & Progress
- Started Academy Turn 1167.
- Entered Tower Turn 1213.
- Sprout Tower 3F (Turn 1397):
  - Sage Jin (ID 1) defeated at (8, 13).
  - Sage Neal (ID 4) defeated at (11, 11).
  - Sage Troy (ID 2) defeated at (8, 9).
  - Sage Li (ID 3) at (10, 2).
  - Poke Ball (ID 5) at (6, 14) (Potion collected).
  - Item Ball (ID 6) at (14, 1).
  - Calcifer is Lv13.
  - Calcifer needs 292 EXP for Lv14.
- **Lesson: Scripted NPC Blockage.** During scripted events (like Malice's appearance), NPCs can temporarily block paths that appear clear on the map. Wait for the event to conclude before attempting to navigate through those tiles.
- **Reflection (Turn 1401):** Verified all tasks. Notepad updated with scripted movement lesson. Map markers for Sages and items are current. Goals are concrete. Root hypothesis for Sprout Tower (HM Flash at top) is confirmed by NPC dialogue.