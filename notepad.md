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
*   **Main Obstacle:** Navigating the multi-floor hideout.

### Confirmed Facts & Discoveries
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.
*   **B2F/B3F Layout:** Both B2F and B3F are split into two disconnected eastern and western sections. This has been confirmed by the `master_navigator` tool.
*   **Path Forward:** A hidden one-way warp tile at coordinate (27, 2) on B2F warps the player to B3F at (27, 2), providing access to the eastern section of B3F.
*   **Locked Door:** The final objective is likely behind the locked door on B3F at coordinates (10, 9) and (11, 9).

### Current Hypothesis
*   **H72 (Current):** There is a hidden switch or warp tile in the eastern section of B3F that provides a path to the western section. I am currently performing a systematic search of all wall tiles to test this.

## IV. Future Testing & Ideas
*   **Agent Idea: `hypothesis_generator`:** An agent that takes the current puzzle state (map description, failed hypotheses from notepad) and suggests new, testable hypotheses. This could formalize my brainstorming process.
*   **Agent Idea: `code_debugger`:** An agent that takes a Python script and an error message as input, and suggests a fix or the location of the bug. This could streamline tool debugging.
*   **Tool Idea: `systematic_searcher`:** A tool that takes a set of coordinates and an action (e.g., 'interact', 'step on') and automatically executes the search pattern. This would be much faster than manual searching.
*   **Agent Idea: `log_summarizer`:** An agent that could periodically review turn history to extract key events and help identify patterns or missed clues.

## V. Archived Hypotheses (Solved/Falsified)
*   **H71 (Falsified):** Leaving and re-entering this area via the ladder at (27, 2) will change the map state, opening a new path. (Result: Falsified by `master_navigator`, which confirmed no path exists after re-entry.)
*   **H70 (Falsified):** One of the floor tiles in the isolated eastern corridor of B2F is a hidden spin or arrow tile. (Result: Falsified. A systematic search of every floor tile in the corridor yielded no results.)
*   **H69 (Falsified):** Re-entering this area via the ladder at (27, 2) will change the map state, opening a path. (Result: Falsified. A systematic search of all walls in the resulting corridor revealed no hidden switches.)
*   **H68 (Falsified):** The ladder at (27, 2) is a two-way warp. Ascending from B3F at (27, 2) will lead to a new, accessible section of B2F. (Result: Falsified. A systematic search of all walls in the resulting corridor revealed no hidden switches.)
*   **H67 (Falsified):** There is a missed interaction or hidden switch in the eastern section of B2F. (Result: Falsified by `master_navigator` tool, which confirmed no path exists to the transmitter from the eastern section.)
*   **H65 (Falsified):** A hidden arrow tile maze on B3F is the key to crossing between the disconnected eastern and western sections. (Result: Falsified by `master_navigator` tool, which confirmed no path exists between the eastern and western sections of this floor.)
*   **H63 (Falsified):** A path connecting the disconnected sections of B2F exists via the floor below, B3F. (Result: Falsified by `master_navigator` tool, which confirmed no path exists between the eastern and western sections of this floor.)
*   **H62 (Falsified):** A 'spin tile maze' connects the eastern and western sections of B2F. (Result: Falsified by `puzzle_master` agent's suggestion being immediately disproven by the `master_navigator` tool, which confirmed no path exists between the two sections on this floor.)
*   **H60 (Falsified):** Lance has moved to the locked door on B2F at coordinates (14, 12) and is waiting for me there. (Result: Falsified. Lance was not at the door, and it did not open.)
*   **H59 (Falsified):** There is a hidden trigger on a wall or floor tile in the western chamber of B3F that opens the path to the locked door. (Result: Falsified. A systematic search of all walls and objects in the chamber yielded no results, and my `master_navigator` confirmed no path exists.)
*   **H58 (Falsified):** The bookshelves in the western chamber of B3F contain a hidden switch. (Result: Falsified. Interacting with all accessible bookshelves yielded only flavor text.)
*   **H57 (Falsified):** A path exists from my current location to the tile in front of the locked door at (10, 10). (Result: Falsified. The `master_navigator` tool confirmed no path exists, indicating the western section of B3F is also split.)
*   **H56 (Falsified):** The ladder at (27, 14) on B3F leads to the true path to the transmitter. (Result: Falsified. Leads to a dead-end section of B2F.)
*   **H55 (Falsified):** The eastern and western sections of B2F are connected. (Result: Falsified. My `master_navigator` tool confirmed no path exists between (27, 2) and (5, 13).)
*   **H52 (Falsified):** There is a hidden passage or switch in the outer corridor of B2F. (Result: Falsified. Interacting with every wall tile in the eastern loop yielded no results.)
*   **H49 (Falsified):** Lance has moved to the locked door on B2F and is waiting for me there. (Result: Falsified. Lance is not on B2F.)
*   **H48 (Falsified):** Speaking to Lance on B3F after obtaining both passwords is the required trigger to open the locked door on B2F. (Result: Falsified. Lance is no longer on B3F.)
*   **H47 (Falsified):** With the arrow tiles on B1F permanently disabled, a new path is now accessible within the central maze area. (Result: Falsified. The central maze area is a series of dead ends.)
*   **H46 (Falsified):** The switch at (19, 11) on B1F can be toggled back on. (Result: Falsified. It's a one-time switch.)
*   **H45 (Falsified):** The western corridor of B2F, accessed via the ladder at (3, 14), contains a path to the eastern section of the floor. (Result: Falsified. It's a dead end.)
*   **H41 (Falsified):** The eastern corridor of B1F, accessed via the warp panel at (5, 15), contains a path to the boss. (Result: Falsified. It's a one-way exit.)
*   **H39 (Falsified):** The invisible floor maze near the entrance contains the primary path forward. (Result: Falsified. It's a series of dead ends or loops.)
*   **B2F Locked Door Interaction:** Interacting with the locked door at (14, 12) on B2F does not prompt for a password.
*   **Lance's Location:** Lance is not on B3F or B2F waiting to open any doors.
*   **B1F Maze:** The central arrow-tile maze and the invisible floor maze on B1F are dead ends.
*   **B2F/B3F Connectivity:** The eastern and western sections of B2F and B3F are not physically connected.
*   **Bookshelf Puzzle:** Interacting with the 'Oath' bookshelves does not seem to trigger any immediate event or unlock any paths.