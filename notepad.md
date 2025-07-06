# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions to verify passability.
- **Ledge Test:** For any ledge-like tile, I must attempt to move up/against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable:** `WALL`, `HEADBUTT_TREE`, `PC`, `COUNTER`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `WINDOW`, `STATUE`, `TABLE`, `CHAIR`, `MART_SHELF`, `BIRD` (Farfetch'd), `CUT_TREE`, `WATER`
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS` (Wild Encounters)
*   **Warps:** `DOOR`, `CAVE`, `LADDER` (Move onto tile), `WARP_CARPET_RIGHT/LEFT/DOWN` (Move in specified direction). Gatehouse warps are triggered by walking into the building side.
*   **One-Way Ledges:** `LEDGE_HOP_DOWN/LEFT/RIGHT`. Verified by attempting to move against the ledge direction.
*   **Complex Tiles:** `FLOOR_UP_WALL` (Verified: Enter by moving UP; Exit by moving LEFT/RIGHT).
*   **Untested:** `VOID` (Must test when reachable)

### Other Mechanics
*   **Item Effects:**
    *   **BERRY:** Restores 10 HP. Found at `FRUIT_TREE`s.
    *   **EVERSTONE:** Prevents evolution.
    *   **MOOMOO MILK:** Restores 100 HP. Purchased at MOOMOO FARM.
*   **SLOWPOKETAIL:** Offered for sale on Route 32. Purpose unknown.

## II. Key Items & HMs
*   **HM01 (CUT):** Clears small trees. Requires the Hive Badge from Azalea Town to use outside of battle. Taught to SUNDEW.
*   **TM49 (Fury Cutter):** Gets stronger with each consecutive hit.

## III. Puzzles & Quests

### Puzzle-Solving Methodology
1.  **Observe:** Describe the situation based only on what I see.
2.  **Hypothesize:** Form a single, testable hypothesis.
3.  **Test:** Design and execute the simplest possible test.
4.  **Conclude:** State whether the hypothesis was confirmed or denied. Document all steps.

### Ilex Forest - Farfetch'd Puzzle
*   **Objective:** Herd the Farfetch'd to the apprentice at `(7, 28)`.
*   **Verified Mechanics:**
    *   The Farfetch'd's movement and orientation are changed by my position relative to it.
    *   Interacting directly (pressing 'A') or getting into a wild battle resets the puzzle by making the bird disappear and reappear elsewhere.
*   **Status: SOLVED!** Received HM01 (CUT) as a reward.

### Ruins of Alph - Sliding Panels
*   **Objective:** Solve the sliding stone panel puzzle.
*   **Clue:** Liz mentioned hearing a strange radio broadcast from the Ruins of Alph. This might be a clue.

## IV. Tool & Agent Development

### Core Directives
*   I must act on tool/notepad management tasks IMMEDIATELY in the same turn I decide to do them.
*   I must mark moving objects (like the Farfetch'd) using their `object_id` to ensure the marker tracks them correctly. Static markers are for static objects/locations only.
*   I must remember to use `strategic_advisor` when feeling stuck and feed failed attempts into `quest_strategist` for better hypotheses.

### Future Tool Development
*   **Exploration Agent/Tool:** I keep getting lost in mazes. I should create a tool that can systematically explore an area, keeping track of visited paths and prioritizing unseen tiles to avoid going in circles. This would be more efficient than manual searching.