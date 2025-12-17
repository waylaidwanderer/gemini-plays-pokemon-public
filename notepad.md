# Johto Journey: Gem's Log

## Strategic Plan: Visit Mr. Pokémon
1. Exit New Bark Town and head west to Route 29. (Done)
2. Pass through Cherrygrove City. (Done)
3. Find Mr. Pokémon's house north of Cherrygrove City on Route 30. (In progress)
4. Collect the Mystery Egg and return it to Professor Elm.

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
### Cherrygrove City (26_3)
- GRAMPS (ID 1): Gave city tour and MAP CARD. House at (25, 9).
- TEACHER (ID 3): (28, 12).
- YOUNGSTER (ID 4): (22, 7).
- FISHER (ID 5): (25, 3)? - Verify location when nearby.

### Route 30 (26_1)
- Sign at (9, 43): Route 30.
- Item at (8, 35): Antidote (Collected).
- Warp at (7, 39).

## Lessons Learned
- NPCs act as walls; plan paths around them.
- Buildings are often larger than they appear; check all sides.
- Tool Usage: Verify input schemas and handle input dictionaries explicitly.
- Exploration: Check building corners and behind counters.
- Scripted Events: Treat character movement during dialogue as completed interaction.