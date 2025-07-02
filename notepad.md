# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW.
- **Traversable:** FLOOR, GRASS.
- **Standard Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN, WARP_CARPET_LEFT.
- **WARP_CARPET_RIGHT:** Confirmed bidirectional warp. Activated by stepping onto the tile.
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT (Cannot be climbed up).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

### Tile Mechanics Verification Log
*This log tracks every unique tile type encountered and its verified behavior.*
- **AzaleaTown (8_7):**
  - `FLOOR`: Traversable (Verified)
  - `WALL`: Impassable (Verified)
  - `HEADBUTT_TREE`: Impassable (Verified)
  - `WARP_CARPET_LEFT`: Warp (Verified)
  - `DOOR`: Warp (Verified)
  - `CAVE`: Warp (Verified)
  - `LEDGE`: One-way down (Verified)

### Key Learnings
- HMs must be used from the PACK menu.
- HM moves are permanent.
- All map objects (NPCs, items, signs) act as walls.

## II. Quest Progression

### Current Objective: Clear Team Rocket from Azalea Town
- **Status:** I am currently exploring Ilex Forest, which seems connected to the Farfetch'd quest needed to get the HM for CUT. This HM is required to advance past the tree blocking the path to the western part of the forest.

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree that requires CUT. I will return here after obtaining the HM.

## III. Strategy & Planning

### Slowpoke Well Puzzle
- **Goal:** Get past the Rocket Grunt at (31, 9) to enter the well at (31, 7).
- **Hypothesis 1:** Talk to Kurt, then the grunt, then return to Kurt. **Result: FAILED.** Kurt repeats dialogue.
- **Hypothesis 2:** The grunt at (31, 9) is not fully blocking the path. I can walk around him. **Result: PENDING.** My pathfinder tool says no path exists, but I suspect the tool is flawed.

## IV. Tool Development Notes

### `farfetchd_herder`
- **Status:** Updated and functional. Now correctly searches the map for the Farfetch'd object before attempting any herding logic.
- **Complex Warps:** Some warps, like the 1x2 WARP_CARPET_RIGHT in Ilex Forest, may have special activation conditions (e.g., only one of the tiles is an exit).
- **Impassable:** BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW.