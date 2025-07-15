# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors. I will use my `sequential_puzzle_solver` for puzzles like this in the future.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## II. Game Systems & Mechanics

### Verified Tile Types

**Traversable:**
*   `FLOOR`
*   `GRASS`
*   `TALL_GRASS`
*   `LONG_GRASS`
*   `RAILING`
*   `PIPE_HORIZONTAL`
*   `PIPE_VERTICAL`

**Impassable:**
*   `BIRD`
*   `BOOKSHELF`
*   `BUOY`
*   `CHAIR`
*   `CHIMNEY`
*   `COUNTER`
*   `FENCE`
*   `FLOWER`
*   `INCENSE_BURNER`
*   `LINK_CABLE`
*   `LINK_RECEPTIONIST`
*   `MART_SHELF`
*   `PC`
*   `PILLAR`
*   `PRINTER`
*   `RADIO`
*   `ROCK`
*   `ROOF`
*   `SIGN`
*   `TABLE`
*   `TOWN_MAP`
*   `TRADE_MACHINE`
*   `TREE_TOP`
*   `TV`
*   `VOID`
*   `WALL`
*   `WATER_EDGE_UP`
*   `WATER_EDGE_DOWN`
*   `WATER_EDGE_LEFT`
*   `WATER_EDGE_RIGHT`
*   `WEIRD_TREE`
*   `WINDOW`

**Warps:**
*   `CAVE`
*   `DOOR`
*   `LADDER`
*   `STAIRCASE`
*   `WARP_CARPET_DOWN` (Requires 'Down' to activate)
*   `WARP_PANEL` (One-way teleporter)
*   `WARP_PANEL` (One-way teleporter)

**Conditional / One-Way:**
*   `BREAKABLE_ROCK` (Requires Rock Smash)
*   `CUT_TREE` (Requires HM01 Cut)
*   `FLOOR_UP_WALL` (One-way ledge, hoppable from above)
*   `LEDGE_HOP_DOWN`
*   `LEDGE_HOP_DOWN/RIGHT`
*   `LEDGE_HOP_LEFT`
*   `PIT` (One-way down)

### Untested Tile Types (Requires Verification)
*   `PERSIAN_STATUE_L`
*   `PERSIAN_STATUE_R`
*   `ARROW_TILE_UP`
*   `ARROW_TILE_DOWN`
*   `ARROW_TILE_LEFT`
*   `ARROW_TILE_RIGHT`
*   `COMPUTER`

## III. Current Investigation: Team Rocket Hideout

*   **Objective:** Find the secret Team Rocket entrance in Mahogany Town, as per Lance's instructions, and disable the radio signal.
*   **Key Discoveries:** The hideout entrance is in the Mahogany Mart. A switch at (19, 11) on B1F disables the security cameras. B2F and B3F appear to be dead ends for finding the second password, suggesting the path is on B1F.

### Passwords
*   **Password 1:** SLOWPOKETAIL (from Rocket Girl on B3F)

### Floor Puzzle (B1F)
*   **Status:** Actively investigating. My previous conclusion that this was a red herring was incorrect. This puzzle is the only remaining path forward.
*   **Hypothesis 1:** The floor is a sequence puzzle. Stepping on the correct tiles in order will unlock the path.
*   **Test 1 (Failed):** Unsystematic exploration. Walked along row 5 and parts of row 6 with no effect. Also walked right from (7, 5) to (11, 5) with no effect.
*   **Conclusion:** A systematic approach is required. Manual exploration is inefficient and prone to error. Will use `sequential_puzzle_solver` agent to determine the next logical step.

## IV. Battle Discoveries & Type Chart

### Verified Type Interactions
*   **Water (Surf) vs. Gyarados (Water/Flying):** Observed as "not very effective". This contradicts standard type charts. Need to investigate further.

## V. Open Investigations

### Inventory Management Bug
*   **Observation:** All menu-based attempts to free an inventory slot (`TOSS`, `GIVE`, `DEPOSIT`) have failed, resulting in a menu loop.
*   **Primary Hypothesis:** The only way to free an inventory slot is to consume an item during a battle. **Test:** Initiate a battle and use a Potion.
*   **Test 2 (Failed):** Systematic pathfinding. Successfully navigated from (7, 5) to (23, 5). The path to the right is blocked by a WALL at (24, 5). My initial assessment that (23, 6) was a trap tile was incorrect. I have since confirmed it is a safe path but failed to explore it. I must backtrack to (23, 5) and investigate the path at (23, 6).

## VI. Future Strategy Notes
*   For complex sequential puzzles like the Team Rocket Hideout floor trap, I MUST use my `sequential_puzzle_solver` agent to avoid manual error and increase efficiency.