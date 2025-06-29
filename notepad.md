## I. Core Protocols & Immediate Actions (v52)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays. Lapses, like on turn 34801, are unacceptable and have been corrected.
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

## II. Game Mechanics & Battle Intel
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

## III. Tool Development Log (v91)
### A. Development Pipeline
- **TOP PRIORITY: `encounter_grinder_tool` (New):** Define a tool to automate pacing back and forth in a specified area to efficiently trigger wild encounters for training. This will replace my inefficient manual grinding.
- **HIGH PRIORITY: `dungeon_navigator` (BUG FIX):** This tool is bugged and quarantined. The current DFS implementation is faulty and needs to be rewritten to ensure it explores all reachable tiles correctly. DO NOT USE UNTIL FIXED.
- **New Agent Idea: `puzzle_solver_agent`:** An agent (not a tool) to analyze map state and documented hypotheses to suggest the next logical step in solving complex puzzles. This is a reasoning task, better suited for an agent.
- **Tool Refinement Idea: `pathfinder`:** Needs to be updated to better handle moving NPCs, or I need a new protocol for dealing with them (like using `stun_npc`).

### B. Active Agents & Tools
- `team_composition_advisor_agent` (v2) - Reliable
- `protocol_enforcement_agent` (v1) - Reliable
- `battle_strategist_agent` (v11) - Refined and reliable.

- `select_battle_option` (v1) - Reliable
- `pathfinder` (v3) - Refined to handle NPCs, reliable.
- `object_finder` (v1) - Reliable
- `wkg_checker` (v3) - Reliable

## IV. Silph Co. Investigation Log (v12)
### A. Confirmed Intel & Lessons Learned
- **MUK's Immunity:** MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Bugged Rocket (5F West):** The Rocket at (9,17) in the western segment of 5F is bugged and soft-locks progress. The only exit is the teleporter back to 9F.
- **Boardroom Location:** A Rocket on 10F at (2,10) confirmed the boardroom is on the 11th floor.

### B. Solved Puzzles
- **Solved: 5F Gate Puzzle:** The gates in the southern corridor are controlled by the player's X-coordinate in the northern corridor (Y=2). Standing at X=11-13 opens the western gates. Standing at X=14-16 opens the eastern gates. The corridors are physically separated, requiring a teleporter to cross.

### C. Untested Assumptions & Hypotheses
- **Assumption 1 (From Silph Co.):** The teleporter at (6, 8) on 7F is the correct path forward after defeating Pixel.
  - **Test:** After the battle, navigate to and use the teleporter.
- **Assumption 2 (From Silph Co.):** Defeating Pixel is the only way to proceed.
  - **Test:** If stuck after the battle, re-explore the floor for other triggers.
- **Assumption 3 (High Priority Test):** My `pc_navigator_agent` will work correctly. **Test:** Use the agent the next time I need to access the PC to swap Pokémon.
- **Assumption 4 (New):** My current team composition, once leveled, will be sufficient for clearing Silph Co.
  - **Test:** This will be validated upon my return to Silph Co. If I am defeated again, I will use the `team_composition_advisor_agent` to re-evaluate my party.
- **Battle Mechanic Anomaly:** During the battle with Pixel's Dodrio on Silph Co. 7F, Dodrio used Fly, but the game displayed "But, it failed!". My subsequent move, Confuse Ray, also failed. The turn then reset to the main battle menu, with Dodrio not in the air. The reason for these failures is unknown.
- **CRITICAL: Tool Maintenance Protocol:** If a custom tool is found to be faulty or bugged, fixing it becomes the highest priority secondary goal, superseding other gameplay objectives until resolved.
- **Pokémon Tower 5F Healer:** The friendly Channeler at (13, 9) only restores Pokémon HP, NOT PP. Confirmed on turn 35402.