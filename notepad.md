# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC)
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE, LADDER (Acts as a two-way vertical warp)
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must walk in the indicated direction to activate, 'A' button does not work).
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Hypotheses
- **BUOY:** Likely impassable, similar to WATER. Needs testing.
- **FLOOR_ALLOW_HOP_RIGHT:** Likely a one-way ledge to the right. Needs testing.
- **FLOOR_ALLOW_HOP_DOWN_LEFT:** Likely a one-way ledge down and/or left. Needs testing.
- **FLOOR_ALLOW_HOP_DOWN_RIGHT:** Likely a one-way ledge down and/or right. Needs testing.

## II. Quest Progression & Puzzles

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

### Azalea Town Slowpoke Well Puzzle
- **Status:** I am currently stuck on this puzzle. All hypotheses have failed.
- **Current Plan:** The Slowpoke Well puzzle is on hold. The immediate objective is to backtrack through the southern part of the region to access the northern part of Route 32, which is required to continue towards Azalea Town.
- **Failed Attempts Log (Consolidated):
  2. Talking to the Rocket Grunt at the well does not make him move.
  3. Talking to Kurt's apprentice does not trigger anything.
  4. Interacting with the Farfetch'd statue at (5, 6) in Kurt's house does nothing.
  5. The path to the well at (31, 7) is physically blocked by the grunt at (31, 9); there is no way around him.
  8. Talking to the Rocket Grunt at the gym (10, 16) to learn about SLOWPOKETAILs and then talking to Kurt does not make him move.

### Route 30 Blocked Path
- **Status:** Solved.
- **Solution:** Leaving the area and re-entering caused the blocking NPC (Youngster Mikey) to move.
- **Failed Attempts Log:
  1. Talking to Youngster Mikey at (5, 23) does not make him move.
  2. Talking to Youngster Joey at (2, 28) does not make Youngster Mikey move.

## III. Tool Development Log
- **`path_master_v3` (Fixed again):** The tool's one-way tile logic was still flawed and failed to prevent moving sideways onto a vertical `LEDGE`. I have rewritten the logic to be more explicit about which directions are allowed for each specific hop tile type. This should be more robust.
- **HEADBUTT_TREE:** Quest Strategist suggests these require the move 'Headbutt' to interact with, not the standard 'A' button.

## IV. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **FRUIT_TREE:** Gives a 'BERRY' item when interacted with. Seems to be a one-time collection per tree.