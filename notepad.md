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

### Mahogany Mart Puzzle Log (Re-evaluation)
*   **Objective:** Find the secret Team Rocket entrance.
*   **New Conclusion:** My previous assessment that this puzzle was a "dead end" was incorrect. The trainers on Route 43 are a story block, confirming that the solution *must* be within this Mart. I need to re-examine all interactable objects and NPCs with a fresh perspective.
*   **Recap of Failed Hypotheses:**
    *   The warp at (7, 3) is not a direct entrance.
    *   The Pharmacist is not the trigger. (Test confirmed)
    *   The incense burner at (6, 1) is not a switch. (Test confirmed, marker placed)
    *   The bookshelf at (7, 1) is not a switch. (Test confirmed, marker placed)
*   **New Discovery & Correction:** The Black Belt at (1, 6) did NOT disappear. He reappeared after I attempted to move into his previous location. My hypothesis was incorrect.
*   **New Hypothesis:** The puzzle involves a sequence of events that resets or changes based on my actions. The Black Belt's presence is a key part of this sequence, not a one-time event.
*   **Next Step:** Interact with the Black Belt again from my current position to see if his dialogue has changed.

## VI. Immediate Tasks & Reminders

*   **Unmarked Warps on Route 43:** I must investigate the warps at (10, 51), (17, 35), and (18, 31) after resolving the Lake of Rage event.