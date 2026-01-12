# Gem's Pokémon Crystal Knowledge Base

## Global Tile Mechanics
- FLOOR: Standard traversable tile.
- FLOOR (Route 17): Downhill coasting mechanic. (Verified Turn 42121)
- WALL: Impassable collision. (4, 31) confirmed as WALL despite label.
- WATER: Impassable on foot. Requires SURF.
- TALL_GRASS / grass: Standard traversable tile. Wild encounters.
- DOOR / WARP / CAVE: Entry/exit points.
- WARP_CARPET_DOWN: Entry/exit point.
- LADDER / STAIRCASE: Vertically connects maps.
- COUNTER: Impassable. Interaction possible from adjacent tiles.
- MART_SHELF: Impassable collision.
- LEDGE_HOP_DOWN: One-way traversal (North to South only).
- FLOOR_LEFT_WALL / FLOOR_RIGHT_WALL / FLOOR_UP_WALL: Collision that blocks movement in specified direction.
- OBJECTS (NPCs/Items): Impassable. Interaction possible from adjacent tiles.
- PC / BOOKSHELF: Impassable. Interaction possible from adjacent tiles.

## Battle and Pokemon Information
### Party Movesets
- Calcifer (Typhlosion): Flamethrower (0 PP), Return, Smokescreen, Thunderpunch.
- GNEISS (Graveler): Earthquake, Defense Curl, Strength, Rollout.
- ICARUS (Pidgeotto): Fly, Sand-Attack, Gust, Quick Attack.
- XENON (Haunter): Hypnosis, Confuse Ray, Night Shade, Dream Eater.
- LAPIS (Poliwag): Waterfall, Surf, Hypnosis, Whirlpool.
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder.

### Significant Battles
- Erika (Celadon Gym): Defeated.
- Rival Silver (Mt. Moon): Defeated.
- Biker Charles (6, 80): Defeated.
- Bird Keeper Bob (13, 6): Defeated.

## Evolution Methods
- Poliwag -> Poliwhirl -> Poliwrath (Water Stone) or Politoed (Trade with King's Rock).
- Gloom -> Vileplume (Leaf Stone) or Bellossom (Sun Stone).
- Haunter -> Gengar (Trade).
- Graveler -> Golem (Trade).

## PC Storage
- Box 1: GORP (Snorlax Lv50), etc. (9/20 full)

## Fuchsia City Investigation (Started Turn 42186)
- Objective: Find Pokemon Center and Gym.
- Soul Badge: Fuchsia City Gym (Leader Janine).
- NPC Lore:
    - Youngster (Object 1, Overworld): Elite Four member used to be the Gym Leader.
    - Pokefan F (Bill's Older Sister, 11, 27): Grandpa is at Bill's place.
- Safari Zone Main Office: (22, 13). Visited. No items or useful NPCs.
- Route 15 Gatehouse: Eastern exit of city.
- Fuchsia Gym: (8, 27). Inside (Turn 42253). Leader Janine.
- Gym Dimmension: 10x18.
- NPC Lore:
    - Youngster (Object 1, Overworld): Elite Four member used to be the Gym Leader.
    - Pokefan F (Bill's Older Sister, 11, 27): Grandpa is at Bill's place.
    - Lass Linda (5, 11): Janine look-alike. Team: Bulbasaur (Lv 30), Venusaur (Lv 34), Ivysaur (Lv 32). Defeated. (Turn 42269)

## Strategy for Remaining Kanto Journey
- Goals: Fuchsia (Soul), Cinnabar/Seafoam (Volcano), Viridian (Earth).
- Priority: Find Pokemon Center to restore Calcifer's PP.

## General Lessons & Error Log
- NPC Interaction: Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- Ledges: Hop down south only.
- Menu Navigation: Use single `press_buttons` to verify menu state.
- Route 17 Physics: Downhill mechanic requires constant Northward inputs.
- Fuchsia Navigation: Row 22 wall blocks North movement except at X=0, 1. (4, 31) is a wall.
- Fuchsia Gym Hint: Trainers look like Janine. Need to find the real one. (Source: Gym Guide)
## Fuchsia Pokecenter NPCs (Turn 42278)
- Cooltrainer M (7, 4)
- Cooltrainer F (1, 4)
- Janine Impersonator (5, 3): Another look-alike!