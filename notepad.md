# Johto Journey: Gem's Log

## Strategic Plan: Visit Mr. Pokémon
1. Exit New Bark Town and head west to Route 29.
2. Pass through Cherrygrove City.
3. Find Mr. Pokémon's house north of Cherrygrove City.
4. Collect the Mystery Egg and return it to Professor Elm.

## Tile Mechanics
### Global
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
- AIDE (ID 2): Gave a Potion for the journey.

## Discovered Locations (New Bark Town 24_4)
- Player's House: Door (13, 5), Sign (11, 5).
- Elm's House: Door (11, 13), Sign (9, 13).
- Neighbor's House: Door (3, 11).
- Professor Elm's Lab: Door (6, 3), Sign (3, 3).
- Town Sign: (8, 8).

## Lessons Learned
- NPCs act as walls; plan paths around them.
- Buildings are often larger than they appear; check all sides for entrances.
- Signs identify buildings without entering.
- Starter Pokémon: Cyndaquil (Fire), Totodile (Water), Chikorita (Grass). Cyndaquil chosen. Nickname: Calcifer.
- Tool Usage: Verify input schemas and handle input dictionaries explicitly to avoid KeyErrors.
- Exploration: Check building corners and behind counters for unseen tiles.
- Scripted Events: Some NPCs may move the player during dialogue. Treat the move as a completed interaction unless new dialogue is triggered.