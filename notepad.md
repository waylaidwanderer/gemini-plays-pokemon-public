# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER, PILLAR.
- **Traversable:** FLOOR, GRASS.
- **Standard Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN, WARP_CARPET_LEFT.
- **One-Way Exit Warps:** WARP_CARPET_RIGHT (Seems to be a one-way entrance from IlexForestAzaleaGate. Cannot be used to return).
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN (Cannot be climbed up. Horizontal movement needs testing).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

### Key Learnings
- HMs must be used from the PACK menu.
- HM moves are permanent.
- All map objects (NPCs, items, signs) act as walls.

## II. Quest Progression

### Current Objective: Clear Team Rocket from Azalea Town
- **Status:** I am currently exploring Ilex Forest, which seems connected to the Farfetch'd quest needed to get the HM for CUT. This HM is required to advance past the tree blocking the path to the western part of the forest.
- **Active Hypothesis:** I need to find the boy who ran off with the Farfetch'd. My main lead is the spot where a Youngster vanished at (22, 29).

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree that requires CUT. I will return here after obtaining the HM.

## III. Strategy & Planning
- The `area_explorer` tool has been fixed and is now reliable. I need to solve the Farfetch'd puzzle with a new approach, as simple exploration has failed.
- I must be more diligent about immediate data management (notepad, markers, world graph) to avoid cascading errors.

### Puzzles
- **Ilex Forest Farfetch'd Puzzle:**
    - **Current Situation:** I am trapped in the forest. The warp at (3, 42) is a one-way entrance. I cannot leave until this puzzle is solved. All walkable paths have been confirmed to be dead ends.
    - **Primary Hypothesis (Sound-Based Herding):** The solution *must* involve herding the Farfetch'd by making sounds with the available twigs. The bird moves through impassable terrain (trees) in the opposite direction of the sound.
    - **Secondary Hypothesis (Directional Input):** The direction I am facing when I step on a twig might influence the direction the Farfetch'd runs. I need to test this systematically.
    - **Known Twig Interactions:**
        1. Stepping on twig at (22, 30) scared Farfetch'd from (22, 29) to (22, 27).
        2. Stepping on twig at (23, 30) scared Farfetch'd from (22, 27) to an unknown location (presumed northwest).
    - **Current Goal:** Find the Farfetch'd and/or experiment with the twigs to herd it towards the exit near the CUT tree.