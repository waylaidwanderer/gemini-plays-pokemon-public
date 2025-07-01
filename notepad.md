## I. Core Protocols & Immediate Actions (v39898)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **CRITICAL: WKG Protocol (v16 - Three-Step Verification):** My manual WKG management has been error-prone. I will now follow a strict three-step process. **Step 1: Node Verification.** I will first query the WKG to ensure both source and destination nodes exist. If a node is missing, I will add it using `manage_world_knowledge` with the `add_node` action and descriptive tags. **Step 2: Edge Verification.** After confirming both nodes exist, I will query for an edge between them. **Step 3: Edge Creation.** Only if no edge exists will I create one. This protocol prevents graph corruption.
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
- **`cuttable`:** A tree that can be cut with HM Cut. Becomes `ground` after cutting but respawns after a short time, even without leaving the map.
- **`steps`:** Allows **vertical-only** movement between `ground`, `grass`, and `elevated_ground`.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered in Silph Co. 9F at (12, 2) and Safari Zone East at (17, 23).
- **Hidden Passages:** Seemingly impassable tiles that are actually traversable. Discovered in Safari Zone East at (7, 25).

### D. Investigation & Hypothesis Log
- **Current Plan:** Fully explore the Safari Zone. The trainers on Route 19 proved to be too high-level, indicating it's not the correct path for now. My new primary objective is to find any key items (such as HM Surf or the Gold Teeth) that may be located within the Safari Zone to enable further progress.
- **Hypothesis (Active):** The Safari Zone contains key items required to access the area where the Soul Badge is located. The path south from Fuchsia City via Route 19 is a late-game area I am not yet prepared for.

## III. System & Tool Development
### A. Tool Debugging Protocol (v2)
- **CRITICAL:** If a custom tool is suspected to be faulty, the **first and only** debugging step is to use `run_code` with extensive `print()` statements to trace its execution and identify the point of failure. Blindly redefining the tool is a waste of turns and a violation of this protocol.

### B. Development Failures & Lessons
- **Systematic Tile Testing:** I must be more rigorous in testing and documenting the behavior of every new tile type I encounter. This includes confirming impassable tiles by attempting to walk into them from multiple directions and recording the results.
- **Impassable Roofs:** Building roofs, even if visually over traversable ground, can act as impassable walls when approached from above. (Discovered on Route 19 at (6, 9)).
- **Summer Beach House Trap:** The house on Route 19 at (6, 10) is a one-way trap. The entrance warp is one-way, and Fly cannot be used to escape. The only way out is to use the southern exit warp.