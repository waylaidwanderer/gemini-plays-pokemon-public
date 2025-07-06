# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Tile Rules

### Tile Traversal Rules
- **Testing Protocol:** When a new, reachable tile type is seen, I MUST test it immediately. Test movement *into* and *out of* the tile from all 4 cardinal directions to verify passability and check for one-way paths. For ledges, I must attempt to move up against them to confirm they are one-way.
- **IMMEDIATE Priority Test List:** The tile at (8, 22) where the IlexForestShrineScript object is located.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `COUNTER`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `VOID`, `MART_SHELF`, `BIRD` (Farfetch'd)
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `WARP_CARPET_RIGHT/LEFT/DOWN` (Move in specified direction). Exception: Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Enter by moving UP; Exit by moving LEFT/RIGHT).

## II. Quests & Puzzles

### Ilex Forest - Farfetch'd Puzzle
*   **Objective:** Get HM01 (CUT) by herding the Farfetch'd to the apprentice at `(7, 28)`.
*   **Verified Mechanics:**
    1.  **Turning:** My movement to an adjacent tile causes the bird to turn. The logic is complex and based on my final position relative to the bird, not just my direction of approach.
    2.  **Puzzle Reset:** Wild Pokémon battles reset the entire puzzle, causing the bird to return to its respawn point at (28, 31). Leaving the forest also resets it.
    3.  **Twigs:** The twigs at (22, 30) and (29, 30) cause the bird to turn, NOT move.
*   **Current State:** I am at (27, 31), in front of the bird, which is at (28, 31) facing down.
*   **Test 5 (Interact from Front):** Interacting with the bird from (27, 31) only produced a "Kwaa!" sound. **Result: FAILED.** Interaction is not the trigger for movement.
*   **Current Test:** The bird is at (28, 31) facing left. I am at (27, 31). I will move to (27, 32). Hypothesis: Moving from a position in front of the bird to a position diagonally below it will cause it to move forward one step.
*   **Alternative Hypotheses to Test if Above Fails:**
    *   The twigs must be stepped on in a specific sequence.
    *   I need to interact with something else in the forest to change the bird's behavior.

### Ruins of Alph - Sliding Panels
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

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