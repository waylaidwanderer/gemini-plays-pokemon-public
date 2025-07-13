# Gem's Pokémon Crystal Notepad

## I. Current Strategy & Hypotheses

### Primary Objective: Find the Secret Medicine
*   **Problem:** The Ampharos in the Olivine Lighthouse is sick, blocking access to the upper floors. I need to find a 'SECRETMEDICINE' to cure it.
*   **Current Hypothesis:** The medicine is somewhere in Cianwood City. My previous assumption that it was a reward for beating the gym was likely incorrect.
*   **Plan:** Systematically re-explore every building and talk to every NPC in Cianwood City. Pay close attention to any new dialogue or potential key items.
    *   ~~Cianwood Pharmacy~~: Visited. The pharmacist runs a normal shop and does not have the medicine.
    *   ~~Mania's House~~: Visited. Received a Shuckle.
    *   **Next:** Talk to Pokefan F at (11, 46).

### Cianwood Gym - Puzzle Solved & Documented
*   **Core Mechanic:** The gym's state changes based on player movement on specific trigger tiles. The central path contains boulders that block the way.
*   **Solution (Verified):**
    1.  **Trigger:** Step on the tile at (8, 6) on the eastern path. This causes the boulders and the Gym Leader to appear.
    2.  **Strength:** Use the HM Strength to push the boulders out of the way. This must be done carefully to avoid blocking the path.
    3.  **Path:** A clear path to the Gym Leader can be made by pushing each of the three central boulders up one tile.
*   **Trap:** The tile at (4, 8) is a reset switch. Stepping on it will return the boulders to their original positions.

## II. Game Systems & Mechanics

### Tile Traversal Protocol
*   **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
*   **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
*   **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
*   **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `STATUE`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `FLOOR`, `WATER` (Requires HM03 Surf).
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`, `PIT` (One-way), `WARP_CARPET_DOWN` (Requires pressing 'Down' while standing on tile).
*   **One-Way Ledges (Verified):** `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`.
*   **Special Requirement (Verified):** `CUT_TREE` (Requires HM01 Cut), `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Special Requirement (Hypothesized):** `WHIRLPOOL` (Requires HM).

### Tiles Under Investigation (High Priority)
*   `FLOOR_UP_WALL`: Attempting to move south from a `FLOOR` tile at (27, 45) onto this tile at (27, 46) failed. Hypothesis: This is a one-way ledge that can only be hopped **DOWN** (south). Test required: Find a path to the upper level to test jumping down.

## III. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact. A trainer is only defeated after a battle victory is confirmed by the game.
*   **Trust Tools Over Perception:** My `pathfinder` tool's output is based on the game's ground truth. If it says 'no path', I must trust it and investigate my own understanding, not assume the tool is broken.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.
*   **Map Corrections:** Map ID `20_1` is not just 'Pokecenter2F'. It also contains the Link Club and its associated record rooms. Interacting with a Link Receptionist can warp the player to one of these rooms. The visual content on screen is the only way to differentiate.