## I. Core Protocols & Immediate Actions (v41861)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **CRITICAL: WKG Protocol (v19 - Entry Point Mandate):** I will follow a strict three-step process using numeric map IDs only. Step 1: Node Verification. Query the WKG to ensure both source and destination nodes exist. If a node is missing, add it. Step 2: Edge Verification. After confirming both nodes exist, query for an edge. Step 3: Edge Creation. Only if no edge exists will I create one, ensuring I include the `destination_entry_point` for all warp-type connections. This protocol prevents graph corruption.
- **CRITICAL: Map Marker Protocol (v9):** Mark defeated trainers, used warps (entry and exit), and confirmed dead ends *immediately*. **DO NOT MARK MAP-EDGE TRANSITIONS.** These are handled exclusively by the World Knowledge Graph.
- **CRITICAL: Agent & Tool Protocol (v3 - REVISED):** Agents are for **reasoning and high-level strategy**. Computational tasks (e.g., pathfinding, data parsing) MUST be handled by `run_code` or a custom tool defined with `define_tool`.

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

### C. Map Mechanics Discoveries
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered in Silph Co. 9F at (12, 2), Safari Zone East at (17, 23), and Fuchsia Gym.
- **Hidden Passages:** Seemingly impassable tiles that are actually traversable. Discovered in Safari Zone East at (7, 25).
- **Impassable Roofs:** Building roofs, even if visually over traversable ground, can act as an impassable wall when approached from above. (Discovered on Route 19 at (6, 9)).
- **Summer Beach House Trap:** The house on Route 19 at (6, 10) is a one-way trap. The entrance warp is one-way, and Fly cannot be used to escape. The intended solution is to walk *through* Pikachu to reach the southern exit warp.

### D. Investigation & Hypothesis Log
- **Current Plan:** Systematically explore the Safari Zone to find the 'SECRET HOUSE' (likely containing HM SURF) and the Warden's lost GOLD TEETH. I will prioritize exploring the western area first, as I was interrupted there last time.

### E. Defeated Bosses Log
- **Koga (Fuchsia Gym):** GOLBAT (Lv. 42), MUK (Lv. 42, knows MEGA DRAIN, ACID ARMOR), TENTACRUEL (Lv. 41, knows SURF, ICE BEAM), VENOMOTH (Lv. 43, knows PSYCHIC)

## III. System & Tool Development
### A. Tool Debugging & Refinement Protocol (v4 - IMMEDIATE ACTION & SYSTEMATIC DEBUGGING)
- **CRITICAL:** If a custom tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. **Abandoning a tool is a protocol violation.**
- **DEBUGGING STEP 1:** Use `run_code` with extensive `print()` statements to trace execution, inspect variables, and isolate the exact point of failure. Avoid iterative guesswork.
- **DEBUGGING STEP 2:** Use `define_tool` to submit a corrected version of the script based on systematic analysis.

### B. Pathfinder Tool Development Log (T41755-T41806)
- **Initial Protocol Violation (T41483):** I deleted the faulty `pathfinder` tool instead of debugging it. This was a direct cause of my navigational issues.
- **Systematic Debugging (T41755-T41806):** After acknowledging my protocol violation, I engaged in a multi-turn, systematic debugging process. I used diagnostic scripts to isolate the error, eventually rebuilding the tool with a robust BFS algorithm that correctly handles elevation changes. This process, while lengthy, restored a critical capability and reinforced the importance of my debugging protocol.

## IV. Tile Mechanics & Traversal Rules
- **`elevated_ground`:** Walkable ground at a different elevation. Cannot be accessed directly from `ground` or `grass` tiles.
- **`steps`:** Allows vertical movement between `ground`/`grass` and `elevated_ground` tiles.
- **`ledge`:** Can only be traversed downwards. Moving onto a ledge from above (Y-1) will place the player on the tile below the ledge (Y+2).