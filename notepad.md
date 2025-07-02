# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER.
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
- **Status:** Kurt has gone to the Slowpoke Well to confront Team Rocket. This is the main story objective.
- **Hypothesis:** I need to enter the well and help Kurt defeat Team Rocket.

### Blocked Path: Ilex Forest
- **Status:** The western part of Ilex Forest is blocked by a tree that requires CUT. My initial attempts to find a way around or a trigger to get CUT within the eastern part of the forest have failed. I will return here after dealing with the Slowpoke Well.

## III. Technical Notes

### Pathfinder Bug
- **Issue:** The `path_finder_plus` tool incorrectly reported no path available when a path around an on-screen NPC was possible. 
- **Status:** Tool has been updated with better debugging, but the core logic flaw may still exist. Needs to be monitored.

## IV. Future Experiments
- Test horizontal movement on LEDGE tiles.