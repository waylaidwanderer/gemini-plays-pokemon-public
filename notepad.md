# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, BED, TWIN (NPC), GYM_GUIDE (NPC)
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

## III. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **BERRY:** Restores 10 HP. Obtained from FRUIT_TREEs.

## IV. Procedural Reminders
- **IMMEDIATE WKG UPDATES:** Update the World Knowledge Graph IMMEDIATELY after every map transition. No exceptions.
- **DOCUMENT ALL TILES:** Document and test every new tile type encountered.
- **TRUST THE AGENT:** Follow the agent's advice, especially after multiple failed manual attempts. Refine the agent if its advice is flawed.

## V. Self-Correction Log
- **CRITICAL FAILURE:** I spent over 20 turns stuck in Kurt's House because I failed to consult my own notepad regarding the `WARP_CARPET_DOWN` mechanic. I must be more diligent about using my own documented knowledge.

## VI. Gym Puzzle Mechanics

### Azalea Gym Puzzle
- **Objective:** Find the correct sequence to activate the two spider-switches to reach Bugsy.
- **Failed Attempts:**
  1. Activating right statue only. (Path blocked)
  2. Activating left statue only. (Path blocked)
  3. Activating right statue, then left statue. (Path blocked)
  4. Activating left statue, then right statue. (Path blocked)
  5. Talking to Gym Guide after switch interactions. (Dialogue unchanged)
  6. Talking to Bug Catcher Al after switch interactions. (Dialogue unchanged)
  7. Activating left statue, then talking to Gym Guide, then activating right statue. (Path blocked)