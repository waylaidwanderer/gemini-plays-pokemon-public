# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC)
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE, LADDER (Acts as a two-way vertical warp)
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must walk in the indicated direction to activate, 'A' button does not work).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Hypotheses & Assumptions

#### Tile Mechanics
- **BUOY:** Likely impassable, similar to WATER. Needs testing.

#### General Gameplay
- **Route 32 Path:** My pathfinder has confirmed that the eastern fork of Route 32 is a dead end due to one-way `FLOOR_UP_WALL` tiles. The only way south to Union Cave is via the western path.
- **Headbutt Move:** Assumption that `HEADBUTT_TREE`s require the 'Headbutt' move. I need to find the TM or a move tutor to test this.

## II. Quest Progression & Puzzles

### Blocked Path: Ilex Forest West
- **Objective:** Clear the CUT tree at (8, 25) to access the western part of the forest.
- **Prerequisite:** Obtain HM01 (CUT).
- **Plan:** After dealing with the Slowpoke Well situation and getting CUT, I will return to this location.

## III. Tool Development Log
- **`path_master_v3` (Corrected):** My pathfinder tool was correct all along. I incorrectly assumed it was broken when it failed to find a path on the eastern fork of Route 32. My manual tests confirmed that the path is indeed blocked by one-way `FLOOR_UP_WALL` tiles at (14, 6), just as the tool predicted. I must trust the tool's output and analyze the map more carefully when it reports no path.
- **HEADBUTT_TREE:** Quest Strategist suggests these require the move 'Headbutt' to interact with, not the standard 'A' button.

## IV. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **FRUIT_TREE:** Gives a 'BERRY' item when interacted with. Seems to be a one-time collection per tree.

### To-Do/Reminders
- Test the following tile types on Route 32 when possible:
  - BUOY
  - FLOOR_ALLOW_HOP_RIGHT
  - FLOOR_ALLOW_HOP_DOWN_LEFT
  - FLOOR_ALLOW_HOP_DOWN_RIGHT

## Personal Rules & Reminders
- **Check Map Markers!** Before interacting with an NPC or navigating to a specific spot, always check existing map markers to avoid wasting time on defeated trainers or repeating actions.