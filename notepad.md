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

### Current Objective: Clear Team Rocket from Azalea Town
- **Status:** A Rocket Grunt is blocking the Azalea Gym.
- **Hypothesis 1 (Gym Grunt):** Talk to Kurt to get him to scare the grunt away. (Failed, Kurt just gave cryptic dialogue about the 'forest's protector'.)
- **New Hypothesis:** The solution involves the 'forest's protector' and the Farfetch'd in Kurt's house. I should talk to Kurt's apprentice again.

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