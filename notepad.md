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
*   **Confirmed Obstacles:** Defeated trainer sprites are impassable objects.

### Menu Mechanics
*   **Inventory Bug (Confirmed):** The inventory is permanently locked. 'TOSS', 'GIVE', 'USE' (in battle), and 'SELL' commands are all non-functional for freeing inventory space. No new items can be picked up.

## III. Current Puzzle: Team Rocket Hideout

*   **Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Main Obstacle:** Navigating the multi-floor hideout.

### Confirmed Facts & Discoveries
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.
*   **B2F/B3F Layout:** Both B2F and B3F are split into two disconnected eastern and western sections.
*   **Path Forward:** A hidden one-way warp tile at coordinate (27, 2) on B2F warps the player to B3F at (27, 2), providing access to the eastern section of B3F.

### Current Hypothesis
*   **H56 (Current):** The ladder at (27, 14) on B3F leads to a new, unexplored area, which contains the true path to the transmitter. This is the only remaining unexplored warp in the entire hideout.

## IV. Future Testing & Ideas
*   **Agent Idea: `code_debugger`:** An agent that takes a Python script and an error message as input, and suggests a fix or the location of the bug. This could streamline tool debugging.
*   **Alternative Hypothesis (Team Rocket Hideout):** If the ladder at (27, 14) is a dead end, there might be another hidden warp tile on B3F. The tile behind the impassable item at (17, 2), specifically (16, 2), is a candidate, as it mirrors the layout of the warp that brought me here.

## V. Archived Hypotheses (Solved/Falsified)
*   **B2F Locked Door Interaction:** Interacting with the locked door at (14, 12) on B2F does not prompt for a password.
*   **Lance's Location:** Lance is not on B3F or B2F waiting to open any doors.
*   **B1F Maze:** The central arrow-tile maze and the invisible floor maze on B1F are dead ends.
*   **B2F/B3F Connectivity:** The eastern and western sections of B2F and B3F are not physically connected.
*   **Bookshelf Puzzle:** Interacting with the 'Oath' bookshelves does not seem to trigger any immediate event or unlock any paths.
*   **H48:** Speaking to Lance on B3F after obtaining both passwords is the required trigger to open the locked door on B2F. (Result: Lance is no longer on B3F.)
*   **H47:** With the arrow tiles on B1F permanently disabled, a new path is now accessible within the central maze area that leads to the eastern section of B2F. (Result: The central maze area is a series of dead ends.)
*   **H46:** The switch at (19, 11) on B1F can be toggled back on. (Result: It's a one-time switch.)
*   **H45:** The western corridor of B2F, accessed via the ladder at (3, 14), contains a path to the eastern section of the floor. (Result: It's a dead end.)
*   **H41:** The eastern corridor of B1F, accessed via the warp panel at (5, 15), contains a path to the boss. (Result: It's a one-way exit.)
*   **H39:** The invisible floor maze near the entrance contains the primary path forward. (Result: It's a series of dead ends or loops.)
*   **H49:** Lance has moved to the locked door on B2F and is waiting for me there. Interacting with him in front of the door will trigger the event. (Result: Falsified. Lance is not on B2F. Pathfinding confirms B2F is a closed loop, inaccessible from the eastern B3F ladder.)
*   **H52:** There is a hidden passage or switch in the outer corridor of B2F. (Result: Falsified. Interacting with every wall tile in the eastern loop yielded no results.)
*   **H55:** The eastern and western sections of B2F are connected. (Result: Falsified. My `master_navigator` tool confirmed no path exists between (27, 2) and (5, 13).)