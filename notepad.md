# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction.
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
*   `BOOKSHELF` (Some are interactable puzzle elements)
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

*   **Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Current Location:** Team Rocket Hideout, Floor B3F.
*   **Key Discoveries:** The hideout entrance is in the Mahogany Mart. The ladder at (27, 2) on B1F is a one-way exit to the Mahogany Mart. Picking up an item with a full bag causes a dialogue loop. Defeated NPC sprites can block paths. The eastern and western halves of B3F are disconnected.
*   **Current Hypothesis:** I missed a trigger on B1F or B2F that opens the path forward. My next step is to return to B2F to re-explore.
*   **Alternative Hypothesis:** The `OathScript` bookshelves in the western part of B3F are a puzzle, but I need to find a different way to access them.

### Passwords
*   **Password 1:** SLOWPOKETAIL (from Rocket Girl on B3F)
*   **Password 2:** RATICATE TAIL (from Rocket Grunt on B3F)

## IV. Battle Discoveries & Type Chart

### Verified Type Interactions
*   **Water (Surf) vs. Gyarados (Water/Flying):** Observed as "not very effective". This contradicts standard type charts. Need to investigate further.

## Reflection & Strategy (Turn 44696)
*   **Hypothesis:** The way forward on B3F is blocked by a switch/event on B2F.
*   **Alternative Hypothesis:** Progress requires interacting with the computer terminals on B2F, or defeating all Voltorb sprites on the floor.
*   **Plan:** Fully explore B2F. If no switch is found, test alternative hypotheses. I created a new tool, `find_next_exploration_target`, to make this exploration more systematic.