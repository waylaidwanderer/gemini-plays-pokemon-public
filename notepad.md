## I. Core Protocols & Immediate Actions (v51241)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure. My WKG updates are my highest priority upon any map change.
- **CRITICAL: WKG Protocol (v51241):** My workflow for documenting map transitions: 1. Use the warp/connection. 2. Upon arrival, use `find_wkg_node_by_coords` to check if the destination node exists. If not, create it. All payload values (including `map_id` as a string) MUST be correct. 3. Use `find_wkg_node_by_coords` to get the source node ID. 4. **Empirically test bidirectionality by immediately returning.** 5. Create the edge(s): For bidirectional warps, create *two separate one-way edges*, each with its respective `destination_entry_point`. For map_edge connections, create one bidirectional edge. 6. I will treat 'edge already exists' errors as confirmations that my documentation is correct and move on.
- **CRITICAL: Map Marker Protocol:** I will use standardized emojis and labels for all new markers: '☠️' for defeated trainers, '✅' for picked-up items. ALL teleporter markers, whether for departure or arrival, MUST use the format: '🚪 Warp to/from (X, Y) [Bi-directional/One-way]'. This ensures consistent parsing by my tools. This will be placed *immediately*. **Redundant 'arrival' markers are forbidden.**
- **CRITICAL: Agent & Tool Protocol:** Agent and tool refinement is an IMMEDIATE action, not a deferred goal. If an agent or tool is faulty or a better one can be conceived, I MUST define/redefine it on the IMMEDIATE next turn. **Agents are for reasoning; computational tasks (pathfinding, data parsing) MUST be handled by tools.** I will not use `xml.etree.ElementTree` in `run_code`.
- **CRITICAL: Hypothesis Testing Protocol:** When stuck, I will not repeat the same action more than twice. If a hypothesis fails after two documented attempts, I MUST formulate and test a new one. I will avoid confirmation bias by actively trying to disprove my own theories.

## II. System & Tool Development
### A. Agent & Tool Usage Notes
- **`pc_navigator_agent`:** Generates a sequence of button presses to navigate the Pokémon PC menu to withdraw or deposit a specific Pokémon. Reliable for PC operations.
- **`battle_strategist_agent`:** Provides battle advice. **STATUS: REFINED.** The agent now correctly validates against fainted, sleeping, and active Pokémon to avoid invalid switch recommendations.

## III. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules (v13)
- **Ledges:** Ledges are one-way only. They can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Water Tiles (Silph Co.):** The water tiles on the first floor of Silph Co. are purely cosmetic and function as `impassable` walls. They cannot be surfed on.
- **Spinner Tiles:** Spinner tiles force movement in a specific direction. I need to map out their destinations to navigate spinner mazes effectively.
- **Gates:** `closed_gate` tiles are impassable. Some are opened by switches, while others (like in Silph Co.) require the CARD KEY.
- **Elevators (Silph Co.):** To use the elevator, you must first interact with the control panel (usually on a wall) to select a destination floor. After selecting a floor, you must walk onto the warp tiles at the back of the elevator room to trigger the map transition.
- **PC Interaction:** To use a Pokémon Center PC, I must stand on the tile directly below it and face up before pressing 'A'.
- **Saffron Gym Teleporters:** These are 1x1 warp tiles. To use a warp, I must move onto the tile. If I'm already on a warp tile, I must move off and then back on to trigger it. This is crucial for testing bidirectionality.
- **Open Gates:** `open_gate` tiles are unlocked `closed_gate` tiles and function as `ground`.

### B. Confirmed ROM Hack Changes (v13)
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying** (confirmed: KADABRA's PSYBEAM vs ECHO's GOLBAT)
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison).
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **Electric is effective vs Sabrina's Psychic team, confirming Psychic types are NOT immune to Electric.**; **HYPNO immune to STUN SPORE** (powder moves).

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

## IV. Archived Hypotheses
- **Saffron Gym Hypothesis (Attempt 1):** Defeating all trainers in the gym will unlock the path to Sabrina.
- **Saffron Gym Hypothesis (Attempt 2 - Defeat all trainers in Sabrina's room):** Defeating all trainers in Sabrina's immediate room will unlock the path to her. **Conclusion (T50140):** FAILED. The path remained blocked.
- **Saffron Gym Hypothesis (Attempt 3):** Defeating all trainers in the room with the Channeler at (4, 8) does not open the path to Sabrina. **Conclusion (T50170):** FAILED. The trigger is something else entirely.
- **Saffron Gym Hypothesis (Attempt 4):** The maze has a simple, linear solution. **Conclusion (T50796):** FAILED. All reachable warps have been visited.
- **Saffron Gym Hypothesis (Attempt 5 - T51005):** The path to Sabrina was blocked because I hadn't cleared Team Rocket out of Silph Co. first. Now that Giovanni is defeated, the trigger to open the path might be active. I must return to Saffron Gym and re-test the teleporter maze.
- **Silph Co. 10F Hypothesis (Attempt 1 - Beds):** The 'Guaranteed Reachable Interactable Tiles' are the beds. **Conclusion (T51108):** FAILED. Interacting with both beds yielded no result.
- **Silph Co. 10F Hypothesis (Attempt 2 - Systematic Search):** The two 'Guaranteed Reachable Interactable Tiles' are hidden floor switches or pressure plates. **Conclusion (T51157):** FAILED. Systematic search of tiles (2,2), (2,1), (3,1), (4,2), (4,1), (5,1), and (6,1) yielded no results. This method is too inefficient.
- **Silph Co. 10F Hypothesis (Attempt 3 - Systematic Search):** The interactable tiles are hidden floor switches activated by standing on an adjacent tile and pressing 'A'. **Conclusion (T51157):** FAILED. Systematic search of tiles (2,2), (2,1), (3,1), (4,2), (4,1), (5,1), and (6,1) yielded no results. This method is inefficient and the new game hints suggest it's the wrong approach.
- **Silph Co. 10F Hypothesis (Attempt 4 - Re-investigating Warps):** The 'interactable tiles' are the warps themselves, and their state or destination may have changed after defeating Giovanni. The game state's insistence that (11, 1) is unvisited was a major clue. **Conclusion (T51212):** This hypothesis was partially correct. The warps are key, but the systematic search of walls was a dead end. The game has now revealed the exact interactable tiles.

## V. Current Hypotheses
- **Silph Co. 4F Puzzle:** The game has hinted at two 'Guaranteed Reachable Interactable Tiles'. Their locations are currently unknown. My hypothesis is that a simple move is required to reveal their coordinates.

## VI. Agent & Tool Ideas (v51241)
- **Marker Compliance Tool (Implemented):** A tool that parses map markers against my notepad protocols to find non-compliant entries.
- **Systematic Searcher Tool (Implemented):** A tool to automate the process of systematically sweeping an area for interactable tiles. It parses the map XML to find valid tiles.
- **WKG Manager Tool:** A tool to automate the multi-step WKG documentation process. It would take source/destination details and execute the necessary `find_wkg_node_by_coords` and `manage_world_knowledge` calls, ensuring protocol compliance (e.g., string payloads).