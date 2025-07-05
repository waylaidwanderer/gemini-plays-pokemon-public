## I. Core Protocols & Immediate Actions (v50101)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure. My WKG updates must be my highest priority upon any map change. I will use a 'check-then-add' protocol, using `find_wkg_node_by_coords` before adding new nodes.
- **CRITICAL: WKG Protocol (v46 - Tags & Standardization):** When documenting a map transition, I will follow this strict workflow: 1. Use the warp/connection. 2. Upon arrival, immediately add a node for the destination, including descriptive `tags` (e.g., `["teleporter"]`, `["stairs", "up"]`). 3. Confirm the source node exists (creating it if necessary). 4. **Empirically test if the warp is bidirectional by immediately attempting to return.** 5. Create the connecting edge, meticulously verifying the **`destination_entry_point`** and setting `is_one_way` based on the test result.
- **CRITICAL: Map Marker Protocol (v22 - Standardization):** I will use standardized emojis and labels for all new markers: '☠️' for defeated trainers, '✅' for picked-up items, and '🚪 Warp to (X, Y) [Direction]' for all warps. This will be placed *immediately*.
- **CRITICAL: Agent & Tool Protocol (v20 - IMMEDIATE Refinement):** Agent and tool refinement is an IMMEDIATE action, not a deferred goal. If an agent or tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. Agents are for reasoning; computational tasks (pathfinding, data parsing) MUST be handled by tools. I will use my `protocol_enforcement_agent` to check my plans before execution.

## II. System & Tool Development
### A. Active Tool Debugging & Refinement (v22 - IMMEDIATE ACTION)
- **CURRENT TASK:** The `get_unvisited_warps` tool is faulty. It failed in the Saffron Gym by incorrectly identifying warps in disconnected rooms as reachable. My immediate priority is to debug and fix this tool.
- **My Debugging Process:**
    1.  **Trace:** Use `run_code` with a modified pathfinding script. Print the `current` node inside the main loop to trace the BFS exploration path.
    2.  **Analyze `came_from`:** If no path is found, print the entire `came_from` dictionary to visualize the full explored area and identify the boundary where pathfinding fails.
    3.  **Boundary Analysis:** If the above is insufficient, use a `run_code` script to parse the `came_from` dictionary and the `map_xml_string`. This script will identify all 'boundary tiles' (unexplored tiles adjacent to explored ones) and print their coordinates and tile types.
    4.  **Implement Fix:** Use `define_tool` to submit a corrected version of the script based on the analysis.
### B. Agent & Tool Usage Notes
- **`pc_navigator_agent`:** Generates a sequence of button presses to navigate the Pokémon PC menu to withdraw or deposit a specific Pokémon. Reliable for PC operations.
- **`battle_strategist_agent`:** Provides battle advice. **STATUS: REFINED.** The agent now correctly validates against fainted, sleeping, and active Pokémon to avoid invalid switch recommendations.

## III. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules (v9)
- **Ledges:** Ledges are one-way only. They can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Water Tiles (Silph Co.):** The water tiles on the first floor of Silph Co. are purely cosmetic and function as `impassable` walls. They cannot be surfed on.
- **Spinner Tiles:** Spinner tiles force movement in a specific direction. I need to map out their destinations to navigate spinner mazes effectively.
- **Gates:** `closed_gate` tiles are impassable. Some are opened by switches, while others (like in Silph Co.) require the CARD KEY.
- **Elevators (Silph Co.):** To use the elevator, you must first interact with the control panel (usually on a wall) to select a destination floor. After selecting a floor, you must walk onto the warp tiles at the back of the elevator room to trigger the map transition.
- **PC Interaction:** To use a Pokémon Center PC, I must stand on the tile directly below it and face up before pressing 'A'.
- **Saffron Gym Teleporters:** These tiles warp the player between rooms. Their destinations need to be mapped systematically.

### B. Confirmed ROM Hack Changes (v12)
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying** (confirmed: KADABRA's PSYBEAM vs ECHO's GOLBAT)
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison).
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **Psychic immune to Electric** (confirmed: SPARKY's THUNDERBOLT vs JYNX); **HYPNO immune to STUN SPORE** (powder moves).

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts (e.g., from MINIMIZE).
- **Struggle:** A Pokémon with 0 PP for all moves will use Struggle, which has low accuracy and causes recoil damage.
- **Multi-Hit Moves:** Moves like FURY ATTACK are a critical threat, bypassing "sturdy" effects.
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **HM Usage:** Flash, Cut, and Fly MUST be taught to a Pokémon to be used in the field.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any that participated via switch-in.
- **PC Box Full:** When a Pokémon is caught and the active PC box is full, the caught Pokémon is still sent to the PC, but the active box must be changed manually later.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center. You respawn in front of the trainer you lost to.

#### B3. NPC & Item Interactions
- **NPC Catch Event:** Some NPCs can trigger a Pokémon 'catch' event upon interaction (e.g., Rocker in Safari Zone East Rest House gave a CHANSEY).
- **Eevee Evolution:** An NPC in Safari Zone North mentioned Eevee can evolve into Flareon or Vaporeon, suggesting multiple evolution paths via stones.
- **EXP.ALL:** Gives EXP to all party Pokémon, even non-participants, but reduces the total EXP gained per Pokémon. Best used for targeted training.

## IV. Active Hypotheses & Lessons Learned
- **Saffron Gym Hypothesis:** Defeating all trainers in the gym will unlock the path to Sabrina. I will systematically hunt down and defeat all remaining trainers.
- **Hypothesis:** Seafoam Islands contains a legendary Pokémon.
- **Visual Bug:** In battle, NEPTUNE (LAPRAS) is sometimes displayed as a GHOST type, though its actual typing is Water/Ice. Similarly, ECHO (GOLBAT) is sometimes shown as GHOST type instead of Flying/Poison.
- **`run_code` Limitation:** The `run_code` tool does not have access to the `xml.etree.ElementTree` module. XML parsing must be done with other methods or tools.

## V. Future Development & Hypotheses (Post-Reflection)
- **New Tool Idea:** Create a `find_reachable_tiles` tool based on the BFS logic from my debugging scripts. This would be a powerful, general-purpose utility for exploration.
- **New Hypothesis:** It may not be necessary to defeat all trainers in a gym to challenge the leader. I will test this by attempting to approach Sabrina after defeating the final Channeler in her room.