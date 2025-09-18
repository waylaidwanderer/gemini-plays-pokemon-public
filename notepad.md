# I. Active Quests & Investigation Logs

## Main Quest: The Enigmatic Old Amber
-   **Objective:** Retrieve the Old Amber.
-   **Location:** Pewter Museum of Science.
-   **Obstacle:** A Scientist at (13, 5) on 1F blocks the path.
-   **Failed Hypotheses:**
    1.  Showing a living Aerodactyl/Kabutops to the Old Man at (2, 5) will move the blocking Scientist. (Result: No change)
    2.  Triggering both the Kabutops and Aerodactyl Fossil traps in succession will move the Scientist. (Result: No change)
    3.  Reading the "SPACE SHUTTLE COLUMBIA" sign on 2F will change NPC dialogue, revealing a clue. (Result: No change)

## **Stalled Quest: The Copycat's Gift**

-   **Objective:** Obtain a POKé DOLL and give it to COPYCAT.
-   **Status:** Active. All leads in Cerulean City exhausted for now.

# II. Game Mechanics & World Rules

-   **POKé DOLL Escape:** A POKé DOLL can be used to guarantee an escape from a wild Pokémon battle.
-   **Battle Menu Anomaly:** The game appears to intentionally restrict move selection in certain wild battles to the first move slot.
-   **Shop Menu Navigation Anomaly:** The Cerulean Mart shop menu does not follow a standard grid layout and requires 'B' to exit.
-   **Pikachu Trap Mechanic:** On Rocket Hideout floors and in the Pewter Museum, interacting with specific objects can trigger a trap that locks the player on an impassable tile. This trap is escaped by pressing the 'B' button.
-   **PC Mechanics:** The PC is **stateful**. Any automation tool MUST account for this by having a reset sequence to return to a known state.
-   **Route 4 Access:** There are two distinct maps named 'Route 4'. The eastern section is a one-way path *from* Mt. Moon.

# III. Key Discoveries & Lessons Learned

-   **Confirmation Bias & Over-Correction (CRITICAL):** My handling of the Rocket Hideout B2F maze was a cascade of cognitive errors. **Lesson:** Do not swing from one bias to another. Trust verifiable data and tool outputs over intuition.
-   **Hypothesis Testing Failure (Preparation):** Arrived at a location to test a hypothesis without the required Pokémon/items/moves. **Lesson:** Always verify party composition and necessary items/moves *before* traveling.
-   **Pikachu Following Mechanic (CRITICAL CLARIFICATION):** A button press in Pikachu's direction will only cause a turn *if the player is not already facing that direction*. Pathfinding tools must account for this.
-   **Tool Deferral Failure (CRITICAL):** Repeatedly deferred the creation of necessary tools instead of building them immediately. **Lesson Reinforced:** If a repetitive manual task can be automated, or a complex reasoning task can be delegated, building a tool or agent for it is the highest priority.
-   **Game Corner Entry Failure (CRITICAL):** Became stuck in a loop attempting to enter the Celadon Game Corner while Pikachu blocked a warp tile. **Lesson:** If a specific path or objective is repeatedly blocked, do not persist with the same failed approach. Re-evaluate, check for alternate routes, or pivot to a different high-priority goal.