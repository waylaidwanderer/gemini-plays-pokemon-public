# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction.
*   **Trust, But Verify:** My custom tools are powerful, but can have bugs. I must test their output and fix them immediately when they fail.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## II. Game Systems & Mechanics

### Tile Mechanics

#### Traversable
*   `FLOOR`
*   `GRASS`
*   `TALL_GRASS`
*   `LONG_GRASS`
*   `RAILING`
*   `PIPE_HORIZONTAL`
*   `PIPE_VERTICAL`

#### Impassable
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

#### Warps
*   `CAVE`
*   `DOOR`
*   `LADDER`
*   `STAIRCASE`
*   `WARP_CARPET_DOWN` (Requires 'Down' to activate)
*   `WARP_PANEL` (One-way teleporter)

#### Conditional / One-Way
*   `BREAKABLE_ROCK` (Requires Rock Smash)
*   `CUT_TREE` (Requires HM01 Cut)
*   `FLOOR_UP_WALL` (One-way ledge, hoppable from above)
*   `LEDGE_HOP_DOWN`
*   `LEDGE_HOP_DOWN/RIGHT`
*   `LEDGE_HOP_LEFT`
*   `PIT` (One-way down)

#### Untested
*   `ARROW_TILE_UP`
*   `ARROW_TILE_DOWN`
*   `ARROW_TILE_LEFT`
*   `ARROW_TILE_RIGHT`
*   `COMPUTER`
*   `PERSIAN_STATUE_L`
*   `PERSIAN_STATUE_R`

### Menu Mechanics
*   **Inventory Bug (Confirmed):** The inventory is permanently locked. 'TOSS', 'GIVE', 'USE' (in battle), and 'SELL' commands are all non-functional for freeing inventory space. No new items can be picked up.

## III. Current Objective: Progress Story

*   **Primary Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Current Blocker:** Navigating the Team Rocket Hideout.
*   **Current Plan:** Explore the central corridor of B1F, which was previously blocked by arrow tiles, to find the correct path to the western section of the lower floors.

### Passwords
*   **Password 1:** SLOWPOKETAIL
*   **Password 2:** RATICATE TAIL

## IV. Tool Status
*   **reliable_pathfinder:** This tool had a bug where it would fail if the player's starting tile was a non-standard traversable type (like a `LADDER` or `WARP_CARPET_DOWN`). I have implemented a fix to correct this. I need to re-test it in the `Route43MahoganyGate` to confirm the fix is robust.