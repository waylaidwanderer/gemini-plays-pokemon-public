# Gem's Strategic Journal (v111 - Tactical Retreat)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Trust Agent Outputs:** Agents are extensions of my own reasoning. A negative result (e.g., 'path not found') is a valid and crucial piece of information, not a failure. It should be trusted and used to reformulate strategy immediately.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on. The Channeler at (15, 13) on Pokémon Tower 4F is confirmed to be bugged; avoid interacting.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*. Manually fix failed agent calls.
- **Agent Usage:** Use agents proactively for pathfinding, team building, and complex tasks. Prioritize refining agents that show flaws.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic-type moves are SUPER-EFFECTIVE against Ghost/Poison types (e.g., Gastly/Haunter).
- **PC System:** "BILL's PC" is for Pokémon Storage; "Gem's PC" is for Item Storage.
### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.

## III. Active Plans & Hypotheses
### **Current Plan: Pokémon Tower 4F Descent for Healing**
*   **Action Plan (v5 - Confirmed Non-Combatant):**
    1.  **Situation:** Currently on Pokémon Tower 4F. Party is critically injured.
    2.  **Failed Hypothesis:** The Channeler at (16, 8) is NOT a trainer. Interacting with her only yields dialogue. The plan to intentionally lose to her is invalid.
    3.  **New Insight:** Since she is not a trainer, her line of sight does not block the path to the eastern side of the floor.
    4.  **Revised Goal:** Navigate to the stairs at (19, 10) to descend to 3F, exit the tower, and heal at the Pokémon Center.
    5.  **Next Step:** Use `stealth_pathfinder_agent` to find a path from my current location to (19, 10), providing an empty list for the `trainers` argument.

### Long-Term Goals & Hypotheses
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Pipeline
- **(CRITICAL PRIORITY): `wkg_manager_agent` Refinement:** The agent repeatedly fails to create valid payloads. It must be fixed to ensure WKG accuracy.
- **(HIGH PRIORITY): `battle_advisor_agent` Refinement:** The agent's logic is flawed for wild encounters (recommends fighting instead of running) and needs better risk assessment.
- **(Future Idea): `shopping_planner_agent`:** To plan TM and item purchases.
- **(Future Idea): `item_finder_agent`:** To plan paths for collecting all items on a map.
- **(Future Idea): `healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **(New Idea): `wild_encounter_strategist_agent`:** To handle repetitive wild battles by always recommending 'RUN' unless specific conditions are met (e.g., capture target, training goal).