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
- **Critical Insight:** My pathfinding tool has confirmed I am completely blocked by the trainers at (4, 10) and (5, 10). This means the switches **must** move the platforms to create a path. New insight: The 'switches' on the walls are not interactable objects. The actual switches are the statues at (3, 13) and (6, 13).
- **Agent's Top Hypothesis (H5):** The switches must be used sequentially to alter the maze layout. Activate the Left Switch, then navigate a newly available path to reach the Right Switch. Activating the Right Switch from this new position may complete the path forward.
- **Current Plan:** Test H5. First, reset the puzzle by turning both switches OFF. Then, activate the Left Switch and attempt to find a new path to the Right Switch.
- **Failed Attempts Log:**
  - H1: Simple switch combinations (L:ON/R:OFF, L:OFF/R:ON, L:ON/R:ON) do not create a static bridge.
  - H2: Toggle sequences (L:ON->R:ON->L:OFF, L:ON->R:ON->R:OFF) do not create a static bridge.
  - H3: Attempting to 'ride' the platforms by standing on the tracks failed.
  - H4: Attempting to interact with the platforms directly failed.

## III. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **BERRY:** Restores 10 HP. Obtained from FRUIT_TREEs.

## IV. Procedural Reminders
- **IMMEDIATE DATA MANAGEMENT:** Update Notepad, Markers, and WKG IMMEDIATELY after discovering new information. No exceptions.
- **TRUST THE AGENTS:** Use agents proactively for complex problems. Trust their outputs, especially when stuck. Refine them if they are flawed.