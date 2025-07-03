## I. Core Protocols & Immediate Actions (v45100)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure. My WKG updates must be my highest priority upon any map change.
- **CRITICAL: WKG Protocol (v35 - Comprehensive & Verified):** When documenting a map transition, I will first add the source node, then the destination node, and finally the connecting edge in sequential turns. I will always use the correct **numeric string IDs** for maps and verify node existence before creating edges. For `connection_type: "warp"`, I MUST include the `destination_entry_point` property.
- **CRITICAL: Map Marker Protocol (v17):** Mark defeated trainers, significant wild battles, **used warps (entry and exit)**, picked up items, and confirmed dead ends *immediately*. Mark unvisited warps and key locations to track exploration targets.
- **CRITICAL: Agent & Tool Protocol (v13):** Agents are for **reasoning and high-level strategy**. Computational tasks (e.g., pathfinding, data parsing) MUST be handled by `run_code` or a custom tool defined with `define_tool`. I will use my `protocol_enforcement_agent` to check my plans before execution.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison), Flying > Grass/Poison (super-effective), Electric !> Grass, Rock !> Ground.
- **Type Immunities:** Psychic is immune to Electric. Flying-type is immune to Ground-type moves. MUK is immune to Poison-type moves.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Battle Mechanics:** Multi-hit moves (e.g., FURY ATTACK) are a critical threat and can bypass the "sturdy" effect of surviving on 1 HP.
- **Ghost-Type Effectiveness:** Ghost-type moves (like Lick) are effective against Rock/Ground-types.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **HM & Field Move Mechanics:** Flash, Cut, and Fly MUST be taught to a Pokémon to be used in the field.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any Pokémon that participated by switching in.
- **Battle Initiation Mechanics:** To battle a trainer on an adjacent tile, you must face them and press 'A' to interact.
- **NPC Interaction Catch:** Some NPCs, upon interaction, can trigger a Pokémon 'catch' event (Observed with Rocker in Safari Zone East Rest House giving a CHANSEY).
- **Safari Game Time Limit:** The Safari Game has a time limit. When it expires, the player is automatically warped back to the Safari Zone Gate.
- **PC Box Full Mechanic:** When a Pokémon is caught and the active PC box is full, the caught Pokémon is still sent to the PC, but a warning is displayed. I must remember to manually change the active box at a Pokémon Center.
- **Eevee Evolution:** An NPC in the Safari Zone North Rest House mentioned that Eevee can evolve into Flareon or Vaporeon, suggesting multiple evolution paths likely influenced by evolution stones.
- **Item Mechanics:** EXP.ALL gives EXP to all party Pokémon, even non-participants. However, it reduces the total EXP gained per Pokémon. Best used for targeted training, otherwise store in PC.
- **Silph Co. Puzzles:** The building contains unique navigation puzzles. Some floors have gates that open sequentially as you walk along a specific path (e.g., a northern corridor). The building also uses a complex network of teleporters that link different floors and isolated rooms.
- **SURF Field Move Mechanics (v3 - Partially Confirmed):** Attempts to use SURF on Route 19 with TITANESS (Normal-type) have failed with the error 'No SURFing on TITANESS here!'. This strongly suggests that only specific Pokémon, likely Water-types, can use SURF in the field. Current plan: Use the SUPER ROD to fish for a Water-type Pokémon to confirm this hypothesis.

## III. System & Tool Development
### A. Tool Debugging & Refinement Protocol (v17 - IMMEDIATE ACTION)
- **CRITICAL:** If a custom tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. **Abandoning a tool is a protocol violation.**
- **DEBUGGING STEP 1 (Advanced):** Use `run_code` with a modified pathfinding script. Print the `current` node inside the main loop to trace the BFS exploration path.
- **DEBUGGING STEP 2 (Advanced Analysis):** If no path is found, print the entire `came_from` dictionary to visualize the full explored area and identify the boundary where the pathfinding fails. This will confirm if the map is segmented.
- **DEBUGGING STEP 3 (Boundary Analysis):** If STEP 2 is insufficient, use a `run_code` script to parse the `came_from` dictionary and the `map_xml_string`. This script will identify all 'boundary tiles' (unexplored tiles adjacent to explored ones) and print their coordinates and tile types. This provides a definitive list of where the pathfinding algorithm is getting stuck.
- **DEBUGGING STEP 4:** Use `define_tool` to submit a corrected version of the script based on systematic analysis.

### B. Agent & Tool Usage Notes
- **`pc_navigator_agent`:** This agent now correctly differentiates between 'BILL's PC' (for Pokémon) and 'Gem's PC' (for items). It is a reliable tool for depositing and withdrawing Pokémon.
- **`pathfinder`:** After extensive debugging, this tool now correctly handles dynamic land-to-water transitions by accepting a `can_surf` parameter. It is my primary and reliable pathfinding tool for all overworld navigation.

## IV. Battle Plans & Strategies
### A. Rival Pixel (Silph Co. Rematch)
- **Opponent Team:** Alakazam (Lv. 45), Sandslash (Lv. 43), Exeggutor (Lv. 43), Cloyster (Lv. 43), Magneton (Lv. 43).
- **Recommended Team:** SPARKY, CRAG, ECHO, TITANESS, GUILLOTIN, LEGION.
- **Counters:**
  - SPARKY > Cloyster
  - CRAG > Magneton
  - ECHO > Exeggutor
  - TITANESS > Alakazam (Bite) & Sandslash (Surf)
  - GUILLOTIN > Exeggutor & Alakazam (Bug moves)
  - LEGION > Sandslash (backup) & Psychic pivot
- **Training Plan:** Train TITANESS, GUILLOTIN, and LEGION to Lv. 45 in Seafoam Islands (B1F), targeting Jynx, Golbat, and Krabby for high EXP.

## V. Tile Mechanics Documentation
- *This section is for documenting the properties and behaviors of different tile types as they are discovered.*

## VI. Future Agent & Tool Development Ideas
- **HM Teacher Agent/Tool:** An agent or tool to automate the process of navigating the menu to teach a specific HM to a specific Pokémon, including selecting which move to replace.
- **Tool Debugger Agent:** An agent that takes a tool name and debug objective (e.g., 'trace_path') to automatically generate a `run_code` script with debugging print statements. This would streamline fixing faulty tools.
- **Strategic Exploration Agent:** An agent that analyzes the entire map, identifies clusters of unseen tiles, and suggests a more strategic exploration plan, especially for complex maps like Silph Co. or caves.