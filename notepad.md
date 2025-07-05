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
- **Untested Tiles:** LEDGE, FLOOR_ALLOW_HOP_DOWN.

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
## V. Future Tool & Agent Ideas
- **Maze Navigator Tool:** A tool that can analyze the `map_xml_string` to find the shortest path through a maze, accounting for unseen tiles and obstacles.
- **WKG Connection Checker:** A tool to check if a connection between two nodes already exists in the World Knowledge Graph to prevent duplicate entries.
- **H8 (Falsified):** After talking to the apprentice, the Farfetch'd would appear near him at (7, 28).
  - **Test 8.1:** Traveled to (8, 28).
  - **Result:** Farfetch'd was not present. **Conclusion: H8 Falsified.**
- **H9 (Current Hypothesis):** The Farfetch'd has fled to a new location after being scared from the east. The next logical location to search is the area north of the apprentice's position.