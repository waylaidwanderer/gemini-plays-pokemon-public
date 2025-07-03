# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, LADDER, CAVE
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must walk in the indicated direction to activate, 'A' button does not work).
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT
- **Complex One-Way Tiles:** FLOOR_UP_WALL (A one-way tile. Can only be entered by moving UP onto it. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Hypotheses
- **BUOY:** Likely impassable, similar to WATER. Needs testing.

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

- **Current Plan:** Travel from Azalea Town to New Bark Town to meet Professor Elm.

## IV. Tool Development Log
- **`path_master` & `path_master_v2` (abandoned):** Multiple attempts to fix my BFS-based pathfinders for Route 32 have failed. The logic for handling one-way tiles was insufficient. These tools are now considered deprecated. I am developing a new `path_master_v2` with completely revised logic.