# Gem's Strategic Journal (v117 - Post-Wipe Reflection)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle. Obsessing over a broken tool mid-crisis is a recipe for failure.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic-type moves are SUPER-EFFECTIVE against Ghost/Poison types (e.g., Gastly/Haunter).
### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.

## III. Active Plans & Hypotheses
### **Current Plan: Team Rebuilding**
1.  **Situation:** Wiped out in Pokémon Tower. My team is under-leveled and poorly suited for the threats.
2.  **Action Plan:** 
    a. Use `team_composition_advisor_agent` to formulate a new team composition better suited for the tower's Ghost and Psychic types.
    b. Identify an effective training location based on agent recommendations (Diglett's Cave is a strong candidate).
    c. Train the selected team members up to the level 35 cap.

### Long-Term Goals & Hypotheses
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`stealth_pathfinder_agent` (v2 - RELIABLE):** Successfully finds complex paths it previously failed. Considered reliable for navigation.
- **`exploration_agent` (v1 - FUNCTIONAL):** Logic is sound for finding efficient exploration paths, but its performance is dependent on server stability.
- `wkg_manager_agent` (v2 - RELIABLE): Successfully identifies existing nodes and creates edges without duplication. Considered reliable for WKG management.

### B. Agent Development Backlog
- **(Future Idea): `shopping_planner_agent`:** To plan TM and item purchases.
- **(Future Idea): `item_finder_agent`:** To plan paths for collecting all items on a map.
- **(Future Idea): `healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.

### C. Retired / Failed Agents
- **`battle_advisor_agent` (v1-v5 - DELETED):** Catastrophic failure. Repeatedly failed to grasp fundamental Gen 1 type matchups (e.g., Poison's weakness to Psychic), even after multiple forceful prompt corrections. Its flawed logic was a direct liability and cause of a party wipe. Do not attempt to rebuild until a more robust method for ensuring rule adherence is developed.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.

### **PC Glitch Investigation**
- **Bug:** Selecting "Gem's PC" leads to the "Item Storage System" after the "Accessed my PC." message appears.
- **Failed Hypotheses:**
    1. Repeatedly selecting "Gem's PC" does not work.
    2. Logging out of the PC entirely and re-engaging does not fix the issue.
- **New Hypothesis:** After the "Accessed my PC." message appears, press 'B' instead of 'A' to see if it bypasses the glitch and enters the Pokémon Storage.

- (Future Idea): Consolidate `stealth_pathfinder_agent` and `exploration_agent` into a single, more robust `pathfinding_agent` with optional parameters, as suggested by the AI critic.

- (Future Idea): Consolidate `stealth_pathfinder_agent` and `exploration_agent` into a single, more robust `pathfinding_agent` with optional parameters, as suggested by the AI critic.