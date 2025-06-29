## I. Core Protocols & Immediate Actions (v44)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays.
- **CRITICAL: WKG Protocol:**
  - Before adding any node or edge, I will FIRST query the WKG with `run_code` (or a future tool) to confirm it doesn't already exist.
  - All `warp` type edges MUST include a `destination_entry_point` if known. All new nodes MUST have descriptive `tags`.
- **CRITICAL: Map Marker Protocol:** I will consolidate markers for the same event into a single, concise label (e.g., '🚪 To/From [Location]').
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents for complex reasoning and my custom tools for computational tasks. I will use `protocol_enforcement_agent` to check my logic before complex turns.
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
- **`reachable` Flag is Global:** The `reachable` flag for warps and map sprites is a global check for the entire map, NOT a local check based on the player's current isolated segment. I must use `map_segment_analyzer` to determine local reachability.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **Teleporter Tiles:** Instant warps. Stepping on them immediately transports the player.
- **Closed Gates:** Impassable tiles that block movement until a specific trigger or puzzle is solved.
- **Dynamic Gates (Silph Co. 5F):** The southern gates on 5F open and close based on the player's X-coordinate in the northern corridor (Y=2).
- **Spinner Tiles:** Force movement in a specific direction. Encountered in Rocket Hideout.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).

### D. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35, 4 badges: 43.

### E. HM & Field Move Mechanics
- **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.

### F. Key Items Obtained
- **SUPER ROD:** From Fishing Guru in house on Route 12 (accessed via warp at (12, 78)).

## III. Agent & Tool Development Log (v74)
### A. Development Priorities
- **New Tool Idea: `pc_navigator`:** A tool to generate a sequence of button presses to navigate the Pokémon PC menu for depositing and withdrawing Pokémon.
- **New Tool Idea: `object_finder`:** A tool to find the coordinates of a named NPC or item on the current map.
- **New Tool Idea: `wkg_checker`:** A tool to check if a specific node or edge already exists in the World Knowledge Graph.
- **Agent Refinement Idea: `floor_strategist_agent`:** Refine prompt to de-prioritize non-essential NPCs like Pikachu.
### B. Active Agents & Tools
- `team_composition_advisor_agent` (v2) - Reliable
- `protocol_enforcement_agent` (v1) - Reliable
- `battle_strategist_agent` (v10) - Reliable
- `pathfinder` (v2) - Newly improved to ignore impassable types.

## IV. Silph Co. Investigation Log (v6)
### A. Confirmed Intel & Lessons Learned
- **MUK's Immunity:** MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Bugged Rocket (5F West):** The Rocket at (9,17) in the western segment of 5F is bugged and soft-locks progress. The only exit is the teleporter back to 9F.
- **Boardroom Location:** A Rocket on 10F at (2,10) confirmed the boardroom is on the 11th floor.

### B. Solved Puzzles
- **Solved: 5F Gate Puzzle:** The gates in the southern corridor are controlled by the player's X-coordinate in the northern corridor (Y=2). Standing at X=11-13 opens the western gates. Standing at X=14-16 opens the eastern gates.

### C. Open Puzzles & Hypotheses
- **CARD KEY Location (Hypothesis):** The key is likely an item somewhere in Silph Co. The item at (22, 17) on 5F is blocked by impassable objects. The item at (5,7) on 5F is blocked by a closed gate.
- **Giovanni's Location (Hypothesis):** He is on the 11th floor behind the doors that require the CARD KEY.
- **New Agent Idea: `puzzle_solver_agent`:** An agent to analyze map state and documented hypotheses to suggest the next logical step in solving complex puzzles, like the Silph Co. gate puzzle.
- **Solved: 5F Gate Puzzle:** The gates in the southern corridor are controlled by the player's X-coordinate in the northern corridor (Y=2). Standing at X=11-13 opens the western gates. Standing at X=14-16 opens the eastern gates.