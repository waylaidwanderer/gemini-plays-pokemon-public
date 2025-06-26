## I. **TOP PRIORITY** - Agent Refinement & Protocol Adherence (Post-Critique #27482)
- **Immediate Task:** Halt all non-essential progress. Go to the nearest Pokémon Center and fix `wkg_manager_agent_v2` and `pathfinding_agent_v2`.
- **Reasoning:** The critique was correct. My agent workflow is inefficient and unreliable.
- **Protocol Enforcement:** I will *strictly* use `encounter_tracker_agent` after every wild encounter. No more lapses.

## II. Core Principles & Lessons Learned
- **CRITICAL: Agent & Workflow Discipline:** My workflow has been sloppy. The critique was a necessary wake-up-call.
  - **Faulty Agent Protocol:** A consistently failing agent is a liability. I will no longer use it until it is refined.
  - **Logging Protocol:** I will strictly adhere to my established protocols, especially using `encounter_tracker_agent` after every wild encounter. No exceptions.
- **CRITICAL: Map Marker Discipline:** Markers must only be placed *after* an event is verified.
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Verify Assumptions:** Do not record intel as "completed" or "confirmed" until it has been empirically verified. Non-battling trainers exist.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.

## III. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic.
- **Poison Status Immunity:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.

### Navigation & Traversal Rules
- **Defeated Trainers as Obstacles:** Defeated trainers act as impassable walls.

### New Battle Mechanics Discovered
- **'No Will to Fight' Mechanic:** A Pokémon with very low HP may refuse to be switched into battle.
- **No Blackout on Loss (Rocket Hideout/Silph Co.):** Losing a battle inside a Team Rocket controlled area does not cause a blackout.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.
- **Repel Mechanics:** MAX REPEL lasts longer than SUPER REPEL.

## IV. World Knowledge Graph Manual Entry Checklist (v8 - Post-Critique)
*This is a fallback procedure for when `wkg_manager_agent_v2` is non-functional.*
1.  **Check Nodes:** `run_code` to check if both source and destination nodes exist.
2.  **Add Missing Nodes:** If any node is missing, use `manage_world_knowledge` `add_node` with a manually constructed JSON payload (including tags).
3.  **Get Node IDs:** If new nodes were added, `run_code` to get their IDs.
4.  **CRITICAL - Check Edge:** `run_code` to check if an edge *already exists* between the two nodes. **DO NOT SKIP THIS STEP.**
5.  **Add Edge:** **ONLY IF STEP 4 CONFIRMS NO EDGE EXISTS**, use `manage_world_knowledge` `add_edge` with a manually constructed JSON payload. **For warp connections, remember to include the `destination_entry_point`!**

## V. Agent Development Log
### A. **TOP PRIORITY** - Agent Refinement
*No new agents will be developed until these core agents are stable and reliable.*
1.  **`pathfinding_agent_v2`:** Unreliable in Saffron City. Needs immediate logic overhaul to correctly handle complex layouts and trust game state reachability data.
2.  **`wkg_manager_agent_v2`:** Refined in turn 27588. Monitoring for reliability.

### B. Active Agents (Reliable)
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v3):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`encounter_tracker_agent` (v1):** **CRITICAL REMINDER:** I MUST use this agent after every wild encounter.

### C. Agent Development Backlog (Low Priority - Paused)
- `damage_calculator_agent`: Takes player/opponent Pokémon data and calculates move damage ranges to confirm KOs.
- `item_finder_agent`

## VI. Saffron City Intel
- **Team Rocket Takeover:** Confirmed by a Rocket Grunt. Their goal is to take over the city.
- **Fighting Dojo:** Cleared. Claimed Hitmonchan as the prize Pokémon.

## VII. Silph Co. Strategic Plan
- **Methodology:** Explore each floor completely. Map all warps, spinners, and locked doors. Defeat all grunts and scientists. Find the CARD KEY. Use the CARD KEY to unlock all previously inaccessible areas. Heal at a Pokémon Center as needed between floors.

- `silph_co_teleporter_mapper_agent`: Takes the current floor's XML and the WKG. Its job would be to identify all teleporters on the current floor and try to map out where they lead based on existing WKG data or suggest which ones are unexplored.

- Pikachu can block warp tiles, preventing entry.