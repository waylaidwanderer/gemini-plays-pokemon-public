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

## VII. Lessons Learned & Protocol Corrections
- **Protocol Failure (T30985):** I attempted to log a Silph Co. warp connection (8F 12,6 to 2F 28,16) that already existed in the World Knowledge Graph. I had clearly forgotten this path because I failed to mark the warp with '🚪' on both ends immediately after using it the first time. **Correction:** Must be more disciplined. Trust system errors. Mark ALL warps immediately.
- **Protocol Failure (T30988):** I misidentified a warp on Silph Co. 8F at (4,12) as navigable. It was in an isolated room. **Correction:** I must verify warp reachability from my current position before listing it in my validation checks.
- **Protocol Update (T31290):** A single bidirectional edge (`is_one_way: false`) in the WKG covers two-way travel. Do not create a second, reversed edge for the same connection.
- **Protocol Failure (T31320):** I have repeatedly hallucinated my location and map ID, leading to multiple failed tool calls and wasted turns. **Correction:** I MUST verify my current `map_id` and coordinates from the Game State Information *before* every single action, especially navigation and documentation. I will also trust system warnings about reachability and dead ends.
- **Protocol Failure (T31322):** I have been using `select_battle_option` redundantly by also manually inputting the button presses. **Correction:** I will rely solely on the tool for battle menu selections to improve efficiency.
- **Hypothesis Failure (T31370):** The pier on Route 12 is segmented. I was stuck on an isolated section and could not reach the southern trainers or the exit to Route 13. All manual and pathfinder attempts failed. **Correction:** The game state shows reachable warps. I must trust the game state over my own perception and explore all reachable warps before assuming I am stuck.
- **Hypothesis Failure (Route 12 South Path):** The warp at (12, 78) on Route 12 leads to the Super Rod House, not south. The path south must be found elsewhere.
- **Protocol Failure (T31644):** I failed to mark the exit warp of the Route 12 Gatehouse before transitioning to Route 12. I must be more disciplined and mark both sides of a warp connection immediately.
- **Protocol Failure (T31645):** I set a navigation goal to a trainer at (15, 32) on Route 12 without checking my map markers first. The marker clearly indicated this NPC was non-battling and I had already interacted with them. This is a major failure in following my own established protocols and wasted a turn. I MUST check markers before every navigation or interaction action.
- **Protocol Failure (T32111):** The `pathfinder` tool is fundamentally broken for segmented maps like Celadon City. Multiple fix attempts, including simplifying the logic, have failed. **Correction:** Ignoring a faulty tool is unacceptable. My absolute highest priority is to develop a new, more advanced navigation tool that can parse the World Knowledge Graph to find paths across complex, multi-part maps. I will not proceed with any other major objectives until this is complete. The existing `pathfinder` will be reserved for simple, on-map navigation only after it's been properly debugged for that purpose.
- **Protocol Failure (T32206):** I hallucinated the number of navigable warps on Route 8 while I was in the gatehouse. I listed unreachable warps as navigable. **Correction:** I must ONLY use the Game State Information for the CURRENT map and double-check reachability status before making any assumptions.
- **CRITICAL PROTOCOL FAILURE (T32211):** I had a severe, multi-turn hallucination, believing I was in Saffron City (map 10) while still on Route 8 (map 19). This led to multiple failed tool calls (`manage_world_knowledge`, `delete_map_marker`) and a failed `notepad_edit` due to attempting a massive, incorrect overwrite. This is my worst violation of the core protocol: **VERIFY CURRENT LOCATION BEFORE EVERY ACTION.**
  - **Correction:** I must be hyper-vigilant. I will ALWAYS check my `map_id` and `(x, y)` from the Game State Information before any documentation or navigation-related tool call. I will explicitly confirm map transitions by checking the game state on the following turn before documenting anything.
**`pathfinder` Tool Limitation (T32222):** The `pathfinder` tool is unreliable for complex, segmented maps (e.g., Saffron City, Route 12). I will use manual navigation in these areas until a more robust tool is developed. This is in response to a direct AI critique.
- **CRITICAL PROTOCOL FAILURE (T32243):** I hallucinated my position for the second time in a row, believing I was at (18, 31) when I was actually at (19, 31). This is unacceptable. I MUST verify my coordinates from the Game State Information before every single action, especially after a failed movement.
- **Protocol Failure (T32218 -> T32241):** I used the `pathfinder` tool in Saffron City, a map I explicitly documented as too complex for it. This directly violated my own protocol (T32222) and wasted several turns. **Correction:** I must trust my own documented limitations. The `pathfinder` tool is now forbidden for navigation in any map noted as 'complex' or 'segmented'. I will use manual navigation until the `overworld_navigator` is complete.

## VII. Lessons Learned & Protocol Corrections (v3)
### A. CRITICAL: Core Protocol Violations
- **Location & State Hallucination (T31320, T32206, T32211, T32243):** I have repeatedly failed to verify my current `map_id` and `(x, y)` from the Game State Information before acting. This has led to severe, multi-turn hallucinations (e.g., believing I was in Saffron City while still on Route 8), causing numerous failed tool calls and wasted time.
  - **CORRECTION:** I MUST be hyper-vigilant. I will ALWAYS check my `map_id` and `(x, y)` from the Game State Information before ANY documentation or navigation-related tool call. I will explicitly confirm map transitions by checking the game state on the following turn before documenting anything. I will trust system warnings about reachability and dead ends.
- **Failure to Use Documentation (T31645, T32218 -> T32241, T32252):** I have set navigation goals to NPCs already marked as non-battling and repeatedly used the `pathfinder` tool on maps explicitly documented in this notepad as 'complex' or 'segmented'.
  - **CORRECTION:** My documentation is useless if I do not consult it. I MUST check map markers before every navigation or interaction action. I will adhere strictly to my own documented tool limitations.

### B. Tool & Agent Usage
- **`pathfinder` Tool Limitation (T32111, T32222):** The `pathfinder` tool is fundamentally broken for segmented or complex maps (e.g., Saffron City, Celadon City, Route 12).
  - **CORRECTION:** The `pathfinder` tool is now forbidden for navigation in any map noted as 'complex' or 'segmented'. I will use manual navigation in these areas until the `overworld_navigator` is complete.
- **Redundant Tool Calls (T31322):** I have used `select_battle_option` while also manually inputting the button presses.
  - **CORRECTION:** I will rely solely on the tool for battle menu selections to improve efficiency.

### C. Data Management & World Knowledge
- **Inconsistent Warp Marking (T30985, T31644):** I have failed to mark both the entry and exit points of warps with '🚪' immediately after transitioning, leading to confusion and attempts to log existing connections.
  - **CORRECTION:** I must be more disciplined. I will mark ALL warps on both sides of the transition immediately.
- **WKG Edges (T31290):** A single bidirectional edge (`is_one_way: false`) in the WKG covers two-way travel. I will not create redundant reversed edges.
- **Warp Reachability (T30988):** I must verify a warp is reachable from my current position before assuming it's a valid path.

### D. Navigation & Exploration
- **Hypothesis Failure (Route 12, T31370):** Getting stuck on segmented maps is often due to missing a reachable warp.
  - **CORRECTION:** I must trust the game state over my own perception and explore all reachable warps before assuming I am stuck. The warp at (12, 78) leads to the Super Rod House, not south.