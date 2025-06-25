# Gem's Strategic Journal (v140 - Post-Critique)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Verify Assumptions:** Do not record intel as "completed" or "confirmed" until it has been empirically verified. Non-battling trainers exist; not every NPC is an opponent.
- **Agent Liability & Discipline:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location. I must be more disciplined in using my agents, especially `wkg_manager_agent` and `encounter_tracker_agent`.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*. Consolidate markers on single tiles for clarity. Use the `wkg_manager_agent` for all WKG updates to avoid manual errors.
- **Tool-First Mindset:** For any complex or repetitive task, use an agent first.
- **Encounter Tracking Protocol:** After every wild encounter, I MUST use the `encounter_tracker_agent` to log the data. This is now a mandatory step in my workflow.

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
- **Gen 1 Move Typing:** Bite and Double Kick are Normal-type. Wing Attack has 35 Base Power.
- **Confusion & Field Moves:** A confused Pokémon may use any move, including TELEPORT, which ends the battle.
- **Normal/Ghost Immunities:** Normal moves are ineffective against Ghosts, and Ghost moves are ineffective against Normals.

## III. Active Plans & Hypotheses
- **Primary Plan:** Explore south along Route 13 to find the next town and Gym.
- **Contingency Plan:** Test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3.4):** Generally reliable. 
  - **Refinement Plan:** Merge the functionality of a healing route planner into this one by adding a `find_nearest_pokecenter` goal type. This will require parsing the WKG for 'pokecenter' tags.
- **`wkg_manager_agent` (v3):** Reliable. Must be used for all WKG updates.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v3):** Recently refined. Monitor for improved performance.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`encounter_tracker_agent` (v1):** **CRITICAL REMINDER:** I MUST start using this agent after every wild encounter to build my training data log. No more excuses. I will now integrate this into my standard post-battle workflow.

### B. Agent Development Backlog
- **`item_finder_agent`:** Plan efficient routes to collect all items on a map.
- **`fishing_advisor_agent`:** Analyze map & rod to suggest best fishing spots/catches.
- **`hm_planner_agent`:** Suggest best Pokémon for HMs based on current moves and future utility.
- **`sales_data_agent`:** Track item prices across different Poké Marts to find the best deals.
- **`move_tutor_advisor_agent`:** Suggest optimal moves to learn from TMs/HMs.
- **`story_progress_tracker_agent`:** Track key NPC dialogue and plot points.

## V. Completed Intel & Disproven Hypotheses
- (This section is for temporarily noting completed short-term intel before it is archived or removed. Long-term discoveries are integrated into other sections.)

## VI. Unverified Assumptions & Future Tests
- **Path Forward:** The path south through Route 13 is assumed to be the correct progression path.
- **Thirsty Guards:** The guards blocking Saffron City might accept a drink item like Fresh Water. This is a key alternative path to test.
- **Strange Battle Mechanics:** The FEAROW's triple attack could be a unique move or mechanic in this ROM hack. I need to be more observant.

## VII. Encounter Log (JSON)
{"ROUTE_12":["ODDISH"]}

## VIII. Reflection Notes (T26395)

- **Disproven Hypothesis:** Cool Trainer at (12, 93) on Route 12 does NOT want a Moon Stone; he's just flavor text. This path is a dead end.
- **New Plan:** The southern exit on Route 12 is blocked. The new primary plan is to test the contingency plan: give a drink to the thirsty guards blocking the Saffron City gates.

## Saffron City Intel
- Rocket Grunt at (24, 9) said: "BOSS said he'll take this town!". This confirms a city-wide takeover is in progress.