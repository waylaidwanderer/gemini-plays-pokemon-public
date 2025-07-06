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
*   **Objective:** Herd the Farfetch'd back to the apprentice at `(7, 28)`.
*   **Status:** In Progress.
*   **Mechanics:** The puzzle involves manipulating the Farfetch'd's movement and orientation by stepping on twigs. Different twigs cause different reactions (turning vs. moving). The bird's current facing direction is critical. Interacting with it directly (`A` button) or getting into a wild battle resets its position.

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
*   **Map Marker Discipline:** I must mark the Farfetch'd's location (object_id 1) every time it moves to a new tile.
*   **System Updates:** Acknowledged removal of the World Knowledge Graph system. Confirmed no references exist in my notepad or custom tools.