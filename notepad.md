# Johto Journey: Gem's Log

## Tile Mechanics (Verified)
- FLOOR: Standard traversable ground.
- WALL: Impassable barrier.
- TALL_GRASS: Standard traversable grass; triggers wild encounters.
- LEDGE_HOP_RIGHT: One-way (East only).
- LEDGE_HOP_DOWN: One-way (South only).
- LEDGE_HOP_LEFT: One-way (West only).
- DOOR / STAIRCASE / WARP_CARPET: Warp points.
- BOOKSHELF: Impassable (acts as WALL).
- WINDOW: Impassable (acts as WALL).
- TREE / HEDGE: Impassable (acts as WALL).
- HEADBUTT_TREE / CUT_TREE / WATER: Impassable; require HM moves.
- unseen (❓): Unknown traversability; requires exploration.

## NPCs & Interactions
### Mr. Pokémon's House (26_10)
- MR. POKÉMON (ID 1): (3, 5). Gave MYSTERY EGG.
- PROF. OAK (ID 2): (6, 5). Gave POKéDEX.

### Cherrygrove City (26_3)
- GRAMPS (ID 1): Gave city tour and MAP CARD. House at (25, 9).
- TEACHER (ID 3): (28, 12).
- YOUNGSTER (ID 4): (22, 7).

### Route 30 (26_1)
- Sign at (9, 43): Route 30.
- Item at (8, 35): Antidote (Collected).
- Warp at (7, 39).
- YOUNGSTER (ID 5): (7, 30). Confirmed Mr. Pokémon's house is "a bit farther ahead". (Talked to)
- Sign at (13, 29): MrPokemonsHouseDirectionsSign. Says "STRAIGHT AHEAD!". (Read)
- YOUNGSTER (ID 1): (5, 26).

## Lessons Learned
- NPCs act as walls.
- Buildings are often larger than they appear.
- Tool Usage: Verify input schemas and handle input dictionaries explicitly.
- Navigation: Use 'navigate' tool with 'find_path' coordinates for efficiency.
- Ledges: Strictly one-way. Jumping moves the player two tiles.

## Cherrygrove Pokecenter 1F (26_5)
- NPCs: Nurse (Counter at Row 2), Teacher (1, 6), Fisher (2, 3), Gentleman (8, 6).
- Waypoint: Face counter at (3, 3) or (4, 3) to heal.
- GENTLEMAN (ID 3): (8, 6). Confirmed PC is free to use. (Talked to)
- TEACHER (ID 4): (1, 6). Mentioned Communication Center upstairs is still being finished. (Talked to)

## Strategy: Johto Gym Challenge
- Goal: Defeat Gym Leader Falkner in Violet City.
- HOW: 
  1. Exit New Bark Town West to Route 29 (Target: (0, 9)).
  2. Capture first team members (Pidgey/Rattata/etc.) using POKé BALLS.
  3. Pass through Cherrygrove City to Route 30.
  4. Navigate North through Route 30 and Route 31 to Violet City.
  5. Train Calcifer and new team members to ~Lv10 before the Gym.

## Progress Log
- RIVAL ENCOUNTER: Defeated Rival (Totodile Lv5) at eastern exit of Cherrygrove City (34, 6). Rival's name confirmed as "MALICE". (Turn 315)
- EVENT: Delivered Mystery Egg to Prof. Elm. Received POKé BALL x5 from Aide. Elm suggested Gym Challenge. (Turn 324)
- EVENT: Set up money saving with Mom. (Turn 334)