# Gem's Pokémon Crystal Notepad

## I. Game Mechanics

### Tile Traversal Rules
- **Testing Protocol:**
  1.  When a new tile type is seen, test movement from all 4 directions.
  2.  If any direction works, test all others to confirm one-way paths.
  3.  Record all verified findings.
- **Verified Impassable:** PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), VOID, MART_SHELF, BLACK_BELT (NPC)
- **Untested Impassable (To Be Verified):** WALL, CUT_TREE, WATER, HEADBUTT_TREE
- **Verified Interactable Obstacles:** HEADBUTT_TREE (Impassable, can be interacted with via 'A').
- **Verified Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Verified Warps:**
  - **Standard:** DOOR, CAVE
  - **Movement-Based:** LADDER (Move onto tile).
  - **Directional:** WARP_CARPET_RIGHT/LEFT/DOWN (Move onto tile in specified direction). Exception: Ilex Forest Azalea Gate and other similar gatehouse warps are triggered by walking into the correct side of the building, not by directional presses on the carpet.
- **Verified One-Way Ledges:** LEDGE_HOP_DOWN/LEFT/RIGHT.
- **Verified Complex Tiles:** FLOOR_UP_WALL (Enter by moving UP; Exit by moving LEFT/RIGHT).

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

## IV. Ilex Forest Puzzle Log
*Goal: Find the lost Farfetch'd to get HM01 (CUT).*
- **Current Status:** Spoke to Kurt's apprentice at (7, 28). He confirmed he lost the Farfetch'd and is too scared to retrieve it. This has initiated the puzzle.
- **Current Hypothesis (H19):** The Farfetch'd has fled to a new, previously unexplored location within the forest. The next step is to systematically search the western maze area, starting from the apprentice's position at (7, 28).
- **Falsified Hypotheses Summary:**
  - H1-H3: Pre-puzzle interaction attempts with twigs/trees were ineffective.
  - H8-H15: Early attempts to locate the Farfetch'd after scaring it from the east were unsuccessful.
  - H17: The Farfetch'd did not return to its original puzzle area after speaking to the apprentice.
  - H18: Leaving and re-entering the forest did not reset the puzzle.

## V. Untested Assumptions & Alternative Hypotheses

- **HEADBUTT_TREE Interaction:** Confirmed that pressing 'A' on a HEADBUTT_TREE does nothing. This interaction method is invalid.
- **Farfetch'd Location Alternatives:**
  1. The Farfetch'd is in a hidden area of the forest, accessible through a path I haven't found yet.
  2. The Ilex Forest Shrine at (8, 22) is involved in the puzzle, and I need to interact with it again.