# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Tile Rules

### Tile Traversal Rules
- **Testing Protocol:** When a new, reachable tile type is seen, I MUST test it immediately. Test movement *into* and *out of* the tile from all 4 cardinal directions to verify passability and check for one-way paths. For ledges, I must attempt to move up against them to confirm they are one-way.
- **IMMEDIATE Priority Test List:** `CUT_TREE` (requires HM), `WATER` (requires HM), `IlexForestShrineScript`.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `COUNTER`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `VOID`, `MART_SHELF`, `BIRD` (Farfetch'd)
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `WARP_CARPET_RIGHT/LEFT/DOWN` (Move in specified direction). Exception: Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Enter by moving UP; Exit by moving LEFT/RIGHT).

## II. Quests & Puzzles

### Ilex Forest - Farfetch'd Puzzle (CORRECTED MODEL)
*   **Objective:** Get HM01 (CUT) by herding the Farfetch'd to the apprentice at `(7, 28)`.
*   **Verified Mechanics (Self-Corrected):**
    1.  **Turning Mechanism:** My own movement onto a tile adjacent to the Farfetch'd is the primary mechanism that causes it to turn. The exact turning logic is complex and seems to depend on the direction of my approach, but it is NOT random. My previous belief that twigs caused turning was incorrect.
    2.  **Twig Function:** The twigs have a different function. The Farfetch'd disappearing when my REPEL wore off is a major clue. Hypothesis: The twigs likely make the Farfetch'd appear, disappear, or move. Their effect is NOT directly related to turning the bird.
        *   **Twig 1 at (22, 30):** Function needs to be re-tested systematically.
        *   **Twig 2 at (29, 30):** Function needs to be re-tested systematically.
    3.  **Reset Conditions:** Wild battles, leaving the area, or direct interaction (pressing 'A') resets the puzzle.
*   **Systematic Testing Plan:**
    1.  Get the Farfetch'd to appear.
    2.  Use my movement to orient it to face a desired direction (e.g., left/west).
    3.  Carefully move to a twig *without* changing the bird's orientation.
    4.  Step on the twig to test if it causes the bird to *move* in the direction it's facing.

### Ruins of Alph - Sliding Panels
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

## III. Items & Battle
*   **EVERSTONE:** Prevents evolution.
*   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.

## IV. Misc. Info
*   Liz mentioned a Pokémon Salon in Goldenrod run by two brothers.