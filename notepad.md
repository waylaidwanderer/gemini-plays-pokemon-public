# I. Active Quests & Investigation Logs

## Main Quest: The Enigmatic Old Amber
-   **Objective:** Retrieve the Old Amber.
-   **Location:** Pewter Museum of Science.
-   **Obstacle:** A Scientist at (13, 5) on 1F blocks the path to an item.
-   **Key Finding:** The Scientist at (13, 5) is in an area completely surrounded by impassable tiles. Hypotheses requiring direct interaction are invalid. **CRITICAL:** Avoid confirmation bias that this specific Scientist is the *only* key. The solution may lie elsewhere in the museum.
-   **New Hypotheses (to be tested):**
    1.  Interact with the large Space Shuttle exhibit on 1F with a Clefairy in the party lead.
-   **Note:** Overwatch critique identified a hallucinated hypothesis (hidden switch) and a tedious one (reading all signs). Both have been removed. Will use puzzle_hypothesis_generator for better ideas.
-   **Failed Hypotheses (Consolidated):**
    - Use the 'POKé DOLL' item while standing next to the barrier in front of the Scientist. (Result: Professor Oak's dialogue prevents use.)
    - Use a Pokémon with the move 'Dig' in front of the scientist. (Result: Warped out of the museum, similar to an Escape Rope).
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