# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, BED
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE, LADDER (Acts as a two-way vertical warp)
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must walk in the indicated direction to activate).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.

## II. Quest Progression & Puzzles

### Blocked Path: Slowpoke Well
- **Objective:** Gain access to the Slowpoke Well.
- **Clues:** Team Rocket is selling SLOWPOKETAILS. Kurt makes custom Poké Balls. Kurt has gone to the well to confront Team Rocket.
- **Hypothesis #1 (Failed):** Approaching the grunt at (31, 9) will trigger an event with Kurt. (Result: No event triggered).
- **Hypothesis #2 (Failed):** Speaking to Kurt's apprentice after Kurt leaves will provide new info. (Result: Repeated dialogue).
- **Hypothesis #3 (Failed):** Speaking to Gramps after Kurt leaves will provide new info. (Result: Repeated dialogue).
- **Hypothesis #4 (Success):** Speaking to Kurt inside his house triggers the event where he confronts the grunt. (Result: Kurt left for the well).
- **Hypothesis #5 (Failed):** Speaking to the grunt at (31, 9) after Kurt leaves will make him move. (Result: Grunt gives dialogue but does not move).
- **Current Hypothesis:** The grunt at (31, 9) is a simple obstacle. I must navigate around him to enter the well at (31, 7).

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

### Slowpoke Well - Update
- **New Clue from Kurt:** After returning to his house, Kurt mentioned that all the SLOWPOKE have disappeared and that the 'forest's protector' may be angry. This suggests the solution is in Ilex Forest.