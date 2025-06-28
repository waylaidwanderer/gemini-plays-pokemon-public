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
- **Protocol Failure (T32321):** The `pathfinder` tool failed to find a path to the Rocket at (15, 16) on Silph Co. 6F. This confirms my protocol: the tool is unreliable for anything but simple, open-area navigation. I must strictly adhere to using manual navigation in complex, maze-like interiors like this.