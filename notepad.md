# Gem's Pokémon Crystal Knowledge Base

## Global Tile Mechanics
- FLOOR: Standard traversable tile.
- FLOOR (Route 17): Downhill coasting mechanic. (Verified Turn 42121)
- WALL: Impassable collision.
- INVISIBLE WALL: Appears as FLOOR visually but acts as WALL in collision data. (Verified Turn 42304)
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
- KIMCHI (Gloom): Flash, Petal Dance, Cut, Sleep Powder. (Lv 49 Turn 42339)

### Significant Battles
- Erika (Celadon Gym): Defeated.
- Rival Silver (Mt. Moon): Defeated.
- Biker Charles (6, 80): Defeated.
- Bird Keeper Bob (13, 6): Defeated.
- Janine (Fuchsia Gym): Defeated. (Turn 42346)

## Evolution Methods
- Poliwag -> Poliwhirl -> Poliwrath (Water Stone) or Politoed (Trade with King's Rock).
- Gloom -> Vileplume (Leaf Stone) or Bellossom (Sun Stone).
- Haunter -> Gengar (Trade).
- Graveler -> Golem (Trade).

## PC Storage
- Box 1: GORP (Snorlax Lv50), etc. (9/20 full)

## Fuchsia City Investigation (Started Turn 42186)
- Objective: Find Pokemon Center and Gym.
- Soul Badge: Obtained. (Turn 42346)
- NPC Lore:
    - Youngster (Object 1, Overworld): Elite Four member used to be the Gym Leader.
    - Pokefan F (Bill's Older Sister, 11, 27): Grandpa is at Bill's place.
- Safari Zone Main Office: (22, 13). Visited. No items or useful NPCs.
- Route 15 Gatehouse: Eastern exit of city.
- Fuchsia Gym: (8, 27). Inside (Turn 42253). Leader Janine.
- Gym Dimension: 10x18.
- Fuchsia Gym NPCs:
    - Janine (1, 10): Leader. Defeated. (Turn 42346)
    - Janine Look-alike (4, 2): Camper Barry. Defeated. (Turn 42318)
    - Janine Look-alike (5, 11): Lass Linda. Defeated. (Turn 42269)
    - Janine Look-alike (5, 7): Talked to. Non-battling decoy. (Turn 42352)
    - Janine Look-alike (9, 4): Talked to. Non-battling decoy. (Turn 42358)
    - Janine Look-alike (9, 14): Targeting now.
- Fuchsia Gym Invisible Walls:
    - The gym layout is a maze of invisible walls.
    - Navigation to Janine: Turn 42253 to 42328 (75 turns).
    - Janine Battle Log:
        - Crobat (Lv 36): Defeated with Thunderpunch.
        - Weezing (Lv 36) x2: Defeated with Flamethrower.
        - Venomoth (Lv 39): Defeated with Flamethrower.
        - Ariados (Lv 33): Defeated with Flamethrower.
    - Soul Badge and TM06 (Toxic) obtained. (Turn 42346)

## Strategy for Remaining Kanto Journey
- Goals: Fuchsia (Soul), Cinnabar/Seafoam (Volcano), Viridian (Earth).

## General Lessons & Error Log
- NPC Interaction: Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- Ledges: Hop down south only.
- Menu Navigation: Use single `press_buttons` to verify menu state.
- Route 17 Physics: Downhill mechanic requires constant Northward inputs.
- Fuchsia Navigation: Row 22 wall blocks North movement except at X=0, 1. (4, 31) is a wall.
- Notepad Edits: Use exact matches for `old_text` or use `overwrite` for major changes. (Turn 42348)