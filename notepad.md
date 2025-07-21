# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### A. Tile Traversal Rules
*   **Verified Impassable:** WALL, COUNTER, MART_SHELF, PC, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID, RADIO, INCENSE_BURNER, BOOKSHELF.
*   **Verified Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA (with Surf).
*   **Verified Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN/LEFT/RIGHT, WARP_PANEL.
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL.
*   **One-Way:** PIT (fall), LEDGE_HOP_RIGHT/LEFT/DOWN, FLOOR_UP_WALL (one-way 'up' ledge).
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
*   **Special Movement:** ICE (slide in one direction until an obstacle is hit).
*   **Mahogany Gym Puzzle:** **Hypothesis:** Defeating all trainers is required to reach Pryce. **Alternative Hypothesis:** The puzzle is purely navigational, and a correct sequence of slides can bypass trainers. **Test:** After defeating Boarder Douglas, the path is still complex. My new `ice_puzzle_solver` tool will find the optimal path to Pryce at (5, 4). The remaining BEAUTY at (4, 6) might be an optional battle.