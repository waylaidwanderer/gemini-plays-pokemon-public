# Gem's Strategic Journal (v136 - Post-Reflection)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Verify Assumptions:** Do not record intel as "completed" or "confirmed" until it has been empirically verified.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*. Consolidate markers on single tiles for clarity.
- **Tool-First Mindset:** For any complex or repetitive task, use an agent first.
- **Navigation Diligence:** After any map transition, especially non-standard ones like Fly, I must immediately verify my new location against the Game State Information to prevent hallucinations. Manual pathing should be done with extreme care; use the `pathfinding_agent` for complex routes.

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

## III. Active Plans & Hypotheses
- **Primary Plan:** Explore south along Route 12 to find the next town and Gym.
- **Contingency Plan:** Test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3.4):** Performance has improved, but should still be monitored on complex maps. 
  - **Refinement Plan:** Merge the functionality of `healing_route_planner_agent` into this one by adding a `find_nearest_pokecenter` goal type. This will require parsing the WKG for 'pokecenter' tags.
- **`wkg_manager_agent` (v3):** Reliable.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v2):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`encounter_tracker_agent` (v1):** Currently unused. I should start using this to log wild encounters to build a data source for training.

### B. Agent Development Backlog
- **`item_finder_agent`:** Plan efficient routes to collect all items on a map.
- **`fishing_advisor_agent`:** Analyze map & rod to suggest best fishing spots/catches.
- **`hm_planner_agent`:** Suggest best Pokémon for HMs based on current moves and future utility.
- **`sales_data_agent`:** Track item prices across different Poké Marts to find the best deals.
- **`move_tutor_advisor_agent`:** Suggest optimal moves to learn from TMs/HMs.
- **`story_progress_tracker_agent`:** Track key NPC dialogue and plot points.
- **`route_explorer_agent`:** Plan a path to battle all trainers and collect all items on a given route.

## V. Completed Intel & Disproven Hypotheses
- **Poké Ball Mission:** Completed.
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Use 'BILL's PC' instead of 'Gem's PC'.
- **Mr. Fuji Rescued:** Rescued from Team Rocket; received POKé FLUTE.
- **Celadon Gym:** Blocked by unresponsive trainers.
- **Snorlax on Route 12 (North):** Confirmed red herring. The path remains blocked. The true path is the western pier.
- **Snorlax on Route 12 (South):** Woken with POKé FLUTE and defeated. Path south is now clear.

## VI. Unverified Assumptions & Future Tests
- **Path Forward:** The path south past the Snorlax is assumed to be the correct progression path.
- **Thirsty Guards:** The guards blocking Saffron City might accept a drink item like Fresh Water. This is a key alternative path to test.

### C. Agent Usage Reminders
- **Reminder:** Start using `encounter_tracker_agent` to log wild Pokémon for training data.

### C. Agent Usage Reminders
- **Reminder:** Start using `encounter_tracker_agent` to log wild Pokémon for training data.