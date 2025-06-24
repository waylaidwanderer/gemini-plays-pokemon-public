# Gem's Strategic Journal (v115 - Agent Refinement)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Trust, but Verify Agent Outputs:** Agents are powerful, but their reasoning can be flawed. A negative result ('path not found') must be scrutinized. If the agent's reasoning contradicts the map data, the agent itself is flawed and must be refined.
- **Agent Input Integrity:** Agents are only as good as their input. Ensure data provided (e.g., list of hostile trainers) is accurate and not based on unverified assumptions. Garbage in, garbage out.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic-type moves are SUPER-EFFECTIVE against Ghost/Poison types (e.g., Gastly/Haunter).
- **PC System:** "BILL's PC" is for Pokémon Storage; "Gem's PC" is for Item Storage.
### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.

## III. Active Plans & Hypotheses
### **Current Plan: Pokémon Tower 6F**
1.  **Situation:** On Pokémon Tower 6F, in battle with a Channeler.
2.  **Action Plan:** Defeat the Channeler, then continue exploring the floor to find the stairs to 7F.

### Long-Term Goals & Hypotheses
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Pipeline
- **(COMPLETE): `stealth_pathfinder_agent` Refinement:** The agent's system prompt has been completely rewritten with more explicit instructions. It has successfully found a complex path it previously failed, confirming the fix. The agent is now considered reliable for navigation.
- **(CRITICAL FIX): `wkg_manager_agent` Refinement:** The agent's core logic is flawed. It generates a batch of tool calls that fail due to sequential dependency. It needs to be redesigned to output node/edge data, not pre-formatted tool calls, so I can sequence them correctly.
- **(Future Idea): `shopping_planner_agent`:** To plan TM and item purchases.
- **(Future Idea): `item_finder_agent`:** To plan paths for collecting all items on a map.
- **(Future Idea): `healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.

## VI. Agent Task Backlog

### `battle_advisor_agent` (COMPLETE - v3)
- **Problem:** The agent struggled to differentiate between wild and trainer battles, leading to incorrect run/fight recommendations.
- **Root Cause:** The logic for identifying battle type was weak and relied on fallible text analysis.
- **Solution:** The agent has been successfully redesigned. It now requires a boolean `is_trainer_battle` input, which acts as the absolute source of truth. The system prompt has been updated to strictly enforce that the agent CANNOT recommend running if this flag is true. This has proven to be a robust and reliable fix.