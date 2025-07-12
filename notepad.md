# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions. Document results.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'. Document results.
- **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path. Document results.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `CUT_TREE` (becomes traversable after using CUT), `FLOOR`.
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a one-way warp when stepped on).
*   **One-Way Ledges (Verified):**
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
*   **Special Requirement (Verified):**
    *   `WATER` (Requires HM03 Surf, must be used from adjacent `FLOOR` tile).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Special Requirement (Hypothesized):**
    *   `WHIRLPOOL` (Requires HM): Impassable via normal movement and interaction.

### Tiles Under Investigation
*   `ROCK` (Route 41): Untested. This is a high priority as per the overwatch system critique.
*   `FLOOR_UP_WALL`: Attempting to move south from a `FLOOR` tile at (27, 45) onto this tile at (27, 46) failed. Interaction test also failed. Hypothesis: This is a one-way ledge that can only be hopped **DOWN** (south). Next step: Find a path to the upper level to test jumping down.

## II. Strategic Plans & Hypotheses

### Current Quest: The Secret Medicine
*   **Goal:** Find the special medicine in Cianwood City to cure the sick Ampharos in the Olivine Lighthouse.
*   **Current Location:** I have discovered the Cianwood Pharmacy. *   **FAILED Hypothesis:** The Pharmacist in Cianwood Pharmacy has the Secret Medicine. This was proven false; he just runs a regular shop.
*   **Alternative Hypothesis:** The Pharmacist may require me to complete another task first, such as defeating the Cianwood Gym Leader.

### Cianwood Gym Puzzle (FAILED - ALL HYPOTHESES INVALIDATED)
*   **Final Failed Hypothesis:** The puzzle requires a complex sequence of triggers, resets, and defeating specific trainers. All attempts based on this have failed. The solution is likely external to the gym itself.
*   **New Working Hypothesis:** The Gym Leader, Chuck, is not in the gym. A gym guide mentioned he is training under a waterfall. The current objective is to find this waterfall.

### Cianwood City NPCs
*   **Pokefan F (11, 46):** Will give a gift (likely HM02 FLY) after defeating the Cianwood Gym Leader.
*   **Glitched Battle State:** Encountered a glitched battle on a WATER tile at (28, 40) in Cianwood City. The game state became corrupted (empty party, incorrect player info) but resolved after attempting to run.