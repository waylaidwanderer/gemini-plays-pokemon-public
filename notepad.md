# I. Active Quests & Investigation Logs

## Main Quest: The Enigmatic Old Amber
-   **Objective:** Retrieve the Old Amber.
-   **Location:** Pewter Museum of Science.
-   **Obstacle:** A Scientist at (13, 5) on 1F blocks the path to an item.
-   **New Hypotheses (from Agent):**
    1.  **Rank 1:** Place a revived Omanyte or Kabuto in the first slot of your party and speak to the blocking scientist at (13, 5).
    2.  **Rank 2:** Read the descriptive plaque on the wall directly in front of the Aerodactyl fossil display at (3, 3).
    3.  **Rank 3:** Interact with the potted plant at (11, 8) in the southeastern corner of the main room, checking for a hidden switch.
-   **Untestable Hypotheses:**
    -   Set a Clefairy/Clefable as your lead party Pokémon and speak to the scientist standing near the meteorite display. (Reasoning: Cannot reach the scientist in the partitioned eastern section).
-   **Failed Hypotheses (Consolidated):**
    -   Interact with the Aerodactyl Fossil at (3,4) and Kabutops Fossil at (3,7). (Result: Both exhibits are simple traps that temporarily lock the player. Pressing 'B' escapes. They do not open any new paths.)
    -   Use the Itemfinder on the first floor. (Result: The Itemfinder isn't responding, no items found.)
    -   Interact with the large space shuttle model on 2F of the museum. (Result: Displayed the text "SPACE SHUTTLE COLUMBIA", no other effect.)
    -   Move onto the tile at (3, 3) to interact with the Aerodactyl fossil plaque. (Result: The tile at (3,3) is impassable.)
    -   Place a Clefairy/Clefable in the first party slot and speak to the scientist near the Moon Stone display on 2F. (Result: No change in dialogue.)
    -   Attempt to ride the Bicycle indoors on the first floor. (Result: Professor Oak's dialogue prevents use.)
    -   Use the 'POKé DOLL' item while standing next to the barrier in front of the Scientist. (Result: Professor Oak's dialogue prevents use.)
    -   Use a Pokémon with the move 'Dig' in front of the scientist. (Result: Warped out of the museum, similar to an Escape Rope).
    -   Use a Poké Doll on the blocking Scientist at (13, 5). (Result: Untestable, path is blocked)
    -   Interact with the large Moon Stone display on the 2nd floor. (Result: No change)
    -   Talk to the Youngster at (2, 8) on 2F, then return to the blocking Scientist on 1F. (Result: No change)
    -   Use the Itemfinder on the 2nd floor to find a hidden item. (Result: No item found)
    -   Give a 'Fresh Water', 'Soda Pop', or 'Lemonade' to the thirsty man in NW Pewter City. (Result: Could not locate the NPC in the specified area.)
    -   Examine the exterior rear wall of the museum for a hidden switch. (Result: Interacting with the wall at (6,1) had no effect.)
    -   Interact with the large Space Shuttle Columbia model at (8, 4). (Result: No text or event triggered.)
    -   Examine the small meteorite display at (8, 6). (Result: No text or event triggered.)
-   **Anomalies Investigated (2F Grass Tile):**
    -   The single `grass` tile at (12, 2) on 2F is inaccessible from the main area. **Conclusion:** This is likely an exit point from a hidden area on 1F, not an entrance.
-   **Invalidated Hypotheses:**
    -   Go behind the main counter on 1F: The tiles behind the counter are marked as impassable. (Verified by map data).
    -   Use 'Cut' on the east-side tree (before event): The path to the tree is physically blocked by the impassable museum building itself. (Verified by pathfinder).

## Active Quest: The Copycat's Gift
-   **Objective:** Give the POKé DOLL to COPYCAT.
-   **Location:** Cerulean City (exact location of COPYCAT TBD).
-   **Status:** Item obtained. Ready to proceed once COPYCAT is found.

# II. Game Mechanics & World Rules

-   **Battle Menu Anomaly:** The game sometimes restricts move selection to the first slot in wild battles.
-   **PC Statefulness:** The PC is stateful. Automation tools MUST have a reset sequence.
-   **Pikachu Following Mechanic:** A button press in Pikachu's direction only causes a turn if not already facing that direction.
-   **Trap Mechanics:**
    -   **Pewter Museum:** Interacting with fossil exhibits or Pikachu after cutting the tree at (27, 5) can trigger a lock. Pressing 'B' escapes.
-   **Item Usage:**
    -   A POKé DOLL guarantees escape from a wild battle.
- **Pewter Museum Fee Trigger:** The entrance fee tile at (10, 5) can be re-triggered even after entering the museum.

# IV. Key Discoveries & Lessons Learned

-   **Confirmation Bias & Over-Correction (CRITICAL):** My handling of the Rocket Hideout B2F maze was a cascade of cognitive errors. **Lesson:** Do not swing from one bias to another. Trust verifiable data and tool outputs over intuition.
-   **Hypothesis Testing Failure (Preparation):** Arrived at a location to test a hypothesis without the required Pokémon/items/moves. **Lesson:** Always verify party composition and necessary items/moves *before* traveling.
-   **Pikachu Following Mechanic (CRITICAL CLARIFICATION):** A button press in Pikachu's direction will only cause a turn *if the player is not already facing that direction*. Pathfinding tools must account for this.
-   **Tool Deferral Failure (CRITICAL):** Repeatedly deferred the creation of necessary tools instead of building them immediately. **Lesson Reinforced:** If a repetitive manual task can be automated, or a complex reasoning task can be delegated, building a tool or agent for it is the highest priority.
-   **Game Corner Entry Failure (CRITICAL):** Became stuck in a loop attempting to enter the Celadon Game Corner while Pikachu blocked a warp tile. **Lesson:** If a specific path or objective is repeatedly blocked, do not persist with the same failed approach. Re-evaluate, check for alternate routes, or pivot to a different high-priority goal.

# III. Tile Traversal & Movement Rules
- **PC Interaction:** Must be activated from the tile directly below (Y+1), while facing up.
- **Ledges:** Can only be jumped down (from Y-1 to Y+2 in one move). Impassable from all other directions.
    - Interact with the potted plant at (11, 8). (Result: No plant exists at this location; it is a warp tile. Interaction failed.)