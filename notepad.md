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
- OVERWORLD NAVIGATION: (10, 6) is a FLOOR tile. (Verified Turn 42415)

## Fly Map Navigation (Kanto)
- Indigo Plateau: Starting point.
- Down from Indigo -> Fuchsia City. (Turn 42411)
- Down from Fuchsia -> Saffron City. (Turn 42426)
- Observation: Pewter City is NOT on the Fly list (I never entered the PC there).
- Strategy: Use Diglett's Cave (Route 11 to Route 2) to reach Western Kanto.
- Goal: Fly to Vermilion City.

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
    - Janine Look-alike (9, 14): Empty.
    - Janine Look-alike (1, 14): Empty.
- Fuchsia Gym Invisible Walls:
    - The gym layout is a maze of invisible walls.
    - Navigation to Janine: Turn 42253 to 42328 (75 turns).
    - Janine Battle Log:
        - Crobat (Lv 36): Defeated with Thunderpunch.
        - Weezing (Lv 36) x2: Defeated with Flamethrower.
        - Venomoth (Lv 39): Defeated with Flamethrower.
        - Ariados (Lv 33): Defeated with Flamethrower.
    - Soul Badge and TM06 (Toxic) obtained. (Turn 42346)
- Fuchsia Gym Cleared: All trainers defeated/interacted with. (Turn 42368)

## Strategy for Remaining Kanto Journey
- Goals: Fuchsia (Soul), Cinnabar/Seafoam (Volcano), Viridian (Earth).

## General Lessons & Error Log
- NPC Interaction: Face the counter tile in front of NPCs (Nurses, Clerks, etc.) then press A.
- Ledges: Hop down south only.
- Menu Navigation: Use single `press_buttons` to verify menu state.
- Route 17 Physics: Downhill mechanic requires constant Northward inputs.
- Fuchsia Navigation: Row 22 wall blocks North movement except at X=0, 1. (4, 31) is a wall.
- Notepad Edits: Use exact matches for `old_text` or use `overwrite` for major changes. (Turn 42348)
## Rematch Requests
- Dana (Lass, Route 38): Wants to battle. (Turn 42369)
## Route 19 Exploration (Started Turn 42373)
- Goal: Find the path to Seafoam Islands/Cinnabar.
- Fisher (9, 5): Facing to talk.
- Fisher (10, 5): Moving NPC.
- Sign (11, 1): 'Careful Swimming' warning.
- Route 19 Blockage: Fisher at (9, 5) confirmed Route 19 is closed for construction. Recommended route to Cinnabar is south from Pallet Town. (Turn 42376)
- Fisher (11, 5): "Who knows how long it would take to move this boulder…" Confirms Route 19 blockage. (Turn 42379)
- Strategy Update: Route 19 is impassable. New route to Cinnabar: Fly to Indigo Plateau, walk south to Pallet Town, and Surf south to Cinnabar. (Note: Pallet Town not yet registered for Fly). (Turn 42396)
- Game Mechanic: To register a town for Fly, you MUST enter its Pokemon Center. (Turn 42396)
## Indigo Plateau (Arrived Turn 42400)
- Location: Route 23.
- Pokemon Center: (9, 5) or (10, 5).
- Victory Road Entrance: (9, 13) or (10, 13).

## Revised Cinnabar Strategy (Turn 42400)
- Problem: Route 19 is blocked.
- Solution: Reach Cinnabar via Pallet Town.
- Path:
    1. Fly to Pewter City.
    2. Travel South through Route 2 to Viridian City.
    3. Travel South through Route 1 to Pallet Town.
    4. Surf South through Route 21 to Cinnabar Island.
## Diglett's Cave Internal Connections (Verified Turn 42438)
- Ladder at (5, 31) <-> Ladder at (17, 33).
- Ladder at (3, 3) <-> Ladder at (17, 3).
- Ladder at (17, 33) is a sub-area dead end (no path to exit at 15, 5).