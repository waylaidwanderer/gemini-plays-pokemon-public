# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions. Document results.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'. Document results.
- **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path. Document results.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `VOID`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `CUT_TREE` (becomes traversable after using CUT), `FLOOR`, `WATER` (Requires HM03 Surf).
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`, `WARP_CARPET_DOWN` (Move onto tile), `PIT` (Acts as a one-way warp when stepped on).
*   **One-Way Ledges (Verified):**
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
*   **Special Requirement (Verified):**
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Special Requirement (Hypothesized):**
    *   `WHIRLPOOL` (Requires HM): Impassable via normal movement and interaction.

### Tiles Under Investigation (High Priority)
*   `ROCK` (Route 41): Untested. Must investigate.
*   `FLOOR_UP_WALL`: Attempting to move south from a `FLOOR` tile at (27, 45) onto this tile at (27, 46) failed. Interaction test also failed. Hypothesis: This is a one-way ledge that can only be hopped **DOWN** (south). Next step: Find a path to the upper level to test jumping down.

## II. Strategic Plans & Hypotheses

### Current Quest: The Secret Medicine
*   **Goal:** Find the special medicine in Cianwood City to cure the sick Ampharos in the Olivine Lighthouse.
*   **FAILED Hypothesis:** The Pharmacist in Cianwood Pharmacy has the Secret Medicine. This was proven false; he just runs a regular shop.
*   **FAILED Hypothesis:** The Gym Leader, Chuck, is training under a waterfall somewhere *outside* the gym. This was proven false after exploring the city and finding the Photo Studio instead.
*   **Current Working Hypothesis:** The solution to obtaining the Secret Medicine is inside the Cianwood Gym. The path to the leader is blocked by boulders. FAILED Hypothesis: Interacting with the gym statues is the trigger. This was proven false; they only display the gym's name.
*   FAILED Hypothesis: The Cianwood Gym puzzle is solved by stepping on the trigger tile at (8, 6) on the eastern path, then leaving and re-entering the gym. This was proven false; moving off the trigger tile changed the gym state, but leaving and re-entering simply reset it to the initial state. The central path is a trap that resets the puzzle. Current Working Hypothesis: The gym puzzle is a dynamic sequence. Moving off the trigger tile at (8, 6) caused the original side trainers and the Gym Leader to disappear, and two new trainers to appear at (2, 12) and (7, 12). The next step is to defeat these new trainers to trigger the next phase of the puzzle.