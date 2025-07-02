# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER, PILLAR.
- **Traversable:** FLOOR, GRASS.
- **Standard Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN, WARP_CARPET_LEFT.
- **One-Way Entrance Warps:** WARP_CARPET_RIGHT (A one-way entrance. Cannot be used to exit the forest).
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT (Cannot be climbed up. Sideways movement needs testing).
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
- **Current Hypothesis (H1):** The Farfetch'd moves based on the direction the player is *facing* when stepping on a twig. Noise from stepping on a twig scares it away in the opposite direction of the player's facing direction.
- **Experiment Log:**
    - **Test 1:** Stood on twig at (22, 30), faced down, pressed 'A'. **Result:** No effect. Hypothesis that 'A' button makes noise is likely false. The noise is from stepping *onto* the twig.
    - **Test 2:** Stood at (22, 31), moved up to (22, 30) to step on the twig while facing up. **Result:** No effect. Farfetch'd did not appear or move.

## IV. Tool Development Notes

### `farfetchd_herder`
- **Status:** Critically flawed. The tool cannot solve the puzzle.
- **Known Issues:**
    1. The tool hardcodes the Farfetch'd's starting position. It needs to be able to find the Farfetch'd on the map first.
    2. The movement logic is incorrect. It doesn't accurately predict how the Farfetch'd moves in response to the player.
- **Next Steps:** I must first understand the puzzle mechanics through experimentation before I can fix this tool.