## I. Core Protocols & Immediate Actions (v49329)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure. My WKG updates must be my highest priority upon any map change.
- **CRITICAL: WKG Protocol (v40 - Meticulous Data Entry):** When documenting a map transition, I will follow this strict workflow: 1. Use the warp/connection. 2. Upon arrival, immediately add a node for the destination. 3. Confirm the source node exists (creating it if necessary). 4. Create the connecting edge, meticulously verifying the `destination_entry_point` against the Game State Information's warp list. I will also use the `tags` array to categorize nodes (e.g., `["stairs", "up"]`, `["teleporter"]`) for better graph analysis.
- **CRITICAL: Map Marker Protocol (v19 - Check First):** I will check for existing markers before adding new ones to avoid redundancy. I will continue to mark defeated trainers, significant wild battles, **used warps (entry and exit)**, picked up items, and confirmed dead ends *immediately*.
- **CRITICAL: Agent & Tool Protocol (v16 - Immediate Refinement):** Agent and tool refinement is an IMMEDIATE action, not a deferred goal. If an agent or tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. Agents are for reasoning; computational tasks (pathfinding, data parsing) MUST be handled by tools. I will use my `protocol_enforcement_agent` to check my plans before execution.

## II. System & Tool Development
### A. Tool Debugging & Refinement Protocol (v19 - IMMEDIATE ACTION)
- **CRITICAL:** If a custom tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. **Abandoning a tool is a protocol violation.**

- **DEBUGGING STEP 1 (Advanced):** Use `run_code` with a modified pathfinding script. Print the `current` node inside the main loop to trace the BFS exploration path.
- **DEBUGGING STEP 2 (Advanced Analysis):** If no path is found, print the entire `came_from` dictionary to visualize the full explored area and identify the boundary where the pathfinding fails. This will confirm if the map is segmented.
- **DEBUGGING STEP 3 (Boundary Analysis):** If STEP 2 is insufficient, use a `run_code` script to parse the `came_from` dictionary and the `map_xml_string`. This script will identify all 'boundary tiles' (unexplored tiles adjacent to explored ones) and print their coordinates and tile types. This provides a definitive list of where the pathfinding algorithm is getting stuck.
- **DEBUGGING STEP 4:** Use `define_tool` to submit a corrected version of the script based on systematic analysis.
### B. Agent & Tool Usage Notes
- **`pc_navigator_agent`:** Generates a sequence of button presses to navigate the Pokémon PC menu to withdraw or deposit a specific Pokémon. It now correctly differentiates between 'BILL's PC' (for Pokémon) and 'Gem's PC' (for items) and is context-aware of the current menu. It is a reliable tool for depositing and withdrawing Pokémon.
- **`battle_strategist_agent`:** Provides the safest, most cautious move. **MEMORY FLAW:** The agent has forgotten established game mechanics (Psychic > Electric immunity) across turns, leading to contradictory advice. I must refine its system prompt after this gym battle to improve its context retention.
- **`maze_navigator_agent`:** An agent that can parse the World Knowledge Graph to suggest the next optimal, unvisited teleporter to take for systematic maze exploration. **MUST USE IN SAFFRON GYM.**

## III. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules (v7)
- **Ledges:** Ledges are one-way only. They can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Water Tiles (Silph Co.):** The water tiles on the first floor of Silph Co. are purely cosmetic and function as `impassable` walls. They cannot be surfed on.
- **Spinner Tiles:** Spinner tiles force movement in a specific direction. I need to map out their destinations to navigate spinner mazes effectively.
- **Gates:** `closed_gate` tiles are impassable. Some are opened by switches, while others (like in Silph Co.) require the CARD KEY.
- **Elevators (Silph Co.):** To use the elevator, you must first interact with the control panel (usually on a wall) to select a destination floor. After selecting a floor, you must walk onto the warp tiles at the back of the elevator room to trigger the map transition.
- **PC Interaction:** To use a Pokémon Center PC, I must stand on the tile directly below it and face up before pressing 'A'.
- **Saffron Gym Teleporters:** These tiles warp the player between rooms. Their destinations need to be mapped.

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Bite (Normal) > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying** (confirmed: KADABRA's PSYBEAM vs ECHO's GOLBAT)
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **Psychic immune to Electric** (confirmed: SPARKY's THUNDERBOLT vs JYNX)

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts (e.g., from MINIMIZE).
- **Struggle:** A Pokémon with 0 PP for all moves will use Struggle, which has low accuracy and causes recoil damage.
- **Multi-Hit Moves:** Moves like FURY ATTACK are a critical threat, bypassing "sturdy" effects.
- **'No Will to Fight':** A fainted Pokémon cannot be switched into battle.
- **HM Usage:** Flash, Cut, and Fly MUST be taught to a Pokémon to be used in the field.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any that participated via switch-in.
- **PC Box Full:** When a Pokémon is caught and the active PC box is full, the caught Pokémon is still sent to the PC, but the active box must be changed manually later.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.

#### B3. NPC & Item Interactions
- **NPC Catch Event:** Some NPCs can trigger a Pokémon 'catch' event upon interaction (e.g., Rocker in Safari Zone East Rest House gave a CHANSEY).
- **Eevee Evolution:** An NPC in Safari Zone North mentioned Eevee can evolve into Flareon or Vaporeon, suggesting multiple evolution paths via stones.
- **EXP.ALL:** Gives EXP to all party Pokémon, even non-participants, but reduces the total EXP gained per Pokémon. Best used for targeted training.

## IV. Confirmed Facts & Strategic Lessons
- **Confirmed:** The Saffron City Gym was blocked until Silph Co. was cleared. Now that Giovanni is defeated, the gym is accessible.
- **Lesson:** Defeated Rival Pixel on Silph Co. 7F. His team was tough, especially the Alakazam and Flareon. My strategic switching was key to victory.
- **Lesson:** Route 19 trainers are significantly higher level than my team. Grinding is necessary before proceeding further south.
- **Lesson:** Some gates in Silph Co. are not opened by the CARD KEY and likely require a different switch or event.
- **Marker Labeling Protocol (v1):** For all defeated trainers, I will use the standardized label 'Trainer defeated'.

## V. Active Hypotheses
- **Hypothesis:** Seafoam Islands contains a legendary Pokémon.
- **Hypothesis:** The teleporters in Saffron Gym may not be two-way. **Test:** I will use my `maze_navigator_agent` to systematically explore the gym and map out the teleporter connections.
- **Visual Bug:** In battle, NEPTUNE (LAPRAS) is sometimes displayed as a GHOST type, though its actual typing is Water/Ice.