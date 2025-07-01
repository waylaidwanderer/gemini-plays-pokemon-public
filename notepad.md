## I. Core Protocols & Immediate Actions (v38859)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure. This is my highest priority.
- **CRITICAL: WKG Protocol (v11 - Manual Multi-Turn Process):** Upon any map transition, I will immediately begin the WKG update process. **Turn 1:** `manage_world_knowledge('add_node', ...)` to create the source node. **Turn 2:** `manage_world_knowledge('add_node', ...)` to create the destination node. **Turn 3:** `manage_world_knowledge('add_edge', ...)` to create the connection using the IDs from the previous turns. This must be done without fail.
- **CRITICAL: Map Marker Protocol (v8):** Mark defeated trainers, used warps (both entry and exit), and confirmed dead ends *immediately*. **DO NOT MARK MAP-EDGE TRANSITIONS.** These are handled exclusively by the World Knowledge Graph.
- **CRITICAL: WKG Coordinate Accuracy:** I MUST use the exact arrival coordinates provided in the `GameStatus` immediately after a transition. Hallucinating coordinates is a primary source of navigational failure.
- **CRITICAL: Agent & Tool Maintenance:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the **ABSOLUTE HIGHEST PRIORITY**, superseding ALL other gameplay objectives.

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
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).
- **Silph Co. Gate Mechanic:** Gates in Silph Co. appear to be controlled by the player's X-coordinate in a corresponding, physically separate corridor.
- **Cycling Road Movement:** It is not possible to get off the Bicycle on Route 17. It is a one-way path forcing movement south.

## III. Investigation & Hypothesis Log (v38859)
- **Primary Plan:** Obtain the Soul Badge. Current strategy is to explore the Safari Zone to find key items (HM Surf, Gold Teeth) that may be required for gym access or progression.
- **Hypothesis (Disproven, T38440):** The path through the newly discovered cuttable tree area on Route 14 leads to Fuchsia City. **Result:** This path is a small, dead-end loop.
- **Hypothesis (Disproven, T38833):** The cuttable tree at (23,8) in Fuchsia City is a valid path. **Result:** The tile is not a cuttable tree.

## IV. Past Failures & Corrections Log
- **CRITICAL PROCESS FAILURE: Repeated WKG Protocol Violations (T37321 - T38858):** I have a persistent behavioral issue of failing to immediately and correctly document map transitions. This corrupts my world model and leads to severe navigational errors and multi-turn failures. **Correction:** ALL data management tasks (`manage_world_knowledge`, `define_map_marker`, `notepad_edit`) MUST be performed on the same turn a discovery is made. I will follow the manual multi-turn WKG protocol until the automation tool is built.
- **Navigational Failure (Route 14, T38161):** I incorrectly believed the path to Fuchsia City was through the southern part of Route 14. This was confirmed to be a one-way dead end for northbound travel. The correct path was through Route 17 and 18.

## V. Immediate Development Priorities
- **HIGHEST PRIORITY: WKG Connection Manager Tool:** The repeated, catastrophic failures in manually updating the WKG (T38841-38858) prove that automation is non-negotiable. I will define a tool named `wkg_connection_manager` that takes source and destination map/coordinate info and handles the entire node/edge creation process in a single, reliable call. This will eliminate a major source of error and inefficiency. This is my top priority outside of critical story progression.