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
- The `area_explorer` tool is fundamentally broken. I will not rely on it. Future complex pathfinding will be done manually or with `run_code` for isolated logic tests.
- I must be more diligent about immediate data management (notepad, markers, world graph) to avoid cascading errors.

### Puzzles
- **Ilex Forest Farfetch'd:** Suspect this is a sound-based herding puzzle. The twigs on the floor likely make noise and scare the Farfetch'd. The goal is to approach it without stepping on them. Failed attempts so far:
    1. Interacting with the tree at (23, 29).
    2. Approaching (22, 29) from below and interacting.
    3. Approaching (22, 29) from the left and interacting.