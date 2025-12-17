# Johto Journey: Gem's Log

## Strategic Plan: Visit Mr. Pokémon
1. Exit New Bark Town and head west to Route 29. (Done)
2. Pass through Cherrygrove City.
3. Find Mr. Pokémon's house north of Cherrygrove City.
4. Collect the Mystery Egg and return it to Professor Elm.

## Route 29 (24_3)
### Tile Mechanics
- FLOOR: Standard traversable ground.
- WALL: Impassable barrier (trees/ledges).
- GRASS: Potential wild Pokemon encounters.

### Discovered Locations
- Route Sign: (51, 7).
- New Bark Town Entrance: (59, 9).

### Wild Encounters
- Pidgey (Lv2)

## Tile Mechanics (Global)
- FLOOR: Standard traversable ground.
- WALL: Impassable barrier.
- DOOR: Warp tile leading inside/outside.
- STAIRCASE: Warp tile between floors.
- WATER: Impassable without Surf HM.
- HEADBUTT_TREE: Impassable small tree.
- WARP_CARPET_DOWN: Exit tile at the bottom of building interiors.
- BOOKSHELF: Impassable background object.
- WINDOW: Impassable background object.
- HEALING_MACHINE: Potential restoration point at (2, 1).
- TRASHCAN: Impassable background object at (9, 3).
- PC: Impassable background object at (3, 5).
- BOOKSHELVES: Impassable at (6,1)-(9,1) and (6,7)-(9,7).
- WINDOW: Impassable at (5,0).

## NPCs & Interactions
### New Bark Town (24_4)
- TEACHER (ID 1): Standing near the town sign at (6, 8).
- FISHER (ID 2): Wandering the southern part of town.
- RIVAL (ID 3): Peering into the Lab window at (3, 2).
- MOM (PlayersHouse1F): Provides Pokégear.

### PlayersNeighborsHouse (24_8)
- COOLTRAINER_F (ID 1): Researcher enthusiast at (2, 3).

### ElmsLab (24_5)
- PROF_ELM (ID 1): Researcher at (5, 2).
- AIDE (ID 2): Located in the lab.

### Route 29 (24_3)
- COOLTRAINER_M (ID 1): Standing at (50, 12). Advised that Pokemon hide in grass. (Talked to)

## Lessons Learned
- NPCs act as walls; plan paths around them.
- Buildings are often larger than they appear; check all sides for entrances.
- Signs identify buildings without entering.
- Tool Usage: Verify input schemas and handle input dictionaries explicitly to avoid KeyErrors.
- Exploration: Check building corners and behind counters for unseen tiles.
- Scripted Events: Some NPCs may move the player during dialogue. Treat the move as a completed interaction unless new dialogue is triggered.
- LEDGE_HOP_RIGHT: One-way traversable. Can jump to the right (east) from the left tile, but acts as a wall from the right.
- LEDGE_HOP_DOWN: One-way traversable. Can jump down (south) from the top tile, but acts as a wall from the bottom.
- TALL_GRASS: Standard traversable grass that triggers wild encounters.
- Ledge Barrier: (43, 8)-(43, 12) (Right jump) and (39, 13)-(42, 13) (Down jump). Path west discovered at (43, 14)-(43, 15).
- Barrier at x=37: Wall of trees from y=12 to y=15. Passable via Row 16.
- YOUNGSTER (ID 2): Wandering near (27, 15). Advised to stay out of grass if Pokemon are weak. (Talked to)