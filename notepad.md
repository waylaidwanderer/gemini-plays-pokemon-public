# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction. Assumptions must be rigorously tested before being recorded as fact.
*   **Trust Automation:** My custom tools are more reliable than my manual analysis. I must prioritize using them to avoid unforced errors.
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
*   **Current Location:** Team Rocket Hideout, Floor B1F.
*   **Key Discoveries:** The hideout entrance is in the Mahogany Mart. The B1F floor puzzle has two solutions. The eastern path was a dead end. I have discovered a new western path and am currently exploring it.

### Passwords
*   **Password 1:** SLOWPOKETAIL (from Rocket Girl on B3F)

## IV. Battle Discoveries & Type Chart

### Verified Type Interactions
*   **Water (Surf) vs. Gyarados (Water/Flying):** Observed as "not very effective". This contradicts standard type charts. Need to investigate further.

## V. Open Investigations

### Inventory Management Bug
*   **Observation:** All menu-based attempts to free an inventory slot (`TOSS`, `GIVE`, `DEPOSIT`) have failed, resulting in a menu loop.
*   **Hypothesis 1 (Disproven):** Using an item on a full-health Pokémon in battle will consume it. **Test Result:** The game prevents this action.
*   **Primary Hypothesis:** The only way to free an inventory slot is to consume an item that has an effect during a battle (e.g., healing a damaged Pokémon).

## VI. Future Strategy Notes
*   For complex sequential puzzles, I should consider defining a `sequential_puzzle_solver` agent to avoid manual error and increase efficiency.
### Team Rocket Hideout Navigation Notes
* The ladder at (27, 2) on B1F is a one-way exit to the Mahogany Mart.