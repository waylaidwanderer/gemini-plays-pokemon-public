# Gem's Pokémon Crystal Notepad

## I. Game Mechanics

### Tile Traversal Rules
- **Testing Protocol:**
  1.  When a new tile type is seen on screen and is reachable, I MUST immediately test it.
  2.  Test movement *into* the tile from all 4 adjacent, traversable cardinal directions.
  3.  If movement is possible, test movement *out of* the tile to all 4 adjacent, traversable cardinal directions to check for one-way paths.
  4.  Record all verified findings for both passable and impassable tiles immediately.
- **Verified Impassable:** PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), VOID, MART_SHELF, BLACK_BELT (NPC)
- **Untested (To Be Verified Immediately):** WALL, CUT_TREE, WATER, HEADBUTT_TREE, IlexForestShrineScript
- **Verified Interactable Obstacles:** HEADBUTT_TREE (Impassable, can be interacted with via 'A', but no effect observed).
- **Verified Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Verified Warps:**
  - **Standard:** DOOR, CAVE
  - **Movement-Based:** LADDER (Move onto tile).
  - **Directional:** WARP_CARPET_RIGHT/LEFT/DOWN (Move onto tile in specified direction). Exception: Ilex Forest Azalea Gate and other similar gatehouse warps are triggered by walking into the correct side of the building, not by directional presses on the carpet.
- **Verified One-Way Ledges:** LEDGE_HOP_DOWN/LEFT/RIGHT.
- **Verified Complex Tiles:** FLOOR_UP_WALL (Enter by moving UP; Exit by moving LEFT/RIGHT).

## II. Quests & Puzzles

### Ilex Forest Puzzle
- **Objective:** Get HM01 (CUT) by catching the Farfetch'd.
- **Current Hypothesis (H21):** The Farfetch'd teleported to the western part of the maze. I need to find it there.
- **Verified Mechanics:**
    1. **Proximity (Turning):** Approaching Farfetch'd causes it to turn.
    2. **Teleportation (Twigs):** Stepping on twigs *sometimes* teleports Farfetch'd. The trigger seems to depend on its position and facing direction relative to the specific twig used. Direct interaction also causes it to move.
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

## IV. Untested Assumptions & Alternative Hypotheses

- **Farfetch'd Puzzle Alternatives:**
  1. The Farfetch'd has teleported to a different, unexplored area of the forest.
  2. The puzzle has reset, and the Farfetch'd is back at its starting position in the eastern part of the maze.
  3. There is another way to interact with the Farfetch'd besides stepping on twigs (e.g., approaching from a specific angle).
  4. The Ilex Forest Shrine at (8, 22) is involved in the puzzle, and I need to interact with it again.

## Misc. Tips & Info
- Liz mentioned a Pokémon Salon in Goldenrod run by two brothers. One is good, one isn't, but the younger one is sometimes better.