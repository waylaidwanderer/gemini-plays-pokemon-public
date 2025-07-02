## I. Core Protocols & Immediate Actions (v42542)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **CRITICAL: WKG Protocol (v22 - Agent-Assisted):** My manual WKG management has been error-prone. I will use the `wkg_manager_agent` to handle node/edge verification and creation to prevent future errors.
- **CRITICAL: Map Marker Protocol (v11):** Mark defeated trainers, **used warps (entry and exit)**, picked up items, and confirmed dead ends *immediately*. **DO NOT MARK MAP-EDGE TRANSITIONS.**
- **CRITICAL: Agent & Tool Protocol (v6):** Agents are for **reasoning and high-level strategy**. Computational tasks (e.g., pathfinding, data parsing) MUST be handled by `run_code` or a custom tool defined with `define_tool`.

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
- **Eevee Evolution:** An NPC in the Safari Zone North Rest House mentioned that Eevee can evolve into Flareon or Vaporeon, suggesting multiple evolution paths likely influenced by evolution stones.

### C. Map Mechanics Discoveries
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered in Silph Co. 9F at (12, 2), Safari Zone East at (17, 23), and Fuchsia Gym.
- **Hidden Passages:** Seemingly impassable tiles that are actually traversable. Discovered in Safari Zone East at (7, 25).
- **Impassable Roofs:** Building roofs, even if visually over traversable ground, can act as an impassable wall when approached from above. (Discovered on Route 19 at (6, 9)).
- **Summer Beach House Trap:** The house on Route 19 at (6, 10) is a one-way trap. The entrance warp is one-way, and Fly cannot be used to escape. The intended solution is to walk *through* Pikachu to reach the southern exit warp.
- **Elevation Traversal:** Movement between `ground` and `elevated_ground` tiles is only possible via `steps` tiles. Direct movement between them is blocked.

## III. System & Tool Development
### A. Tool Debugging & Refinement Protocol (v13 - IMMEDIATE ACTION)
- **CRITICAL:** If a custom tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. **Abandoning a tool is a protocol violation.**
- **DEBUGGING STEP 1 (Advanced):** Use `run_code` with a modified pathfinding script. Print the `current` node inside the main loop to trace the BFS exploration path.
- **DEBUGGING STEP 2 (Advanced Analysis):** If no path is found, print the entire `came_from` dictionary to visualize the full explored area and identify the boundary where the pathfinding fails.
- **DEBUGGING STEP 3 (Boundary Analysis):** If STEP 2 is insufficient, use a `run_code` script to parse the `came_from` dictionary and the `map_xml_string`. This script will identify all 'boundary tiles' (unexplored tiles adjacent to explored ones) and print their coordinates and tile types. This provides a definitive list of where the pathfinding algorithm is getting stuck.
- **DEBUGGING STEP 4:** Use `define_tool` to submit a corrected version of the script based on systematic analysis.

## IV. Investigation & Hypothesis Log
- **Current Plan:** Systematically explore the Safari Zone to find the 'SECRET HOUSE' (containing HM SURF) and the Warden's lost GOLD TEETH. The GOLD TEETH are confirmed to be in the Safari Zone West area.
- **Hypothesis:** Not all warps on the same map are reachable from a single contiguous area. Some maps are segmented. (Confirmed for Safari Zone West).

### E. Safari Zone Mechanics Testing (T41962)
- **Hypothesis:** Rock increases catch rate but also flee rate. Bait decreases flee rate but also catch rate.
- **Test Plan:** For future identical encounters, I will test different action sequences to observe their effects on catch and flee rates.
  1.  **Control:** Throw only Safari Balls.
  2.  **Bait Strategy:** Throw Bait, then throw Safari Balls.
  3.  **Rock Strategy:** Throw Rock, then throw Safari Balls.
- I will log the results to build a reliable strategy.

## V. Defeated Bosses Log
- **Koga (Fuchsia Gym):** GOLBAT (Lv. 42), MUK (Lv. 42, knows MEGA DRAIN, ACID ARMOR), TENTACRUEL (Lv. 41, knows SURF, ICE BEAM), VENOMOTH (Lv. 43, knows PSYCHIC)

## VI. Tool Usage Notes
- **`select_battle_option` Tool Scope:** This tool is only for the standard battle menu (FIGHT, PKMN, ITEM, RUN). It **does not work** for the Safari Zone battle menu (BALL, BAIT, THROW ROCK, RUN).
- **PC Box Full Mechanic (v2):** After catching TITANESS, the active PC box is full again. Must remember to manually change the active box at a Pokémon Center before attempting to catch more Pokémon.

## VII. Protocol Adherence Log (T42542)
- **WKG Management:** I have repeatedly failed to document map transitions immediately and correctly in a single turn. My new protocol is to add all nodes and the connecting edge for a transition in the *same turn* it is discovered. I will not defer any part of this process.
- **Agent Trust:** I must trust my agents' outputs unless proven wrong by direct testing. I will not second-guess them without evidence.
- **Agent vs. Tool Usage:** My `exploration_strategist_agent` was a misuse of an agent for a computational task. It has been deleted. Future development of exploration or debugging aids must be implemented as custom tools, not agents.