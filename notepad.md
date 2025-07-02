# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER, PILLAR.
- **Traversable:** FLOOR, GRASS.
- **Standard Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN, WARP_CARPET_LEFT.
- **One-Way Entrance Warps:** WARP_CARPET_RIGHT (A one-way entrance. Cannot be used to exit the forest).
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT (Cannot be climbed up. Horizontal movement needs testing).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

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

### Puzzles
- **Ilex Forest Farfetch'd Puzzle:**
    - **Current Situation:** I am trapped in the forest. The warp at (3, 42) is a one-way entrance. I cannot leave until this puzzle is solved. All walkable paths have been confirmed to be dead ends.
    - **Failed Hypothesis (Reset Puzzle):** My `quest_strategist` suggested that leaving the area entirely and returning might reset the Farfetch'd's position. This failed as the entrance warp is one-way.
    - **Active Plan:** My `farfetchd_herder` tool is critically flawed. I will redefine it with a more robust logic that can find the Farfetch'd regardless of its starting position. After fixing the tool, I will use it to solve the puzzle.