## I. Core Protocols & Immediate Actions (v28)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays. I will verify my current map_id and coordinates from the Game State Information BEFORE every documentation action. I will also consult map markers before navigating to or interacting with a target.
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents whenever a task can be automated or requires complex reasoning. I will prioritize developing agents that solve my most immediate problems.
- **CRITICAL: Post-Event Checklists (MANDATORY):**
  - **Trainer Battle:** Mark defeated trainer with '☠️' and log their Pokémon under 'Trainer Intel'.
  - **Wild Encounter:** Log EVERY wild Pokémon with `encounter_tracker_agent`.
  - **Map Transition (Warp/Stairs/Edge):** Immediately use `manage_world_knowledge` to document the connection and mark used warps (entry/exit) with '🚪'.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison).
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Poison Type Effectiveness:** Poison-type moves are NOT-VERY-EFFECTIVE against Poison-types.

### B. Battle Protocols (v2)
- **Agent Reliance (MANDATORY):** I will use the `battle_strategist_agent` for all significant battles (Gyms, Rival, unique encounters like Snorlax) to ensure optimal move selection. Manual control is for routine wild battles only. This protocol is a direct response to repeated AI critiques about underutilizing my agents.

### C. Navigation & Traversal Rules
- **Pikachu Movement:** A walkable object. Requires two button presses to move onto its tile if not already facing it.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. The `pathfinder` tool is unreliable here. Using FLY is the most efficient method for traveling between distant points.
- **Silph Co. Elevator:** Requires a two-step process. First, interact with the panel to select a floor. Second, walk onto one of the warp tiles at the back of the elevator room to trigger the map change.
- **Route 12 Pier:** The pier is segmented into isolated sections, making manual navigation tricky and the `pathfinder` tool highly unreliable (it frequently suggests paths into water). The only way to proceed south from the northern pier is to find the correct warp point, not by walking.

### D. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35, 4 badges: 43.

### E. HM & Field Move Mechanics
- **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field. This contradicts the general rule for other HMs.

### F. Key Items Obtained
- **SUPER ROD:** From Fishing Guru in house on Route 12 (accessed via warp at (12, 78)).

## III. Agent & Tool Development Log (v48)
### A. Development Priorities
- **`overworld_navigator` (CRITICAL - TOP PRIORITY):** My `pathfinder` tool is fundamentally broken for segmented maps. My absolute highest priority is to develop a new, robust navigation tool that integrates with my World Knowledge Graph to handle complex, multi-map pathfinding. I will not pursue other major objectives until this is complete.
- **`wkg_debugger_tool` (HIGH PRIORITY):** To automate checking for broken links in my World Knowledge Graph.
- **`json_payload_generator` (TOP PRIORITY):** To prevent syntax errors when calling tools like `manage_world_knowledge`. Manual JSON scripting is too slow and error-prone.
- **`dungeon_navigator_tool` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. This must be a **tool**, not an agent, as it requires direct map data analysis.

### B. Active Agents (Reliable)
- `pc_navigator_agent` (v2)
- `team_composition_advisor_agent` (v2)
- `protocol_enforcement_agent` (v1)
- `battle_strategist_agent` (v9)

### C. Active Tools (Reliable)
- `pathfinder` (limitation: unreliable for complex, segmented maps like Saffron City and Route 12).
- `select_battle_option`
- `overworld_navigator` (Under Development)

## VII. Lessons Learned & Protocol Corrections (v3)

## VIII. Future Development & Research
- **Notepad Maintenance Agent:** An agent that can take notepad content and a set of rules (e.g., 'remove duplicate H2 sections') to automate cleanup.
- **Tile Glossary:** Start a dedicated section in the notepad to document the behavior of every discovered tile type (`ground`, `impassable`, `closed_gate`, `teleport`, etc.) to build a comprehensive physics guide.