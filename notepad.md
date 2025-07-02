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
    - **Active Hypothesis (Reset Puzzle):** My `quest_strategist` suggested that leaving the area entirely and returning might reset the Farfetch'd's position. I am currently attempting to exit the forest to test this.
    - **Secondary Hypotheses (from Agent):**
        1. Find a path out of the current dead-end area to find new twigs on the other side of the Farfetch'd.
        2. Use twigs to intentionally push the bird through 'impassable' trees to a new area.
        3. Step on the two known twigs in very quick succession to push the bird directly north.
- **HEADBUTT_TREE:** Impassable.