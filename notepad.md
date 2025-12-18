# Johto Journey: Gem's Log

## Tile Mechanics
- FLOOR: Traversable. Verified.
- WALL / FLOOR_UP_WALL: Impassable. Verified.
- TALL_GRASS: Traversable; wild encounters. Verified.
- LEDGE_HOP_DOWN: One-way South. Verified.
- LEDGE_HOP_RIGHT: One-way East. Verified.
- COUNTER: Impassable. Interaction with NPCs behind counters must be done by facing the counter tile directly. Verified.
- HEADBUTT_TREE / CUT_TREE: Impassable. Verified.
- WARP_CARPET: Exit map. Verified.
- LADDER / DOOR / CAVE: Warp. Triggered immediately upon entering the tile. Verified.
- PC / BOOKSHELF / RADIO: Interactable objects. Stand below, face up, and press A to activate. Verified.
- WATER / ROCK / INCENSE_BURNER: Impassable. Verified.
- NPCs / Objects: Act as walls. Navigate around or interact from adjacent tile. Verified.

## Training Strategy: Route 31 & Dark Cave
- **Location:** Route 31 grass and Dark Cave.
- **Process:**
  1. Lead with Gneiss (Lv4) or Rocky (Lv5).
  2. Switch to Calcifer (Lv14) to finish the battle.
  3. Repeat until Gneiss hits Lv11 (Rock Throw).
  4. Repeat until Rocky hits Lv14 (Rock Throw - long term).
- **Turn Start:** 1559.

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
- **Medium Slow Growth Rate:** Pokémon in this group (like Cyndaquil/Quilava) require more EXP as they reach higher levels. Verified.
- **Obedience:** Traded Pokémon or high-level Pokémon may not obey without the appropriate Gym Badges. Verified (NPC info).

## PC Storage
- Items: Empty. Verified Turn 1454.
- Pokemon: Empty.

## Type Effectiveness Observations
- FIRE vs GRASS: Super Effective (2x). Verified (Ember vs Bellsprout).
- NORMAL vs GHOST: No Effect (0x). Verified (Tackle vs Gastly).

## Defeated Trainers
- Route 30: Bug Catcher Don.
- Route 31: Bug Catcher Wade.
- Sprout Tower: Sage Chow, Sage Nico, Sage Edmond, Sage Jin, Sage Neal, Sage Troy, Sage Li (Elder).

## NPC Archive (Active/Relevant)
- New Bark: ELM, OFFICER, MOM.
- Route 30/31: MR. POKEMON, OAK.
- Violet City: KYLE (Trade), EARL (Spinning Master) at (25, 14).
- Sprout Tower: Sage at (7, 4) (HM info).
- Violet Pokecenter: Nurse Joy (3, 1), Gentleman (1, 4), Gameboy Kid (7, 6), Youngster (8, 1) (Obedience info).
- Route 32: Cooltrainer M at (19, 8) - Blockade; requires Zephyr Badge.

## Lore & Information
- Radio (MARY): Poliwhirl seen around Route 44. Lovely. Arbok mentioned by Oak.
- Bookshelf: POKéMON magazines... POKéMON PAL, POKéMON HANDBOOK, POKéMON GRAPH...
- Incense Burner: Flavor text "Oh, it's an incense burner!"
- Youngster at (5, 18): "I saw a wiggly tree up ahead!" (Likely Route 36 blockage).

## Lessons Learned
- **Object Collision:** NPCs and items are walls. Navigate around them.
- **Battle Menus:** Selecting NO for switching is faster if current Pokemon is fine.
- **Level Requirements:** Cyndaquil learns Ember at Lv12 and evolves into Quilava at Lv14 in Crystal.
- **Tool Hygiene:** Always provide full moveset and move data to `battle_strategist_v2`.
- **Scripted NPC Blockage:** During scripted events, NPCs can temporarily block paths. Wait for the event to conclude.
- **Menu Navigation:** Verify cursor position before pressing A for critical items or complex menu paths.
- **Route 32 Blockage:** A Cooltrainer prevents access to Route 32 south until the Violet Gym is defeated.