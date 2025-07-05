# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Mechanics Testing Protocol
*Goal: Build a comprehensive guide to the game's physics. This must be followed for every new tile type.*
1.  **New Tile Encountered:** When a new, undocumented tile type appears on the map, I must immediately begin testing.
2.  **Impassable Test:** Attempt to move onto the tile from all four cardinal directions (Up, Down, Left, Right).
3.  **One-Way Test:** If traversal is possible from one direction, I must immediately test all other directions to confirm if it is a one-way path. Every direction must be individually verified.
4.  **Record Results:** Document all findings in the 'Verified' section below. No assumption is valid until tested.

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, BED, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), HEADBUTT_TREE
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE
- **Movement-Based Warps:** LADDER (Activated by moving onto the tile).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
*Goal: Test these tiles as soon as they are encountered.*
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.
- **WARP_CARPET_DOWN:** Test this warp tile in Kurt's House.
- **WARP_CARPET_LEFT:** Test this warp tile in the Ilex Forest Gatehouse.
- **WARP_CARPET_RIGHT:** Test this warp tile in the Ilex Forest Gatehouse.

## II. Quest Progression & Puzzles

### Current Assumptions to Test
1.  The Headbutt tutor exists in Ilex Forest and can teach me the move.
2.  Learning Headbutt is related to solving the Farfetch'd puzzle.
3. The Farfetch'd puzzle state is persistent and does not reset upon leaving the map.

### Ilex Forest - Farfetch'd Puzzle
- **Objective:** Guide the lost FARFETCH'D to the apprentice at (7, 28) to get HM01 CUT.
- **Verified Mechanics:**
    - **Proximity (Turning):** Moving to a tile adjacent to the Farfetch'd causes it to turn and face the player.
    - **Proximity (Herding):** Approaching the Farfetch'd from the direction **OPPOSITE** to where it is currently facing will scare it, causing it to move one tile directly away from the player.
    - **Movement Mechanic (Twigs):** Stepping on a twig causes the Farfetch'd to turn towards the sound and then move to a new, seemingly predetermined location. 
    - **Direct Interaction:** Causes the Farfetch'd to squawk and then disappear from the map, failing the puzzle. This is a confirmed fail state.
- **Failed Hypotheses Log:**
    - Leaving and re-entering the forest does not reset the Farfetch'd's position.
    - The `HEADBUTT_TREE` tiles are not the twigs for the puzzle.
    - Stepping on/off a twig is not the trigger.

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
- **IMMEDIATE DATA MANAGEMENT:** Update Notepad, Markers, and WKG IMMEDIATELY after discovering new information.
- **AGENT & TOOL PHILOSOPHY:** Use agents for high-level reasoning and planning. Use tools for computation and repetitive actions. Refine or delete them immediately if they are flawed. Test agent output before discarding.
- **BATTLE STRATEGY REMINDER:** Always check a Pokémon's moveset before making a strategic switch in battle. My Onix had no Rock-type moves against Scyther.
- **AGENT DELETION PLAN:** Delete the `farfetchd_herder` agent after obtaining HM01 CUT, as it will be obsolete.