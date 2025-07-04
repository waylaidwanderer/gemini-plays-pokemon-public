# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, BED, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC), HEADBUTT_TREE
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE
- **Movement-Based Warps:** LADDER (Activated by moving onto the tile, not by interaction).
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must press the indicated direction *while standing on the tile* to activate).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.

## II. Quest Progression & Puzzles

### Ilex Forest Quest
- **Objective:** Guide the lost FARFETCH'D back to the Charcoal Man's apprentice at (7, 28).
- **Status:** The puzzle seems to be a fixed sequence of interactions from specific tiles.
- **Known Sequence Steps:**
  1. Interact from (15, 26) [below] -> Teleports to (20, 24).
  2. Interact from (15, 24) [above] -> Teleports to (15, 29).
  3. Interact from (16, 29) [right] -> Teleports to (15, 25).
- **Failed Attempts:**
  - Interacting from (21, 24) [right] caused it to vanish.

### Ruins of Alph Puzzle
- **Objective:** Solve the sliding stone panel puzzle.
- **Current Hypothesis:** The solution is not in the first chamber. The ladder at (10, 13) is the only other path forward.

### Azalea Gym Puzzle (SOLVED)
- **Solution:** Defeating all trainers in the gym reconfigures the platforms, opening a path to the leader.

## III. Item Effects
- **EVERSTONE:** A Pokémon holding this item will not evolve.
- **BERRY:** Restores 10 HP. Obtained from FRUIT_TREEs.
- **TM49 (Fury Cutter):** A move that gets stronger with each consecutive hit.
- **SLOWPOKETAIL:** A man on Route 32 offered to sell this. Its purpose is unknown.

## IV. Procedural Reminders
- **IMMEDIATE DATA MANAGEMENT:** Update Notepad, Markers, and WKG IMMEDIATELY after discovering new information. No exceptions.
- **TRUST THE AGENTS:** Use agents proactively for complex problems. Trust their outputs, especially when stuck. Refine them if they are flawed.
- **BATTLE STRATEGY REMINDER:** Always check a Pokémon's moveset before making a strategic switch in battle. My Onix had no Rock-type moves against Scyther.
- **Current State (Farfetch'd Puzzle):** The bird is at (20, 24). I need to find the correct interaction to move it west towards the apprentice at (7, 28).