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
- **Objective:** Guide the lost FARFETCH'D to the apprentice at (7, 28) to get HM01 CUT.
- **Current State:** I am trapped in a sealed-off section of the forest. The puzzle must be solved to proceed. The Farfetch'd is not currently on screen.
- **Verified Mechanics:**
    1. **Proximity (Turning):** Approaching the Farfetch'd from a specific side causes it to turn and face you.
    2. **Teleportation (Twigs):** Stepping on a twig causes the Farfetch'd to *teleport* to a new, seemingly fixed location. The destination is determined by a combination of the twig used and the bird's facing direction *before* the teleport.
    3. **Reset Conditions:** The puzzle resets if the player enters a wild battle or interacts directly with the Farfetch'd.

#### Systematic Test Log
*This log will track every hypothesis and its outcome to avoid repeating mistakes.*
- **Hypothesis 1:** The twig at (22, 30) triggers the puzzle.
  - **Test 1.1:** Stepped on the twig at (22, 30). **Result:** No effect. Farfetch'd did not appear.
  - **Conclusion:** Hypothesis 1 is falsified.
- **Hypothesis 2:** The twig at (29, 30) triggers the puzzle.
  - **Test 2.1:** Stepped on the twig at (29, 30). **Result:** No effect. Farfetch'd did not appear.
  - **Test 2.2:** Stood on the twig at (29, 30) and pressed 'A'. **Result:** No effect.
  - **Conclusion:** Hypothesis 2 is falsified.
- **Hypothesis 3:** The two twigs are linked sequentially.
  - **Test 3.1:** Stepped on the twig at (22, 30) after visiting (29, 30). **Result:** No effect. Farfetch'd did not appear.
  - **Conclusion:** Hypothesis 3 is falsified.

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

## V. Lessons Learned & Self-Correction Archive
- **External Knowledge:** I must stop making assumptions based on other Pokémon games. All mechanical knowledge must be built **exclusively** from verified, in-game observations within Pokémon Crystal.
- **Data Management as Priority:** Data management (WKG, Map Markers, Notepad) is the highest priority action, to be performed in the same turn a discovery is made, overriding any other planned action. Deferring these tasks leads to hallucinations and wasted turns.
- **Tool Reliability:** I must ensure my custom tools are flawless. When a tool fails, I must immediately redefine it with a more robust script.
- **Goal Flexibility:** I must be willing to abandon a failing strategy and explore alternatives when progress stalls, rather than becoming fixated on a single approach. The Farfetch'd puzzle is a key example; my long-distance pathing was a flawed strategy due to random encounters resetting the puzzle state.
- **Tile Documentation:** The 'unknown' tile type represents a placeholder for tiles that have not been fully implemented in the game's code, but are still present on the map. They are **traversable** and function as floor tiles.
- **Hypothesis 4:** The player's facing direction matters when interacting with the puzzle twigs. 
  - **Test 4.1:** Stand on the twig at (22, 30), turn to face UP, and press 'A'. **Result:** TBD.
- **Hypothesis 5:** The player must be adjacent to the twig and facing it to interact, rather than standing on it.
  - **Test 5.1:** Stand at (29, 29), turn to face DOWN towards the twig at (29, 30), and press 'A'. **Result:** TBD.

## V. Systematic Puzzle Testing

### Ilex Forest - Farfetch'd Puzzle

- **Objective:** Guide the lost FARFETCH'D to the apprentice at (7, 28) to get HM01 CUT.
- **Current State:** I am trapped in a sealed-off section of the forest. The Farfetch'd and apprentice are not currently on screen. This may be a bug or a state I need to reset.
- **Verified Mechanics:**
    1. **Proximity (Turning):** Approaching the Farfetch'd from a specific side causes it to turn and face you.
    2. **Teleportation (Twigs):** Stepping on a twig causes the Farfetch'd to teleport.
    3. **Reset Conditions:** The puzzle resets if the player enters a wild battle, leaves the area, or interacts directly with the Farfetch'd.

#### Hypothesis Test Log
- **Hypothesis 1:** Standing *on* the twig at (22, 30) triggers the puzzle.
  - **Conclusion:** Falsified. (Multiple tests, no effect).
- **Hypothesis 2:** Standing *on* the twig at (29, 30) triggers the puzzle.
  - **Conclusion:** Falsified. (Multiple tests, no effect).
- **Hypothesis 3:** The two twigs are linked sequentially.
  - **Conclusion:** Falsified. (No interaction between them).
- **Hypothesis 4:** Player's facing direction matters when standing *on* the puzzle twigs. 
  - **Conclusion:** Falsified. (Multiple tests with different facings yielded no effect and caused looping).
- **Hypothesis 5 (Current):** The player must be *adjacent* to the twig and facing it to interact.
  - **Test 5.1:** Stand at (29, 29), face DOWN towards (29, 30), and press 'A'.
  - **Result:** TBD.