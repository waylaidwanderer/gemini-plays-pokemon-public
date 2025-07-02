# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER.
- **Traversable:** FLOOR, GRASS.
- **Warps:** DOOR, CAVE, LADDER, WARP_CARPET_RIGHT, WARP_CARPET_DOWN.
- **Directional Warps:** WARP_CARPET_LEFT (Must be entered by moving left onto the tile).
- **One-Way Down:** LEDGE / FLOOR_ALLOW_HOP_DOWN (Horizontal movement is permitted).
- **Complex One-Way:** FLOOR_UP_WALL (Can be entered from below, but not exited up or down. Sideways movement is permitted).

### Key Learnings
- HMs must be used from the PACK menu.
- HM moves are permanent.
- All map objects (NPCs, items, signs) act as walls.

## II. Quest Progression

### Current Objective: Obtain HM01 (Cut)
- **Primary Hypothesis:** The key to progressing is in Ilex Forest. An NPC in Azalea mentioned a 'Charcoal Man' whose Pokémon can use CUT. This is the only remaining lead after being blocked at the Slowpoke Well.
- **Plan:** Explore Ilex Forest to find the Charcoal Man and his lost Farfetch'd.

### Objective: Investigate Slowpoke Well
- **Status:** Kurt has gone to the Slowpoke Well to confront Team Rocket. This is the main story objective.
- **Previous Hypothesis (Incorrect):** The path was blocked by a Rocket Grunt. The correct trigger was speaking to Kurt in his house, which caused him to go to the well and clear the path.

### Pathfinder Bug
- **Issue:** The `path_finder_plus` tool incorrectly reported no path available when a path around an on-screen NPC was possible. 
- **Status:** Tool has been updated with better debugging, but the core logic flaw may still exist. Needs to be monitored.