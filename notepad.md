# Johto Journey: Gem's Log

## Tile Mechanics (Verified)
- FLOOR: Standard traversable ground.
- WALL: Impassable barrier.
- TALL_GRASS: Standard traversable grass; triggers wild encounters.
- LEDGE_HOP_RIGHT: One-way (East only). Jump from left, wall from right.
- LEDGE_HOP_DOWN: One-way (South only). Jump from top, wall from bottom.
- LEDGE_HOP_LEFT: One-way (West only). Jump from right, wall from left.
- DOOR / STAIRCASE / WARP_CARPET: Warp points between maps or floors.
- HEADBUTT_TREE / CUT_TREE / WATER: Impassable; require HM moves.

## NPCs & Interactions
### Mr. Pokémon's House (26_10)
- MR. POKÉMON (ID 1): (3, 5). Gave MYSTERY EGG.
- PROF. OAK (ID 2): (6, 5). Gave POKéDEX. (Left the building)

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

## Verification List
- Route 29 (24_3): Verify Cut Tree at (21, 11).

## Lessons Learned
- NPCs act as walls; plan paths around them.
- Buildings are often larger than they appear; check all sides.
- Tool Usage: Verify input schemas and handle input dictionaries explicitly.
- Exploration: Check building corners and behind counters.
- Scripted Events: Treat character movement during dialogue as completed interaction.
- Ledges: Strictly one-way. Jumping simulates moving two tiles.
- Pathfinding: Treat 'unseen' tiles as potentially walkable but verify in-game.
- Navigation: Use 'navigate' tool with 'find_path' coordinates for efficiency.

## Strategy for Return Trip
- [Turn 245] Current Goal: Returning to New Bark Town via Cherrygrove City.
- Note: Prepare for a potential rival encounter near the Cherrygrove exit.
- Healing: Heal at Cherrygrove Pokemon Center (29, 3) before heading east.