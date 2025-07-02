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
    - **Current Hypothesis:** This is a sound-based *herding* puzzle. Stepping on twigs makes noise, causing the Farfetch'd to run in the opposite direction, likely through impassable terrain like trees. The goal is to strategically make noise to guide it to its owner.
    - **Successful Steps:**
        1. Stepped on twig at (22, 30), scaring Farfetch'd from (22, 29) to (22, 27).
        2. Stepped on twig at (23, 30), scaring Farfetch'd from (22, 27) to an unknown location (presumed northwest).
    - **Failed Approach:** Systematic exploration of all walkable paths in the maze has confirmed they are all dead ends. The solution is not simple pathfinding.

### Reflection & New Hypotheses (Post-Dead-Ends)
My systematic exploration revealed all paths are dead ends, and I have confirmed I cannot leave the forest. This means the solution must be contained entirely within this maze.
- **Primary Hypothesis (Sound-Based Herding):** The puzzle is not about finding a single path. I must step on twigs in a specific sequence or from specific directions to guide the Farfetch'd through the impassable trees. The bird moves opposite to the sound source.
- **Secondary Hypothesis (Hidden Mechanic):** There is a hidden mechanic I'm missing. I need to experiment with facing different directions when stepping on a twig.