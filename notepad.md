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
*   **Directional Warps (Verified):** `WARP_CARPET_DOWN` (Requires pressing 'Down' to activate).
*   **Special Requirement (Verified):** `CUT_TREE` (Requires HM01 Cut), `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Conditional Traversal (Verified):** `FLOOR_UP_WALL` (A one-way ledge, hoppable from the top).

### Tiles Under Investigation (High Priority)
*   **Special Requirement (Hypothesized):** `WATER` (Hypothesis: Requires HM03 Surf.), `WHIRLPOOL` (Requires HM), `HEADBUTT_TREE` (Hypothesis: Can be interacted with using the move Headbutt.)

## II. Core Principles & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## III. Current Plans & Investigations

### Current Objective: Investigate Mahogany Town
*   **Status:** Lance confirmed a mysterious radio broadcast is originating from Mahogany Town, causing the Gyarados rampage. This is the location of the Team Rocket hideout.
*   **Next Step:** Travel to Mahogany Town and locate the source of the broadcast.

## IV. Puzzle Logs

### Mahogany Town & Route 43 Investigation
*   **Objective:** Find the secret Team Rocket entrance.
*   **Initial Hypothesis (Route 43):** The eastern path of Route 43 is the correct way to Mahogany Town.
*   **Test:** Attempted to pass the Super Nerd at (14, 7).
*   **Result:** Encountered a dialogue loop that could not be broken by pressing A, B, or stunning the NPC. The path is impassable.
*   **Conclusion:** The eastern path is a dead end for now. The western path is the only way forward.
*   **Hypothesis (Mahogany Mart):** The puzzle's purpose is not to open a passage *inside* the mart or to the gym. Its completion (triggering the bookshelf event, then speaking to the guard) must have triggered an event elsewhere.
*   **Current Conclusion:** After speaking with Lance at the Lake of Rage, the next step is to find the source of the radio signal within Mahogany Town.

## V. Battle Discoveries & Type Chart

### Verified Type Interactions
*   **Water (Surf) vs. Gyarados (Water/Flying):** Observed as "not very effective". This contradicts standard type charts. Need to investigate further.