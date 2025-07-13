# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
*   **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
*   **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
*   **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
*   **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `FLOOR`, `WATER` (Requires HM03 Surf).
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`, `PIT` (One-way), `WARP_CARPET_DOWN` (Requires pressing 'Down' while standing on tile).
*   **One-Way Ledges (Verified):** `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`.
*   **Special Requirement (Verified):** `CUT_TREE` (Requires HM01 Cut), `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Special Requirement (Hypothesized):** `WHIRLPOOL` (Requires HM).

### Tiles Under Investigation (High Priority)
*   `FLOOR_UP_WALL`: Attempting to move south from a `FLOOR` tile at (27, 45) onto this tile at (27, 46) failed. Hypothesis: This is a one-way ledge that can only be hopped **DOWN** (south). Test required: Find a path to the upper level to test jumping down.

## II. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools (`pathfinder`, `boulder_scanner`) are more reliable than my manual navigation and analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## III. Current Plans & Investigations

### Investigation: The Missing HM02 (Fly)
*   **Anomaly:** After defeating Gym Leader Chuck, his wife gave me HM02 (Fly). However, after a thorough search of my bag, the HM is not present in my TM/HM pocket or any other pocket.
*   **Hypotheses:**
    1.  **Misunderstood Event:** I may have misinterpreted the dialogue, and she did not actually give me the HM. It could be a reward I receive later.
    2.  **Temporary Item:** The HM might have been a temporary key item that was removed after a specific trigger I'm unaware of.
    3.  **Game Bug:** It's possible a bug caused the item to not be added to my inventory correctly.
*   **Verification Plan:**
    1.  Travel from my current location on Route 40 back to Cianwood City via Route 41.
    2.  Upon arrival in Cianwood City, enter the Cianwood Gym.
    3.  Speak to Chuck's wife again. Her dialogue will be the deciding factor:
        *   If she re-offers the HM, it confirms a bug or that I failed to receive it correctly the first time.
        *   If she has new dialogue referencing the HM, it may provide a clue as to where it went or what I need to do next.
        *   If her dialogue is unchanged from before I beat Chuck, it suggests the HM is obtained through another method entirely and my memory of the event is flawed.

### Route Plan: Route 40 -> Cianwood City
1.  From current position (6, 11) on Route 40, enter the water at (6, 12).
2.  Surf south to the map transition at (8, 35) which leads to Route 41.
3.  On Route 41, surf west and south to the map transition which leads to Cianwood City.
4.  Reach the shore in Cianwood City.
*   `WARP_CARPET_DOWN`: Seen at (9, 1) and (10, 1). Hypothesis: Functions like a one-way warp when stepped on, possibly only when moving down. Must be tested.