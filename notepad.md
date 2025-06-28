## I. Core Protocols & Immediate Actions (v29)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays.
- **CRITICAL: WKG Management Workflow:** Before adding a new node, I will first use `run_code` to query the `world_knowledge_graph_json_string` to check if a node at the destination already exists. This prevents failed tool calls.
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents for complex reasoning and my custom tools for computational tasks. I will not use tools in contexts where I have documented them as unreliable (e.g., `pathfinder` in puzzle-heavy dungeons).
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
- **Agent Reliance (MANDATORY):** I will use the `battle_strategist_agent` for all significant battles (Gyms, Rival, unique encounters) to ensure optimal move selection.

### C. Navigation & Traversal Rules
- **Pikachu Movement:** A walkable object. Requires two button presses to move onto its tile if not already facing it.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **Silph Co. Elevator:** Requires a two-step process. First, interact with the panel to select a floor. Second, walk onto one of the warp tiles at the back of the elevator room to trigger the map change.
- **Route 12 Pier:** The pier is segmented into isolated sections. The only way to proceed south from the northern pier is to find the correct warp point.

### D. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35, 4 badges: 43.

### E. HM & Field Move Mechanics
- **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.

### F. Key Items Obtained
- **SUPER ROD:** From Fishing Guru in house on Route 12 (accessed via warp at (12, 78)).

### G. Tile Glossary (v2)
- **ground:** Standard walkable tile.
- **impassable:** Walls, objects, and other barriers that cannot be walked through.
- **closed_gate:** An impassable gate. On Silph Co. floors, these appear to be opened by hidden floor triggers rather than keys.
- **grass:** Tall grass where wild Pokémon can be encountered.
- **teleport:** A tile that instantly warps the player to another location on the same map. Includes spinner tiles and teleporter pads.
- **elevator:** A special type of warp tile found in larger buildings. Requires interaction with a panel to select a floor before the warp can be used.

## III. Agent & Tool Development Log (v49)
### A. Development Priorities
- **`dungeon_navigator_tool` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. It must be able to systematically test every reachable tile to find puzzle triggers. This is a **tool**, not an agent.
- **`wkg_query_tool` (HIGH PRIORITY):** To automate checking for broken links or existing nodes in my World Knowledge Graph, formalizing my new WKG workflow.
- **`json_payload_generator` (TOP PRIORITY):** To prevent syntax errors when calling tools like `manage_world_knowledge`.

### B. Active Agents (Reliable)
- `pc_navigator_agent` (v2)
- `team_composition_advisor_agent` (v2)
- `protocol_enforcement_agent` (v1)
- `battle_strategist_agent` (v9)

### C. Active Tools (Reliable)
- `pathfinder` (limitation: unreliable for complex, segmented, or puzzle-based maps like Saffron City, Route 12, and Silph Co. **Do not use in these areas.**).
- `select_battle_option`

## VII. Lessons Learned & Protocol Corrections (v4)
- **`pathfinder` is unreliable in complex dungeons.** My `pathfinder` tool is a simple BFS that cannot account for hidden puzzle triggers (like on Silph Co. 5F and 7F). The Game State Information's `Reachable Unseen Tiles` is the source of truth. If the tool fails but reachable tiles exist, I MUST switch to a manual, systematic search for the trigger and not waste turns re-running the faulty tool.