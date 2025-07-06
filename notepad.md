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

### Ilex Forest - Farfetch'd Puzzle (REVISED MODEL)
*   **Objective:** Get HM01 (CUT) by herding the Farfetch'd to the apprentice at `(7, 28)`.
*   **Verified Mechanics (Self-Corrected after AI Critique):**
    1.  **Turning Mechanism:** My own movement onto a tile adjacent to the Farfetch'd is the primary mechanism that causes it to turn. The exact turning logic is complex and seems to depend on the direction of my approach, but it is NOT random.
    2.  **Disappearance/Reappearance:** The Farfetch'd does NOT disappear when REPEL wears off. My previous observation was likely a coincidence. The disappearance must be caused by something else. It reappeared at (28, 31) after I stepped on the twig at (22, 30).
    3.  **Twig Function:** The function of the twigs is NOT to turn the bird. My previous model was flawed. The twigs are likely used to make the Farfetch'd appear, disappear, or *move* once it is correctly oriented.
*   **Current Working Hypothesis (REVISED):** The function of the twigs is still unknown, but my last test proved they don't simply make the bird move forward. Stepping on the twig at (29, 30) while the bird was at (28, 31) and facing left caused it to turn to face right. This invalidates the previous hypothesis.
*   **New Test Plan:**
    1. Re-orient the bird to face LEFT by approaching it from the RIGHT (moving to (29, 31)).
    2. Once it is facing left, step on the OTHER twig at (22, 30).
    3. Hypothesis: A specific twig must be used to make the bird move once it is correctly oriented.
*   **Alternative Hypotheses to Test if Above Fails:**
    *   The twigs are sound cues. Stepping on one makes the bird turn to face the sound's origin from a distance.
    *   The sequence of twig activations matters.

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