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
- **Directional Warps:** WARP_CARPET_RIGHT (Activated by moving onto the tile in the specified direction).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
*Goal: Test these tiles as soon as they are encountered.*
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.
- **WARP_CARPET_DOWN:** Found in Kurt's House. Test by walking on, pressing A, and pressing Down.
- **WARP_CARPET_LEFT:** Found in Ilex Forest Gatehouse. Test by walking on, pressing A, and pressing Left.

## II. Quest Progression & Puzzles

### Ilex Forest - Farfetch'd Puzzle
- **Objective:** Guide the lost FARFETCH'D to the apprentice at (7, 28) to get HM01 CUT.
- **Verified Mechanics:**
    1. **Proximity (Turning):** Moving near the Farfetch'd can cause it to turn and face you.
    2. **Movement (Twigs):** Stepping on a twig causes the Farfetch'd to move to a new, predetermined location.
    3. **Direct Interaction (Disappears):** Pressing 'A' on the Farfetch'd causes it to disappear. It does not immediately reappear.
- **Failed Hypotheses & Observations:**
    1. **Hypothesis:** Talking to the apprentice at (7, 28) will reset the puzzle. **Result:** FAILED. The apprentice gives the same dialogue and the Farfetch'd does not reappear.
- **Current Hypotheses (To be tested in order):**
    1. The puzzle resets by leaving and re-entering the Ilex Forest map. **Test:** Exit to the Ilex Forest Gatehouse and return, then check the Farfetch'd's starting position at (22, 29).
    2. The Farfetch'd must be herded to the apprentice at (7, 28) using the twigs to guide its movement from a distance.
    3. The puzzle requires trapping the Farfetch'd in a corner near the apprentice, rather than direct delivery.
    4. The twigs must be stepped on in a specific sequence, regardless of player or Farfetch'd position.

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