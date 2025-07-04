# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW, SUPER_NERD (NPC), FISHER (NPC), LASS (NPC), TEACHER (NPC), YOUNGSTER (NPC), OFFICER (NPC), STATUE, TABLE, CHAIR, BED, TWIN (NPC), GYM_GUIDE (NPC), BUG_CATCHER (NPC)
- **Traversable:** FLOOR, GRASS, TALL_GRASS (Wild Encounters)
- **Standard Warps:** DOOR, CAVE
- **Movement-Based Warps:** LADDER (Activated by moving onto the tile, not by interaction).
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must press the indicated direction *while standing on the tile* to activate).
- **One-Way Ledges:** LEDGE_HOP_DOWN, LEDGE_HOP_LEFT, LEDGE_HOP_RIGHT (One-way traversal in the specified direction).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered by moving UP. Once on it, you can only exit by moving LEFT or RIGHT. You cannot move UP or DOWN off of it).

### Untested Tile Mechanics
- **LEDGE:** Test if this is impassable from all directions.
- **FLOOR_ALLOW_HOP_DOWN:** Test if this tile only allows downward movement.
- **HEADBUTT_TREE:** Test if this tile is interactable or just an impassable tree. Must test this soon.

## II. Quest Progression & Puzzles

### Ilex Forest Quest
- **Objective:** Find the lost FARFETCH'D and return it to the Charcoal Man's apprentice.
- **Agent Hypotheses (from `quest_strategist`):** My `farfetchd_herder` tool has failed, indicating a flawed understanding of the puzzle. I must test these new hypotheses provided by my agent:
  1.  **Facing-Based Movement:** The Farfetch'd's movement is determined by the direction the player is facing. Test by approaching from different angles and turning while adjacent to it.
  2.  **Sound-Based Movement:** The puzzle may be similar to the twig puzzle, requiring me to interact with the environment (e.g., trees) to create sounds that guide the Farfetch'd.
  3.  **Missing HM:** I may still need to find the Charcoal Man and get HM01 (CUT) to clear a path.
  4.  **Shrine Interaction:** The Ilex Forest Shrine at (8, 22) could be a trigger for the puzzle.

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