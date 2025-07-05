# Gem's Pokémon Crystal Notepad

## I. Game Mechanics

### Tile Traversal Rules
- **Testing Protocol:**
  1.  When a new tile type is seen, test movement from all 4 directions.
  2.  If any direction works, test all others to confirm one-way paths.
  3.  Record all verified findings.
- **Verified Impassable:** WALL, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), VOID, MART_SHELF, BLACK_BELT (NPC)
- **Verified Interactable Obstacles:** HEADBUTT_TREE (Impassable, can be interacted with via 'A').
- **Verified Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Verified Warps:**
  - **Standard:** DOOR, CAVE
  - **Movement-Based:** LADDER (Move onto tile).
  - **Directional:** WARP_CARPET_RIGHT/LEFT/DOWN (Move onto tile in specified direction). Exception: Ilex Forest Azalea Gate and other similar gatehouse warps are triggered by walking into the correct side of the building, not by directional presses on the carpet.
- **Verified One-Way Ledges:** LEDGE_HOP_DOWN/LEFT/RIGHT.
- **Verified Complex Tiles:** FLOOR_UP_WALL (Enter by moving UP; Exit by moving LEFT/RIGHT).
- **Untested Tiles:** LEDGE, FLOOR_ALLOW_HOP_DOWN. LEDGE, FLOOR_ALLOW_HOP_DOWN. LEDGE, FLOOR_ALLOW_HOP_DOWN. LEDGE, FLOOR_ALLOW_HOP_DOWN.

## II. Quests & Puzzles

### Ilex Forest Puzzle
- **Objective:** Get HM01 (CUT).
- **Current Hypothesis (H5):** After speaking to Kurt, his apprentice will now be present in Ilex Forest. Finding him is the key.
- **Alternative Hypothesis (H6):** The Ilex Forest Shrine at (8, 22) may be involved. Test interaction with it after resolving the apprentice situation to confirm its role (or lack thereof).
- **Verified Mechanics:**
    1. **Proximity (Turning):** Approaching Farfetch'd causes it to turn.
    2. **Teleportation (Twigs):** Stepping on twigs teleports Farfetch'd based on its facing direction.
    3. **Reset Conditions:** Wild battles, leaving the area, or direct interaction resets the puzzle.

### Ruins of Alph Puzzle
- **Objective:** Solve the sliding stone panel puzzle.
- **Current Status:** The ladder at (10, 13) is the only path forward. The solution is likely in another chamber.
- **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue for the puzzle.

## III. Item Effects & Battle Mechanics
- **EVERSTONE:** Prevents evolution.
- **BERRY:** Restores 10 HP. Found at FRUIT_TREEs.
- **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
- **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
- **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.
- **Type Effectiveness:** Water is neutral vs. Bug/Grass (e.g., Paras). Initial assumption was wrong.

## IV. Systematic Puzzle Testing: Ilex Forest
*Goal: Find the trigger to make the Farfetch'd reappear and solve the puzzle.*
- **H1: Interacting with the tree at (23, 29) will make the Farfetch'd reappear.**
  - **Test 1.1:** Move to (23, 30), face UP, press 'A'.
  - **Result:** No effect. **Conclusion: H1 Falsified.**
- **H2: Stepping on the twigs at (22, 30) or (29, 30) will make the Farfetch'd reappear.**
  - **Test 2.1:** Step on the twig at (22, 30).
  - **Result:** No effect. **Conclusion: H2 Falsified.**
- **H3: Interacting with a twig from an adjacent tile will trigger the puzzle.**
  - **Test 3.1:** Stand at (22, 29), face DOWN towards (22, 30), and press 'A'.
  - **Result:** No effect. **Conclusion: H3 Falsified.**
- **H4 (Partially Validated): Spoke with Kurt in Azalea Town.**
  - **Result:** Kurt confirmed his apprentice is still missing in Ilex Forest. He said: "The SLOWPOKE have returned… But my APPRENTICE hasn't come back from ILEX FOREST. Where in the world is that lazy guy?" This confirms the next step is in the forest.
- **H5 (Current Hypothesis): The apprentice will now be present in Ilex Forest.**
  - **Test Plan:** Return to Ilex Forest and find the apprentice to progress the puzzle.
- **H7 (Current Hypothesis): The apprentice's dialogue loop will only break after the lost Farfetch'd is found and returned. The next step is to explore the maze to find it.

- **H8 (Falsified):** After talking to the apprentice, the Farfetch'd would appear near him at (7, 28).
  - **Test 8.1:** Traveled to (8, 28).
  - **Result:** Farfetch'd was not present. **Conclusion: H8 Falsified.**
- **H9 (Falsified):** The Farfetch'd has fled to a new location after being scared from the east. The next logical location to search is the area north of the apprentice's position.
  - **Test 9.1:** Traveled north from (8, 27) to (8, 26).
  - **Result:** Path is blocked by a CUT_TREE at (8, 25). **Conclusion: H9 Falsified.**
- **H10 (Partially Confirmed & Falsified):** The Farfetch'd was found in the western maze, but fled again upon approach.
- **H11 (Falsified):** The Farfetch'd fled to the area south of its last position. 
  - **Test 11.1:** Explored south from (8, 29).
  - **Result:** The path is a dead end at (8, 36).
  - **Conclusion: H11 Falsified.**
- **H12 (Falsified):** After being scared from the western maze, the Farfetch'd would return to its original puzzle location in the east.
  - **Test 12.1:** Traveled back to (22, 29).
  - **Result:** Farfetch'd was not present. **Conclusion: H12 Falsified.**
- **H13 (Falsified):** The agent's suggestion that the Farfetch'd fled north from its last western position was incorrect. The area is a dead end blocked by a CUT_TREE or walls.
- **H14 (Current Hypothesis):** Leaving and re-entering Ilex Forest will reset the entire Farfetch'd puzzle, causing it to reappear at its original location.
- **H15 (Falsified):** Systematically re-exploring every path from the apprentice's location yielded nothing.

- **H16 (Confirmed):** Spoke to the apprentice at (7, 28). He confirmed he lost the Farfetch'd used for cutting trees and is too scared to find it himself. This initiates the next phase of the puzzle.
- **H17 (Falsified):** Checked the original puzzle area at (22, 29) after speaking to the apprentice, but the Farfetch'd was not there.
- **H18 (Current Hypothesis):** Leaving and re-entering Ilex Forest will reset the entire Farfetch'd puzzle, causing it to reappear at its original location.
- **H18 (Falsified):** Leaving and re-entering Ilex Forest will reset the entire Farfetch'd puzzle, causing it to reappear at its original location.
  - **Test 18.1:** Left and re-entered the forest, then returned to (22, 28).
  - **Result:** Farfetch'd was not present. **Conclusion: H18 Falsified.**
- **H19 (Current Hypothesis):** The Farfetch'd has fled to a new, previously unexplored location within the forest after I spoke to the apprentice. The next step is to systematically search the western maze area, starting from the apprentice's position.