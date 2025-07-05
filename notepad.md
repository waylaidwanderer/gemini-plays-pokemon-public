# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Mechanics Testing Protocol
*Goal: Build a comprehensive guide to the game's physics. This must be followed for every new tile type.*
1.  **New Tile Encountered:** When a new, undocumented tile type appears on the map, I must immediately begin testing.
2.  **Impassable Test:** Attempt to move onto the tile from all four cardinal directions (Up, Down, Left, Right).
3.  **One-Way Test:** If traversal is possible from one direction, I must immediately test all other directions to confirm if it is a one-way path. Every direction must be individually verified.
4.  **Record Results:** Document all findings in the 'Verified' section below. No assumption is valid until tested.

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), YOUNGSTER (NPC), VOID
- **Interactable Obstacles:** HEADBUTT_TREE (Impassable to walk on, but can be interacted with using 'A').
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE
- **Movement-Based Warps:** LADDER (Activated by moving onto the tile).
- **Directional Warps (Conditionally Blocked):** WARP_CARPET_RIGHT, WARP_CARPET_LEFT, WARP_CARPET_DOWN. My hypothesis that these are activated by directional movement or pressing 'A' has been falsified at the Ilex Forest exit (3, 42). This exit appears to be blocked until a specific condition is met, likely solving the Farfetch'd puzzle.
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
*Goal: Test these tiles as soon as they are encountered.*
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.

## II. Quest Progression & Puzzles

### Ilex Forest - Farfetch'd Puzzle
*Note: This section is outdated. See the consolidated log under 'V. Systematic Puzzle Testing'.*

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

## IV. Battle Mechanics & Type Effectiveness
- **Water vs. Bug/Grass:** Verified that Water-type moves are neutral against Bug/Grass types (e.g., Paras). My initial assumption that it was 'not very effective' was based on external knowledge and was incorrect.

## V. Systematic Puzzle Testing

### Ilex Forest - Farfetch'd Puzzle
- **Objective:** Guide the lost FARFETCH'D to the apprentice at (7, 28) to get HM01 CUT.
- **Current State:** The Farfetch'd has disappeared. The puzzle state may need to be reset or re-initiated.
- **Verified Mechanics:**
    1. **Proximity (Turning):** Approaching the Farfetch'd from a specific side causes it to turn and face you.
    2. **Teleportation (Twigs):** Stepping on a twig causes the Farfetch'd to teleport.
    3. **Reset Conditions:** The puzzle resets if the player enters a wild battle, leaves the area, or interacts directly with the Farfetch'd.

#### Hypothesis Test Log
*Goal: Find the trigger to make the Farfetch'd reappear and solve the puzzle.*
- **H1: Interacting with the tree at (23, 29) will make the Farfetch'd reappear.**
  - **Test 1.1:** Move to (23, 30), face UP, press 'A'.
  - **Result:** No effect. **Conclusion: H1 Falsified.**
- **H2: Stepping on the twigs at (22, 30) or (29, 30) will make the Farfetch'd reappear.**
  - **Test 2.1:** Step on the twig at (22, 30).
  - **Result:** No effect. **Conclusion: H2 Falsified.**
- **H3: Interacting with a twig from an adjacent tile will trigger the puzzle.**
  - **Test 3.1:** Move to (21, 30) to interact with twig at (22, 30) from the left.
  - **Result:** Path blocked by WALL. Test invalid.
  - **Test 3.2 (Current):** Stand at (22, 29), face DOWN towards (22, 30), and press 'A'.
  - **Result:** No effect. **Conclusion: H3 Falsified.**
- **H4 (Alternative): The puzzle trigger is outside this immediate area.**
  - **Test Plan:** If all local hypotheses are exhausted, systematically backtrack and re-interact with key NPCs and objects (e.g., the apprentice, Kurt).