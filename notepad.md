# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Tile Rules

### Tile Traversal Rules
- **Testing Protocol:** When a new, reachable tile type is seen, I MUST test it immediately. Test movement *into* and *out of* the tile from all 4 cardinal directions to verify passability and check for one-way paths.
- **IMMEDIATE Priority Test List:** `CUT_TREE` (requires HM), `WATER` (requires HM), `IlexForestShrineScript`, `LEDGE_HOP_DOWN` (attempt to move up).

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
    1.  **Direct Interaction:** Pressing 'A' on the Farfetch'd causes it to teleport away and reset the puzzle.
    2.  **Twig Interaction Logic:**
        *   **Twig 1 at (22, 30):** Stepping on this makes the Farfetch'd disappear if it's on the map.
        *   **Twig 2 at (29, 30):** Stepping on this makes the Farfetch'd appear at (28, 31), facing left.
    3.  **Turning:** The turning logic is not simply facing the player. It seems to be related to the player's approach vector to an adjacent tile. This is still inconsistent and needs more rigorous testing.
    4.  **Reset Conditions:** Wild battles, leaving the area, or direct interaction resets the puzzle.
*   **Alternative Hypotheses to Test:**
    1.  The order the twigs are stepped on matters, independent of the Farfetch'd's position.
    2.  The Farfetch'd must be herded along a specific, hidden path.

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