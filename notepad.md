# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER, PILLAR.
- **Traversable:** FLOOR, GRASS.
- **Warps:** DOOR, CAVE, LADDER, WARP_CARPET_RIGHT, WARP_CARPET_DOWN.
- **Directional Warps:** WARP_CARPET_LEFT (Must be entered by moving left onto the tile).
- **One-Way Down:** LEDGE / FLOOR_ALLOW_HOP_DOWN (Horizontal movement needs to be tested).
- **Complex One-Way:** FLOOR_UP_WALL (Can be entered from below, but not exited up or down. Sideways movement is permitted).

### Key Learnings
- HMs must be used from the PACK menu.
- HM moves are permanent.
- All map objects (NPCs, items, signs) act as walls.

## II. Quest Progression

### Current Objective: Investigate Slowpoke Well
- **Status:** I am currently blocked from entering the Slowpoke Well by a Team Rocket Grunt. 
- **Hypothesis 1:** Talk to the grunt directly. (Failed, he just repeats dialogue)
- **Hypothesis 2:** Talk to Kurt in his house to trigger an event. (Failed, Kurt gave dialogue but did not move)
- **Hypothesis 3:** Talk to Kurt's apprentice. (Failed, no dialogue triggered)
- **Current Hypothesis:** Talk to every NPC in Azalea Town to find a new clue.

### Blocked Path: Ilex Forest
- **Status:** The western part of Ilex Forest is blocked by a tree that requires CUT. I will return here after dealing with the Slowpoke Well.

## III. Technical Notes & Experiments

### Pathfinder
- **Status:** The pathfinder now correctly accounts for off-screen obstacles by reading map markers. This should prevent most pathing errors.

### Future Experiments
- Test horizontal movement on LEDGE tiles.
- Formally test all new tile types to confirm traversability from all directions.

### Future Experiments
- Test horizontal movement on LEDGE tiles.
- Formally test all new tile types to confirm traversability from all directions.