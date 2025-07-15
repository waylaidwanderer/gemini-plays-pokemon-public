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
*   `COMPUTER`
*   `COUNTER`
*   `FENCE`
*   `FLOWER`
*   `INCENSE_BURNER`
*   `LINK_CABLE`
*   `LINK_RECEPTIONIST`
*   `MART_SHELF`
*   `PC`
*   `PERSIAN_STATUE_L`
*   `PERSIAN_STATUE_R`
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
*   `WARP_PANEL` (One-way teleporter, now treated as impassable by pathfinder)

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

### Menu Mechanics
*   **Inventory Bug (Confirmed):** The inventory is permanently locked. 'TOSS', 'GIVE', 'USE' (in battle), and 'SELL' commands are all non-functional for freeing inventory space. No new items can be picked up.

## III. Current Objective: Progress Story

*   **Primary Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Current Blocker:** Navigating the Team Rocket Hideout.
*   **Current Plan:** My hypothesis that a hidden passage existed in the wall at Y=12 has been disproven after systematically testing every tile from (8, 12) to (3, 12). The contradiction of the on-screen Voltorb remains. My new hypothesis is that another object on the map is a switch or trigger. The most likely candidate is the Poke Ball at (3, 10). My immediate plan is to interact with this Poke Ball to test this new theory.

### Passwords
*   **Password 1:** SLOWPOKETAIL
*   **Password 2:** RATICATE TAIL

## IV. Tool Status
*   **reliable_pathfinder:** This tool had a bug where it would path through `WARP_PANEL` tiles, causing accidental teleportation. I have implemented a fix to treat `WARP_PANEL` as impassable.