# Gem's Strategic Journal (v109 - Full Refactor)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
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
### **Current Plan: Pokémon Tower 5F Ascent**
*   **Hypothesis:** The stairs to 6F are blocked until all trainers on 5F are defeated. The friendly Channeler's healing spot at (13, 9) may also unlock after this condition is met.
*   **Action Plan:**
    1.  **Defeat Channeler @ (18, 8):** Currently in battle. SPARKY is poisoned and at low HP. The plan is to use Thunderpunch to deal maximum damage before SPARKY faints.
    2.  **Defeat Channeler @ (15, 4):** After the current battle, assess party health. If possible, proceed directly to this trainer. Path will need to be calculated.
    3.  **Defeat Channeler @ (7, 11):** This will be the final trainer. Path will need to be calculated.
    4.  **Re-evaluate:** After all trainers are defeated, check if the stairs at (19, 10) are now accessible. If not, attempt to access the healing spot at (13, 9) again.

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