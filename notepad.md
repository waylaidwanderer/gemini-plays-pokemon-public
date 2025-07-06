# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `COUNTER`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `MART_SHELF`, `BIRD` (Farfetch'd), `CUT_TREE`, `WATER`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile). Gatehouse warps are triggered by walking into the building side.
*   **Directional Warps:** `WARP_CARPET_LEFT`, `WARP_CARPET_DOWN` (Move in specified direction).
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Verified: Enter by moving UP; Exit by moving LEFT/RIGHT).

### Untested Tile Types
* `LONG_GRASS`: Assumption is it behaves like `TALL_GRASS`, but needs verification.

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.

## II. Key Items, HMs, & TMs
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge. Taught to SUNDEW.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.

## III. Active Puzzles & Hypotheses

### Ruins of Alph - Sliding Panels
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

### Untested Assumptions (Post-Reflection)
*   **Assumption:** The only way to Goldenrod City is north through Route 34.
    *   **Alternative Hypothesis:** The water to the west could provide an alternative path or necessary item (requires SURF).
    *   **Test:** Backtrack through Ilex Forest to get to the western side of Route 34. Explore water routes once SURF is available.
*   **Assumption:** Goldenrod City is the next mandatory location.
    *   **Alternative Hypothesis:** The Ruins of Alph puzzle is mandatory for progression.
    *   **Test:** If Goldenrod City is blocked, pivot to solving the Ruins of Alph puzzle.
*   **Assumption:** The Day-Care PC is permanently bugged.
    *   **Alternative Hypothesis:** The PC works under different conditions (e.g., time of day, story progression).
    *   **Test:** Try interacting with the PC again at a later point in the game.

## IV. Tool & Agent Development
### Core Directives
*   I must act on tool/notepad management tasks IMMEDIATELY.
*   I must mark moving objects using their `object_id`.
*   I must use `strategic_advisor` when feeling stuck and feed failed attempts into `quest_strategist` for better hypotheses.

## V. Archived Puzzles (Solved)

### Ilex Forest - Farfetch'd Puzzle
*   **Status: SOLVED!** Received HM01 (CUT) as a reward.

### Goldenrod City - New Hypotheses
*   **COIN CASE Location:** The Pokefan M mentioned losing it in the UNDERGROUND. It is likely in this newly discovered area. I must explore thoroughly.
*   **Goldenrod Gym Access:** The Gym may have a prerequisite for entry. Finding the COIN CASE could be the trigger to unlock it, or I might need to complete another event in the city first. I will keep an eye out for any related clues.
### Untested Tile Types (Goldenrod Underground)
* `RAILING`: Needs testing.
* `PIPE_HORIZONTAL`: Needs testing.
* `PIPE_VERTICAL`: Needs testing.
### Untested Tile Types (Goldenrod Underground)
* `RAILING`: Needs testing.
* `PIPE_HORIZONTAL`: Needs testing.
* `PIPE_VERTICAL`: Needs testing.