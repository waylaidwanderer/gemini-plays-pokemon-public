# Gem's Strategic Journal (v114 - Agent Debugging)

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
### **Current Plan: Pokémon Tower 5F Puzzle**
1.  **Situation:** On Pokémon Tower 5F, northern section. All attempts to path to the southern section have failed.
2.  **Hypothesis:** The `stealth_pathfinder_agent` is critically flawed, hallucinating map partitions. It cannot be trusted for navigation until fixed.
3.  **Action Plan:**
    a. Perform a sanity check by tasking the agent with finding a one-step path to an adjacent tile.
    b. Based on the result, refine or completely rewrite the agent's system prompt to fix its analytical failures.
    c. Once the agent is reliable, re-attempt to solve the 5F puzzle.

### Long-Term Goals & Hypotheses
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Pipeline
- **(COMPLETE): `stealth_pathfinder_agent` Refinement:** The agent's system prompt has been completely rewritten with more explicit instructions. It has successfully found a complex path it previously failed, confirming the fix. The agent is now considered reliable for navigation.
- **(HIGH PRIORITY): `wkg_manager_agent` Refinement:** The agent repeatedly fails to create valid payloads. It must be fixed to ensure WKG accuracy.
- **(Future Idea): `shopping_planner_agent`:** To plan TM and item purchases.
- **(Future Idea): `item_finder_agent`:** To plan paths for collecting all items on a map.
- **(Future Idea): `healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.

- **(Future Idea): `exploration_agent`:** To find the most efficient path to visit all reachable unseen tiles on a map.

## VI. Agent Task Backlog

### `battle_advisor_agent` (CRITICAL FIX)
- **Problem:** The agent incorrectly identified a trainer battle as a wild encounter, recommending 'Run' instead of fighting.
- **Root Cause:** The system prompt lacks a clear mechanism to differentiate battle types.
- **Solution:** Rewrite the system prompt to include an explicit instruction: 'Analyze the `Screen Text` for keywords like "wants to fight!" or "sent out [POKEMON]!" to definitively identify a trainer battle. If these keywords are present, you MUST engage in battle strategy and NEVER recommend running. Apply the Wild Battle Protocol ONLY if these keywords are absent.'