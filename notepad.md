## I. Core Protocols & Immediate Actions (v41338)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **CRITICAL: WKG Protocol (v17 - Numeric ID Mandate):** I will follow a strict three-step process using **numeric map IDs only**. **Step 1: Node Verification.** Query the WKG to ensure both source and destination nodes exist. If a node is missing, add it. **Step 2: Edge Verification.** After confirming both nodes exist, query for an edge. **Step 3: Edge Creation.** Only if no edge exists will I create one. This protocol prevents graph corruption.
- **CRITICAL: Map Marker Protocol (v9):** Mark defeated trainers, used warps (entry and exit), and confirmed dead ends *immediately*. **DO NOT MARK MAP-EDGE TRANSITIONS.** These are handled exclusively by the World Knowledge Graph.
- **CRITICAL: Agent Usage Protocol (v2):** Agents are for **reasoning and high-level strategy**, not for computational tasks like tile-by-tile pathfinding. If I am stuck on navigation, I will use my `exploration_strategist_agent` or a dedicated computational tool.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison), Flying > Grass/Poison (super-effective).
- **Type Immunities:** Psychic is immune to Electric. Flying-type is immune to Ground-type moves. MUK is immune to Poison-type moves.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Battle Mechanics:** Multi-hit moves (e.g., FURY ATTACK) are a critical threat and can bypass the "sturdy" effect of surviving on 1 HP.
- **Ghost-Type Effectiveness:** Ghost-type moves (like Lick) are effective against Rock/Ground-types.

### B. General Field Mechanics
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **HM & Field Move Mechanics:** Flash, Cut, and Fly MUST be taught to a Pokémon to be used in the field. PC Interaction must be activated from the tile directly below the PC (Y+1), facing up.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any Pokémon that participated by switching in.
- **Battle Initiation Mechanics:** To battle a trainer on an adjacent tile, you must face them and press 'A' to interact.
- **NPC Interaction Catch:** Some NPCs, upon interaction, can trigger a Pokémon 'catch' event, adding the Pokémon directly to the player's Pokédex and party/PC. (Observed with Rocker in Safari Zone East Rest House giving a CHANSEY).
- **Safari Game Time Limit:** The Safari Game has a time limit. When it expires, the player is automatically warped back to the Safari Zone Gate.
- **PC Box Full Mechanic:** When a Pokémon is caught and the active PC box is full, the caught Pokémon is still sent to the PC, but a warning is displayed. I must remember to manually change the active box at a Pokémon Center.

### C. Tile Traversal & Map Mechanics
- **`ground`:** A standard, walkable tile.
- **`grass`:** Walkable tile with wild Pokémon encounters.
- **`impassable`:** Walls, objects, and other non-traversable tiles.
- **`water`:** Requires SURF to cross. Currently impassable.
- **`cuttable`:** A tree that can be cut with HM Cut. Becomes `ground` after cutting but respawns after a short time, even without leaving the map.
- **`steps`:** Allows **vertical-only** movement between `ground`, `grass`, and `elevated_ground`.
- **`ledge`:** Can only be traversed downwards (from Y-1 to Y+2 in a single button press). Acts as an impassable wall from all other directions.
- **`warp`:** A tile that transports the player to another location. Some are instant, others require an additional button press.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered in Silph Co. 9F at (12, 2), Safari Zone East at (17, 23), and Fuchsia Gym.
- **Hidden Passages:** Seemingly impassable tiles that are actually traversable. Discovered in Safari Zone East at (7, 25).
- **Impassable Roofs:** Building roofs, even if visually over traversable ground, can act as impassable walls when approached from above. (Discovered on Route 19 at (6, 9)).
- **Summer Beach House Trap:** The house on Route 19 at (6, 10) is a one-way trap. The entrance warp is one-way, and Fly cannot be used to escape. The intended solution is to walk *through* Pikachu to reach the southern exit warp.

### D. Investigation & Hypothesis Log
- **Current Plan:** A sign in Safari Zone North mentioned a 'SECRET HOUSE' with a free HM. This is almost certainly SURF. My current objective is to explore the Safari Zone areas to find this house. I also need to find the Gold Teeth for the Warden.

### E. Defeated Bosses Log
- **Koga (Fuchsia Gym):** GOLBAT (Lv. 42), MUK (Lv. 42, knows MEGA DRAIN, ACID ARMOR), TENTACRUEL (Lv. 41, knows SURF, ICE BEAM), VENOMOTH (Lv. 43, knows PSYCHIC)

## III. System & Tool Development
### A. Tool Debugging & Refinement Protocol (v3 - IMMEDIATE ACTION)
- **CRITICAL:** If a custom tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. Deleting tools or resorting to manual workarounds is a protocol violation.
- **DEBUGGING STEP 1:** Use `run_code` with extensive `print()` statements to trace execution and identify the point of failure.
- **DEBUGGING STEP 2:** Use `define_tool` to submit a corrected version of the script.

### B. Current Tool Development Plan (T41338)
- **WKG Analyst Agent Idea (PENDING):** An agent that analyzes the `world_knowledge_graph_json_string` to suggest the most promising unexplored connections or identify potential sequence breaks. This will be useful if I become completely stuck.
- **Tool Debugger Agent Idea (PENDING):** An agent to automate the analysis of `run_code` debug traces to speed up the debugging process.