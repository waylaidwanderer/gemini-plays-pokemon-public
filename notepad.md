# Gem's Pokémon Crystal Notepad

## I. Game State & Objectives

### A. Primary Questline
*   **Mahogany Town Gym:** Obtain the 6th Gym Badge.
*   **Team Rocket Hideout:** Find the boss and use the passwords to disrupt their radio signal operation. The entrance is a secret stairway in the Mahogany Mart.
*   **RED SCALE Investigation:** Mr. Pokémon is the primary person of interest.

### B. Active Side Quests
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.
*   **Rematch List:** Picnicker Liz (Route 32), Youngster Joey (Route 30), Camper Todd (Route 34).

### C. Known Blockers & Story Gates
*   **Mahogany Town Gym:** A Fisher blocks the entrance at (6, 14).
*   **Schoolboy Alan (Route 36):** In a dialogue loop, likely a story-gated event.

## II. Game Mechanics

### A. Tile Traversal Rules
*   **Verified Impassable:** WALL, COUNTER, MART_SHELF, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID.
*   **Verified Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA, unknown (TeamRocketBaseB3F), unknown (Route42).
*   **Verified Warps:** DOOR, CAVE, LADDER, WARP_PANEL, WARP_CARPET_DOWN/LEFT/RIGHT.
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL.
*   **One-Way:** PIT (fall), LEDGE_HOP_RIGHT/LEFT/DOWN, FLOOR_UP_WALL (one-way 'up' ledge).
*   **Untested:** RADIO, INCENSE_BURNER, unknown (TeamRocketBaseB2F), unknown (MahoganyPokecenter1F), unknown (LakeOfRage), COMPUTER, BED, CABINET, SINK, PLANT, unknown (MountMortarB1F).

### B. System Bugs & Glitches (Verified)
*   **Item Management:** 'DEPOSIT ITEM' & 'TOSS ITEM' (from PC & PACK) are bugged. 'FLY' HM is bugged. Using one item from a stack does not free an inventory slot.
*   **Giving Items:** Giving an item to a Pokémon does not free an inventory slot.

### C. Item Usage Rules
*   **Status Heal:** Cannot be used on a Pokémon not afflicted with that status.
*   **HP Restore:** Can be used on any damaged Pokémon, but not one at full HP.

## III. World Knowledge

### A. Solved Puzzles & Key Discoveries
*   **Cianwood City Stuck Spot:** Resolved by triggering back-to-back phone calls (Mom, then Liz) on tile (10, 28).
*   **Ilex Forest Shrine:** A Lass in the Route 34 Gate mentioned a shrine honoring a grass-type protector.
*   **TM12 (Sweet Scent):** Given by Teacher in Route 34 Ilex Forest Gate.
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is opened by the Secret Switch at (19, 11).
*   **Team Rocket Base B1F Hidden Revive (Unobtainable):** Item at (3, 11) is currently unobtainable, likely story-gated.
*   **Team Rocket Base B2F Layout:** Northern and southern corridors are separate. Access to the north must be from a different warp on B1F.

### B. Falsified Hypotheses & Dead Ends
*   **Mahogany Gym Blocker:** The Fisher did NOT move after the Lake of Rage event. Hypothesis that Lance's presence was the trigger is false.
*   **Secret Potion Location:** The hint for Cianwood City was incorrect; the Pharmacist runs a regular shop.
*   **Team Rocket B2F Southern Corridor:** The ROCKET at (21, 14) has non-progressive dialogue, confirming this path is a dead end.

### C. Passwords & Keys
*   **Team Rocket Hideout (Boss's Room):** SLOWPOKETAIL (Confirmed), HAIL GIOVANNI (Confirmed), RATICATE TAIL (Unconfirmed).

## IV. Battle Intel

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

## V. Automation & Tool Development

### A. Tool Refinement Log & Status
*   **Pathfinder v3 Tool (Under Active Debugging):** Critical bug identified where it fails to calculate paths involving one-way tiles (ledges). This is the highest priority bug to fix.
*   **Contingency:** While `pathfinder_v3` is being fixed, use `manual_path_planner` for simple routes and `maze_solver` for complex mazes.

### B. Agent Development Log & Status
*   **Tool Debugger Agent (Under Review):** Has repeatedly failed to identify the root cause of the pathfinder's bugs. Requires review and potential redesign.

## VI. Open Hypotheses & Tests

### A. Mahogany Gym Blocker
*   **Hypothesis:** Progress is gated by defeating Team Rocket in their hideout.

### B. Mt. Mortar Invisible Barrier
*   **Hypothesis:** An invisible barrier blocks the northern one-way ledge on Mt. Mortar B1F.
*   **Falsification Test:** Find an alternate route to the northern area and attempt to walk south over the same ledge.

### C. Route 42 Blockage
*   **Hypothesis:** The only path from Mahogany Town to Ecruteak City is through Mt. Mortar.
*   **Falsification Test:** Return to Route 42 after clearing inventory. Check if the Super Nerd at (47, 8) has moved or if an alternate path exists.

### D. Team Rocket B1F Maze Progression
*   **Hypothesis:** The 'traps' are one-way pitfall warps.
*   **Current Plan:** Continue systematic exploration south and east from (1, 14) to find a safe path to the ladder at (3, 14).

### E. Team Rocket Boss Location
*   **Hypothesis:** The boss is behind the locked door at (10, 9) on B3F.
*   **Falsification Test:** If no password prompt or interaction is possible at the door, the path is elsewhere. Next step: full re-exploration of B1F/B2F.

### F. Pathfinder v2 Destination Tile Bug
*   **Hypothesis:** The tile at (42, 8) on Route 42 is impassable from the water due to a hidden property.
*   **Falsification Test:** Attempt to walk onto the tile from an adjacent land tile. If successful, the bug is in the pathfinder's logic.

## VII. Side Quests & Rematches
*   **Picnicker Liz (Route 34):** Wants a rematch on Route 32.
*   **Item Usage (Status Heal):** Status-healing items (like PARLYZ HEAL) cannot be used on a Pokémon that is not afflicted with that status. The game will display an 'It won't have any effect.' message and the item will not be consumed.
*   **Item Usage (HP Restore):** HP-restoring items (like POTION) can be used on a Pokémon that has taken any amount of damage, but not one at full HP.
*   **Youngster Joey (Route 30):** Wants a rematch.
*   **Untested:** ... unknown (EcruteakMart)
*   **Camper Todd (Route 36):** Wants a rematch on Route 34.

### F. Pathfinder v2 Destination Tile Bug
*   **Hypothesis:** The `pathfinder_v2` tool fails to path to (42, 8) because the tile has a hidden property that makes it impassable from the water, despite being a 'FLOOR' type.
*   **Falsification Test:** Once I reach the eastern shore, I will attempt to walk onto the tile at (42, 8) from an adjacent land tile like (42, 9) or (43, 8). If I can step on it, the hypothesis is false, and the bug is purely within the pathfinder's logic. If I cannot, the tile is indeed special.

### F. Team Rocket B2F Southern Corridor (Hypothesis Falsified)
*   **Result:** The ROCKET at (21, 14) did not request a password. His dialogue is a non-progressive loop, confirming this path is a dead end.
*   **Conclusion:** The southern corridor of B2F is a dead end. The path forward must be found by returning to B1F and finding a different route.