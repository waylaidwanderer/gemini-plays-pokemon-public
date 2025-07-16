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

## III. Team Rocket Hideout Puzzle Log

*   **Objective:** Find the Team Rocket Boss and disable the radio signal.
*   **Main Obstacle:** A password-locked door on B2F at (14, 12) is blocking progress.

### Confirmed Facts & Discoveries
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.
*   **B2F Locked Door Interaction:** Interacting with the locked door at (14, 12) twice only yields the message "It needs a password to open." It does not prompt for input.
*   **B3F Layout:** B3F is split into two disconnected sections. The western section containing the boss and Lance is inaccessible from the eastern ladder.

### Falsified Hypotheses
*   **H48:** Speaking to Lance on B3F after obtaining both passwords is the required trigger to open the locked door on B2F. (Result: Lance is no longer on B3F.)
*   **H47:** With the arrow tiles on B1F permanently disabled, a new path is now accessible within the central maze area that leads to the eastern section of B2F. (Result: The central maze area is a series of dead ends.)
*   **H46:** The switch at (19, 11) on B1F can be toggled back on. (Result: It's a one-time switch.)
*   **H45:** The western corridor of B2F, accessed via the ladder at (3, 14), contains a path to the eastern section of the floor. (Result: It's a dead end.)
*   **H41:** The eastern corridor of B1F, accessed via the warp panel at (5, 15), contains a path to the boss. (Result: It's a one-way exit.)
*   **H39:** The invisible floor maze near the entrance contains the primary path forward. (Result: It's a series of dead ends or loops.)

*   **H49:** Lance has moved to the locked door on B2F and is waiting for me there. Interacting with him in front of the door will trigger the event. (Result: Falsified. Lance is not on B2F. Pathfinding confirms B2F is a closed loop, inaccessible from the eastern B3F ladder.)

### Current Hypothesis
*   **H52:** There is a hidden passage or switch in the outer corridor of B2F that provides access to the central area.
*   **Test:** Systematically interact with every wall tile in the outer B2F corridor.

## IV. Future Testing & Verification Notes
*   **Ledge Verification:** I must explicitly try to move *up* a ledge at the next opportunity to scientifically confirm this is impossible.
*   **Object Traversal:** I must test if it's possible to walk on object tiles like `BOOKSHELF` when they are not blocked by walls to confirm they are universally impassable.