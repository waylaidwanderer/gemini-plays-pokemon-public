## I. Core Protocols & Immediate Actions (v42325)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **CRITICAL: WKG Protocol (v22 - Agent-Assisted):** My manual WKG management has been error-prone. I will use the `wkg_manager_agent` to handle node/edge verification and creation to prevent future errors.
- **CRITICAL: Map Marker Protocol (v11):** Mark defeated trainers, **used warps (entry and exit)**, picked up items, and confirmed dead ends *immediately*. **DO NOT MARK MAP-EDGE TRANSITIONS.**
- **CRITICAL: Agent & Tool Protocol (v5):** Agents are for **reasoning and high-level strategy**. Computational tasks (e.g., pathfinding, data parsing) MUST be handled by `run_code` or a custom tool defined with `define_tool`.

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

### D. Discovered Tile Mechanics
- `ground`: Standard walkable tile.
- `grass`: Walkable tile with wild Pokémon encounters.
- `impassable`: Walls, trees, and other objects that block movement.
- `water`: Requires SURF to cross.
- `steps`: Allows movement between ground and elevated_ground tiles.
- `elevated_ground`: Walkable ground at a higher elevation.
- `ledge`: Can only be jumped down from above (Y-1).
- `warp`: Teleports the player to a new location.

### E. Investigation & Hypothesis Log
- **Current Plan:** Systematically explore the Safari Zone to find the 'SECRET HOUSE' (likely containing HM SURF) and the Warden's lost GOLD TEETH. The GOLD TEETH are confirmed to be in the Safari Zone West area.

### F. Defeated Bosses Log
- **Koga (Fuchsia Gym):** GOLBAT (Lv. 42), MUK (Lv. 42, knows MEGA DRAIN, ACID ARMOR), TENTACRUEL (Lv. 41, knows SURF, ICE BEAM), VENOMOTH (Lv. 43, knows PSYCHIC)

## III. System & Tool Development
### A. Tool Debugging & Refinement Protocol (v8 - IMMEDIATE ACTION)
- **CRITICAL:** If a custom tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. **Abandoning a tool is a protocol violation.**
- **DEBUGGING STEP 1 (Advanced):** Use `run_code` with a modified pathfinding script. Print the `current` node inside the main loop to trace the BFS exploration path. If no path is found, print the entire `came_from` dictionary to visualize the full explored area and identify the boundary where the pathfinding fails.
- **DEBUGGING STEP 2:** Use `define_tool` to submit a corrected version of the script based on systematic analysis.

### B. Future Development Ideas
- **Global Navigator Agent:** I could define an agent that takes a start and end `map_id` and uses the WKG to plot a multi-map route, providing a sequence of warps and map transitions to follow. This would automate long-distance travel planning.
- **Advanced Exploration Agent:** An agent that integrates pathfinding logic to evaluate the 'explorability' of a cluster of unseen tiles, rather than just proximity, to create more efficient exploration plans.

## V. Safari Zone Mechanics Testing (T41962)
- **Hypothesis:** Rock increases catch rate but also flee rate. Bait decreases flee rate but also catch rate.
- **Test Plan:** For future identical encounters, I will test different action sequences to observe their effects on catch and flee rates.
  1.  **Control:** Throw only Safari Balls.
  2.  **Bait Strategy:** Throw Bait, then throw Safari Balls.
  3.  **Rock Strategy:** Throw Rock, then throw Safari Balls.
- I will log the results to build a reliable strategy.

## VI. Tool Usage Notes
- **`select_battle_option` Tool Scope:** This tool is only for the standard battle menu (FIGHT, PKMN, ITEM, RUN). It **does not work** for the Safari Zone battle menu (BALL, BAIT, THROW ROCK, RUN).
- Safari Zone Item/Time Hint: A Scientist in the North Rest House mentioned that you can keep items found on the ground, but you'll run out of time if you try to get them all at once.
- **Safari Zone Secret House Hint:** A Safari Zone Worker in the North Rest House said, "Go to the deepest part of the SAFARI ZONE. You will win a prize!" This is likely where the Secret House and HM SURF are located.
- **PC Box Full Mechanic (v2):** After catching TITANESS, the active PC box is full again. Must remember to manually change the active box at a Pokémon Center before attempting to catch more Pokémon.