# Johto Journey: Gem's Log

## Tile Mechanics (Verified)
- FLOOR: Standard traversable ground.
- WALL: Impassable barrier.
- TALL_GRASS: Standard traversable grass; triggers wild encounters.
- LEDGE_HOP_RIGHT: One-way (East only).
- LEDGE_HOP_DOWN: One-way (South only).
- LEDGE_HOP_LEFT: One-way (West only).
- DOOR / STAIRCASE / WARP_CARPET: Warp points.
- HEADBUTT_TREE / CUT_TREE / WATER: Impassable; require HM moves.

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

## Strategy: Return to New Bark Town
- HOW: Route 30 path (15, 37) -> (14, 37) -> (13, 37) -> (13, 38) -> (13, 39) -> (13, 40) -> (13, 41) -> (13, 42) -> (13, 43) -> (12, 43) -> (11, 43) -> (11, 44) -> (11, 45) -> (11, 46) -> (11, 47) -> (11, 48) -> (11, 49) -> (10, 49) -> (9, 49) -> (8, 49) -> (7, 49) -> (7, 50) -> (7, 51) -> (7, 52) -> (7, 53) -> (6, 53).
- Prep: Heal at Cherrygrove Pokemon Center (29, 3). Anticipate rival battle at eastern exit of Cherrygrove City.
## Navigation: Path to Pokemon Center (26_3)
- Path: (16, 0) -> (16, 4) -> (29, 4).
- Target: Warp at (29, 3).
## Cherrygrove Pokecenter 1F (26_5)
- NPCs: Nurse (Counter at Row 2), Teacher (1, 6), Fisher (2, 3), Gentleman (8, 6).
- Waypoint: Face counter at (3, 3) or (4, 3) to heal.
- GENTLEMAN (ID 3): (8, 6). Confirmed PC is free to use. (Talked to)
- TEACHER (ID 4): (1, 6). Mentioned Communication Center upstairs is still being finished. (Talked to)