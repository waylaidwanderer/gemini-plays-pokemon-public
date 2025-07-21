# Gem's Pokémon Crystal Notepad

## I. Game State & Objectives

### A. Primary Questline
*   **Team Rocket Hideout:** Find the boss and use the passwords to disrupt their radio signal operation. The entrance is a secret stairway in the Mahogany Mart.
*   **Mahogany Town Gym:** Obtain the 6th Gym Badge.
*   **RED SCALE Investigation:** Mr. Pokémon is the primary person of interest.

### B. Active Side Quests & Rematches
*   **Heal the Sick Miltank (Route 39):** Needs 'lots of BERRIES'.
*   **Rematch List:** Picnicker Liz (Route 32), Youngster Joey (Route 30), Camper Todd (Route 34).

### C. Known Blockers & Story Gates
*   **Mahogany Town Gym:** A Fisher blocks the entrance at (6, 14).
*   **Schoolboy Alan (Route 36):** In a dialogue loop, likely a story-gated event.

## II. Game Mechanics

### A. Tile Traversal Rules
*   **Verified Impassable:** WALL, COUNTER, MART_SHELF, PC, HEADBUTT_TREE, CUT_TREE (uncut), TV, TOWN_MAP, WINDOW, ROCK, BUOY, VOID, RADIO, INCENSE_BURNER.
*   **Verified Traversable:** FLOOR, GRASS, TALL_GRASS, LONG_GRASS, WATER/SEA (with Surf).
*   **Verified Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN/LEFT/RIGHT, WARP_PANEL.
*   **HM Required:** BOULDER (STRENGTH), ROCK_SMASH_BOULDER (ROCK SMASH), WHIRLPOOL.
*   **One-Way:** PIT (fall), LEDGE_HOP_RIGHT/LEFT/DOWN, FLOOR_UP_WALL (one-way 'up' ledge).
*   **Untested:** COMPUTER, BED, CABINET, SINK, PLANT, BOOKSHELF, unknown, and any tile type with `unknown` in its name. My protocol is to test these by attempting to walk into them from all four directions when first encountered.

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
*   **Team Rocket Base Passwords:** SLOWPOKETAIL, HAIL GIOVANNI.
*   **Team Rocket Base B1F Secret Passage:** The 'door' at (10, 9) is opened by the Secret Switch at (19, 11).
*   **Team Rocket Base B2F Layout:** Northern and southern corridors are separate. Access to the north must be from a different warp on B1F.
*   **Mahogany Town:** No shop exists. The mart is a Team Rocket front, and the Poké Center has no vendor. Travel to another city is required for inventory management.
*   **Mahogany Town Story Lock:** FLY is disabled, forcing progression towards the Lake of Rage.
*   **Mahogany Mart Secret Ladder:** The warp to the hideout is not triggered by interaction, but by stepping onto the ladder tile at (7, 3).

### B. Falsified Hypotheses & Dead Ends
*   **Mahogany Gym Blocker:** The Fisher did NOT move after the Lake of Rage event. Hypothesis that Lance's presence was the trigger is false.
*   **Secret Potion Location:** The hint for Cianwood City was incorrect; the Pharmacist runs a regular shop.
*   **Team Rocket B2F Southern Corridor:** The ROCKET at (21, 14) has non-progressive dialogue, confirming this path is a dead end.
*   **Team Rocket B1F Eastern Corridor:** The secret passage at (10, 9) and the entire eastern corridor lead to a dead-end loop.
*   **Team Rocket B1F Switch Function:** The switch at (19, 11) is not a toggle for the invisible maze. Interacting with the ROCKET at (2, 4) produces the same result regardless of the switch's on/off state.

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
*   **Pathfinder v3 Tool (Active):** Critical coordinate system bug fixed on turn 60614. Tool is now fully operational.

### B. Agent Development Log & Status
*   **Tool Debugger Agent v2 (Active):** A specialized agent created to diagnose and fix pathfinding scripts. Successfully identified and helped correct bugs in `pathfinder_v3`.
*   **Inventory Solver Agent (Active):** Created to provide step-by-step plans to free up inventory slots, accounting for known bugs.
*   **Strategy Advisor (Active):** Consolidated strategic advisor that provides high-level planning.

### C. Agent Ideas

### D. Open Hypotheses & Tests
*   **Mahogany Gym Blocker:** **Hypothesis:** Progress is gated by defeating Team Rocket in their hideout.
*   **Mt. Mortar Invisible Barrier:** **Hypothesis:** An invisible barrier blocks the northern one-way ledge on Mt. Mortar B1F. **Falsification Test:** Find an alternate route to the northern area and attempt to walk south over the same ledge.
*   **Team Rocket B1F Maze Progression:** 
    *   **Primary Hypothesis:** The 'traps' are one-way pitfall warps caused by invisible arrow tiles that lead to the northern section of B2F.
    *   **Methodology:** Use the `maze_mapper` tool to systematically explore every floor tile to find all pitfalls. The `maze_mapper` suggests the next unexplored adjacent tile. Once all pitfalls are found, I will use the `maze_solver` tool, providing it with the list of pitfall warp coordinates, to calculate the correct path through the maze.
    *   **Known Pitfalls:** (3, 13) on B1F -> (3, 14) on B2F.
    *   **Falsification Test:** If systematic mapping reveals no path, the hypothesis is wrong. The alternative is that another trigger exists on the map. I would need to re-explore the entire floor looking for other interactable objects.

### E. Untested Assumptions & Falsification Tests
*   **BOOKSHELF Tile Traversal:** **Assumption:** Impassable. **Test:** Navigate to (20, 10) and attempt to walk into the bookshelf at (20, 11) and (21, 11) from all four cardinal directions.

### F. Tile Testing Protocol
*   **New Tile Discovery:** When a new, unknown tile type is encountered, I must systematically test its properties. This includes attempting to walk on it from all four directions and documenting whether it's traversable, a one-way path, or requires a specific item or action to pass.