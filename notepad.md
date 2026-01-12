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
- Calcifer (Typhlosion): Flamethrower, Return, Smokescreen, Thunderpunch. (Healed Turn 42282)
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
- Gym Dimension: 10x18.
- Fuchsia Gym NPCs:
    - Lass Linda (5, 11): Janine look-alike. Team: Bulbasaur (Lv 30), Venusaur (Lv 34), Ivysaur (Lv 32). Defeated. (Turn 42269)
    - Gym Guide (Object 6, 7, 15): Mentions trainers look like Janine.
    - Janine? (Object 1, 1, 10)
    - Janine Look-alike? (Object 2, 5, 7)
    - Janine Look-alike? (Object 4, 9, 14)
    - Janine Look-alike? (Object 5, 1, 14)
- Fuchsia Gym Invisible Walls (Turn 42296):
    - The gym layout is a maze of invisible walls (marked as WALL in Mental Map).
    - Perimeter strategy: Attempt to navigate along the outer edges to find openings.
    - Current Position: (8, 10).
    - Known Walls: (7, 10), (6, 9), (7, 11), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (2, 10), (7, 10), (0, 11), (1, 11), (2, 11), (7, 11), (2, 12), (4, 12), (6, 12), (2, 13), (4, 13), (6, 13), (3, 14), (6, 14).

## Strategy for Remaining Kanto Journey
- Goals: Fuchsia (Soul), Cinnabar/Seafoam (Volcano), Viridian (Earth).

## General Lessons & Error Log
- NPC Interaction: Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- Ledges: Hop down south only.
- Menu Navigation: Use single `press_buttons` to verify menu state.
- Route 17 Physics: Downhill mechanic requires constant Northward inputs.
- Fuchsia Navigation: Row 22 wall blocks North movement except at X=0, 1. (4, 31) is a wall.
## Fuchsia Pokecenter NPCs (Turn 42278)
- Cooltrainer M (7, 4)
- Cooltrainer F (1, 4)
- Janine Impersonator (5, 3): Another look-alike!