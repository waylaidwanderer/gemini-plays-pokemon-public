# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, BED, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC)
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE, LADDER (Acts as a two-way vertical warp)
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must press the indicated direction *while standing on the tile* to activate).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.

## II. Quest Progression & Puzzles

### Blocked Path: Ilex Forest West
- **Objective:** Clear the CUT tree at (8, 25) to access the western part of the forest.
- **Prerequisite:** Obtain HM01 (CUT).

### Ruins of Alph Puzzle
- **Objective:** Solve the sliding stone panel puzzle.
- **Current Hypothesis:** The solution is not in the first chamber. The ladder at (10, 13) is the only other path forward.

### Azalea Gym Puzzle
- **Objective:** Find the correct sequence to activate the two spider-switches to reach Bugsy.
- **Failed Attempts (Systematic Log):**
  1.  **Right Statue ON, Left Statue OFF:** Path to Bugsy blocked.
  2.  **Left Statue ON, Right Statue OFF:** Path to Bugsy blocked.
  3.  **Right Statue ON, Left Statue ON:** Path to Bugsy blocked.
  4.  **Left Statue ON, Right Statue ON:** Path to Bugsy blocked.
  5.  **Talked to Gym Guide** after various switch interactions: Dialogue unchanged.
  6.  **Talked to Bug Catcher Al** after various switch interactions: Dialogue unchanged.
  7.  **Sequence: Left Statue ON -> Talk to Gym Guide -> Right Statue ON:** Path to Bugsy blocked.
- **Current Status:** All simple combinations and NPC interactions have failed. Trusting agent advice to re-evaluate clues.

## III. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **BERRY:** Restores 10 HP. Obtained from FRUIT_TREEs.

## IV. Procedural Reminders
- **IMMEDIATE DATA MANAGEMENT:** Update Notepad, Markers, and WKG IMMEDIATELY after discovering new information. No exceptions.
- **TRUST THE AGENTS:** Use agents proactively for complex problems. Trust their outputs, especially when stuck. Refine them if they are flawed.