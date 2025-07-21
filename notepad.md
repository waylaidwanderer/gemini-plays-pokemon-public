# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### A. Tile Traversal Rules
*   **Verified Impassable:** WALL, COUNTER, MART_SHELF, PC, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID, RADIO, INCENSE_BURNER, BOOKSHELF.
*   **Verified Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA (with Surf).
*   **Verified Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN/LEFT/RIGHT, WARP_PANEL.
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL.
*   **One-Way:** PIT (fall), LEDGE_HOP_RIGHT/LEFT/DOWN, FLOOR_UP_WALL (one-way 'up' ledge).
*   **Special Movement:** 
    *   ICE: Slides the player in a cardinal direction until an obstacle is hit.
    *   FLOOR (on Ice Maps): Acts as a safe stopping point. Player can stand on a FLOOR tile and choose their next slide direction without being forced into movement.
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

### C. Mahogany Gym Ice Puzzle Analysis (Final)
*   **Problem:** Navigate the Mahogany Gym ice puzzle to reach the Gym Leader, Pryce.
*   **Tool Development Log (Final Conclusion):** The `ice_puzzle_solver` is fundamentally unreliable for this puzzle. Its logic is sound, but its data source (`map_xml_string`) only includes on-screen objects. It is blind to off-screen defeated trainers who act as permanent obstacles, leading it to calculate impossible paths or fail to find valid ones. The correct strategic decision is to abandon the tool for this specific puzzle and proceed with a verified manual path.
*   **Correct Manual Path:** Based on a manual trace that accounts for all defeated trainers as obstacles, the following path is confirmed to be correct:
    1.  Start at entrance floor area (e.g., (4, 15)).
    2.  Slide Up from (4, 15) -> land on (4, 14).
    3.  Walk Right to (5, 14).
    4.  Slide Up from (5, 14) -> land on (5, 10).
    5.  Slide Left from (5, 10) -> land on (2, 10).
    6.  Slide Up from (2, 10) -> stopped by defeated trainer at (2, 4), land on ice at (2, 5).
    7.  Slide Right from (2, 5) -> land on (6, 5).
    8.  Slide Down from (6, 5) -> land on (6, 13).
    9.  Slide Left from (6, 13) -> land on (3, 13).
    10. Slide Up from (3, 13) -> land on (3, 4).
    11. Slide Right from (3, 4) -> land on (5, 4), in front of Pryce.

## III. Battle Intel

### A. Type Effectiveness Chart (Verified)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective