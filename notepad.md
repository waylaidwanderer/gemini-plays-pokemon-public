# Gem's Strategic Journal (v118 - Post-Reflection)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle. Obsessing over a broken tool mid-crisis is a recipe for failure.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*.
- **Tool-First Mindset:** For any complex or repetitive task (like pathfinding), use an agent first. Manual attempts should only be a last resort.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:**
  - Psychic is SUPER-EFFECTIVE against Ghost/Poison.
  - Ghost is SUPER-EFFECTIVE against Psychic.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.

## III. Active Plans & Hypotheses
### **Current Plan: Pokémon Tower Ascent**
1.  **Situation:** Ascending the Pokémon Tower to rescue Mr. Fuji.
2.  **Action Plan:** 
    a. Continue climbing the tower, floor by floor.
    b. Use my newly configured team, with ECHO as the primary attacker for Ghost-types, while being mindful of their Psychic counters.
    c. Train lower-level Pokémon like SPARKY as opportunities arise.

### Long-Term Goals & Hypotheses
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`stealth_pathfinder_agent` (v2 - RELIABLE):** Finds complex paths successfully.
- **`exploration_agent` (v1 - FUNCTIONAL):** Logic is sound for exploration paths.
- **`wkg_manager_agent` (v2 - RELIABLE):** Successfully identifies existing nodes and creates edges without duplication.
- **`pc_navigator_agent` (v2 - RELIABLE):** Successfully navigates the PC by using 'BILL's PC' to bypass the 'Gem's PC' glitch.

### B. Agent Development Backlog
- **(PRIORITY): Consolidate `stealth_pathfinder_agent` and `exploration_agent` into a single, more robust `pathfinding_agent` with an optional parameter to specify the goal (e.g., 'explore_unseen' or 'reach_target').**
- **(Future Idea): `shopping_planner_agent`:** To plan TM and item purchases.
- **(Future Idea): `item_finder_agent`:** To plan paths for collecting all items on a map.
- **(Future Idea): `healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.

### C. Retired / Failed Agents
- **`battle_advisor_agent` (v1-v5 - DELETED):** Catastrophic failure. Repeatedly failed to grasp fundamental Gen 1 type matchups. Its flawed logic was a direct liability and cause of a party wipe.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Selecting 'Gem's PC' is bugged and unusable. The correct and reliable method to access Pokémon Storage is to select 'BILL's PC' from the main menu.

- **Pokémon Tower 5F Healing Spot (13, 9) is FAKE:** The Channeler offers dialogue but does NOT heal the party. Do not rely on this spot.