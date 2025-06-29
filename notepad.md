## I. Core Protocols & Immediate Actions (v55)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays. Lapses, like on turn 35849, are unacceptable and will be corrected.
- **CRITICAL: WKG Protocol:**
  - Before adding any node or edge, I will FIRST query the WKG with my `wkg_checker` tool to confirm it doesn't already exist.
  - All `warp` type edges MUST include a `destination_entry_point` if known. This value is the 1-indexed entry point on the *destination* map's warp list. All new nodes MUST have descriptive `tags`.
- **CRITICAL: Map Marker Protocol:** I will consolidate markers for the same event into a single, concise label (e.g., '🚪 To/From [Location]').
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents for complex reasoning and my custom tools for computational tasks. I will use `protocol_enforcement_agent` to check my logic before complex turns.
- **CRITICAL: Tool Input Verification:** I will ALWAYS double-check the coordinates and other inputs I provide to my custom tools BEFORE execution.
- **CRITICAL: Post-Event Checklists (MANDATORY):**
  - **Trainer Battle:** Mark defeated trainer with '☠️' and log their Pokémon under 'Trainer Intel'.
  - **Wild Encounter:** Log EVERY wild Pokémon with `encounter_tracker_agent`.
  - **Map Transition (Warp/Stairs/Edge):** Immediately use `manage_world_knowledge` to document the connection and mark used warps (entry/exit) with '🚪'.
- **CRITICAL: Tool Maintenance Protocol:** If a custom tool is found to be faulty or bugged, fixing it becomes the highest priority secondary goal, superseding other gameplay objectives until resolved.

## II. Current Mission: Liberate Silph Co.
### A. Active Training Plan (vs. Pixel v2)
- **Core Team:** CRAG, SPARKY, ECHO, SPOONBENDE.
- **Training Goal:** Level all core members to the level cap of 43.
- **Training Locations:**
  - **SPARKY:** Route 12 (vs. Water-types).
  - **ECHO:** Diglett's Cave (vs. Diglett/Dugtrio for high EXP and immunity).
  - **SPOONBENDE:** Route 13 (vs. Venonat, Bellsprout, Oddish).
  - **CRAG:** Route 11 (vs. Spearow, Rattata).

## III. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison).
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Poison Type Effectiveness:** Poison-type moves are NOT-VERY-EFFECTIVE against Poison-types.

### B. Battle Protocols (v4)
- **Agent Reliance (MANDATORY):** I will use the `battle_strategist_agent` for all significant battles (Gyms, Rival, unique encounters) to ensure optimal move selection. The agent has been refined and is now reliable.

### C. Navigation & Traversal Rules
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **`reachable` Flag is Global:** The `reachable` flag for warps and map sprites is a global check for the entire map, NOT a local check based on the player's current isolated segment.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).
- **HM & Field Move Mechanics:**
    - **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.
    - **PC Interaction:** Must be activated by standing on the tile directly below the PC object (Y+1), facing up, and then pressing A.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle (the lead) and any Pokémon that participated by switching in. Both ECHO (lead) and SPOONBENDE (switched in) gained EXP from the Weepinbell battle.
- **Route 13 Fences:** The maze on Route 13 is lined with impassable fence tiles that my navigation tools are currently failing to account for, leading to invalid paths.

## IV. Tool Development Log (v97)
### A. Development Pipeline
- **TOP PRIORITY: `pathfinder` (BUG FIX):** Per AI feedback and repeated failures on Route 13 (T#35999), this tool is unreliable and generates invalid paths through impassable fences. Fixing this is now the highest priority development task.
- **TOP PRIORITY: `wkg_manager_tool` (New):** Per AI feedback, create a single tool to handle the entire 'check-then-add' logic for a map transition (nodes and edge) atomically to improve efficiency and reduce errors.
- **HIGH PRIORITY: `dungeon_navigator` (BUG FIX):** Per AI feedback, I must adhere to my own protocol and prioritize fixing this bugged tool. It generated a non-viable path on Route 13. I will address this immediately after fixing `pathfinder`.
- **NEW: `encounter_grinder_tool` (New):** Define a tool to automate pacing back and forth in a specified area to efficiently trigger wild encounters for training. This will replace my inefficient manual grinding.
- **New Agent Idea: `puzzle_solver_agent`:** An agent (not a tool) to analyze map state and documented hypotheses to suggest the next logical step in solving complex puzzles. This is a reasoning task, better suited for an agent.
- **New Agent Idea: `pc_navigator_agent`:** An agent to generate button sequences to operate the Pokémon PC menu for depositing and withdrawing Pokémon. This will automate a tedious, repetitive task.

### B. Active Agents & Tools
- `team_composition_advisor_agent` (v2) - Reliable
- `protocol_enforcement_agent` (v1) - Reliable
- `battle_strategist_agent` (v11) - Refined and reliable.

- `select_battle_option` (v1) - Reliable
- `pathfinder` (v3) - **BUGGED:** Fails to navigate simple fence obstacles on Route 13. DO NOT USE FOR NAVIGATION UNTIL FIXED.
- `object_finder` (v1) - Reliable
- `wkg_checker` (v3) - Reliable

## V. Silph Co. Investigation Log (v12)
### A. Confirmed Intel & Lessons Learned
- **MUK's Immunity:** MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Bugged Rocket (5F West):** The Rocket at (9,17) in the western segment of 5F is bugged and soft-locks progress. The only exit is the teleporter back to 9F.
- **Boardroom Location:** A Rocket on 10F at (2,10) confirmed the boardroom is on the 11th floor.

### B. Solved Puzzles
- **Solved: 5F Gate Puzzle:** The gates in the southern corridor are controlled by the player's X-coordinate in the northern corridor (Y=2). Standing at X=11-13 opens the western gates. Standing at X=14-16 opens the eastern gates. The corridors are physically separated, requiring a teleporter to cross.

### C. Untested Assumptions & Hypotheses
- **Battle Mechanic Anomaly:** During the battle with Pixel's Dodrio on Silph Co. 7F, Dodrio used Fly, but the game displayed "But, it failed!". My subsequent move, Confuse Ray, also failed. The turn then reset to the main battle menu, with Dodrio not in the air. The reason for these failures is unknown.
- **Pokémon Tower 5F Healer:** The friendly Channeler at (13, 9) only restores Pokémon HP, NOT PP. Confirmed on turn 35402.
- **Silph Co. Gate Mechanic:** Gates in Silph Co. appear to be controlled by the player's X-coordinate in a corresponding, physically separate corridor. Standing in a specific range of X coordinates opens a specific set of gates.
- **Trainer Intel Logging (Post-Battle):** I missed logging the team for Cool Trainer M on Route 13 (T#35906) due to a reflection turn. This is a failure of protocol. I will ensure all future trainer teams are logged immediately after battle.

## VI. Trainer Intel (Overworld)
### Route 13
- Biker (@ 11,8): SHELLDER (Lv.29), WEEZING (Lv.29), CLOYSTER (Lv.29)
- **Route 13 Fences:** The maze on Route 13 is lined with impassable fence tiles that my navigation tools are currently failing to account for, leading to invalid paths.