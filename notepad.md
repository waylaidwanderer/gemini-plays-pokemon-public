# Gem's Pokémon Crystal Notepad

## I. Game Mechanics

### Tile Traversal Rules
- **Testing Protocol:**
  1.  When a new tile type is seen, test movement from all 4 directions.
  2.  If any direction works, test all others to confirm one-way paths.
  3.  Record all verified findings.
- **Verified Impassable:** WALL, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), VOID, MART_SHELF
- **Verified Interactable Obstacles:** HEADBUTT_TREE (Impassable, can be interacted with via 'A').
- **Verified Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Verified Warps:**
  - **Standard:** DOOR, CAVE
  - **Movement-Based:** LADDER (Move onto tile).
  - **Directional:** WARP_CARPET_RIGHT/LEFT/DOWN (Move onto tile in specified direction). Exception: Ilex Forest Azalea Gate warp is triggered by walking into the correct side of the building.
- **Verified One-Way Ledges:** LEDGE_HOP_DOWN/LEFT/RIGHT.
- **Verified Complex Tiles:** FLOOR_UP_WALL (Enter by moving UP; Exit by moving LEFT/RIGHT).
- **Untested Tiles:** LEDGE, FLOOR_ALLOW_HOP_DOWN.

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
## III. Item Effects
- **EVERSTONE:** Prevents evolution.
- **BERRY:** Restores 10 HP. Found at FRUIT_TREEs.
- **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
- **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
- **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.

## IV. Battle Mechanics
- **Type Effectiveness:** Water is neutral vs. Bug/Grass (e.g., Paras). Initial assumption was wrong.