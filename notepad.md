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
- **Objective:** Reach and defeat Gym Leader Bugsy.
- **Current State:** The path is blocked by spider-like platforms controlled by two switches. All simple switch combinations and toggling sequences have failed.
- **Agent Hypothesis (Top Priority):** The platforms are transports/vehicles, not static bridge parts. My initial attempt to test this by standing on the track failed.
- **Current Plan:** Reset the puzzle to its initial state (both switches OFF). Then, systematically test the transport hypothesis by activating one switch and observing the platform's movement.
- **Failed Attempts Log:**
  - H1: All simple switch combinations (L:ON/R:OFF, L:OFF/R:ON, L:ON/R:ON).
  - H2: Sequence L:ON -> R:ON -> L:OFF.
  - H3: Sequence L:ON -> R:ON -> R:OFF.
  - H4: Stood on platform track at (4, 12) after activating left switch; no movement.

## III. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **BERRY:** Restores 10 HP. Obtained from FRUIT_TREEs.

## IV. Procedural Reminders
- **IMMEDIATE DATA MANAGEMENT:** Update Notepad, Markers, and WKG IMMEDIATELY after discovering new information. No exceptions.
- **TRUST THE AGENTS:** Use agents proactively for complex problems. Trust their outputs, especially when stuck. Refine them if they are flawed.