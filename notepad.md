## I. Core Protocols & Immediate Actions (v36)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays.
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

### D. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35, 4 badges: 43.

### E. HM & Field Move Mechanics
- **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.

### F. Key Items Obtained
- **SUPER ROD:** From Fishing Guru in house on Route 12 (accessed via warp at (12, 78)).

### G. Tile Glossary (v4)
- **ground:** A standard, walkable tile.
- **impassable:** A non-traversable tile, like a wall or object.
- **warp:** A tile that transports the player to another location, which can be on the same or a different map.
- **closed_gate:** An impassable gate. On Silph Co. floors, these appear to be opened by hidden puzzle triggers rather than keys.
- **teleport:** A tile that instantly warps the player to another location on the same map. Includes spinner tiles and teleporter pads.
- **elevator:** A special type of warp tile found in larger buildings. Requires interaction with a panel to select a floor before the warp can be used.

## III. Agent & Tool Development Log (v55)
### A. Development Priorities
#### Tools
- **`dungeon_navigator_tool` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. It must be able to systematically test every reachable tile to find puzzle triggers.
- **`map_segment_analyzer` (HIGH PRIORITY):** To analyze the current reachable segment of a map, identifying all reachable tiles, warps, and objects. This will be the computational backend for the `floor_strategist_agent`.
- **`wkg_query_tool` (MEDIUM PRIORITY):** To automate checking for broken links or existing nodes/edges in my World Knowledge Graph.
- **`json_payload_generator` (LOW PRIORITY):** To prevent syntax errors when calling tools like `manage_world_knowledge`.
#### Agents
- **`floor_strategist_agent` (MEDIUM PRIORITY):** To analyze the output of the `map_segment_analyzer` tool and create a prioritized list of exploration targets.
- **`puzzle_logic_agent` (LOW PRIORITY):** To recall complex puzzle solutions (e.g., Silph Co. gate triggers) to avoid manual re-discovery.

### B. Active Agents & Tools
- `pc_navigator_agent` (v2) - Reliable
- `team_composition_advisor_agent` (v2) - Reliable
- `protocol_enforcement_agent` (v1) - Reliable
- `battle_strategist_agent` (v10) - Reliable
- `select_battle_option` - Reliable
- `pathfinder`: A simple BFS. **UNRELIABLE** in complex, segmented dungeons. To be used for simple, direct paths only until `dungeon_navigator_tool` is developed.

## VII. Lessons Learned & Untested Assumptions (v9)
- **Tool Refinement is Mandatory:** My `pathfinder` tool is a simple BFS that cannot account for hidden puzzle triggers. My previous plan to avoid the tool was a protocol violation. **Corrective Action:** I will prioritize fixing `pathfinder` or accelerating the development of its replacement, `dungeon_navigator_tool`.
- **Untested Assumptions:**
    - The CARD KEY is on a higher floor of Silph Co. (Test: Continue exploring upwards.)
    - The elevator provides access to all previously inaccessible segments of the floors. (Test: Use the elevator to visit each floor and check for access to new areas.)
    - Giovanni is on the 11th floor, as a Rocket grunt mentioned. (Test: Reach the 11th floor and explore it.)

## IX. Battle Log & Lessons Learned
### Scientist on Silph Co. 7F (vs. MUK Lv.39)
- **Lesson:** THUNDERBOLT can miss. A miss at a critical moment led to SPARKY fainting.
- **Lesson:** SPARKY fainted to a critical hit from MUK's BODY SLAM. RNG can be brutal.
- **Lesson:** CONFUSE RAY is not 100% accurate and can fail.
- **Opponent Moveset (MUK):** ACID ARMOR, SLUDGE, BODY SLAM, MINIMIZE.