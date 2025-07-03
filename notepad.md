# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, LADDER, CAVE
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must walk in the indicated direction to activate, 'A' button does not work).
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Hypotheses
- **BUOY:** Likely impassable, similar to WATER. Needs testing.
- **FLOOR_ALLOW_HOP_RIGHT:** Likely a one-way ledge to the right. Needs testing.
- **FLOOR_ALLOW_HOP_DOWN_LEFT:** Likely a one-way ledge down and/or left. Needs testing.
- **FLOOR_ALLOW_HOP_DOWN_RIGHT:** Likely a one-way ledge down and/or right. Needs testing.

## II. Quest Progression & Blockers

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

### Azalea Town Slowpoke Well Puzzle
- **Status:** I am currently stuck on this puzzle. All hypotheses have failed.
- **New Plan:** I am abandoning this quest for now. My new primary objective is to travel to New Bark Town to show Professor Elm the hatched Togepi, as he requested in a phone call. Progressing this quest may unlock the events in Azalea Town.
- **Failed Attempts Log (Consolidated):
  1. Talking to Kurt does not make him move.
  2. Talking to the Rocket Grunt at the well does not make him move.
  3. Talking to Kurt's apprentice does not trigger anything.
  4. Interacting with the Farfetch'd statue at (5, 6) in Kurt's house does nothing.
  5. The path to the well at (31, 7) is physically blocked by the grunt at (31, 9); there is no way around him.
  6. Talking to the Rocket Grunt at the well (31, 9) and then immediately talking to Kurt (2, 3) does not make him move.
  7. Talking to Kurt (2, 3) and then his apprentice (6, 2) does not trigger anything.
  8. Talking to the Rocket Grunt at the gym (10, 16) to learn about SLOWPOKETAILs and then talking to Kurt does not make him move.

## III. Strategic Plans & Hypotheses

- **Current Plan:** Travel from Azalea Town to New Bark Town to meet Professor Elm. This is currently blocked by my inability to navigate Route 32.

## IV. Tool Development Log
- **`path_master` & `path_master_v2` (abandoned):** Multiple attempts to fix my BFS-based pathfinders for Route 32 have failed. My strategy of making small patches was flawed.
- **New Strategy:** I will develop a new, robust pathfinding tool (`path_master_v3`) from scratch. The journey to New Bark Town is on hold until this tool is fully functional and verified. My secondary goal is now dedicated to this task.