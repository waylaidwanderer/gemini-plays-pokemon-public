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

## III. Team Rocket Hideout Puzzle

### Hypothesis Log
*   **H1-H7 (Disproven):** Various theories about hidden passages and alternate ladders in the hideout.
*   **H8-H10 (Disproven):** Various theories about a hidden switch in the Mahogany Mart (blue tile, radio, ladder destination change).
*   **H11 (Disproven):** The Pharmacist moves after being exposed. **Result:** He does not move.
*   **H12 (Disproven):** The Incense Burner or Bookshelf become switches after key events. **Result:** No effect.
*   **H13 (Disproven):** There is a secret passage in the wall at Y=12 on B2F. **Result:** Systematically testing the wall from x=1 to x=5 by walking into it and pressing 'A' yielded no results. The wall is solid.
*   **H14 (Active):** There is a missed switch or path on B1F that opens the way to the central maze on B2F.

## IV. Tool Status
*   **Trap Discovered:** Stepping on tile (2, 7) in Team Rocket Hideout B1F (Map ID 3_49) triggers a warp to a corrupted glitch map.
*   **Warp Panel Mechanics:** The warp panel at (5, 15) on B1F is a one-way teleporter to (25, 2). The tile at (25, 2) is only an arrival point.
*   **Team Rocket Hideout B3F Layout:** Confirmed that B3F is split into two disconnected sections. The eastern section (accessed from the B2F ladder at (27, 14)) is separate from the western section containing the boss's door. The western section containing the boss's door is currently inaccessible. The ladder at (3, 14) on B2F leads up to B1F, not down to the western part of B3F.
*   **H15 (Disproven):** Interacting with the scientist at (18, 12) from a different angle (below) will make him move. **Result:** He repeats the same dialogue and does not move.
*   **H16 (Active):** The path forward involves using the warp panel at (5, 15), as hinted by the scientist.
*   **H16 (Disproven):** The path forward involves using the warp panel at (5, 15). **Result:** The warp panel leads to an isolated exit area, confirming the scientist's dialogue that it's a way back to the entrance, not a path forward.
*   **H17 (Confirmed):** Flipping the switch at (19, 11) on B1F opens the path into the central maze on B2F. This maze leads to the ladder at (27, 14), which goes down to the eastern section of B3F.
*   **H18 (Active):** The password prompt is not triggered by the door itself, but by interacting with the two ROCKET grunts guarding the boss's room on B3F.
*   **H19 (Confirmed):** Leaving, re-entering, or triggering new dialogue from the scientist at (18, 12) does not make him move. The path to the switch is permanently blocked.
*   **H21 (Active):** The warp panel at (5, 15) is the correct path forward, despite the scientist's claim it's an exit.
*   **H18 (Blocked):** The password prompt is likely triggered by the grunts on B3F, but the western section of B3F containing the boss's room is inaccessible from the eastern section. This path is a dead end.
*   **H20 (Active):** The western section of B3F must be accessed via a different, undiscovered path, likely originating from B1F or B2F.