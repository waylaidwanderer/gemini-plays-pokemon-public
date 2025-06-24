# Gem's Strategic Journal (v107 - Major Refactor)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (`map_id`, `current_position`) is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on. The Channeler at (15, 13) on Pokémon Tower 4F is confirmed to be bugged; avoid interacting.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*. Re-issue failed calls.
- **Agent Usage:** Use agents proactively for pathfinding, team building, and complex tasks. Prioritize refining agents that show flaws.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic-type moves are SUPER-EFFECTIVE against Ghost/Poison types (e.g., Gastly/Haunter).
- **PC System:** "BILL's PC" is for Pokémon Storage; "Gem's PC" is for Item Storage.
### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.

## III. Active Hypotheses & Long-Term Goals
- **Pokémon Tower:** The stairs to the next floor are likely unlocked by defeating all trainers on the current floor. A Channeler at (13, 9) on 5F offers healing, but is currently inaccessible.
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Pipeline
- **(CRITICAL PRIORITY): `wkg_manager_agent` Refinement:** The agent repeatedly fails to create valid payloads. It must be fixed to ensure WKG accuracy.
- **(HIGH PRIORITY): `battle_advisor_agent` Refinement:** The agent's logic is flawed for wild encounters (recommends fighting instead of running) and needs better risk assessment.
- **(Future Idea): `shopping_planner_agent`:** To plan TM and item purchases.
- **(Future Idea): `item_finder_agent`:** To plan paths for collecting all items on a map.
- **(Future Idea): `healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.
- **(Future Idea): `wild_battle_manager_agent`:** To automate the fight/run decision in wild battles.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.

## VI. Hallucination & Correction Log
- **CRITICAL (WKG Management):** Multiple consecutive turns wasted attempting to add WKG nodes/edges due to a flawed understanding of the toolchain and faulty agent payloads.
- **CRITICAL (Map Data):** Repeatedly failed to acknowledge the correct number of reachable unseen tiles, despite system warnings. Must trust game state data.
- **Player Hallucination (Typing):** Incorrectly logged ECHO (Golbat) as a GHOST type. Corrected to Poison/Flying.
- **Battle Logic Hallucination (Type Matchups):** Assumed standard Gen 1 type matchups. Discovered Psychic is SUPER-EFFECTIVE against Ghost/Poison in this ROM hack.