## I. Core Protocols & Immediate Actions (v38)
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
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.

### D. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35, 4 badges: 43.

### E. HM & Field Move Mechanics
- **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.

### F. Key Items Obtained
- **SUPER ROD:** From Fishing Guru in house on Route 12 (accessed via warp at (12, 78)).

## III. Agent & Tool Development Log (v57)
### A. Development Priorities
- **`dungeon_navigator_tool` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. It must be able to systematically test every reachable tile to find puzzle triggers.
- **`floor_strategist_agent` (HIGH PRIORITY):** To analyze the output of the `map_segment_analyzer` tool and create a prioritized list of exploration targets.

### B. Active Agents & Tools
- `pc_navigator_agent` (v2) - Reliable
- `team_composition_advisor_agent` (v2) - Reliable
- `protocol_enforcement_agent` (v1) - Reliable
- `battle_strategist_agent` (v10) - Reliable
- `select_battle_option` - Reliable
- `map_segment_analyzer` (v2) - Reliable
- `pathfinder`: A simple BFS. **UNRELIABLE** in complex, segmented dungeons. To be used for simple, direct paths only until `dungeon_navigator_tool` is developed.

## VII. Silph Co. Investigation Log
### A. Confirmed Lessons
- **Tool Refinement is MANDATORY & IMMEDIATE:** My `pathfinder` tool is a simple BFS that cannot account for hidden puzzle triggers. **Protocol Violation Recorded (T33005):** I failed to adhere to this rule by using manual navigation instead of immediately halting to fix the tool. **Corrective Action:** The development of `dungeon_navigator_tool` is now my absolute highest priority, superseding all other exploration and story progression until it is functional.
- **MUK's Immunity:** MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).

### B. Untested Assumptions
1. The CARD KEY is on a higher floor of Silph Co. (Test: Continue exploring upwards.)
2. The elevator provides access to all previously inaccessible segments of the floors. (Test: Use the elevator to visit each floor and check for access to new areas.)
3. Giovanni is on the 11th floor, as a Rocket grunt mentioned. (Test: Reach the 11th floor and explore it.)
- **Teleporter Tiles:** These act as instant warps. Stepping on them immediately transports the player to another location, sometimes on a different floor. They are a key part of navigating complex dungeons like Silph Co.