# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC)
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE, LADDER (Acts as a two-way vertical warp)
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must walk in the indicated direction to activate).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Hypotheses & Assumptions
- **BUOY:** Likely impassable, similar to WATER. Needs testing once Surf is available.
- **Headbutt Move:** Assumption that `HEADBUTT_TREE`s require the 'Headbutt' move. I need to find the TM or a move tutor to test this.

## II. Quest Progression & Puzzles

### Blocked Path: Ilex Forest West
- **Objective:** Clear the CUT tree at (8, 25) to access the western part of the forest.
- **Prerequisite:** Obtain HM01 (CUT).
- **Plan:** After dealing with the Slowpoke Well situation and getting CUT, I will return to this location.

## III. Tool Development Log
- **`path_master_v5` (New):** Created to correctly handle directional `LEDGE_HOP_*` tiles, which the previous version failed to do. This is critical for accurate pathfinding.
- **`path_master_v4` (Corrected):** Fixed an issue where the tool was incorrectly marking all off-screen objects as impassable. It now correctly takes a list of on-screen obstacles.
- **`path_master_v3` (Corrected):** Confirmed the tool was not broken. My manual tests confirmed the path on Route 32 was indeed blocked by one-way `FLOOR_UP_WALL` tiles. I must trust the tool's output.

## IV. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **FRUIT_TREE:** Gives a 'BERRY' item when interacted with. Seems to be a one-time collection per tree.

## V. Procedural Reminders & Methodologies

### Tile Testing Protocol
- **Immediate Testing:** Upon encountering a new, non-obvious tile type on the current map, I must immediately test its traversal properties if it is reachable.
- **Documentation:** All findings, positive or negative, must be immediately recorded in the 'Tile Traversal Rules' section.
- **Prioritization:** This testing protocol is a high priority, to be completed before continuing with other exploration goals unless physically impossible (e.g., requires an HM I don't possess).

### Personal Rules & Reminders
- **Check Map Markers!** Before interacting with an NPC or navigating to a specific spot, always check existing map markers to avoid wasting time on defeated trainers or repeating actions.