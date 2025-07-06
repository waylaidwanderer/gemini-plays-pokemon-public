# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Tile Rules

### Tile Traversal Rules
- **Testing Protocol:** When a new, reachable tile type is seen, I MUST test it immediately. Test movement *into* and *out of* the tile from all 4 cardinal directions to verify passability and check for one-way paths. For ledges, I must attempt to move up against them to confirm they are one-way.
- **IMMEDIATE Priority Test List:** The tile at (8, 22) where the IlexForestShrineScript object is located.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `COUNTER`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `VOID`, `MART_SHELF`, `BIRD` (Farfetch'd), `CUT_TREE`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `WARP_CARPET_RIGHT/LEFT/DOWN` (Move in specified direction). Exception: Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Enter by moving UP; Exit by moving LEFT/RIGHT).

## II. Quests & Puzzles

### Ilex Forest - Farfetch'd Puzzle
*   **Objective:** Get HM01 (CUT) by herding the Farfetch'd to the apprentice at `(7, 28)`.
*   **Verified Mechanics:**
    1.  **Turning:** The bird's turning is complex and based on my final position relative to it.
    2.  **Twigs:** The twigs at (22, 30) and (29, 30) can trigger movement or turning. Stepping on the twig at (29, 30) while the bird was at (29, 22) and facing UP caused it to disappear. Stepping on the twig at (22, 30) made the bird appear at (28, 31).
    3.  **Interaction:** Pressing 'A' on the bird makes it disappear. I just confirmed this at (29, 22).
    4.  **Reset:** Wild battles can reset the puzzle, causing the bird to respawn at a different location.
*   **Current Hypothesis:** The puzzle is solved. The bird has returned to the apprentice. I need to go to (7, 28) to confirm.

### Ruins of Alph - Sliding Panels
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

### Ilex Forest Shrine
*   **Objective:** Investigate the shrine at (8, 22).
*   **Test Plan:** Approach from an adjacent tile and press 'A'.

## III. Items & Battle
*   **EVERSTONE:** Prevents evolution.
*   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.

## IV. Reflection & Methodology Insights (Turn 21362)
*   **Core Failure:** I failed to update my internal knowledge base (notepad) when my observations repeatedly contradicted my recorded hypotheses. This led to a major loop. I must be more rigorous and scientific.
*   **Action Item:** Trust direct observation over my notes. If my notes are wrong, I must correct them IMMEDIATELY. Deferring documentation is a critical error.
*   **Tool Usage:** I created a redundant, hyper-specific agent (`farfetchd_herder`) when a general one (`quest_strategist`) existed. I will leverage general, reusable tools and agents going forward.
*   **Test 2:** Approached from above at (28, 30). **Result: FAILED.** Bird turned to face down. The turning logic is not simply 'face the player'.
*   **Test 3:** Approached from below at (28, 32). **Result: SUCCESS!** Bird turned to face left. This confirms the turning logic is based on relative position, not just player facing direction. The bird is now correctly oriented.
*   **New Test Plan (FAILED):** Stepped on twig at (22, 30) while bird was at (28, 31) facing left. **Result: FAILED.** Bird turned to face down. The twigs do not cause movement, they cause re-orientation.
*   **Puzzle Reset:** Wild Pokémon battles reset the entire Farfetch'd puzzle, causing the bird to return to its respawn point at (28, 31).
*   **Test 4 (Chasing):** Approached from behind at (29, 31) and attempted to move onto the bird's tile at (28, 31). **Result: FAILED.** Bird did not move, it turned to face UP. Chasing is not the solution.

## V. System Updates
*   Acknowledged removal of the World Knowledge Graph system. Confirmed no references exist in my notepad or custom tools.