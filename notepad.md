# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Mechanics Testing Protocol
*Goal: Build a comprehensive guide to the game's physics. This must be followed for every new tile type.*
1.  **New Tile Encountered:** When a new, undocumented tile type appears on the map, I must immediately begin testing.
2.  **Impassable Test:** Attempt to move onto the tile from all four cardinal directions (Up, Down, Left, Right).
3.  **One-Way Test:** If traversal is possible from one direction, I must immediately test all other directions to confirm if it is a one-way path. Every direction must be individually verified.
4.  **Record Results:** Document all findings in the 'Verified' section below. No assumption is valid until tested.

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, BED, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), VOID
- **Interactable Obstacles:** HEADBUTT_TREE (Impassable to walk on, but can be interacted with using 'A').
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE
- **Movement-Based Warps:** LADDER (Activated by moving onto the tile).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
*Goal: Test these tiles as soon as they are encountered.*
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.
- **WARP_CARPET_DOWN:** Found in Kurt's House. Test by walking on, pressing A, and pressing Down.
- **WARP_CARPET_LEFT:** Found in Ilex Forest Gatehouse. Test by walking on, pressing A, and pressing Left.
- **WARP_CARPET_RIGHT:** Found in Ilex Forest Gatehouse. Test by walking on, pressing A, and pressing Right.

## II. Quest Progression & Puzzles

### Ilex Forest - Farfetch'd Puzzle
- **Objective:** Guide the lost FARFETCH'D to the apprentice at (7, 28) to get HM01 CUT.
- **Verified Mechanics:**
    - **Proximity (Turning):** Moving near the Farfetch'd can cause it to turn.
    - **Movement Mechanic (Twigs):** Stepping on a twig causes the Farfetch'd to disappear and reappear at a new, predetermined location. This resets the immediate puzzle state.
    - **Direct Interaction (Fail State):** Pressing 'A' on the Farfetch'd causes it to squawk and then disappear from the map, failing the puzzle.
- **Current Hypotheses & Tests:**
    - **Hypothesis 1 (Primary):** The Farfetch'd must be herded to the apprentice's last known location at (7, 28).
    - **Hypothesis 2 (Alternative):** The Farfetch'd needs to be herded to a different, unknown location.
        - **Test:** Once found, attempt to herd it North, South, and East to observe its behavior.
    - **Hypothesis 3 (Alternative):** Specific twigs have unique effects, rather than all twigs simply resetting the puzzle.
        - **Test:** Find the Farfetch'd, note its location, step on a specific twig, and document where it reappears. Repeat for all accessible twigs to map out their effects.
- **Failed Hypotheses Log:**
    - Leaving and re-entering the forest does not reset the Farfetch'd's position.
    - The puzzle cannot be solved by exploring outside the immediate maze; all paths are dead ends.
    

### Ruins of Alph Puzzle
- **Objective:** Solve the sliding stone panel puzzle.
- **Current Status:** The ladder at (10, 13) is the only path forward. The solution is likely in another chamber.
- **Clue:** Liz mentioned hearing a strange broadcast from the Ruins of Alph. This might be a clue for the puzzle.

## III. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **BERRY:** Restores 10 HP. Obtained from FRUIT_TREEs.
- **TM49 (Fury Cutter):** A move that gets stronger with each consecutive hit.
- **SLOWPOKETAIL:** A man on Route 32 offered to sell this. Its purpose is unknown.
- **MOOMOO MILK:** Restores 100 HP. Can be purchased at MOOMOO FARM.

## IV. Procedural Reminders
- **IMMEDIATE DATA MANAGEMENT:** Update Notepad, Markers, and WKG IMMEDIATELY after discovering new information. This is a higher priority than any in-game action.
- **AGENT & TOOL PHILOSOPHY:** Use agents for high-level reasoning. Use tools for computation. Refine or delete them immediately if they are flawed. Trust agent output until it is proven wrong through testing.

## V. Reflections & Corrections
- **Hallucination Correction:** I incorrectly believed the apprentice at (7, 28) disappeared. This is a recurring hallucination. I must trust the game state information and not my assumptions. The apprentice's presence is not a puzzle trigger.