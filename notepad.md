# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW
- **Traversable:** FLOOR, GRASS
- **Standard Warps:** DOOR, CAVE, LADDER
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

### World Knowledge Graph (WKG) Commitment
- **WKG Status:** My WKG is more complete than I thought. My attempts to retroactively add edges were based on a flawed memory. I must trust my tools' data analysis over my own assumptions and be diligent about adding *new* connections moving forward.

## II. Quest Progression & Blockers### SOLVED: Ilex Forest Gatehouse Puzzle
- **Solution:** Interact with the Officer at (5, 2) from a 2-tile distance (at position (5, 4)). This triggers a dialogue warning about Ilex Forest and unlocks the western warps leading into the forest.

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

## III. Tool Notes
- **`path_master`:** My pathfinding tool is reliable. I must be more careful to provide it with valid, traversable coordinates as input to avoid failed calls.
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT