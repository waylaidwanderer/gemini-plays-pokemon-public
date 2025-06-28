## I. Core Protocols & Immediate Actions (v39)
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
- **Teleporter Tiles:** These act as instant warps. Stepping on them immediately transports the player to another location, sometimes on a different floor. They are a key part of navigating complex dungeons like Silph Co.
- **Closed Gates:** These tiles are impassable and block movement until a specific trigger or puzzle is solved.
- **Dynamic Gates (Silph Co. 5F):** The southern gates on 5F open and close based on the player's X-coordinate while in the northern corridor (at Y=2). The exact mapping needs to be tested systematically.

### D. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35, 4 badges: 43.

### E. HM & Field Move Mechanics
- **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.

### F. Key Items Obtained
- **SUPER ROD:** From Fishing Guru in house on Route 12 (accessed via warp at (12, 78)).

## III. Agent & Tool Development Log (v59)
### A. Development Priorities
- **`dungeon_navigator_tool` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. It must be able to systematically test every reachable tile to find puzzle triggers. This is my highest priority.
- **`floor_strategist_agent` (HIGH PRIORITY):** To analyze the output of the `map_segment_analyzer` tool and create a prioritized list of exploration targets (warps, objects, unseen tiles). This will serve as the input for the `dungeon_navigator_tool`.

### B. Active Agents & Tools
- `pc_navigator_agent` (v2) - Reliable
- `team_composition_advisor_agent` (v2) - Reliable
- `protocol_enforcement_agent` (v1) - Reliable
- `battle_strategist_agent` (v10) - Reliable
- `select_battle_option` - Reliable
- `map_segment_analyzer` (v5) - Fixed to handle `closed_gate` tiles. Awaiting final verification.
- `pathfinder`: A simple BFS. **UNRELIABLE** in complex, segmented dungeons. To be used for simple, direct paths only until `dungeon_navigator_tool` is developed.

## VII. Silph Co. Investigation Log
### A. Confirmed Lessons
- **Misleading `reachable` Flag:** The `reachable` flag for Map Sprites in the Game State Information appears to be a global check, not a local pathing check. In segmented maps like Silph Co., an item can be marked as `reachable: yes` even if it's in a completely separate, inaccessible area. I must rely on visual confirmation and my fixed `map_segment_analyzer` tool.
- **MUK's Immunity:** MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).

### B. Tool Development Log (`map_segment_analyzer`)
- **v2-v4 Flaws:** Initial versions of the tool had critical logic errors, failing to perform a proper BFS and incorrectly handling segmented maps with `closed_gate` tiles. This led to multiple wasted turns and incorrect exploration plans.
- **v5 Corrective Action (T33242):** The tool was updated to correctly treat `closed_gate` tiles as impassable, which should now allow it to accurately analyze segmented map areas. Awaiting final verification.

### C. Open Puzzles & Hypotheses (NEW)
1.  **5F Gate Puzzle:** The southern gates are controlled by the player's X-coordinate in the northern corridor (Y=2). The exact mechanism is still unknown. **Test:** Systematically walk from X=18 to X=9 in the northern corridor, checking the state of all southern gates at each step to map the trigger conditions.
2.  **CARD KEY Location:** The key is likely behind one of the puzzles in Silph Co. The item at (22, 17) on 5F is a prime candidate, but is in a currently inaccessible segment.
3.  **Giovanni's Location:** He is likely on the 11th floor behind the doors that require the CARD KEY. **Test:** Find the key, then return to 11F and attempt to open the doors at (7,7) or (11,7).