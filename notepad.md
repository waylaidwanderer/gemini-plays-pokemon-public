# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Verified Traversability)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with SURF.
- TALL_GRASS / grass: Traversable.
- DOOR / WARP / CAVE: Entry points.
- LADDER / STAIRCASE: Moves between floors.
- COUNTER: Impassable. Interact from front.
- MART_SHELF: Impassable.
- LEDGE_HOP_DOWN: One-way North to South.
- FLOOR_LEFT_WALL / FLOOR_RIGHT_WALL / FLOOR_UP_WALL: Impassable.
- WARP_CARPET: (7,3) and (8,3) in Celadon Dept Store 5F are traversable floor tiles, not active warps. (Verified Turn 41878)
- OBJECTS (NPCs/Items): Impassable.
- PC / BOOKSHELF: Impassable.

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
### Box 1 (9/20)
- GORP (Snorlax) Lv50
- AAAAAAAAAA (Spinarak) Lv13
- GLAIVE (Scyther) Lv14
- SELKIE (Seel) Lv24
- DELTA (Mantine) Lv20
- RANGOON (Krabby) Lv22
- NOMURA (Tentacool) Lv17
- Ravioli (Krabby) Lv10
- Ouroboros (Dratini) Lv15

## Economy & Shopping
- **Celadon Dept Store Exploration (Started Turn 41740, Sunday 3:00 PM):**
    - 1F: Directory checked.
    - 2F: Fully explored. Stocked up on healing items (Full Heal, Max Potion, Revive).
    - 3F: Fully explored. TM Shop inventory: TM10, TM11, TM17, TM18, TM37.
    - 4F: Fully explored. Wiseman Gifts inventory: Poke Doll, Lovely Mail, Surf Mail. No Evolution Stones.
    - 5F: Fully explored. Drugstore inventory documented.
    - 6F: Arrived Turn 41903. Vending machines located.
- **Long Term Shopping Plan:**
    - 6F: Buy drinks from vending machines. Give to thirsty girl for TMs.
    - Find Evolution Stones (still missing).

## Strategy for 6F Exploration (Turn 41905)
1. Read Directory at (14, 0). (Done)
2. Talk to Youngster (ID 2). (Done Turn 41919)
3. Talk to Super Nerd (ID 1) at (9, 2). (Done)
4. Buy Fresh Water and Soda Pop from Vending Machines (8,1)-(11,1).
5. Explore western unseen area using `find_reachable_unseen_tiles`.
6. Find thirsty girl and trade drinks for TMs.

## Celadon City Investigation
- **Secret Wing Access:** Reached via back door at (16,3).
- **Mansion Roof House:** Pharmacist (3,2) tells "terrifying tale" ONLY at night.
- **Gym Access:** Path behind southern hedges (Cut tree at 28,35). Follow path west to (5,35), then north through the gap in the ledge at (5,33). Warp at (10, 29).

## Kanto Secrets & NPC Schedules
- **Daisy Oak (Pallet Town):** Has tea every day from 3:00 PM to 4:00 PM. (Source: Chad)

## Strategy for Remaining Kanto Journey
- **Objective:** Defeat Janine (Fuchsia), Blaine (Cinnabar/Seafoam), Blue (Viridian).
- **Strategic Plan for Kanto Badges:**
    1. Celadon (Rainbow) - COMPLETED.
    2. Fuchsia (Soul) - Next target. Use Cycling Road or Route 12-15.
    3. Cinnabar/Seafoam (Volcano) - After Fuchsia. Use Surf from Pallet or Fuchsia.
    4. Viridian (Earth) - Final badge. Blue is the leader.
- **Rematches:** Alan (Route 36) wants a battle.

## General Lessons & Error Log
- **NPC Interaction:** Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- **Ledges:** Hop down south only.
- **Celadon Pillars:** Col 12 and Col 36 block horizontal movement.
- **Tool Maintenance:** Ensure tool logic includes all traversable types. Fix immediately when missing types are identified.
- **Inventory Sync:** Calcifer is Lv 62. 2x IRON and 1x RARE CANDY used successfully. Bag slots cleared.
- Teacher (1, 7): Mentions using items on Pokemon makes them happy, but they hate certain items.