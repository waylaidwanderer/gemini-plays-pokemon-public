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
*   **Key Discoveries:** The hideout entrance is in the Mahogany Mart. A switch at (19, 11) on B1F disables the security cameras.
*   **Untested Assumptions:**
    1.  **Assumption:** The radio signal source is on a lower floor, guarded by a leader.
        *   **Alternative Hypothesis:** The source is on B1F behind a secret passage, or is a Pokémon itself.
        *   **Test:** Before descending, perform a final sweep of B1F, interacting with all suspicious walls/objects.
    2.  **Assumption:** Defeating the leader automatically stops the broadcast.
        *   **Alternative Hypothesis:** A separate interaction with a machine is required after the battle.
        *   **Test:** After the leader battle, interact with any machinery in the room before leaving.

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

### Tool & Agent Concepts (Brainstorm)
*   `inventory_manager` (Agent): Could analyze my bag and suggest items to toss when it's full.
*   `map_scanner` (Tool): A tool to scan the current map for specific objects (e.g., all item balls) or tile types to speed up exploration planning.
*   **Special Warps (Verified):** `WARP_PANEL` (One-way teleporter).