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

## III. World & Story

### A. Active Quests & Blockers
*   **Mahogany Town Gym Block:** A Fisher is blocking the gym entrance. Hypothesis: I must find and speak to Lance at the Lake of Rage to progress the story.
*   **Team Rocket Hideout:** Find the boss and use the passwords to disrupt their radio signal operation. The entrance is a secret stairway in the Mahogany Mart, revealed by interacting with the Pharmacist.
*   **RED SCALE Investigation:** Mr. Pokémon is the primary person of interest.
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.

### B. Passwords & Keys
*   **Team Rocket Hideout (Boss's Room):
    1. SLOWPOKETAIL (Confirmed)
    2. RATICATE TAIL (Unconfirmed)
    3. HAIL GIOVANNI (Confirmed)

### C. Solved Puzzles & Key Discoveries
*   **Cianwood City Stuck Spot:** Was stuck on tile (10, 28). Solution was to trigger and complete the back-to-back phone calls (Mom, then Liz).
*   **Team Rocket Base B2F Layout:** The northern and southern corridors are separated by a wall and are not connected on this floor. Access to the northern section must be from a different warp on B1F.
*   **Secret Potion Location (Hypothesis Debunked):** The NPC hint pointing to Cianwood City was incorrect. The Pharmacist runs a regular shop and does NOT have the Secret Potion.
*   **Schoolboy Alan (Route 36):** My hypothesis that he had an item for me was incorrect. He is in a dialogue loop, which confirms he is a story-gated event.
*   **Ilex Forest Shrine:** A Lass in the Route 34 Gate mentioned a shrine honoring a grass-type protector of the forest.
*   **TM12 (Sweet Scent):** Given by Teacher in Route 34 Ilex Forest Gate. Attracts wild Pokémon.
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is a secret passage, not a locked door. It is opened by activating the Secret Switch at (19, 11).
*   **Team Rocket Base B1F Hidden Revive (Unobtainable):** The hidden Revive at (3, 11) is currently unobtainable. Systematic testing from all adjacent tiles and facings failed to trigger the item pickup, suggesting a story flag or other unmet condition is required.

## IV. Battle and Pokemon Information

### A. Type Effectiveness Chart (Verified in-game)
*   Water (Surf) vs. Water/Flying (Gyarados) -> Not Very Effective

### B. Observed Movesets
*   **Youngster Joey's RATTATA:** Tackle, Tail Whip
*   **Falkner's PIDGEY:** Tackle
*   **Falkner's PIDGEOTTO:** Tackle, Gust
*   **Bugsy's METAPOD:** Harden
*   **Bugsy's KAKUNA:** Harden
*   **Bugsy's SCYTHER:** Fury Cutter, Leer
*   **Whitney's CLEFAIRY:** Doubleslap, Encore
*   **Whitney's MILTANK:** Rollout, Stomp, Attract
*   **Morty's GASTLY:** Lick, Spite
*   **Morty's HAUNTER:** Curse, Hypnosis, Dream Eater
*   **Morty's GENGAR:** Shadow Ball, Hypnosis, Dream Eater
*   **Jasmine's MAGNEMITE:** Thunderbolt, Thunder Wave, Supersonic
*   **Jasmine's STEELIX:** Iron Tail, Screech, Rock Throw
*   **Chuck's PRIMEAPE:** Leer, Rage, Karate Chop
*   **Chuck's POLIWRATH:** Hypnosis, Mind Reader, Dynamicpunch

## V. Automation & Tool Development

### A. Tool Refinement Methodology
1.  **Immediate Action:** Any identified bug, flaw, or opportunity for improvement in a tool or agent MUST be addressed in the *immediate* turn. This task takes absolute precedence over any gameplay action.
2.  **Rigorous Testing:** After any modification, a tool must be subjected to a battery of tests to confirm the fix and check for unintended side effects. A single successful use case is not sufficient proof of correctness.
3.  **Iterative Refinement:** Assume that multiple, independent bugs may exist. If a tool fails after a fix, a new, unrelated bug is the most likely cause. The debugging process must be iterative and persistent.

### B. Pathfinder v3 Tool (Under Active Debugging)
*   **Status:** Critical bug identified. The tool fails to correctly calculate paths involving one-way tiles (ledges). This is the highest priority bug to fix.
*   **Action Plan:**
    1. Refine the `tool_debugger_agent` to improve its analytical capabilities.
    2. Use the improved agent to diagnose the root cause of the pathing failure.
    3. Implement the corrected script and perform rigorous testing.
*   **Contingency:** While `pathfinder_v3` is being fixed, navigation will be handled by the `manual_path_planner` tool for simple routes and the `maze_solver` tool for complex mazes. Manual pathing is a last resort.

### C. Tool Debugger Agent (Under Review)
*   **Status:** The agent has repeatedly failed to identify the root cause of the pathfinder's bugs. It requires review and potential redesign.

## VI. Hypotheses & Falsification Tests

### A. Mahogany Gym Blocker (Hypothesis Falsified)
*   **Result:** The Fisher blocking the Mahogany Town Gym at (6, 14) did NOT move after the Lake of Rage event was completed. The hypothesis is false.
*   **New Hypothesis:** Progress is likely gated by defeating Team Rocket in their hideout, which is accessible via the Mahogany Mart.

### B. Mt. Mortar Invisible Barrier
*   **Hypothesis:** An invisible barrier blocks the entire northern one-way ledge on Mt. Mortar B1F.
*   **Falsification Test:** If I find a way to the northern area from a different path and can successfully walk south over that same ledge, the hypothesis is false. The blockage is likely an event trigger I haven't met.

### C. Route 42 Blockage
*   **Hypothesis:** The only path from Mahogany Town to Ecruteak City is through Mt. Mortar.
*   **Falsification Test:** After clearing inventory in Ecruteak, return to Route 42. Check if the Super Nerd at (47, 8) has moved or if there is an alternative way to access the northern water route. If another path exists, the hypothesis is false.

### D. Team Rocket B1F Maze Progression
*   **Current State:** The dialogue from the Grunt at (2, 4) confirms the existence of invisible 'traps'. My systematic exploration has revealed that these are not forced-movement arrow tiles, but likely one-way pitfall warps.
*   **Current Progress:** I have confirmed pitfalls at (2, 13) and (3, 13). I have successfully navigated south along the western wall to (1, 14).
*   **Current Plan:** Continue systematic, one-tile-at-a-time exploration south and east from my current position at (1, 14) to find a safe path to the ladder at (3, 14).

### E. Team Rocket Boss Location
*   **Hypothesis:** The Team Rocket boss is located behind the locked door at (10, 9) on B3F.
*   **Falsification Test:** If, after reaching the door, there is no password prompt, no visible switch, and no interaction possible, this hypothesis is false. The path forward must be on a different floor or via a hidden passage I have missed. My next step would be a full, systematic re-exploration of B1F and B2F.

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