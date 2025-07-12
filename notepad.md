# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
- **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
- **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions. Document results.
- **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'. Document results.
- **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path. Document results.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD` (Farfetch'd), `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `WINDOW`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `CUT_TREE` (becomes traversable after using CUT), `FLOOR`.
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE` (Move onto tile), `PIT` (Acts as a one-way warp when stepped on).
*   **One-Way Ledges (Verified):**
    *   `LEDGE_HOP_DOWN`: A one-way ledge that can only be hopped **DOWN**.
    *   `LEDGE_HOP_DOWN/RIGHT`: A one-way ledge that can only be hopped in the specified direction.
    *   `LEDGE_HOP_LEFT`: A one-way ledge that can only be hopped **LEFT**.
    *   `FLOOR_UP_WALL`: A complex one-way ledge. Can move **UP** from `FLOOR` to `FLOOR_UP_WALL`. Can move **DOWN** from `FLOOR_UP_WALL` to `FLOOR` (the jump). Cannot move **DOWN** from `FLOOR` to `FLOOR_UP_WALL`.
*   **Special Requirement (Verified):**
    *   `WATER` (Requires HM03 Surf, must be used from adjacent `FLOOR` tile).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Special Requirement (Hypothesized):**
    *   `WHIRLPOOL` (Requires HM): Impassable via normal movement and interaction.
*   **Complex Tiles (Verified):**
    *   `WARP_CARPET_DOWN`: Traversable. Activated by pressing 'Down' while standing on the tile to trigger a warp.
    *   `WARP_CARPET_DOWN/LEFT/RIGHT`: Traversable. Activated by pressing the corresponding direction while standing on the tile to trigger a warp.
    *   `WARP_CARPET_LEFT`: Traversable. Activated by pressing 'Left' while standing on the tile to trigger a warp.

### Other Mechanics
*   **Object Impassability:** All Map Objects (NPCs, items, signs, etc.) are impassable.
*   **Haircuts:** Increases a Pokémon's happiness.

## II. Strategic Plans & Hypotheses

### Current Quest: The Secret Medicine
*   **Goal:** Find the special medicine in Cianwood City to cure the sick Ampharos in the Olivine Lighthouse.
*   **Current Location:** I have discovered the Cianwood Pharmacy. My working hypothesis is that the Pharmacist inside will give me the medicine.
*   **Alternative Hypothesis:** The Pharmacist may require me to complete another task first, such as defeating the Cianwood Gym Leader.

### Cianwood Gym Puzzle (FAILED - ALL HYPOTHESES INVALIDATED)
*   **Final Failed Hypothesis:** The puzzle requires a complex sequence of triggers, resets, and defeating specific trainers. All attempts based on this have failed. The solution is likely external to the gym itself.
*   **New Working Hypothesis:** The Gym Leader, Chuck, is not in the gym. A gym guide mentioned he is training under a waterfall. The current objective is to find this waterfall.

### Cianwood City NPCs
*   **Pokefan F (11, 46):** Will give a gift (likely HM02 FLY) after defeating the Cianwood Gym Leader.
*   **Glitched Battle State:** Encountered a glitched battle on a WATER tile at (28, 40) in Cianwood City. The game state became corrupted (empty party, incorrect player info) but resolved after attempting to run.
### Tiles Under Investigation
*   `ROCK` (Route 41): Untested. This is a high priority as per the overwatch system critique.