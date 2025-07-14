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
*   **Key Discoveries:** The hideout entrance is in the Mahogany Mart. A switch at (19, 11) on B1F disables the security cameras. Both ladders on B1F are either dead ends or one-way exits. Interacting with Scientist Jed at (18, 12) causes him to move temporarily, but he blocks the path again.
*   **Current Plan:** Use the `sequential_puzzle_solver` agent to determine the next step in the hidden floor puzzle. Mark each correct step with a map marker.

### Floor Puzzle - Team Rocket Hideout B1F
*   **Mechanics:** This is a state-based sequence puzzle. Stepping on incorrect tiles may reset the puzzle or trigger traps. Stepping on correct tiles causes environmental changes (objects appearing/disappearing) that indicate progress. Backtracking along the correct path does not reset the puzzle.
*   **Successful Sequence (so far):** (20, 7) -> (19, 7) -> (18, 7) -> (17, 7) -> (16, 7) -> (15, 7) -> (14, 7) -> (14, 6) -> (14, 5) -> (13, 5) -> (12, 5) -> (11, 5) -> (10, 5) -> (9, 5) -> (8, 5) -> (7, 5) -> (8, 5) -> (9, 5) -> (10, 5) -> (11, 5) -> (12, 5) -> (13, 5) -> (14, 5) -> (15, 5) -> (16, 5) -> (17, 5) -> (18, 5) -> (19, 5) -> (20, 5) -> (21, 5) -> (22, 5) -> (23, 5) -> (23, 6) -> (24, 6) -> (25, 6) -> (26, 6) -> (26, 7) -> (26, 8) -> (26, 9) -> (25, 9) -> (24, 9) -> (24, 10) -> (24, 11) -> (24, 12) -> (24, 13) -> (25, 13) -> (26, 13) -> (27, 13) -> (27, 12) -> (28, 12) -> (28, 11) -> (28, 10) -> (28, 9) -> (27, 9) -> (26, 9) -> (26, 8).
*   **Key State Changes:**
    *   Stepping on (14, 7) makes the Poke Ball at (21, 12) disappear.
    *   Stepping on (14, 6) makes the Scientist at (18, 12) disappear.
    *   Stepping on (8, 5) makes the ROCKET grunt at (2, 4) disappear.
    *   Stepping on (21, 5) makes a Poke Ball appear at (27, 6).
    *   Stepping on (26, 7) makes the Poke Ball at (21, 12) reappear.
    *   Stepping on (24, 12) makes the Poke Ball at (27, 6) disappear.
    *   Stepping on (27, 13) makes the Poke Ball at (21, 12) disappear.
    *   Stepping on (28, 11) makes the Poke Ball at (27, 6) reappear.
    *   Stepping on (26, 9) makes the Poke Ball at (21, 12) reappear.
    *   Stepping on (27, 9) makes the Poke Ball at (21, 12) disappear.
*   **Failed Paths:** 
    *   The entire path starting with `(7, 5) -> (7, 6)` is a confirmed dead end.
    *   The step from `(23, 6) -> (23, 7)` is a TRAP that resets the puzzle state.
    *   The step from `(27, 12) -> (26, 12)` is a TRAP that resets the puzzle state.
*   **Current Hypothesis:** The path continues downwards from (24, 12).

## IV. Battle Discoveries & Type Chart

### Verified Type Interactions
*   **Water (Surf) vs. Gyarados (Water/Flying):** Observed as "not very effective". This contradicts standard type charts. Need to investigate further.

## V. Open Investigations

### Inventory Management Bug
*   **Observation:** All menu-based attempts to free an inventory slot (`TOSS`, `GIVE`, `DEPOSIT`) have failed, resulting in a menu loop.
*   **Primary Hypothesis:** The only way to free an inventory slot is to consume an item during a battle. **Test:** Initiate a battle and use a Potion.
*   **Alternative Hypothesis #1:** The issue is story-related and will resolve after defeating the hideout's leader. **Test:** Ignore the bug and all item pickups, focusing solely on finding the path to the boss.
*   **Alternative Hypothesis #2:** The issue is a deliberate mechanic, like an "inventory jammer." **Test:** Search for a machine, a generator, or a switch that could be responsible for this effect and interact with it.
*   **Alternative Hypothesis #3:** The inventory issue is a temporary story mechanic, not a bug. It may resolve automatically after defeating the hideout's leader. **Test:** If other hypotheses fail, ignore all item pickups and focus solely on finding the path to the boss.