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
    - 3F: TM Shop: TM10, TM11, TM17, TM18, TM37.
    - 4F: Wiseman Gifts: Poke Doll, Lovely Mail, Surf Mail.
    - 5F: Drugstore: Vitamins (Clerk 1), Battle Items (Clerk 2).
    - 6F: Vending Machines: Fresh Water (¥200), Soda Pop (¥300), Lemonade (¥350).
- **Long Term Shopping Plan:**
    - Find Evolution Stones (not in Dept Store).

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
- **Teacher (1, 7):** Mentions using items on Pokemon makes them happy, but they hate certain items.
- **Thirsty Girl (6F):** Does not exist in Crystal version. (Verified Turn 41936)
## Strategy for Celadon Game Corner (Turn 41953)
1. Mark entrance/exit warps. (Done)
2. Explore the floor to reveal all unseen tiles.
3. Talk to all NPCs:
    - Pokefan M at (14, 10): Slot machines are state of the art. (Done)
    - Fishing Guru at (11, 7): The odds vary among machines. (Done Turn 41964)
    - Teacher at (17, 7).
    - Fisher at (8, 10): Gave GEM 20 coins. (Done Turn 41968)
4. Check prize exchange prices (usually in an adjacent building or at a counter).
5. Look for hidden coins on the floor using Itemfinder or by interacting with empty spaces.
6. Check for any Team Rocket activity (hidden switches, etc.).
7. Move to Prize Exchange building.