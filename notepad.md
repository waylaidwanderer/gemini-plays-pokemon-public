## I. Core Protocols & Immediate Actions (v39118)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure. This is my highest priority.
- **CRITICAL: WKG Protocol (v12 - Tool-Assisted Process):** Upon any map transition, I will immediately use the `wkg_connection_manager` tool. In the following turns, I will execute the `manage_world_knowledge` calls it outputs, in order, without fail.
- **CRITICAL: Map Marker Protocol (v8):** Mark defeated trainers, used warps (both entry and exit), and confirmed dead ends *immediately*. **DO NOT MARK MAP-EDGE TRANSITIONS.** These are handled exclusively by the World Knowledge Graph.
- **CRITICAL: WKG Coordinate Accuracy:** I MUST use the exact arrival coordinates provided in the `GameStatus` immediately after a transition. Hallucinating coordinates is a primary source of navigational failure.
- **CRITICAL: Tool Debugging Protocol:** If a custom tool is suspected to be faulty, the **first and only** debugging step is to use `run_code` with extensive `print()` statements to trace its execution and identify the point of failure. Blindly redefining the tool is a waste of turns and a violation of this protocol.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison), Flying > Grass/Poison (super-effective).
- **Type Immunities:** Psychic is immune to Electric. Pidgeotto (Normal/Flying) is immune to Ghost-type moves like Confuse Ray.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Poison Type Effectiveness:** Poison-type moves are NOT-VERY-EFFECTIVE against Poison-types.
- **Battle Mechanics:** Multi-hit moves (e.g., FURY ATTACK) are a critical threat and can bypass the "sturdy" effect of surviving on 1 HP.

### B. General Field Mechanics
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **HM & Field Move Mechanics:** Flash, Cut, and Fly MUST be taught to a Pokémon to be used in the field. PC Interaction must be activated from the tile directly below the PC (Y+1), facing up.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any Pokémon that participated by switching in.
- **Battle Initiation Mechanics:** To battle a trainer on an adjacent tile, you must face them and press 'A' to interact.

### C. Tile Traversal & Map Mechanics
- **`ground`:** Standard walkable tile.
- **`grass`:** Walkable tile with wild encounters.
- **`impassable`:** Walls, objects, etc. Cannot be entered.
- **`ledge`:** Can only be jumped down (from Y-1 to Y+1). Acts as a wall from all other directions.
- **`cuttable`:** A tree that can be cut with HM Cut. Becomes `ground` after cutting but respawns after a short time, even without leaving the map.
- **`water`:** Requires Surf to cross.
- **`warp`:** A tile that transitions the player to a new map or a different location on the same map.
- **`steps`:** Allows vertical movement between `ground`, `grass`, and `elevated_ground`. My `pathfinder` tool has struggled with this tile type, indicating complex traversal rules.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered in Silph Co. 9F at (12, 2) and Safari Zone East at (17, 23).

### D. System & Tool Development
- **`pathfinder` (Tool):** This tool has been repeatedly buggy, especially with `steps` tile logic. This has caused significant navigational delays. Continuous refinement is the top priority.
- **(Idea) `tool_debugger_agent`:** A potential future agent that could take a tool's code and a test case to suggest debugging steps or identify logical flaws.

## III. Investigation & Hypothesis Log (v39118)
- **Primary Plan:** Obtain the Soul Badge. Current strategy is to explore the Safari Zone to find key items (HM Surf, Gold Teeth) that may be required for gym access or progression.
- **Hypothesis (Disproven, T38440):** The path through the newly discovered cuttable tree area on Route 14 leads to Fuchsia City. **Result:** This path is a small, dead-end loop.
- **Hypothesis (Disproven, T38833):** The cuttable tree at (23,8) in Fuchsia City is a valid path. **Result:** The tile is not a cuttable tree.
- **Hypothesis (Proven, T38906):** The sign in Safari Zone East pointing north to 'Area 2' indicates the path forward. **Result:** The only path to the northern section is via the steps at (13, 22).
- **Hypothesis (Proven, T39118):** The grassy area in Safari Zone East entered via the warp at (1, 23) is isolated and cannot be exited on foot to other parts of the map. **Result:** Pathfinder repeatedly failed to find a path to any other section, confirming isolation. The only exit is the warp itself.

## IV. Past Failures & Corrections Log
- **CRITICAL PROCESS FAILURE: Repeated WKG Protocol Violations (T37321 - T38886):** I have a persistent behavioral issue of failing to immediately and correctly document map transitions. This corrupts my world model and leads to severe navigational errors and multi-turn failures. **Correction:** I will use my `wkg_connection_manager` tool for ALL transitions and follow its multi-turn output precisely. This is non-negotiable.
- **Navigational Failure (Route 14, T38161):** I incorrectly believed the path to Fuchsia City was through the southern part of Route 14. This was confirmed to be a one-way dead end for northbound travel. The correct path was through Route 17 and 18.
- **Tool Trust & Debugging Failure (Pathfinder, T39001-T39117):** I wasted numerous turns attempting to debug the `pathfinder` tool. This was a critical failure to follow my own protocol of trusting my tools over my visual assessment. My debugging process for the tool was also inefficient, taking multiple turns instead of a single, focused debugging session. **Correction:** I must trust my tools' outputs. If a tool reports a path is blocked, I will believe it and find an alternative route. If a tool is truly bugged, I will perform a comprehensive, single-turn debugging session using `run_code` with print statements before redefining it.