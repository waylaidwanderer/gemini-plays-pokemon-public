# Gem's Strategic Journal (v142 - Post-Dojo & Critique Overhaul)

## I. Core Principles & Lessons Learned
- **CRITICAL: Agent & Workflow Discipline:** My workflow has been sloppy. The critique was a necessary wake-up call.
  - **Faulty Agent Protocol:** A consistently failing agent (like `wkg_manager_agent`) is a liability and must be immediately decommissioned and replaced. I will no longer use it.
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

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.

## III. Active Plans & Hypotheses
- **Primary Plan:** Disrupt Team Rocket's operations in Saffron City.
- **Current Objective:** Claim the prize Pokémon from the Fighting Dojo, then investigate the Silph Co. building, which is likely Team Rocket's main base of operations.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3.4):** Reliable.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v3):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`encounter_tracker_agent` (v1):** **CRITICAL REMINDER:** I MUST use this agent after every wild encounter to build my training data log. This is now a mandatory step.
- **`wkg_manager_agent_v2`:** Defined. Needs testing.
- **`spinner_maze_agent`:** Defined. Ready for use.

### B. Agent Development Backlog
- **`item_finder_agent`:** Plan efficient routes to collect all items on a map.
- **`fishing_advisor_agent`:** Analyze map & rod to suggest best fishing spots/catches.
- **`hm_planner_agent`:** Suggest best Pokémon for HMs based on current moves and future utility.
- **`sales_data_agent`:** Track item prices across different Poké Marts to find the best deals.
- **`move_tutor_advisor_agent`:** Suggest optimal moves to learn from TMs/HMs.
- **`story_progress_tracker_agent`:** Track key NPC dialogue and plot points.

### C. Decommissioned Agents
- **`wkg_manager_agent` (v3):** **DECOMMISSIONED.** This agent consistently fails to check for existing nodes, causing tool errors. DO NOT USE.

## V. Completed Intel & Disproven Hypotheses
- **Route 13 Dead End:** The path south through Route 13 was not the correct progression path.
- **Thirsty Guards:** Giving a drink to the thirsty guards opened a path to a different part of Route 5, not directly to Saffron City.

## VI. Saffron City Intel
- **Team Rocket Takeover:** Confirmed by a Rocket Grunt. Their goal is to take over the city.
- **Fighting Dojo:** Cleared. The Karate Master offered a prize Pokémon.

## VII. Silph Co. Strategic Plan
- **Objective:** Systematically clear all 11 floors of Team Rocket, find the CARD KEY, and defeat the boss.
- **Methodology:** Explore each floor completely, starting from 1F. Map all warps, spinners, and locked doors. Defeat all grunts and scientists. Find the CARD KEY, which is likely on a mid-to-upper floor. Use the CARD KEY to unlock all previously inaccessible areas. Heal at a Pokémon Center as needed between floors.

### New Battle Mechanics Discovered
- **'No Will to Fight' Mechanic:** A Pokémon with very low HP (e.g., ECHO at 24/112) may refuse to be switched into battle, displaying the message "There's no will to fight!". This seems to be a fatigue or loyalty mechanic that prevents sacrificing a severely weakened Pokémon.