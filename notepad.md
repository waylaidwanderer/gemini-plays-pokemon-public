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

### Puzzle-Solving Methodology
1.  **Observe:** Describe the situation based only on what I see.
2.  **Hypothesize:** Form a single, testable hypothesis.
3.  **Test:** Design and execute the simplest possible test.
4.  **Conclude:** State whether the hypothesis was confirmed or denied. Document all steps.

### Ilex Forest - Farfetch'd Puzzle
*   **Objective:** Herd the Farfetch'd to the apprentice at `(7, 28)`.
*   **Verified Mechanics:**
    *   The Farfetch'd's movement and orientation are changed by my position relative to it. There are no interactable 'twigs'.
    *   Interacting directly (pressing 'A') or getting into a wild battle resets the puzzle by making the bird disappear and reappear elsewhere.
*   **Current Hypothesis:** I need to find the Farfetch'd again and then use my position to manipulate its movement systematically.

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
*   **Core Directive:** I must act on tool/notepad management tasks IMMEDIATELY in the same turn I decide to do them.
*   **Map Marker Discipline:** I must mark moving objects (like the Farfetch'd) using their `object_id` to ensure the marker tracks them correctly. Static markers are for static objects/locations only.
*   **Agent Usage:** I must remember to use `strategic_advisor` when feeling stuck and feed failed attempts into `quest_strategist` for better hypotheses.

## V. Future Tool Development
*   **Exploration Agent/Tool:** I keep getting lost in mazes. I should create a tool that can systematically explore an area, keeping track of visited paths and prioritizing unseen tiles to avoid going in circles. This would be more efficient than manual searching.