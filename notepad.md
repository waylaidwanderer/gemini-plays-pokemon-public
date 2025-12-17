# Johto Journey: Gem's Log

## Strategic Plan: Visit Mr. Pokémon
1. Exit New Bark Town and head west to Route 29. (Done)
2. Pass through Cherrygrove City.
3. Find Mr. Pokémon's house north of Cherrygrove City.
4. Collect the Mystery Egg and return it to Professor Elm.

## Route 29 (24_3)
- Started exploration at Turn 129.
- Current Status: Heading west on Row 10 floor path.
- Wild Encounters: Pidgey (Lv2).
- Key Locations:
    - New Bark Town Entrance: (59, 9).
    - Route Sign: (51, 7).
    - Northern Path Gap: (36, 9) floor access.
- Obstacles:
    - HM Obstacle: Cut Tree at (21, 11) and (30, 9).
    - HM Obstacle: Headbutt Trees at (18, 13)-(21, 13).

## Tile Mechanics (Verified)
- FLOOR: Standard traversable ground.
- WALL: Impassable barrier.
- TALL_GRASS: Standard traversable grass; triggers wild encounters.
- LEDGE_HOP_RIGHT: One-way (East only). Jump from left, wall from right.
- LEDGE_HOP_DOWN: One-way (South only). Jump from top, wall from bottom.
- LEDGE_HOP_LEFT: One-way (West only). Jump from right, wall from left.
- DOOR / STAIRCASE / WARP_CARPET: Warp points between maps or floors.
- HEADBUTT_TREE: Impassable; requires Headbutt move.
- CUT_TREE: Impassable; requires Cut HM.
- WATER: Impassable; requires Surf HM.
- Interactive: PC (activates from below), Bookshelves, Windows, Trashcans (all impassable).

## NPCs & Interactions
### New Bark Town (24_4)
- TEACHER (ID 1): Near town sign (6, 8).
- FISHER (ID 2): Southern town area.
- RIVAL (ID 3): Lab window (3, 2).
- MOM: PlayersHouse1F; gives Pokégear.
- PROF_ELM: ElmsLab (5, 2); gives starter and quest.

### Route 29 (24_3)
- YOUNGSTER (ID 2): (27, 15). Advised to stay out of grass if weak. (Talked to)
- FISHER (ID 5): (25, 3).
- TEACHER (ID 3): (15, 11).

## Lessons Learned
- NPCs act as walls; plan paths around them.
- Buildings are often larger than they appear; check all sides.
- Tool Usage: Verify input schemas and handle input dictionaries explicitly.
- Exploration: Check building corners and behind counters.
- Scripted Events: Treat character movement during dialogue as completed interaction.
## Exploration Log
- Turn 154: (36, 9). Attempting to follow northern floor path (Row 5/4) west to bypass central barriers.
- Hypothesis: Row 5/4 provides a continuous path west that drops down to Row 10 near x=18.
- Test: Use find_path to (0, 10) and follow it.