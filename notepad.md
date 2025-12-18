# Johto Journey: Gem's Log

## Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable; wild encounters.
- LEDGE_HOP_DOWN: One-way jump South (Verified: Impassable from South).
- LEDGE_HOP_LEFT: One-way jump West (Likely one-way).
- LEDGE_HOP_RIGHT: One-way jump East (Likely one-way).
- HEADBUTT_TREE: Impassable (requires Headbutt).
- COUNTER: Interactable (face to talk to NPC behind).
- WARP_CARPET_DOWN: Exit map South.
- LADDER: Warp to different floor.
- BOOKSHELF / WINDOW / TREE / HEDGE: Impassable (acts as WALL).
- PC: Interactable (face to use).
- MART_SHELF: Impassable (acts as WALL).
- BUOY: Impassable (water barrier).
- DOOR: Traversable (triggers warp).

## Current Strategy & Goals
### Primary Goal: Defeat Gym Leader Falkner (Violet City)
- **Strategy:**
    1. **Training:** Get Icarus (Pidgey) to Lv9 and Calcifer (Cyndaquil) to Lv13.
    2. **Recruitment:** Catch a Geodude in Dark Cave (Route 31) for Rock-type advantage against Falkner's Flying types.
    3. **Sprout Tower:** Use Calcifer's Ember (Lv12) to sweep Bellsprouts and obtain HM05 (Flash).
    4. **Gym Prep:** Collect Bitter Berry (Route 31) to counter Gastly's Confuse Ray in Sprout Tower.

## NPCs & Interactions
### New Bark Town & Lab
- PROF. ELM (ID 1): Gave Starter. Delivered Mystery Egg.
- OFFICER (ID 3): Investigating theft. Named Rival "MALICE".
- MOM (ID 1): Offered to save money. (Turn 334).

### Mr. Pokémon's House (26_10)
- MR. POKÉMON (ID 1): (3, 5). Gave MYSTERY EGG.
- PROF. OAK (ID 2): (6, 5). Gave POKéDEX.

### Cherrygrove City (26_3)
- GRAMPS (ID 1): Gave city tour and MAP CARD. House at (25, 9).
- TEACHER (ID 3): "When you're with POKéMON, going anywhere is fun." (Wandering).
- YOUNGSTER (ID 4): (22, 7).

### Cherrygrove Mart (26_4) & PC (26_5)
- CLERK (ID 1): (1, 3). Face COUNTER at (2, 3) to shop.
- NURSE JOY (ID 1): Heals Pokémon at (3, 3).

### Speech Houses
- GYM SPEECH (26_6): Pokefan M (2, 3), Bug Catcher (4, 5).
- EVOLUTION SPEECH (26_8): Lass (3, 5), Youngster (2, 5).
- BERRY HOUSE (26_9): Pokefan M (2, 3). Gave BERRY.

### Route 30 (26_1)
- Sign at (9, 43): Route 30.
- Item at (8, 35): Antidote (Collected).
- YOUNGSTER (ID 5): (7, 30).
- Sign at (13, 29): MrPokemonsHouseDirectionsSign.
- FRUIT TREE (5, 39): Obtained BERRY.

## Progress Summary
- **Major Events:**
    - Rival MALICE defeated at Cherrygrove City exit. (Turn 315)
    - Mystery Egg delivered to Prof. Elm. (Turn 324)
    - Caught Lv2 Pidgey (ICARUS) on Route 29. (Turn 352)
    - Party fully healed at Cherrygrove PC. (Turn 674)
- **Training Logs:**
    - Turn 668: Icarus fainted to crit vs Lv3 Hoothoot. Calcifer finished battle (EXP 297).
- **Exploration Targets:**
    - Unseen tiles on Route 30 at (12, 3-15) and (1, 26-35). Priority after training.

## Lessons Learned
- NPCs act as walls.
- Buildings are often larger than they appear.
- Ledges are one-way (South confirmed impassable from below).
- Menu Navigation: Do NOT mix directional buttons and action buttons in the same turn.
- Turn Tracking: Always use the turn number provided in the Game State.
- CRITICAL HITS: Can happen anytime! Stay healthy even during training.
- BATTLE MENUS: Directional inputs (Up/Down) and action inputs (A) must be in separate turns.