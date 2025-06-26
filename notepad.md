# Gem's Strategic Journal (v145 - Post-Critique #27172)

## I. Core Principles & Lessons Learned
- **CRITICAL: Agent & Workflow Discipline:** My workflow has been sloppy. The critique was a necessary wake-up-call.
  - **Faulty Agent Protocol:** A consistently failing agent (like `wkg_manager_agent_v2`) is a liability. I will no longer use it until it is refined.
  - **Logging Protocol:** I will strictly adhere to my established protocols, especially using `encounter_tracker_agent` after every wild battle. No exceptions.
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Verify Assumptions:** Do not record intel as "completed" or "confirmed" until it has been empirically verified. Non-battling trainers exist.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.

## II. Game Mechanics & Battle Intel
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

## III. Active Plans & Hypotheses
- **Primary Plan:** Disrupt Team Rocket's operations in Saffron City.
- **Current Objective:** Systematically clear all 11 floors of Silph Co., find the CARD KEY, and defeat the boss.
- **Unverified Assumptions:** The CARD KEY and the boss are on a high floor. This is a common trope, but I must be open to them being anywhere.

## IV. World Knowledge Graph Manual Entry Checklist
*To be used when `wkg_manager_agent_v2` is non-functional.*
1.  **Check Source Node:** `run_code` to check if source node exists.
2.  **Check Destination Node:** `run_code` to check if destination node exists.
3.  **Add Source Node:** If it doesn't exist, `manage_world_knowledge` `add_node` for source.
4.  **Add Destination Node:** If it doesn't exist, `manage_world_knowledge` `add_node` for destination.
5.  **Get New IDs:** If any new nodes were created, `run_code` to get their IDs.
6.  **Add Edge:** `manage_world_knowledge` `add_edge` with the full, correct payload (including all coordinates).

## V. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3.4):** Reliable.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v3):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`encounter_tracker_agent` (v1):** **CRITICAL REMINDER:** I MUST use this agent after every wild encounter.
- **`wkg_manager_agent_v2`:** **NEEDS REFINEMENT.** This agent has failed repeatedly. I will not use it again until I have refined its logic to prevent errors.

### B. Agent Development Backlog
- **`wkg_helper_agent`:** (High Priority) Generate correct JSON payloads for manual `manage_world_knowledge` calls to prevent errors.
- **`silph_co_navigator_agent`:** Specialized agent to navigate Silph Co., aware of all teleporter connections, locked doors, and the CARD KEY location once found.
- **`item_finder_agent`:** Plan efficient routes to collect all items on a map.
- **`fishing_advisor_agent`:** Analyze map & rod to suggest best fishing spots/catches.
- **`hm_planner_agent`:** Suggest best Pokémon for HMs based on current moves and future utility.
- **`sales_data_agent`:** Track item prices across different Poké Marts to find the best deals.
- **`move_tutor_advisor_agent`:** Suggest optimal moves to learn from TMs/HMs.
- **`story_progress_tracker_agent`:** Track key NPC dialogue and plot points.

### C. Decommissioned Agents
- **`wkg_manager_agent` (v3):** **DECOMMISSIONED.** Consistently fails to check for existing nodes, causing tool errors. DO NOT USE.
- **`spinner_maze_agent`:** **DECOMMISSIONED.** Defined prematurely. No spinner mazes encountered yet.

## VI. Saffron City Intel
- **Team Rocket Takeover:** Confirmed by a Rocket Grunt. Their goal is to take over the city.
- **Fighting Dojo:** Cleared. Claimed Hitmonchan as the prize Pokémon.

## VII. Silph Co. Strategic Plan
- **Methodology:** Explore each floor completely. Map all warps, spinners, and locked doors. Defeat all grunts and scientists. Find the CARD KEY. Use the CARD KEY to unlock all previously inaccessible areas. Heal at a Pokémon Center as needed between floors.

## VIII. Unverified Silph Co. Assumptions
1. The CARD KEY is on a higher floor. (Could be anywhere)
2. All areas of a floor are accessible from the main elevator/stairwell. (Could be one-way teleporter sections)
3. The final boss is at the very top. (Could be in a side room on any floor)
4. All teleporters are two-way. (Some may be one-way)