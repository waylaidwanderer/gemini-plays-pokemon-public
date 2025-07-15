# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned

*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction.
*   **Trust, But Verify:** My custom tools are powerful but can have bugs. I must test their output and fix them immediately when they fail.
*   **Act Immediately:** I am an LLM. There is no 'later'. Tool/agent refinement and data management tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## II. Game Systems & Mechanics

### Tile Mechanics

*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `ARROW_TILE_UP`, `ARROW_TILE_DOWN`, `ARROW_TILE_LEFT`, `ARROW_TILE_RIGHT`
*   **Impassable:** `BIRD`, `BOOKSHELF`, `BUOY`, `CHAIR`, `CHIMNEY`, `COMPUTER`, `COUNTER`, `FENCE`, `FLOWER`, `INCENSE_BURNER`, `LINK_CABLE`, `LINK_RECEPTIONIST`, `MART_SHELF`, `PC`, `PERSIAN_STATUE_L`, `PERSIAN_STATUE_R`, `PILLAR`, `PRINTER`, `RADIO`, `ROCK`, `ROOF`, `SIGN`, `TABLE`, `TOWN_MAP`, `TRADE_MACHINE`, `TREE_TOP`, `TV`, `VOID`, `WALL`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `WEIRD_TREE`, `WINDOW`
*   **Warps:** `CAVE`, `DOOR`, `LADDER`, `STAIRCASE`, `WARP_PANEL` (One-way)
*   **Conditional/One-Way:** `BREAKABLE_ROCK` (Requires Rock Smash), `CUT_TREE` (Requires HM01 Cut), `FLOOR_UP_WALL` (One-way ledge), `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`, `PIT` (One-way down), `WARP_CARPET_DOWN` (Requires pressing 'Down' button while standing on tile)

### Menu Mechanics
*   **Inventory Bug (Confirmed):** The inventory is permanently locked. 'TOSS', 'GIVE', 'USE' (in battle), and 'SELL' commands are all non-functional for freeing inventory space. No new items can be picked up.

## III. Team Rocket Hideout Puzzle Log

*   **Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Main Obstacle:** The path to the boss on B3F is inaccessible from the eastern side of the hideout.

### Confirmed Facts & Discoveries
*   **B1F Switch:** Flipping the switch at (19, 11) on B1F disables the arrow tiles, opening the path into the central maze.
*   **B1F Scientist (Jed):** The scientist at (18, 12) permanently blocks the path to the switch. Interacting with him yields dialogue but does not move him.
*   **B1F Warp Panel:** The warp panel at (5, 15) is a one-way teleporter to (25, 2), leading to an isolated exit area via the Mahogany Mart.
*   **B2F Locked Door:** There is a password-locked door at (14, 12). The password trigger is not yet found.
*   **B3F Layout:** B3F is split into two disconnected sections. The eastern section (accessed from B2F) is a dead end. The western section containing the boss is inaccessible from this route.
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.

### Current Hypothesis
*   **H23 (Disproven):** Lance was not waiting in the mart or on B2F. **Result:** No sign of Lance in the explored areas of the hideout.
*   **H24 (Active):** After obtaining the two passwords on B3F, I must speak to Lance again on that same floor to trigger the next event (e.g., him opening the door on B2F).