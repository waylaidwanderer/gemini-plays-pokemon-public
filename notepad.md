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
*   **Inventory Bug:** The 'TOSS' and 'GIVE' commands in the PACK menu are non-functional. They trigger a menu reset without performing the action. The only known way to free an inventory slot is to *use* an item in battle on a Pokémon that can be affected by it (e.g., using a Potion on a damaged Pokémon).

## III. Current Objective: Un-stick Inventory & Progress

*   **Primary Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Current Blocker:** Full inventory and a bugged menu prevent me from picking up key items in the Team Rocket Hideout.
*   **Current Plan:** Intentionally take damage in a wild battle on Route 43, then use a Potion to free up an inventory slot. Once a slot is free, I will return to the hideout to collect the items.

### Passwords
*   **Password 1:** SLOWPOKETAIL
*   **Password 2:** RATICATE TAIL

## IV. Tool Status
*   **reliable_pathfinder:** This tool had a bug where it would fail if the player's starting tile was a non-standard traversable type (like a `LADDER` or `WARP_CARPET_DOWN`). I have implemented a fix to correct this. I need to re-test it in the `Route43MahoganyGate` to confirm the fix is robust.