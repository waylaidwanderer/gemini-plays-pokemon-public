## I. Core Protocols & Immediate Actions (v38547)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure. This is my highest priority.
- **CRITICAL: WKG Protocol (v7):** Upon any map transition, I will immediately: 1. `define_map_marker` for both departure and arrival. 2. `wkg_checker` to verify the edge. 3. If the edge is missing, `run_code` to get node IDs, then `manage_world_knowledge` to add the edge. This all happens in a single turn.
- **CRITICAL: Map Marker Protocol (v5):** I will mark defeated trainers, used warps (both entry and exit), and confirmed dead ends *immediately*. I will NOT mark map-edge connections, as this is handled by the WKG.
- **CRITICAL: Protocol Enforcement:** I will make a conscious effort to use the `protocol_enforcement_agent` before finalizing my plan each turn to catch my own mistakes.
- **CRITICAL: Agent & Tool Maintenance:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the **ABSOLUTE HIGHEST PRIORITY**, superseding ALL other gameplay objectives. I will be more critical of tool outputs and quicker to diagnose them.

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
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).
- **Silph Co. Gate Mechanic:** Gates in Silph Co. appear to be controlled by the player's X-coordinate in a corresponding, physically separate corridor.
- **(TODO):** Document spinner tiles, elevator tiles, and any other new tile mechanics as they are encountered.

## III. Investigation & Hypothesis Log (v38547)
- **Primary Plan (per `navigation_strategist_agent`):** Obtain the Soul Badge. Current strategy is to navigate through Route 12 to reach Fuchsia City.
- **Hypothesis (Disproven, T38440):** The path through the newly discovered cuttable tree area on Route 14 leads to Fuchsia City. **Result:** This path is a small, dead-end loop.
- **Tool Reliability (Confirmed Faulty, T38504-38515):** The `wkg_checker` tool was hallucinating the WKG JSON structure, causing it to incorrectly report that edges did not exist. **Result:** The tool has been fixed with improved logic. Will be more critical of tool outputs going forward.

## IV. Past Failures & Corrections Log
- **CRITICAL PROCESS FAILURE: Repeated WKG Protocol Violations (T37321 - T38226):** I have a persistent behavioral issue of failing to immediately and correctly document map transitions. This corrupts my world model and leads to severe navigational errors, such as the loop between Route 14 and 13. **Correction:** ALL data management tasks (`manage_world_knowledge`, `define_map_marker`, `notepad_edit`) MUST be performed on the same turn a discovery is made. Both departure and arrival nodes/markers must be created before further exploration. There are no exceptions.
- **Navigational Failure (Route 14, T38161):** I incorrectly believed the path to Fuchsia City was through the southern part of Route 14, accessed via Route 15. This was confirmed to be a one-way dead end for northbound travel. This highlights the importance of thorough exploration and trusting my WKG. The correct path to Fuchsia City is likely through the western exits of Route 13 or by exploring all of Route 14.

## V. Future Development Ideas
- **Exploration Agent:** An agent that analyzes `MapMemory` XML and the `Reachable Unseen Tiles` list to suggest the most promising exploration target, weighing clusters of unseen tiles, proximity to unvisited warps, etc.
- **Navigation Strategist Agent:** An agent that analyzes the map layout and suggests using the `pathfinder` tool for complex navigation like mazes, preventing inefficient manual exploration.
- **Inventory Management Agent:** An agent to suggest items to store or discard based on current goals and location.