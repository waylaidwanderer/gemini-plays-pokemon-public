## I. Core Protocols & Immediate Actions (v50692)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure. My WKG updates must be my highest priority upon any map change. I will use a 'check-then-add' protocol, using `find_wkg_node_by_coords` before adding new nodes.
- **CRITICAL: WKG Protocol (v47 - Strict Testing):** When documenting a map transition, I will follow this strict workflow: 1. Use the warp/connection. 2. Upon arrival, immediately add a node for the destination, including descriptive `tags`. 3. Confirm the source node exists (creating it if necessary). 4. **Empirically test if the warp is bidirectional by immediately attempting to return.** 5. Create the connecting edge, meticulously verifying the **`destination_entry_point`** and setting `is_one_way` based on the test result.
- **CRITICAL: Map Marker Protocol (v25 - STRICTER Standardization):** I will use standardized emojis and labels for all new markers: '☠️' for defeated trainers, '✅' for picked-up items. ALL teleporter markers, whether for departure or arrival, MUST use the format: '🚪 Warp to/from (X, Y) [Bi-directional/One-way]'. This ensures consistent parsing by my tools. This will be placed *immediately*. **Redundant 'arrival' markers are forbidden.**
- **CRITICAL: Agent & Tool Protocol (v22 - IMMEDIATE Refinement):** Agent and tool refinement is an IMMEDIATE action, not a deferred goal. If an agent or tool is faulty or a better one can be conceived, I MUST define/redefine it on the IMMEDIATE next turn. Agents are for reasoning; computational tasks (pathfinding, data parsing) MUST be handled by tools. I will use my `protocol_enforcement_agent` to check my plans before execution.

## II. System & Tool Development
### A. Agent & Tool Usage Notes
- **`pc_navigator_agent`:** Generates a sequence of button presses to navigate the Pokémon PC menu to withdraw or deposit a specific Pokémon. Reliable for PC operations.
- **`battle_strategist_agent`:** Provides battle advice. **STATUS: REFINED.** The agent now correctly validates against fainted, sleeping, and active Pokémon to avoid invalid switch recommendations.

## III. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules (v11)
- **Ledges:** Ledges are one-way only. They can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Water Tiles (Silph Co.):** The water tiles on the first floor of Silph Co. are purely cosmetic and function as `impassable` walls. They cannot be surfed on.
- **Spinner Tiles:** Spinner tiles force movement in a specific direction. I need to map out their destinations to navigate spinner mazes effectively.
- **Gates:** `closed_gate` tiles are impassable. Some are opened by switches, while others (like in Silph Co.) require the CARD KEY.
- **Elevators (Silph Co.):** To use the elevator, you must first interact with the control panel (usually on a wall) to select a destination floor. After selecting a floor, you must walk onto the warp tiles at the back of the elevator room to trigger the map transition.
- **PC Interaction:** To use a Pokémon Center PC, I must stand on the tile directly below it and face up before pressing 'A'.
- **Saffron Gym Teleporters:** These are 1x1 warp tiles. To use a warp, I must move onto the tile. If I'm already on a warp tile, I must move off and then back on to trigger it. This is crucial for testing bidirectionality.

### B. Confirmed ROM Hack Changes (v12)
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying** (confirmed: KADABRA's PSYBEAM vs ECHO's GOLBAT)
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison).
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **Psychic immune to Electric** (confirmed: SPARKY's THUNDERBOLT vs JYNX (Ice/Psychic)). **Hypothesis:** This might be specific to Jynx's Ice typing, not a general Psychic immunity. **Evidence against general immunity:** Electric was effective vs Sabrina's Psychic team.; **HYPNO immune to STUN SPORE** (powder moves).

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

## IV. Future Development & Hypotheses (Post-Reflection)
- **`run_code` Limitation:** The `run_code` tool does not have access to the `xml.etree.ElementTree` module. XML parsing must be done with other methods or tools.

## V. Archived Hypotheses
- **Saffron Gym Hypothesis (Attempt 1):** Defeating all trainers in the gym will unlock the path to Sabrina.
- **Saffron Gym Hypothesis (Attempt 2 - Defeat all trainers in Sabrina's room):** Defeating all trainers in Sabrina's immediate room will unlock the path to her. **Conclusion (T50140):** FAILED. The path remained blocked.
- **Saffron Gym Hypothesis (Attempt 3):** Defeating all trainers in the room with the Channeler at (4, 8) does not open the path to Sabrina. **Conclusion (T50170):** FAILED. The trigger is something else entirely.