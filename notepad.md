# I. Active Quests & Investigation Logs

## Main Quest: The Enigmatic Old Amber
-   **Objective:** Retrieve the Old Amber.
-   **Location:** Pewter Museum of Science.
-   **Obstacle:** A Scientist at (13, 5) on 1F blocks the path to an item.
-   **New Hypotheses (from Agent):**
    1.  **Rank 4:** Use the 'Silph Scope' on 1F of the museum near the blocking Scientist. (Reasoning: Unconventional item use for a potentially paranormal puzzle.)
    2.  **Rank 5:** Place a Pokémon with the 'Illuminate' ability in the lead and interact with the unlit fossil display. (Reasoning: Tests an obscure non-HM field ability.)
-   **Failed Hypotheses (Consolidated):**
    - Give a 'Fresh Water', 'Soda Pop', or 'Lemonade' to the thirsty man in NW Pewter City. (Result: Could not locate the NPC in the specified area.)
    - Examine the exterior rear wall of the museum for a hidden switch. (Result: Interacting with the wall at (6,1) had no effect.)
-   **Contingency Plans:**
    - If all other hypotheses fail, use the Itemfinder on both floors of the museum to search for hidden items, including the Old Amber itself.
-   **Anomalies Investigated (2F Grass Tile):**
    - The single `grass` tile at (12, 2) on 2F is inaccessible from the main area. **Conclusion:** This is likely an exit point from a hidden area on 1F, not an entrance.
-   **Invalidated Hypotheses:**
    - Go behind the main counter on 1F: The tiles behind the counter are marked as impassable. (Verified by map data).
    - Use 'Cut' on the east-side tree (before event): The path to the tree is physically blocked by the impassable museum building itself. (Verified by pathfinder).
-   **Failed Hypotheses (Consolidated):**
    - Interact with the large space shuttle model on 2F of the museum. (Result: Displayed the text "SPACE SHUTTLE COLUMBIA", no other effect.)
    - Place a Clefairy/Clefable in the first party slot and speak to the scientist near the Moon Stone display on 2F. (Result: No change in dialogue.)
    - Attempt to ride the Bicycle indoors on the first floor. (Result: Professor Oak's dialogue prevents use.)
    - After talking to the scientist on the 2nd floor next to the Aerodactyl fossil, interact with the fossil display itself. (Result: No change, triggered standard trap.)
    - Use the 'POKé DOLL' item while standing next to the barrier in front of the Scientist. (Result: Professor Oak's dialogue prevents use.)
    - Use a Pokémon with the move 'Dig' in front of the scientist. (Result: Warped out of the museum, similar to an Escape Rope).
    - Use the Itemfinder on the first floor, specifically in front of the large space shuttle exhibit. (Result: The exhibit is on 2F, but using Itemfinder on 1F yielded nothing.)
    - Use a Poké Doll on the blocking Scientist at (13, 5). (Result: Untestable, path is blocked)
    - Interact with the large Moon Stone display on the 2nd floor. (Result: No change)
    - Talk to the Youngster at (2, 8) on 2F, then return to the blocking Scientist on 1F. (Result: No change)
    - Use the Itemfinder on the 2nd floor to find a hidden item. (Result: No item found)

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

# IV. Key Discoveries & Lessons Learned

-   **Confirmation Bias & Over-Correction (CRITICAL):** My handling of the Rocket Hideout B2F maze was a cascade of cognitive errors. **Lesson:** Do not swing from one bias to another. Trust verifiable data and tool outputs over intuition.
-   **Hypothesis Testing Failure (Preparation):** Arrived at a location to test a hypothesis without the required Pokémon/items/moves. **Lesson:** Always verify party composition and necessary items/moves *before* traveling.
-   **Pikachu Following Mechanic (CRITICAL CLARIFICATION):** A button press in Pikachu's direction will only cause a turn *if the player is not already facing that direction*. Pathfinding tools must account for this.
-   **Tool Deferral Failure (CRITICAL):** Repeatedly deferred the creation of necessary tools instead of building them immediately. **Lesson Reinforced:** If a repetitive manual task can be automated, or a complex reasoning task can be delegated, building a tool or agent for it is the highest priority.
-   **Game Corner Entry Failure (CRITICAL):** Became stuck in a loop attempting to enter the Celadon Game Corner while Pikachu blocked a warp tile. **Lesson:** If a specific path or objective is repeatedly blocked, do not persist with the same failed approach. Re-evaluate, check for alternate routes, or pivot to a different high-priority goal.

# III. Tile Traversal & Movement Rules
- **PC Interaction:** Must be activated from the tile directly below (Y+1), while facing up.
- **Ledges:** Can only be jumped down (from Y-1 to Y+2 in one move). Impassable from all other directions.
- **Pewter Museum Fee Trigger:** The tile at (10, 5) on 1F triggers the entrance fee dialogue even if the player is already inside the museum.