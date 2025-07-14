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
*   **Objective:** Find the secret Team Rocket entrance in Mahogany Town, as per Lance's instructions.
*   **Route 43 Status:** The eastern path is blocked by a bugged Super Nerd at (14, 7); all attempts to pass have failed. The western path is the only viable route south.

### Team Rocket Hideout Security Puzzle (Solved)
*   **Observation:** The ROCKET Grunt at (2, 4) provides dialogue warning about floor traps. A secret switch is located at (19, 11), behind a desk in a central room.
*   **Hypothesis:** Activating the switch at (19, 11) will disable the security cameras.
*   **Test:** Interacted with the switch at (19, 11). Walked from (19, 12) to (23, 5), passing in front of the security camera at (24, 5). No battle was triggered.
*   **Conclusion:** The switch at (19, 11) has successfully disabled the security cameras. The path is now safe from camera-triggered encounters.

### Team Rocket Hideout B2F
*   **Status:** Arrived on B2F via a ladder. Lance is here, as is an item ball. This seems to be a significant area.

## V. Battle Discoveries & Type Chart

### Verified Type Interactions
*   **Water (Surf) vs. Gyarados (Water/Flying):** Observed as "not very effective". This contradicts standard type charts. Need to investigate further.

## VI. Ideas & Future Plans

### Tool Concepts
*   **`battle_menu_navigator`:** A potential tool to automate move selection in simple, repetitive battles.
*   **`exploration_advisor`:** An agent to analyze the map and suggest exploration priorities.

### Untested Hypotheses
*   **Floor Trap State:** Are the floor traps random or on fixed tiles? **Test:** After clearing an area, walk back over a tile where a trap was previously triggered.
*   **Camera Switch Scope:** Does the switch at (19, 11) disable *all* security cameras, or only those on B1F? **Test:** If I find cameras on other floors, I must test them by walking in front of them.