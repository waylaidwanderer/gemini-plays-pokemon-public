# Gem's Pokémon Crystal Notepad

## I. Game State & Objectives

### A. Primary Questline
*   **RED SCALE Investigation:** Mr. Pokémon is the primary person of interest.
*   **Team Rocket Hideout:** Find the boss and use the passwords to disrupt their radio signal operation. The entrance is a secret stairway in the Mahogany Mart.
*   **Mahogany Town Gym:** Obtain the 6th Gym Badge.

### B. Active Side Quests
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.
*   **Rematch List:** Picnicker Liz (Route 32), Youngster Joey (Route 30), Camper Todd (Route 34).

### C. Known Blockers & Story Gates
*   **Mahogany Town Gym:** A Fisher blocks the entrance at (6, 14).
*   **Schoolboy Alan (Route 36):** In a dialogue loop, likely a story-gated event.

## II. Game Mechanics

### A. Tile Traversal Rules
*   **Verified Impassable:** WALL, COUNTER, MART_SHELF, PC, BOOKSHELF, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID.
*   **Verified Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA (with Surf), unknown (TeamRocketBaseB3F).
*   **Verified Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN/LEFT/RIGHT, WARP_PANEL.
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL.
*   **One-Way:** PIT (fall), LEDGE_HOP_RIGHT/LEFT/DOWN, FLOOR_UP_WALL (one-way 'up' ledge).
*   **Untested:** RADIO (Test by walking into), INCENSE_BURNER (Test by walking into), unknown (TeamRocketBaseB2F), unknown (LakeOfRage), COMPUTER, BED, CABINET, SINK, PLANT, unknown (MountMortarB1F), unknown (Route43).

### B. System Bugs & Glitches (Verified)
*   **Item Management:** 'DEPOSIT ITEM' & 'TOSS ITEM' (from PC & PACK) are bugged. 'FLY' HM is bugged. Using one item from a stack does not free an inventory slot.
*   **Giving Items:** Giving an item to a Pokémon does not free an inventory slot.

### C. Item Usage Rules
*   **Status Heal:** Cannot be used on a Pokémon not afflicted with that status.
*   **HP Restore:** Can be used on any damaged Pokémon, but not one at full HP.

## III. World Knowledge

### A. Solved Puzzles & Key Discoveries
*   **Red Gyarados Event (Lake of Rage):** Defeated the red Gyarados and obtained the RED SCALE.
*   **Cianwood City Stuck Spot:** Resolved by triggering back-to-back phone calls (Mom, then Liz) on tile (10, 28).
*   **Ilex Forest Shrine:** A Lass in the Route 34 Gate mentioned a shrine honoring a grass-type protector.
*   **TM12 (Sweet Scent):** Given by Teacher in Route 34 Ilex Forest Gate.
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is opened by the Secret Switch at (19, 11).

*   **Team Rocket Base B2F Layout:** Northern and southern corridors are separate. Access to the north must be from a different warp on B1F.
*   **Mahogany Town:** No shop exists. The mart is a Team Rocket front, and the Poké Center has no vendor. Travel to another city is required for inventory management.
*   **Mahogany Town Story Lock:** FLY is disabled, forcing progression towards the Lake of Rage.

### B. Falsified Hypotheses & Dead Ends
*   **Mahogany Gym Blocker:** The Fisher did NOT move after the Lake of Rage event. Hypothesis that Lance's presence was the trigger is false.
*   **Secret Potion Location:** The hint for Cianwood City was incorrect; the Pharmacist runs a regular shop.
*   **Team Rocket B2F Southern Corridor:** The ROCKET at (21, 14) has non-progressive dialogue, confirming this path is a dead end.
*   **Team Rocket B1F Eastern Corridor:** The secret passage at (10, 9) leads to a dead-end corridor.

### C. Passwords & Keys
*   **Team Rocket Hideout Passwords:** SLOWPOKETAIL (from ROCKET_GIRL on B3F), HAIL GIOVANNI (from Moltres statue on B3F). RATICATE TAIL is an unconfirmed password.

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
*   **Pathfinder v3 Tool (Active):** Critical bug fixed where it failed to calculate paths to impassable destinations. Tool is now fully operational.
*   **Manual Path Planner Tool (Deleted):** Became redundant after `pathfinder_v3` was fixed.

### B. Agent Development Log & Status
*   **Tool Debugger Agent v2 (Active):** A specialized agent created to diagnose and fix pathfinding scripts. Successfully identified and helped correct bugs in `pathfinder_v3`.

## VI. Open Hypotheses & Tests

### A. Mahogany Gym Blocker
*   **Hypothesis:** Progress is gated by defeating Team Rocket in their hideout.

### B. Mt. Mortar Invisible Barrier
*   **Hypothesis:** An invisible barrier blocks the northern one-way ledge on Mt. Mortar B1F.
*   **Falsification Test:** Find an alternate route to the northern area and attempt to walk south over the same ledge.

### C. Team Rocket B1F Maze Progression
*   **Hypothesis:** The 'traps' are one-way pitfall warps caused by invisible arrow tiles that lead to the northern section of B2F.
*   **Methodology:** 
    1. Systematically step on each unknown floor tile in the maze area.
    2. If a tile forces movement (a pitfall), record the start and end coordinates.
    3. Compile a JSON string of all discovered pitfalls: `[{"start_x": X1, "start_y": Y1, "end_x": X2, "end_y": Y2, "direction": "up/down/left/right"}, ...]`
    4. Use the `maze_solver` tool with the compiled data to find the path to the warp panel at (5, 15) or any other identified exit point.

## VII. Side Quests & Rematches
*   **Picnicker Liz (Route 34):** Wants a rematch on Route 32.
*   **Youngster Joey (Route 30):** Wants a rematch.
*   **Camper Todd (Route 36):** Wants a rematch on Route 34.

## VIII. Future Development & Reminders

### A. Agent Ideas
*   **Multi-Map Travel Planner:** An agent that takes a high-level destination (e.g., 'Mr. Pokémon's House') and generates a step-by-step route across multiple maps, accounting for known warps and obstacles.

### B. Untested Assumptions & Falsification Tests
*   **HEADBUTT_TREE Traversal:**
    *   **Assumption:** Impassable.
    *   **Test:** Attempt to walk into it from all four directions.

### C. Tile Testing Protocol
*   **New Tile Discovery:** When a new, unknown tile type is encountered, I must systematically test its properties. This includes attempting to walk on it from all four directions and documenting whether it's traversable, a one-way path, or requires a specific item or action to pass.