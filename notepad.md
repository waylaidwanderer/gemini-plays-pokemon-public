# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Tile Rules

### Tile Traversal Rules
- **Testing Protocol:** When a new, reachable tile type is seen, I MUST test it immediately. Test movement *into* and *out of* the tile from all 4 cardinal directions to verify passability and check for one-way paths.
- **IMMEDIATE Priority Test List:** `CUT_TREE` (requires HM), `WATER` (requires HM), `IlexForestShrineScript`

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `COUNTER`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `VOID`, `MART_SHELF`, `BIRD` (Farfetch'd)
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `WARP_CARPET_RIGHT/LEFT/DOWN` (Move in specified direction). Exception: Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Enter by moving UP; Exit by moving LEFT/RIGHT).

## II. Quests & Puzzles

### Ilex Forest - Farfetch'd Puzzle
*   **Objective:** Get HM01 (CUT) by herding the Farfetch'd to the apprentice at `(7, 28)`.
*   **Verified Mechanics:**
    1.  **Direct Interaction:** Pressing 'A' on the Farfetch'd causes it to teleport away.
    2.  **Twig Interaction Logic:**
        *   **Twig 1 at (22, 30):**
            *   When Farfetch'd is at (28, 31), stepping on this twig makes it disappear.
        *   **Twig 2 at (29, 30):**
            *   When Farfetch'd is not on the map, stepping on this twig makes it appear at (28, 31), facing right.
    3.  **Turning:** The turning logic is not simply facing the player. It seems to be related to the player's approach vector.
    4.  **Reset Conditions:** Wild battles or leaving the area resets the puzzle.
*   **Alternative Hypotheses to Test:**
    1.  The puzzle requires a specific sequence of twig-stepping and player movement.
    2.  There is a hidden item or another NPC I haven't found yet that is required.
    3.  The time of day might affect the puzzle.

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