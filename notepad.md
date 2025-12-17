# Johto Journey: Gem's Log

## Strategic Plan: Visit Mr. Pokémon
1. Exit New Bark Town and head west to Route 29. (Done)
2. Pass through Cherrygrove City.
3. Find Mr. Pokémon's house north of Cherrygrove City.
4. Collect the Mystery Egg and return it to Professor Elm.

## Route 29 (24_3)
- Started exploration at Turn 129.
- Current Status: Heading west along Row 6 northern corridor.
- Wild Encounters: Pidgey (Lv2).
- Key Locations:
    - New Bark Town Entrance: (59, 9).
    - Route Sign: (51, 7).
    - Northern Path Gap: (36, 9) floor access.
    - Northern Floor Path Start: (31, 6).
- Obstacles:
    - HM Obstacle: Cut Tree at (21, 11) and (30, 9).
    - HM Obstacle: Headbutt Trees at (18, 13)-(21, 13).
    - Ledge Barrier (Row 10): (28, 10) is LEDGE_HOP_LEFT.
    - Ledge Barrier (Row 4): (15, 4) is LEDGE_HOP_RIGHT (East only).

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
- TEACHER (ID 3): (15, 11).
- FISHER (ID 5): (25, 3).
- COOLTRAINER_M (ID 6): (13, 4).

## Lessons Learned
- NPCs act as walls; plan paths around them.
- Buildings are often larger than they appear; check all sides.
- Tool Usage: Verify input schemas and handle input dictionaries explicitly.
- Exploration: Check building corners and behind counters.
- Scripted Events: Treat character movement during dialogue as completed interaction.

## Exploration Log
- Turn 154: (36, 9). Attempted Row 5/4 path west.
- Turn 158: Row 4 blocked by ledge at (15, 4).
- Turn 159: Dropped to Row 6. Found clear floor path west of x=16.
- Turn 161: (10, 6). Row 6 corridor confirmed as floor/grass path west. Jumped ledge at (8, 6).
- Turn 164: (0, 6). Reached western edge of Route 29. Transitioning to Cherrygrove City.
## Cherrygrove City (26_3)
- Reached at Turn 164.
- Status: Exploring.
- Key Locations:
    - Route 29 Transition: (39, 6).
- GRAMPS (ID 1): Offered a tour of Cherrygrove City at (32, 6). (Accepted tour)