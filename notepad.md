# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Verified Behavior)
- FLOOR: Standard traversable tile. No special effects.
- WALL: Impassable collision. Blocks all movement.
- WATER: Impassable on foot. Requires SURF to traverse.
- TALL_GRASS / grass: Standard traversable tile. May trigger wild encounters.
- DOOR / WARP / CAVE: Entry/exit points. Stepping on them triggers a map transition.
- WARP_CARPET_DOWN: Entry/exit point. Functions like a DOOR/WARP.
- LADDER / STAIRCASE: Vertically connects different maps or floors.
- COUNTER: Impassable collision. Blocks movement but allows interaction with NPCs behind it if faced from an adjacent tile.
- MART_SHELF: Impassable collision. Blocks all movement.
- LEDGE_HOP_DOWN: One-way traversal. Can only be crossed from North to South.
- FLOOR_LEFT_WALL / FLOOR_RIGHT_WALL / FLOOR_UP_WALL: Collision that blocks movement in the specified direction.
- WARP_CARPET: (7,3) and (8,3) in Celadon Dept Store 5F are traversable floor tiles, not active warps. (Verified Turn 41878)
- OBJECTS (NPCs/Items): Impassable collision. Must be navigated around. Interaction possible from adjacent tiles.
- PC / BOOKSHELF: Impassable collision. Interaction possible from adjacent tiles.

## Battle and Pokemon Information
### Party Movesets
- Calcifer (Typhlosion): Flamethrower, Return, Smokescreen, Thunderpunch.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- LAPIS (Poliwag): Waterfall, Surf, Hypnosis, Whirlpool.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.

### Type Effectiveness (Observed)
- Fire (Calcifer) is Super Effective against Grass (Erika's Gym).
- Flying (Icarus) is Super Effective against Grass.
- Poison is not very effective against Poison/Grass.

### Significant Battles
- Erika (Celadon Gym): Defeated with Fire-type moves. Lv 42-46 team.
- Rival Silver (Mt. Moon): Defeated.

## Evolution Methods
- Poliwag -> Poliwhirl -> Poliwrath (Water Stone) or Politoed (Trade with King's Rock). (Source: Fisher at 26,11)
- Gloom -> Vileplume (Leaf Stone) or Bellossom (Sun Stone).
- Haunter -> Gengar (Trade).
- Graveler -> Golem (Trade).

## PC Storage
### Box 1 (Current) (9/20)
- GORP (SNORLAX): Lv50 (Male)
- AAAAAAAAAA (SPINARAK): Lv13 (Male)
- GLAIVE (SCYTHER): Lv14 (Female)
- SELKIE (SEEL): Lv24 (Female)
- DELTA (MANTINE): Lv20 (Male)
- RANGOON (KRABBY): Lv22 (Female)
- NOMURA (TENTACOOL): Lv17 (Female)
- Ravioli (KRABBY): Lv10 (Male)
- Ouroboros (DRATINI): Lv15 (Male)

## Economy & Shopping
- **Celadon Dept Store Inventory Summary:**
    - 2F: Healing items (Full Heal, Max Potion, Revive).
    - 3F: TM Shop inventory documented.
    - 4F: Wiseman Gifts inventory documented.
    - 5F: Drugstore inventory documented.
    - 6F: Vending Machines inventory documented.
- **Long Term Shopping Plan:**
    - Find Evolution Stones (not in Dept Store).

## Celadon City Investigation (Started Turn 41409, Jan 11 3:10 PM)
- **Secret Wing Access:** Reached via back door at (16,3).
- **Mansion Roof House:** Pharmacist (3,2) tells "terrifying tale" ONLY at night.
- **Gym Access:** Path behind southern hedges (Cut tree at 28,35). Follow path west to (5,35), then north through the gap in the ledge at (5,33). Warp at (10, 29).

## Kanto Secrets & NPC Schedules
- **Daisy Oak (Pallet Town):** Has tea every day from 3:00 PM to 4:00 PM. (Source: Chad)

## Strategy for Remaining Kanto Journey
- **Objective:** Defeat Janine (Fuchsia), Blaine (Cinnabar/Seafoam), Blue (Viridian).
- **Strategic Plan for Kanto Badges:**
    1. Celadon (Rainbow) - COMPLETED.
    2. Fuchsia (Soul) - Next target. Soul Badge.
       - HOW: Route 16 (Cycling Road) requires Bicycle. Route 12-15 (Silence Bridge) is alternative.
    3. Cinnabar/Seafoam (Volcano) - After Fuchsia. Volcano Badge.
       - HOW: Surf from Pallet Town or Fuchsia City.
    4. Viridian (Earth) - Final badge. Earth Badge. Blue is the leader.
- **Rematches:** Alan (Route 36) wants a battle.

## General Lessons & Error Log
- **NPC Interaction:** Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- **Ledges:** Hop down south only.
- **Menu Navigation:** Use `press_menu_buttons_v3` for deep menus to avoid "mixed input" errors. (Added Turn 42037)
- **Thirsty Girl (6F):** Does not exist in Crystal version. (Verified Turn 41936)

## Celadon Game Corner Sweep (Turn 41953)
- Posters/Background: No hidden switches. (Done Turn 42010)
- Hidden Items: No response from Itemfinder in major areas. (Done Turn 42018)
## Celadon Game Corner Prize Exchange (Turn 42027)
- Gentleman (0, 2): Wanted PORYGON, but was short by 100 coins.
- TM Vendor (2, 1): TM32 (1500), TM29 (3500), TM15 (7500). (Done Turn 42029)
- Pokemon Vendor (4, 1): PIKACHU (2222), PORYGON (5555), LARVITAR (8888). (Done Turn 42035)
- Pharmacist (4, 3): "I can't lose my cool, or I'll lose all my money..." (Done Turn 42042)