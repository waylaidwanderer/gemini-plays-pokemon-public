# Johto Journey: Gem's Log

## Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable; wild encounters.
- LEDGE_HOP_DOWN: One-way jump South (2 tiles).
- LEDGE_HOP_LEFT: One-way jump West (2 tiles).
- LEDGE_HOP_RIGHT: One-way jump East (2 tiles).
- HEADBUTT_TREE: Impassable (requires Headbutt).
- COUNTER: Interactable (face to talk to NPC behind).
- WARP_CARPET_DOWN: Exit map South.
- LADDER: Warp to different floor.
- BOOKSHELF / WINDOW / TREE / HEDGE: Impassable (acts as WALL).
- PC: Interactable (face to use).

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
- Menu Navigation: Do NOT mix directional buttons and action buttons (A/B/Start/Select) in the same turn.

## Cherrygrove Pokecenter 1F (26_5)
- NPCs: Nurse (Counter at Row 2), Teacher (1, 6), Fisher (2, 3), Gentleman (8, 6).
- GENTLEMAN (ID 3): (8, 6). Confirmed PC is free to use. (Talked to)
- TEACHER (ID 4): (1, 6). Mentioned Communication Center upstairs is still being finished. (Talked to)

## Progress Summary
- RIVAL ENCOUNTER: Defeated MALICE at eastern exit of Cherrygrove City. (Turn 315)
- EVENT: Delivered Mystery Egg to Prof. Elm. Received POKé BALL x5. (Turn 324)
- EVENT: Set up money saving with Mom. (Turn 334)
- WILD ENCOUNTER: Caught Lv2 Pidgey (ICARUS) on Route 29. (Turn 352)

## Training Tracker
- Training Goal: Calcifer and Icarus to Lv10.
- Started: Turn 421.
- Current Status: Icarus Lv2 (5/13 HP), Calcifer Lv6 (12/21 HP).