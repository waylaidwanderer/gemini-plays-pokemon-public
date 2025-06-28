## I. Core Protocols & Immediate Actions (v34)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays.
- **CRITICAL: WKG Management Workflow (v2):** Before adding a new edge, I will first use a dedicated `wkg_query_tool` to check if an edge *and* its corresponding nodes already exist. This prevents duplicate data and failed tool calls.
- **CRITICAL: WKG Edge Precision:** All `warp` type edges MUST include a `destination_entry_point` if known. All new nodes MUST have descriptive `tags`.
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents for complex reasoning and my custom tools for computational tasks.
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

### B. Battle Protocols (v3)
- **Agent Reliance (MANDATORY):** I will use the `battle_strategist_agent` for all significant battles (Gyms, Rival, unique encounters) to ensure optimal move selection.

### C. Navigation & Traversal Rules
- **Pikachu Movement:** A walkable object. Requires two button presses to move onto its tile if not already facing it.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **Silph Co. Elevator:** Requires a two-step process. First, interact with the panel at (4,1) to select a floor. Second, walk onto one of the warp tiles at the back of the elevator room (e.g., (2,4) or (3,4)) to trigger the map change.
- **Route 12 Pier:** The pier is segmented into isolated sections. The only way to proceed south from the northern pier is to find the correct warp point.

### D. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35, 4 badges: 43.

### E. HM & Field Move Mechanics
- **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.

### F. Key Items Obtained
- **SUPER ROD:** From Fishing Guru in house on Route 12 (accessed via warp at (12, 78)).

### G. Tile Glossary (v3)
- **closed_gate:** An impassable gate. On Silph Co. floors, these appear to be opened by hidden floor triggers rather than keys.
- **teleport:** A tile that instantly warps the player to another location on the same map. Includes spinner tiles and teleporter pads.
- **elevator:** A special type of warp tile found in larger buildings. Requires interaction with a panel to select a floor before the warp can be used.

## III. Agent & Tool Development Log (v52)
### A. Development Priorities
- **`dungeon_navigator_tool` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. It must be able to systematically test every reachable tile to find puzzle triggers. This is a **tool**, not an agent.
- **`wkg_query_tool` (HIGH PRIORITY):** To automate checking for broken links or existing nodes/edges in my World Knowledge Graph, formalizing my new WKG workflow.
- **`json_payload_generator` (TOP PRIORITY):** To prevent syntax errors when calling tools like `manage_world_knowledge`.
- **`pathfinder` Refinement (HIGH PRIORITY):** The existing `pathfinder` tool must be refined to handle complex dungeon mechanics like hidden triggers. This is a higher priority than simply avoiding its use.
- **`puzzle_logic_agent` (LOW PRIORITY):** To recall complex puzzle solutions (e.g., Silph Co. gate triggers) to avoid manual re-discovery.

### B. Active Agents & Tools (Reliable)
- `pc_navigator_agent` (v2)
- `team_composition_advisor_agent` (v2)
- `protocol_enforcement_agent` (v1)
- `battle_strategist_agent` (v10)
- `select_battle_option`

## VII. Lessons Learned & Protocol Corrections (v6)
- **Tool Refinement is Mandatory:** My `pathfinder` tool is a simple BFS that cannot account for hidden puzzle triggers. **Protocol Violation:** My previous plan to avoid the tool was incorrect. Per core instructions, faulty tools MUST be refined or replaced immediately. **Corrective Action:** I will prioritize fixing `pathfinder` or accelerating the development of its replacement, `dungeon_navigator_tool`.
- **Untested Assumptions:**
    - The CARD KEY is on a higher floor of Silph Co. (Test: Continue exploring upwards.)
    - The item at Silph Co. 5F (5,7) is inaccessible from the west. (Test: Find a path to the other side of the wall.)

## IX. Battle Log & Lessons Learned (New Section)
### Scientist on Silph Co. 7F (vs. MUK Lv.39)
- **Lesson:** THUNDERBOLT can miss. A miss at a critical moment led to SPARKY fainting.
- **Lesson:** SPARKY fainted to a critical hit from MUK's BODY SLAM. RNG can be brutal.
- **Lesson:** CONFUSE RAY is not 100% accurate and can fail.
- **Opponent Moveset (MUK):** ACID ARMOR, SLUDGE, BODY SLAM, MINIMIZE.