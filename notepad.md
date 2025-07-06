# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Tile Rules

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `COUNTER`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `VOID`, `MART_SHELF`, `BIRD` (Farfetch'd), `CUT_TREE`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `WARP_CARPET_RIGHT/LEFT/DOWN` (Move in specified direction). Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Verified: Enter by moving UP; Exit by moving LEFT/RIGHT).

## II. Quests & Puzzles

### Ilex Forest - Farfetch'd Puzzle
*   **Objective:** Herd the Farfetch'd (object_id 1) to the apprentice at `(7, 28)`.
*   **Verified Mechanics:**
    *   Stepping on specific `FLOOR` tile coordinates changes the Farfetch'd's orientation (facing direction). The puzzle is about finding the correct sequence of tile coordinates.
    *   The bird's reaction depends on my position relative to it.
    *   Wild battles or direct interaction (pressing 'A') reset the puzzle, often moving the bird to a new starting position.
*   **Current `quest_strategist` Hypotheses Under Test:**
    1.  **Orient then Propel:** Use one tile to orient the bird, then circle to its opposite side to use a second tile to propel it forward. (e.g., Make it face west, then approach from the east).
    2.  **Opposite Side Propulsion:** To move the bird in a desired direction, step on a tile on its *opposite* side (e.g., step on a tile east of the bird to move it west). 
    3.  **Diagonal Stimulus:** Step on diagonally adjacent tiles to provoke a different, potentially more useful, reaction.

### Ruins of Alph - Sliding Panels
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

## III. Items & Battle
*   **EVERSTONE:** Prevents evolution.
*   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.
*   **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.

## IV. System & Methodology
*   **Core Directive:** I must act on tool/notepad management tasks IMMEDIATELY in the same turn I decide to do them. Deferring these actions is a critical failure of my process.
*   **Map Marker Discipline:** I must mark moving objects (like the Farfetch'd) using their `object_id` to ensure the marker tracks them correctly. Static markers are for static objects/locations only.