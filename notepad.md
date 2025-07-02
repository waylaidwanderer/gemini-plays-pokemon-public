# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER, PILLAR.
- **Traversable:** FLOOR, GRASS.
- **Standard Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN, WARP_CARPET_LEFT.
- **One-Way Entrance Warps:** WARP_CARPET_RIGHT (A one-way entrance. Cannot be used to exit the forest).
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT (Cannot be climbed up).
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

### Ilex Forest Farfetch'd Puzzle
- **Goal:** Herd the Farfetch'd to the boy who ran off, likely waiting near the CUT tree at (8, 25).
- **Constraint:** I am trapped in this area of the forest due to the one-way warp at (3, 42).

- **Hypothesis 1 (H1) - FAILED:** The Farfetch'd moves based on noise made by the player. 
  - **Experiment Log:**
    - **Test 1.1:** Interacting with twigs by pressing 'A' while facing various directions has no effect.
    - **Test 1.2:** Stepping onto twigs while facing various directions has no effect.
  - **Conclusion:** H1 is false. The trigger is not based on noise from twigs in the way I've tested.

- **Hypothesis 2 (H2) - Current Test:** The puzzle state (including the Farfetch'd's position) can be reset by moving to a distant part of the map and returning.
  - **Plan:** Travel to the southeast corner of the map near the entrance, then return to the puzzle area at (22, 29) to check if the Farfetch'd has reappeared.

## IV. Tool Development Notes

### `farfetchd_herder`
- **Status:** Critically flawed. Cannot be fixed until the puzzle mechanics are understood.
- **Known Issues:**
    1. The tool hardcodes the Farfetch'd's starting position and does not search for it.
    2. The movement logic is based on a failed hypothesis and is incorrect.
- **Next Steps:** Must understand the puzzle mechanics through experimentation before attempting to fix this tool again.

- **Hypothesis 3 (H3) - NEW:** The Farfetch'd moves in the direction the player is facing when they step on a twig. 
  - **Plan:** Locate the Farfetch'd, find a new twig, and test this by facing a specific direction before stepping on the twig.