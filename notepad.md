# Johto Journey: Gem's Log

## Tile Mechanics
- FLOOR: Traversable. Standard ground.
- WALL / FLOOR_UP_WALL: Impassable.
- TALL_GRASS: Traversable. Wild encounters.
- LEDGE_HOP_DOWN: One-way South.
- LEDGE_HOP_RIGHT: One-way East.
- COUNTER: Impassable. Stand in front to talk to NPCs behind.
- HEADBUTT_TREE: Impassable. Requires Headbutt.
- CUT_TREE: Impassable. Requires Cut.
- WARP_CARPET: Map transition at edges.
- LADDER / DOOR / CAVE: Instant warp upon entry.
- PC / BOOKSHELF / RADIO: Interactable from below (face Up + A).
- WATER / ROCK / INCENSE_BURNER: Impassable.

## Gym Progress
- **Zephyr Badge:** Obtained from Falkner (Turn 1864).
  - Effect: Increases Attack power.
  - Ability: Can use FLASH outside battle.
- **Hive Badge:** Target. Azalea Town.

## EXP Tracking
- Gneiss (GEODUDE, Medium Slow): Lv13 (1329 EXP). Next: Lv14 (1596 EXP).
- Rocky (ONIX, Medium Fast): Lv5 (125 EXP). Goal: Lv14 (Rock Throw) - On hold.

## Key Items & TMs
- TM31 (MUD-SLAP): Received from Falkner. Accuracy-lowering Ground move.
- HM05 (FLASH): Received from Sage Li.

## Pokemon Locations
- Route 31: Bellsprout, Weedle, Caterpie, Ledyba, Hoppip, Pidgey.
- Dark Cave: Geodude, Zubat.

## NPC Archive
- Violet City: 
  - KYLE: (6, 4) in his house. Traded Bellsprout for Rocky (ONIX).
  - EARL: (25, 14) at the Academy. Learned about status and items.
  - Cooltrainer: (32, 8) Mentioned Flash hint.
- Violet Pokecenter: 
  - Nurse Joy (3, 1): Heals Pokemon.
  - Youngster (8, 1): Info on Badge obedience.
- Route 30:
  - Mr. Pokemon: (3, 5) Gave Mystery Egg.
  - Prof. Oak: (6, 5) Gave Pokedex.
- Route 31:
  - Bug Catcher Wade: (17, 13) Defeated.
  - Bug Catcher Don: (1, 9) Defeated.

## Flavor & Lore
- Youngster at (5, 18): "I saw a wiggly tree up ahead!" (Route 36 blockage).
- Sage Li: Zephyr Badge required to use Flash outside battle.

## Lessons Learned
- **Battle Menus:** Selecting NO for switching is faster if current Pokemon is fine.
- **Navigation Safety:** Always verify "Current Screen Text" is empty before moving.
- **Battle State:** Do not attempt overworld movement while in battle or during transitions.
- **Gym Strategy:** Rock-types (Geodude) with Rock Throw are extremely effective against Falkner's Flying-types.
## Strategy: Azalea Town
1. **Mystery Egg:** Received Togepi from Aide.
2. **Route 32:** Exit Violet City to the south (14, 35).
3. **Azalea Town:** Follow Route 32 south, pass through Union Cave to reach Azalea Town.
4. **HMs:** Use FLASH in Dark Cave if level grinding is needed or for shortcuts. Requires a Pokemon that can learn it (e.g. Bellsprout).

## Reflection Turn 1869
- **Immediate Execution:** No deferred tasks. Falkner defeated, badge obtained.
- **Notepad Hygiene:** Added Azalea/Egg strategy.
- **Map Hygiene:** Markers for gym clear. Need to mark Aide in Pokecenter.
- **Automation:** Fixed list_reachable_unseen_v3.
- **Goal Clarity:** Focus shifted to next badge and Egg.
- **Error Analysis:** list_reachable_unseen_v3 failed due to return type; fixed now.