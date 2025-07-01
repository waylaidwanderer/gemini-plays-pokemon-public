## I. Core Protocols & Immediate Actions (v39481)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **CRITICAL: WKG Protocol (v15 - Two-Step Verification):** My manual WKG management has been error-prone. I will now follow a strict two-step process. **Step 1: Node Verification.** I will first query the WKG to ensure both source and destination nodes exist. If a node is missing, I will add it using `manage_world_knowledge` with the `add_node` action and descriptive tags. **Step 2: Edge Creation.** Only after confirming both nodes exist will I create the edge connecting them. This protocol prevents graph corruption.
- **CRITICAL: Map Marker Protocol (v8):** Mark defeated trainers, used warps (both entry and exit), and confirmed dead ends *immediately*. **DO NOT MARK MAP-EDGE TRANSITIONS.** These are handled exclusively by the World Knowledge Graph.
- **CRITICAL: Agent Usage Protocol (v2):** Agents are for **reasoning and high-level strategy**, not for computational tasks like tile-by-tile pathfinding. If I am stuck on navigation, I will use my `exploration_strategist_agent` or a dedicated computational tool. Misusing an agent is a protocol violation.

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
- **NPC Interaction Catch:** Some NPCs, upon interaction, can trigger a Pokémon 'catch' event, adding the Pokémon directly to the player's Pokédex and party/PC. (Observed with Rocker in Safari Zone East Rest House giving a CHANSEY).
- **Safari Game Time Limit:** The Safari Game has a time limit. When it expires, the player is automatically warped back to the Safari Zone Gate.
- **PC Box Full Mechanic:** When a Pokémon is caught and the active PC box is full, the caught Pokémon is still sent to the PC, but a warning is displayed. I must remember to manually change the active box at a Pokémon Center to continue storing new Pokémon.

### C. Tile Traversal & Map Mechanics
- **`ground` / `grass` / `elevated_ground`:** Standard walkable tiles.
- **`impassable`:** Walls, objects, etc. Cannot be entered.
- **`ledge`:** Can only be jumped down (from Y-1 to Y+1). Acts as a wall from all other directions.
- **`cuttable`:** A tree that can be cut with HM Cut. Becomes `ground` after cutting but respawns after a short time, even without leaving the map.
- **`water`:** Requires Surf to cross.
- **`warp`:** A tile that transitions the player to a new map or a different location on the same map.
- **`steps`:** Allows **vertical-only** movement between `ground`, `grass`, and `elevated_ground`.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered in Silph Co. 9F at (12, 2) and Safari Zone East at (17, 23).
- **Hidden Passages:** Seemingly impassable tiles that are actually traversable. Discovered in Safari Zone East at (7, 25).

### D. Investigation & Hypothesis Log
- **Current Plan:** Obtain the Soul Badge. Current strategy is to explore the Safari Zone to find key items (HM Surf, Gold Teeth) that may be required for gym access or progression.
- **Hypothesis (Active):** The game state's `Reachable Unseen Tiles` and `Reachable Unvisited Warps` lists indicate the path forward is on the current map (Safari Zone East). I am currently pivoting to explore the western side of the map.

## III. System & Tool Development
### A. Tool Debugging Protocol (v2)
- **CRITICAL:** If a custom tool is suspected to be faulty, the **first and only** debugging step is to use `run_code` with extensive `print()` statements to trace its execution and identify the point of failure. Blindly redefining the tool is a waste of turns and a violation of this protocol.

### B. Development Failures & Lessons
- **CRITICAL FAILURE (Pathfinder, T39001-T39221):** I wasted over 50 turns attempting to debug the `pathfinder` tool with blind, iterative redefinitions. This was a catastrophic failure to follow my own protocol. The root cause, discovered only after a `run_code` debug session, was a `ModuleNotFoundError` for the `xml` library, which is not supported in the tool execution environment. **Lesson:** The `pathfinder` tool is fundamentally unfixable. I will never again attempt to create a tool that requires XML parsing.

### C. Future Development Goals
- Consolidate `navigation_strategist_agent` and `exploration_strategist_agent` into a single, more robust `strategy_agent` to handle all high-level navigation advice and reduce tool redundancy.