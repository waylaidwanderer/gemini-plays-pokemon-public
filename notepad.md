# Gem's Pokémon Crystal Notepad

## I. Game Systems & Mechanics

### Tile Traversal Protocol
*   **Testing Mandate:** When a new, reachable tile type is seen, I MUST test it immediately.
*   **Movement Test:** Attempt to move *into* and *out of* the tile from all 4 cardinal directions.
*   **Interaction Test:** If movement fails, I must attempt to interact with the tile by facing it and pressing 'A'.
*   **Ledge Test:** For any ledge-like tile, I must attempt to move against the apparent direction of the ledge to confirm if it is a one-way path.

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`, `WINDOW`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `FLOOR`.
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`.
*   **One-Way Traversal (Verified):** `PIT` (One-way down), `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`.
*   **Directional Warps (Verified):**
    *   `WARP_CARPET_DOWN`: Requires pressing 'Down' to activate.
*   **Special Requirement (Verified):** 
    *   `CUT_TREE` (Requires HM01 Cut).
    *   `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Conditional Traversal (Verified):**
    *   `FLOOR_UP_WALL`: A one-way ledge, hoppable from the top. If this tile is ever impassable, it is due to an external factor (e.g., an invisible event wall), not a change in the tile's intrinsic properties. My test on Route 42 confirmed this.

### Tiles Under Investigation (High Priority)
*   **Special Requirement (Hypothesized):**
    *   `WATER` (Hypothesis: Requires HM03 Surf. Must be activated from the overworld by facing the water and pressing 'A'.)
    *   `WHIRLPOOL` (Requires HM).
    *   `HEADBUTT_TREE` (Hypothesis: Can be interacted with using the move Headbutt.)

## II. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## III. Current Plans & Investigations

### Current Objective: Investigate the Lake of Rage
*   **Status:** In progress.
*   **Reasoning:** Multiple NPCs have mentioned a "rampage" or "conspiracy" at the Lake of Rage, which is a strong indicator of the main story path. I am currently in Mahogany Town, which is the gateway to the lake.
*   **Hypothesis Testing:**
    1.  **Impassable Ledge on Route 42:** Hypothesis: The ledge is blocked by an event flag. Test: After resolving the Lake of Rage events, I must return to Route 42 and attempt to jump the ledge again.
    2.  **Fisher blocking Mahogany Gym:** Hypothesis: The Fisher will move after the Lake of Rage event. Test: After the event, I will return to the Gym and speak to the Fisher.

## IV. Future Development Ideas

### Agent Ideas
*   **Repel Advisor:** An agent to recommend when to use a Repel based on party level, current location, and goal (e.g., training vs. exploration).

## V. Puzzle Logs

### Mahogany Mart Puzzle Log
*   **Objective:** Find the secret Team Rocket entrance.
*   **Hypothesis 6 (In Progress):** Interacting with the Black Belt at (1, 6) is the first step in a sequence to unlock the secret entrance.
    *   **Step 1 (Complete):** Interact with the Black Belt. Result: Triggers villain monologue. (Note: He does not disappear, correcting a previous faulty observation).
    *   **Step 2 (Failed):** After the monologue, moved to the suspected warp at (7, 3) and attempted to use it by facing multiple directions and pressing 'A'. Result: No effect. Conclusion: The warp is not activated by simple presence or directional interaction.
    *   **Hypothesis 7 (Failed):** The Black Belt's monologue enables a hidden switch on the bookshelf at (7, 1).
    *   **Test:** Interact with the bookshelf at (7, 1).
    *   **Result:** Displays flavor text about Pokémon magazines.
    *   **Conclusion:** FAILED.
*   **Hypothesis 8 (Current):** The Black Belt's monologue enables a hidden switch on the incense burner at (6, 1).
    *   **Test:** Interact with the incense burner.
*   **Hypothesis 2:** The Pharmacist at (4, 3) is the trigger.
    *   **Test:** Interact with him.
    *   **Result:** Opens the standard shop menu.
    *   **Conclusion:** FAILED.
*   **Hypothesis 3:** The warp at (7, 3) is a direct, usable entrance.
    *   **Test:** Step on it, press A while on it, press A while facing it.
    *   **Result:** No effect.
    *   **Conclusion:** FAILED. Requires an external trigger.
*   **Hypothesis 4:** The bookshelf at (7, 1) or incense burner at (6, 1) are hidden switches.
    *   **Test:** Interact with both objects.
    *   **Result:** Only flavor text is displayed.
    *   **Conclusion:** FAILED.
*   **Hypothesis 5:** Repeatedly interacting with the Black Belt will eventually trigger something new.
    *   **Test:** Interact with him multiple times in a row.
    *   **Result:** The dialogue simply repeats. No other changes observed in the room.
    *   **Conclusion:** FAILED. Simple repeated interaction is not the solution.

### Route 43 Gatehouse Log
*   **Conclusion:** The Route 43 Gatehouse is divided into two sections. The officer is unreachable from the entrance. This path is a dead end. The only remaining option is to solve the puzzle in the Mahogany Mart.
    *   **Hypothesis 8 (Failed):** The Black Belt's monologue enables a hidden switch on the incense burner at (6, 1).
    *   **Test:** Interact with the incense burner.
    *   **Result:** Displays flavor text about an incense burner.
    *   **Conclusion:** FAILED. The mart puzzle is a complete dead end. The path forward must be outside in Mahogany Town.

## VI. Immediate Tasks & Reminders

*   **Unmarked Warp:** There is an unmarked warp on Route 43 at (10, 51) that needs to be investigated.