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

#### Standard Floor Tiles (Special Appearance)
*   `ARROW_TILE_UP` (Acts as a normal `FLOOR` tile)
*   `ARROW_TILE_DOWN` (Acts as a normal `FLOOR` tile)
*   `ARROW_TILE_LEFT` (Acts as a normal `FLOOR` tile)
*   `ARROW_TILE_RIGHT` (Acts as a normal `FLOOR` tile)

#### Untested
*   `COMPUTER`
*   `PERSIAN_STATUE_L`
*   `PERSIAN_STATUE_R`

### Menu Mechanics
*   **Inventory Bug (Confirmed):** The inventory is permanently locked. 'TOSS', 'GIVE', 'USE' (in battle), and 'SELL' commands are all non-functional for freeing inventory space. No new items can be picked up.

## III. Current Objective: Progress Story

*   **Primary Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Current Blocker:** Navigating the Team Rocket Hideout.
*   **Current Plan:** All previously explored paths (eastern and western ladders on B1F) have led to dead ends. My previous assumption that the central arrow tiles were disabled was unverified and likely false. My hypothesis that the arrow tiles would force movement was incorrect. Stepping on them simply moves me one tile. This area is a standard maze, likely with hidden floor traps. I will now carefully explore this central path.

### Passwords
*   **Password 1:** SLOWPOKETAIL
*   **Password 2:** RATICATE TAIL

## IV. Tool Status
*   **reliable_pathfinder:** This tool had a bug where it would path through `WARP_PANEL` tiles, causing accidental teleportation. I have implemented a fix to treat `WARP_PANEL` as impassable.

## V. Contingency Plans
*   **Team Rocket Hideout B1F:** If the current eastern corridor proves to be a dead end, the next step is to test the hypothesis that the switch at (19, 11) affected other floors. I must return to the ladder at (3, 14) and re-explore B2F to verify if it is still a dead end.