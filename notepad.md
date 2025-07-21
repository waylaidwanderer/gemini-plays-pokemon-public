# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### A. Tile Traversal Rules
*   **Verified Impassable:** WALL, COUNTER, MART_SHELF, PC, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID, RADIO, INCENSE_BURNER, BOOKSHELF.
*   **Verified Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA (with Surf).
*   **Verified Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN/LEFT/RIGHT, WARP_PANEL.
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL.
*   **One-Way:** PIT (fall), LEDGE_HOP_RIGHT/LEFT/DOWN, FLOOR_UP_WALL (one-way 'up' ledge).
*   **Special Movement:** ICE (slide in one direction until an obstacle is hit).
*   **Untested:** COMPUTER, BED, CABINET, SINK, PLANT, unknown, and any tile type with `unknown` in its name. My protocol is to test these by attempting to walk into them from all four directions when first encountered.

### B. System Bugs & Glitches (Verified)
*   **Item Management:** 'DEPOSIT ITEM' & 'TOSS ITEM' (from PC & PACK) are bugged. 'FLY' HM is bugged. Using one item from a stack does not free an inventory slot.
*   **Giving Items:** Giving an item to a Pokémon does not free an inventory slot.

### C. Item Usage Rules
*   **Status Heal:** Cannot be used on a Pokémon not afflicted with that status.
*   **HP Restore:** Can be used on any damaged Pokémon, but not one at full HP.

## II. World Knowledge & Puzzles

### A. Solved Puzzles & Key Discoveries
*   **Red Gyarados Event (Lake of Rage):** Defeated the red Gyarados and obtained the RED SCALE.
*   **Cianwood City Stuck Spot:** Resolved by triggering back-to-back phone calls (Mom, then Liz) on tile (10, 28).
*   **Ilex Forest Shrine:** A Lass in the Route 34 Gate mentioned a shrine honoring a grass-type protector.
*   **TM12 (Sweet Scent):** Given by Teacher in Route 34 Ilex Forest Gate.
*   **Team Rocket Base Passwords:** SLOWPOKETAIL, HAIL GIOVANNI.
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is opened by the Secret Switch at (19, 11).
*   **Team Rocket Base B2F Layout:** Northern and southern corridors are separate. Access to the north must be from a different warp on B1F.
*   **Mahogany Town:** No shop exists. The mart is a Team Rocket front, and the Poké Center has no vendor. Travel to another city is required for inventory management.
*   **Mahogany Town Story Lock:** FLY is disabled, forcing progression towards the Lake of Rage.
*   **Mahogany Mart Secret Ladder:** The warp to the hideout is not triggered by interaction, but by stepping onto the ladder tile at (7, 3).
*   **Team Rocket B1F Maze (Disguised Path):** The solution, hinted at by the ROCKET Grunt's dialogue ('Collect your courage and walk!'), is not a path through a wall, but a FLOOR tile at (3, 5) disguised to look like a wall. This creates a secret northern passage in the western maze area.

### B. Falsified Hypotheses & Dead Ends
*   **Mahogany Gym Blocker:** The Fisher did NOT move after the Lake of Rage event. Hypothesis that Lance's presence was the trigger is false.
*   **Secret Potion Location:** The hint for Cianwood City was incorrect; the Pharmacist runs a regular shop.
*   **Team Rocket B2F Southern Corridor:** The ROCKET at (21, 14) has non-progressive dialogue, confirming this path is a dead end.
*   **Team Rocket B1F Eastern Corridor:** The secret passage at (10, 9) and the entire eastern corridor lead to a dead-end loop.
*   **Team Rocket B1F Switch Function:** The switch at (19, 11) is not a toggle for the invisible maze. Interacting with the ROCKET at (2, 4) produces the same result regardless of the switch's on/off state.
*   **Team Rocket B1F Maze (Simple Pitfall):** Systematically exploring every floor tile in the western maze area revealed no pitfalls or warps other than the known dead-end ladder. Hypothesis that a simple pitfall was the solution is false.

### C. Active Hypotheses & Tests
*   **Mahogany Gym Blocker:** **Hypothesis:** Progress is gated by defeating Team Rocket in their hideout.
*   **Team Rocket Hideout Progression:** **FALSIFIED HYPOTHESIS:** The eastern corridor is the exit. **REASON:** Pathing attempts failed repeatedly, leading to dead ends. **NEW HYPOTHESIS (from strategy_advisor):** The correct exit is one of the unexplored warps on the western side of the map at (3, 2) or (3, 6).
*   **Mahogany Gym Puzzle Analysis:**
    *   **Problem:** Navigate the Mahogany Gym ice puzzle to reach the Gym Leader, Pryce.
    *   **Initial Observation:** The gym consists of `ICE` tiles that cause sliding until an obstacle is hit, and `FLOOR` tiles that stop movement. Obstacles include `WALL` tiles and NPCs.
    *   **Hypothesis 1 (FALSIFIED):** A simple slide-simulation tool can solve the puzzle. **REASON:** The tool failed multiple times, indicating its model of the puzzle is too simple.
    *   **Hypothesis 2 (FALSIFIED):** A direct path exists to the Gym Leader or the BEAUTY trainer. **REASON:** The `ice_puzzle_solver` tool, which models the puzzle as a graph of FLOOR tiles, consistently returns 'No path found' for these destinations. This indicates they are on a separate, unreachable 'island' of floor tiles from my current position.
    *   **Hypothesis 3 (NEW):** To reach the target island, I must find a specific starting `FLOOR` tile on my current island that has a slide-path connecting to the target island.
    *   **Test Plan 3 (Multi-step):**
        1.  **Identify Reachable Nodes:** Use `run_code` to execute a script that performs a BFS from the player's current position to find all reachable `FLOOR` tiles.
        2.  **Systematic Pathfinding:** For each reachable `FLOOR` tile identified in Step 1, use the `ice_puzzle_solver` to attempt to find a path to each of the target `FLOOR` tiles: (3, 4), (5, 4), and (4, 7).
        3.  **Execution:** Execute the first valid path found by the solver.
    *   **Conclusion 3:** (Pending test results).

## III. Battle Intel

### A. Type Effectiveness Chart (Verified)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Observed Trainer/Gym Leader Movesets
*   **Youngster Joey:** RATTATA (Tackle, Tail Whip)
*   **Falkner:** PIDGEY (Tackle), PIDGEOTTO (Tackle, Gust)
*   **Bugsy:** METAPOD (Harden), KAKUNA (Harden), SCYTHER (Fury Cutter, Leer)
*   **Whitney:** CLEFAIRY (Doubleslap, Encore), MILTANK (Rollout, Stomp, Attract)
*   **Morty:** GASTLY (Lick, Spite), HAUNTER (Curse, Hypnosis, Dream Eater), GENGAR (Shadow Ball, Hypnosis, Dream Eater)
*   **Jasmine:** MAGNEMITE (Thunderbolt, Thunder Wave, Supersonic), STEELIX (Iron Tail, Screech, Rock Throw)
*   **Chuck:** PRIMEAPE (Leer, Rage, Karate Chop), POLIWRATH (Hypnosis, Mind Reader, Dynamicpunch)