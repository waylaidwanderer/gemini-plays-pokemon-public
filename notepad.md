# Gem's Pokémon Crystal Notepad

## I. Game Mechanics

### Tile Traversal Rules
- **Testing Protocol:**
  1. When a new tile type is seen on screen and is reachable, I MUST immediately test it. This is my highest priority.
  2. Test movement *into* the tile from all 4 adjacent, traversable cardinal directions.
  3. If movement is possible, test movement *out of* the tile to all 4 adjacent, traversable cardinal directions to check for one-way paths.
  4. Record all verified findings for both passable and impassable tiles immediately.
- **IMMEDIATE Priority Test List:** WALL, HEADBUTT_TREE, IlexForestShrineScript. Failure to test these immediately is a process violation.
- **Verified Impassable:** PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), VOID, MART_SHELF, BLACK_BELT (NPC)
- **Verified Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Verified Warps:**
  - **Standard:** DOOR, CAVE
  - **Movement-Based:** LADDER (Move onto tile).
  - **Directional:** WARP_CARPET_RIGHT/LEFT/DOWN (Move onto tile in specified direction). Exception: Ilex Forest Azalea Gate and other similar gatehouse warps are triggered by walking into the correct side of the building, not by directional presses on the carpet.
- **Verified One-Way Ledges:** LEDGE_HOP_DOWN/LEFT/RIGHT.
- **Verified Complex Tiles:** FLOOR_UP_WALL (Enter by moving UP; Exit by moving LEFT/RIGHT).

## II. Quests & Puzzles

### Ilex Forest Puzzle
- **Objective:** Get HM01 (CUT) by herding the Farfetch'd to the apprentice at (7, 28).
- **Verified Mechanics:**
    1. **Turning:** Approaching Farfetch'd from a cardinal direction causes it to turn and face the player.
    2. **Teleportation:** Interacting with Farfetch'd directly (pressing 'A') or stepping on a specific twig can cause it to teleport. The trigger seems to depend on its position and facing direction relative to the specific twig used.
    3. **Reset Conditions:** Wild battles, leaving the area, or sometimes direct interaction resets the puzzle to its initial state (Farfetch'd at (29, 22)).
- **Alternative Hypotheses to Test:**
  1. The Ilex Forest Shrine at (8, 22) is involved in the puzzle.
  2. There is a hidden item or another NPC I haven't found yet that is required.

### Ruins of Alph Puzzle
- **Objective:** Solve the sliding stone panel puzzle.
- **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue for the puzzle.

## III. Item Effects & Battle Mechanics
- **EVERSTONE:** Prevents evolution.
- **BERRY:** Restores 10 HP. Found at FRUIT_TREEs.
- **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
- **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
- **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.

## Misc. Tips & Info
- Liz mentioned a Pokémon Salon in Goldenrod run by two brothers.