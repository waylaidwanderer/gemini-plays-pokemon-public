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
*   **Main Obstacle:** A password-locked door on B2F at (14, 12) is blocking progress.

### Confirmed Facts & Discoveries
*   **B1F Switch:** Flipping the switch at (19, 11) on B1F toggles the arrow tiles on and off. It is currently OFF.
*   **Passwords Found:** The two passwords are 'SLOWPOKETAIL' and 'RATICATE TAIL'.
*   **B1F Warp Panel:** The warp panel at (5, 15) is a one-way teleporter to (25, 2), leading to an isolated exit area via the Mahogany Mart.
*   **B2F Locked Door Interaction:** Interacting with the locked door at (14, 12) twice only yields the message "It needs a password to open." It does not prompt for input.
*   **B3F Layout:** B3F is split into two disconnected sections. The western section containing the boss and Lance is inaccessible from the eastern ladder.

### Hideout Progression Plan (v17 - B2F Exploration)
*   **Hypothesis (H45):** The western corridor of B2F, accessed via the ladder at (3, 14), is not a dead end and contains a path to the eastern section of the floor.
*   **Method:** Systematically explore all reachable unseen tiles in the western corridor of B2F, starting from my current position at (3, 13).

### Falsified Hypotheses
*   H41: The eastern corridor of B1F, accessed via the warp panel at (5, 15), contains a path to the boss. (Result: It's a one-way exit.)
*   H39: The invisible maze on B1F contains the primary path forward. (Result: It's a series of dead ends or loops.)
*   H34: Navigating the invisible floor maze and reaching the door does not automatically trigger a password prompt.
*   H35: The key to opening the door is not a direct interaction after learning the passwords. The transmitter area is also inaccessible from any known path on B2F.
*   H33: Disabling the arrow tiles on B1F will open a new path on B2F.
*   H37: The bookshelves at (20, 11) and (21, 11) are a hidden switch.
*   H38: Scientist Jed at (18, 12) only provided a hint about the warp panel being a trap, but no direct solution.

## IV. Future Testing & Verification Notes
*   **Ledge Verification:** I have assumed all `LEDGE_HOP_...` tiles are one-way based on observation. I must explicitly try to move *up* a ledge at the next opportunity to scientifically confirm this is impossible.
*   **Object Traversal:** I must test if it's possible to walk on object tiles like `BOOKSHELF` when they are not blocked by walls to confirm they are universally impassable.
*   **Defeated Trainers:** Defeated trainer sprites remain on the map and act as impassable objects. You cannot walk through them.