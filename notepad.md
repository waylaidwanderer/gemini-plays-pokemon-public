# Gem's Pokémon Crystal Notepad

## I. Core Directives & Lessons Learned
*   **Data Integrity is Paramount:** My internal state (notepad, markers) MUST be 100% accurate. I will not defer data correction or tool refinement.
*   **Trust, But Verify:** My custom tools and agents are powerful but can be flawed. I must test their output and fix them immediately when they fail.
*   **Act Immediately:** I am an LLM. There is no 'later'. All data management and tool/agent refinement tasks must be performed in the current turn, overriding gameplay actions.
*   **Scientific Method:** For all puzzles, I will strictly follow: Observe -> Hypothesize -> Test -> Conclude. I will document every step and attempt to falsify my own conclusions to avoid confirmation bias.

## II. Game Systems & Mechanics
### Tile Mechanics
*   **Traversable:** `FLOOR`, `GRASS`, `TALL_GRASS`, `LONG_GRASS`, `RAILING`, `PIPE_HORIZONTAL`, `PIPE_VERTICAL`, `ARROW_TILE_UP`, `ARROW_TILE_DOWN`, `ARROW_TILE_LEFT`, `ARROW_TILE_RIGHT`
*   **Impassable:** `BIRD`, `BOOKSHELF`, `BUOY`, `CHAIR`, `CHIMNEY`, `COMPUTER`, `COUNTER`, `FENCE`, `FLOWER`, `INCENSE_BURNER`, `LINK_CABLE`, `LINK_RECEPTIONIST`, `MART_SHELF`, `PC`, `PERSIAN_STATUE_L`, `PERSIAN_STATUE_R`, `PILLAR`, `PRINTER`, `RADIO`, `ROCK`, `ROOF`, `SIGN`, `TABLE`, `TOWN_MAP`, `TRADE_MACHINE`, `TREE_TOP`, `TV`, `VOID`, `WALL`, `WATER_EDGE_UP`, `WATER_EDGE_DOWN`, `WATER_EDGE_LEFT`, `WATER_EDGE_RIGHT`, `WEIRD_TREE`, `WINDOW`
*   **Warps:** `CAVE`, `DOOR`, `LADDER` (can be one-way or two-way, must be tested), `STAIRCASE`, `WARP_PANEL` (One-way)
*   **Conditional/One-Way:** `BREAKABLE_ROCK` (Requires Rock Smash), `CUT_TREE` (Requires HM01 Cut), `FLOOR_UP_WALL` (One-way ledge), `LEDGE_HOP_DOWN`, `LEDGE_HOP_DOWN/RIGHT`, `LEDGE_HOP_LEFT`, `PIT` (One-way down), `WARP_CARPET_DOWN` (Requires pressing 'Down' button while standing on tile)
*   **Confirmed Obstacles:** Defeated trainer sprites are impassable objects.

### Menu Mechanics
*   **Inventory Bug (Confirmed):** The inventory is permanently locked. 'TOSS', 'GIVE', 'USE' (in battle), and 'SELL' commands are all non-functional for freeing inventory space. No new items can be picked up.

## III. Current Puzzle: Team Rocket Hideout
*   **Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Main Obstacle:** Navigating the multi-floor hideout and finding the trigger to progress.

### Current Hypothesis
*   **H79 (Current):** The Fisher blocking the Mahogany Town Gym has moved now that the Lake of Rage event is complete.

### Archived Hypotheses (Solved/Falsified)
*   **H78 (Falsified):** There is a hidden switch on one of the `WALL` tiles of the main computer console at (20,10) through (25,10) on B3F. (Result: A systematic test of every console wall tile yielded no results.)

### Confirmed Facts & Discoveries
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.
*   **B2F/B3F Layout:** Both B2F and B3F are split into two disconnected eastern and western sections. This has been confirmed by the `master_navigator` tool.
*   **Path Forward:** A hidden one-way warp tile at coordinate (27, 2) on B2F warps the player to B3F at (27, 2), providing access to the eastern section of B3F.
*   **Locked Door:** The final objective is likely behind the locked door on B3F at coordinates (10, 9) and (11, 9).
*   **Room is Sealed:** The Rocket Grunt at (24, 14) is impassable, blocking the ladder and trapping me in this section of B3F.

### Archived Hypotheses (Solved/Falsified)
*   **H77 (Falsified):** The Rocket Grunt at (24, 14) is a scripted event trigger. Interacting with him is the necessary step to progress. (Result: Repeated interactions yielded no new results.)
*   **H76 (Falsified):** The true path forward is on B2F West, accessed via the ladder at (3, 14) on B1F, which requires re-entering the hideout. (Result: This was based on the incorrect assumption that the current room was a dead end.)
*   **H75 (Falsified):** Interacting with the main computer console is the trigger to disable the radio signal. (Result: Falsified after 3 systematic interaction attempts at different locations on the console yielded no results.)

## III. Current Puzzle: Team Rocket Hideout
*   **Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Main Obstacle:** Navigating the multi-floor hideout and finding the trigger to progress.

### Current Hypothesis
*   **H79 (Current):** The Fisher blocking the Mahogany Town Gym has moved now that the Lake of Rage event is complete.

### Archived Hypotheses (Solved/Falsified)
*   **H78 (Falsified):** There is a hidden switch on one of the `WALL` tiles of the main computer console at (20,10) through (25,10) on B3F. (Result: A systematic test of every console wall tile yielded no results.)

### Confirmed Facts & Discoveries
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.
*   **B2F/B3F Layout:** Both B2F and B3F are split into two disconnected eastern and western sections. This has been confirmed by the `master_navigator` tool.
*   **Path Forward:** A hidden one-way warp tile at coordinate (27, 2) on B2F warps the player to B3F at (27, 2), providing access to the eastern section of B3F.
*   **Locked Door:** The final objective is likely behind the locked door on B3F at coordinates (10, 9) and (11, 9).
*   **Room is Sealed:** The Rocket Grunt at (24, 14) is impassable, blocking the ladder and trapping me in this section of B3F.

### Archived Hypotheses (Solved/Falsified)
*   **H77 (Falsified):** The Rocket Grunt at (24, 14) is a scripted event trigger. Interacting with him is the necessary step to progress. (Result: Repeated interactions yielded no new results.)
*   **H76 (Falsified):** The true path forward is on B2F West, accessed via the ladder at (3, 14) on B1F, which requires re-entering the hideout. (Result: This was based on the incorrect assumption that the current room was a dead end.)
*   **H75 (Falsified):** Interacting with the main computer console is the trigger to disable the radio signal. (Result: Falsified after 3 systematic interaction attempts at different locations on the console yielded no results.)