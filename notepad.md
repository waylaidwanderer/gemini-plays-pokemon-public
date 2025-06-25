# Gem's Strategic Journal (v133 - Route 12)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Verify Assumptions:** Do not record intel as "completed" or "confirmed" until it has been empirically verified.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*. Consolidate markers on single tiles for clarity.
- **Tool-First Mindset:** For any complex or repetitive task, use an agent first.
- **Follow Through:** Documenting a reminder is useless if I don't follow it.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:**
  - Psychic is SUPER-EFFECTIVE against Ghost/Poison.
  - Ghost is SUPER-EFFECTIVE against Psychic.
  - Bite (Normal) is SUPER-EFFECTIVE against Psychic.
  - Normal is NOT-VERY-EFFECTIVE against Psychic.
- **Poison Status Immunity:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.

### Navigation & Traversal Rules
- **Defeated Trainers as Obstacles:** Defeated trainers act as impassable walls and must be navigated around.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.
- **Gen 1 Move Typing:** Bite and Double Kick are Normal-type.
- **Confusion & Field Moves:** A confused Pokémon may use any move, including TELEPORT, which ends the battle.
- **Normal/Ghost Immunities:** Normal moves are ineffective against Ghosts, and Ghost moves are ineffective against Normals.
- **Inventory Limit:** The displayed limit is a visual bug; the actual limit is higher.

### Opponent Battle Intel
- **Channeler Team Composition:** Not all Channelers exclusively use Ghost-types.

## III. Active Plans & Goals
### **Current Plan: Explore Post-Tower World**
1.  **Situation:** I have the POKé FLUTE. SPARKY is critically injured.
2.  **Primary Goal:** Defeat the next available Gym Leader.
3.  **Secondary Goal:** Explore Route 12 and the surrounding areas to find a path forward.
Plan: Explore the 9 reachable unseen tiles on Route 12 to find the correct path forward.

### Long-Term Goals
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3.2 - UNRELIABLE):** Failed *again* on Route 12, attempting to path into impassable tiles at (4,50) and (4,55) (T25813, T25815). The agent's map parsing is critically flawed. Refining prompt again with stricter rule hierarchy.
- **`wkg_manager_agent` (v3):** Reliable.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v2):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.

### B. Agent Development Backlog
- **`item_finder_agent`:** Plan efficient routes to collect all items on a map.
- **`healing_route_planner_agent`:** Find the most efficient path to a Pokémon Center using the WKG.
- **`fishing_advisor_agent`:** Analyze map & rod to suggest best fishing spots/catches.
- **`hm_planner_agent`:** Suggest best Pokémon for HMs based on current moves and future utility.
- **`encounter_tracker_agent`:** Record wild Pokémon encounters per route for training optimization.
- **`sales_data_agent`:** Track item prices across different Poké Marts to find the best deals.

## V. Completed Intel & Disproven Hypotheses
- **Poké Ball Mission:** Completed.
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Use 'BILL's PC' instead of 'Gem's PC'.
- **Inventory Limit is Visual Bug:** Confirmed.
- **Mr. Fuji Rescued:** Rescued from Team Rocket; received POKé FLUTE.
- **Celadon Gym:** Blocked by unresponsive trainers.
- **Snorlax on Route 12:** Encounter seems bugged. Path is blocked even after waking it. The western pier is the correct path.

## VI. Unverified Assumptions & Future Tests
- **Snorlax on Route 12:** The encounter seems bugged or a red herring. The sprite disappeared after using the POKé FLUTE, but the path at (12, 37) remains blocked. The true path seems to be the western pier. **Hypothesis to Test:** Revisit this Snorlax after exploring the rest of the region to see if a different trigger is required.

## VII. Agent Development Priorities
- **`healing_route_planner_agent`:** Create an agent to find the most efficient path to a Pokémon Center using the WKG. This is a high priority due to SPARKY's critical condition.