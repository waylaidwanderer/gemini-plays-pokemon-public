# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## II. Game Systems & Mechanics

### Verified Tile Types
*   **Impassable (Verified):** `WALL`, `PILLAR`, `BOOKSHELF`, `TV`, `RADIO`, `TOWN_MAP`, `TABLE`, `CHAIR`, `BIRD`, `MART_SHELF`, `PC`, `LINK_CABLE`, `TRADE_MACHINE`, `INCENSE_BURNER`, `ROOF`, `CHIMNEY`, `SIGN`, `FLOWER`, `TREE_TOP`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `VOID`, `COUNTER`, `FENCE`, `LINK_RECEPTIONIST`, `WEIRD_TREE`, `PRINTER`, `BUOY`, `ROCK`, `WINDOW`.
*   **Traversable (Verified):** `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `FLOOR`.
*   **Warps (Verified):** `DOOR`, `CAVE`, `LADDER`, `STAIRCASE`.
*   **One-Way Traversal (Verified):** `PIT` (One-way down), `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`.
*   **Directional Warps (Verified):** `WARP_CARPET_DOWN` (Requires pressing 'Down' to activate), `WARP_PANEL` (One-way teleporter).
*   **Special Requirement (Verified):** `CUT_TREE` (Requires HM01 Cut), `BREAKABLE_ROCK` (Requires Rock Smash).
*   **Conditional Traversal (Verified):** `FLOOR_UP_WALL` (A one-way ledge, hoppable from the top).

## III. Current Investigation: Team Rocket Hideout

*   **Objective:** Find the secret Team Rocket entrance in Mahogany Town, as per Lance's instructions, and disable the radio signal.
*   **Key Discoveries:** The hideout entrance is in the Mahogany Mart. A switch at (19, 11) on B1F disables the security cameras. Both ladders on B1F are either dead ends or one-way exits.
*   **Current Plan:** Since all obvious paths have been exhausted, my next step is to systematically re-investigate the central area of B1F after using the warp panel at (5, 15). I will re-interact with all objects and NPCs to check for missed triggers.

## IV. Battle Discoveries & Type Chart

### Verified Type Interactions
*   **Water (Surf) vs. Gyarados (Water/Flying):** Observed as "not very effective". This contradicts standard type charts. Need to investigate further.

## V. Ideas & Future Plans

### Tool & Agent Concepts
*   **`exploration_advisor` (Tool):** A tool to parse the map XML and return a list of coordinates for reachable unseen tiles to guide exploration.
*   **`item_scanner` (Tool):** A tool to scan the current map for all item balls to speed up collection planning.

## VI. Open Investigations

### Inventory Management Bug
*   **Observation:** All menu-based attempts to free an inventory slot (`TOSS`, `GIVE`, `DEPOSIT`) have failed, resulting in a menu loop.
*   **Current Hypothesis:** The only way to free an inventory slot is to consume an item during a battle.
*   **Test:** Initiate a battle and attempt to use a Potion.