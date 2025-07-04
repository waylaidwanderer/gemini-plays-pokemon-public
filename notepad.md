## I. Core Protocols & Immediate Actions (v46223)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge` and `define_map_marker` on the *same turn* a discovery is made. Deferring tasks is a critical failure. My WKG updates must be my highest priority upon any map change.
- **CRITICAL: WKG Protocol (v35 - Comprehensive & Verified):** When documenting a map transition, I will first add the source node, then the destination node, and finally the connecting edge in sequential turns. I will always use the correct **numeric string IDs** for maps and verify node existence before creating edges. For `connection_type: "warp"`, I MUST include the `destination_entry_point` property.
- **CRITICAL: Map Marker Protocol (v17):** Mark defeated trainers, significant wild battles, **used warps (entry and exit)**, picked up items, and confirmed dead ends *immediately*. Mark unvisited warps and key locations to track exploration targets.
- **CRITICAL: Agent & Tool Protocol (v13):** Agents are for **reasoning and high-level strategy**. Computational tasks (e.g., pathfinding, data parsing) MUST be handled by `run_code` or a custom tool defined with `define_tool`. I will use my `protocol_enforcement_agent` to check my plans before execution.

## II. System & Tool Development
### A. Tool Debugging & Refinement Protocol (v17 - IMMEDIATE ACTION)
- **CRITICAL:** If a custom tool is faulty, I MUST redefine and debug it on the IMMEDIATE next turn. **Abandoning a tool is a protocol violation.**
- **DEBUGGING STEP 1 (Advanced):** Use `run_code` with a modified pathfinding script. Print the `current` node inside the main loop to trace the BFS exploration path.
- **DEBUGGING STEP 2 (Advanced Analysis):** If no path is found, print the entire `came_from` dictionary to visualize the full explored area and identify the boundary where the pathfinding fails. This will confirm if the map is segmented.
- **DEBUGGING STEP 3 (Boundary Analysis):** If STEP 2 is insufficient, use a `run_code` script to parse the `came_from` dictionary and the `map_xml_string`. This script will identify all 'boundary tiles' (unexplored tiles adjacent to explored ones) and print their coordinates and tile types. This provides a definitive list of where the pathfinding algorithm is getting stuck.
- **DEBUGGING STEP 4:** Use `define_tool` to submit a corrected version of the script based on systematic analysis.
### B. Agent & Tool Usage Notes
- **`pc_navigator_agent`:** Generates a sequence of button presses to navigate the Pokémon PC menu to withdraw or deposit a specific Pokémon. It now correctly differentiates between 'BILL's PC' (for Pokémon) and 'Gem's PC' (for items) and is context-aware of the current menu. It is a reliable tool for depositing and withdrawing Pokémon.

## III. Game Mechanics & Battle Intel
### A. Tile Mechanics & Traversal Rules (v4)
- **Ledges:** Ledges are one-way only. They can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Water Tiles (Silph Co.):** The water tiles on the first floor of Silph Co. are purely cosmetic and function as `impassable` walls. They cannot be surfed on.
- **Spinner Tiles:** Spinner tiles force movement in a specific direction. I need to map out their destinations to navigate spinner mazes effectively.

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:**
  - Psychic > Ghost
  - Psychic > Poison
  - Ghost > Psychic
  - Bite (Normal) > Psychic
  - Electric > Rock/Water
  - CUT (Normal) > VICTREEBEL (Grass/Poison)
  - Flying > Grass/Poison
- **Not Very Effective:**
  - Normal !> Psychic
  - Electric !> Grass
  - Rock !> Ground
  - Psychic !> Psychic
- **Immunities:**
  - Psychic is immune to Electric.
  - Flying-type is immune to Ground-type moves.
  - MUK is immune to Poison-type moves.

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

## IV. Strategic Lessons & Hypotheses
- **Lesson:** Defeated Rival Pixel on Silph Co. 7F. His team was tough, especially the Alakazam and Flareon. My strategic switching was key to victory.
- **Lesson:** Route 19 trainers are significantly higher level than my team. Grinding is necessary before proceeding further south.
- **Hypothesis:** The Saffron City Gym is the next logical badge target after Fuchsia City. This is blocked until Silph Co. is cleared.
- **Hypothesis:** Seafoam Islands contains a legendary Pokémon.
- **Marker Labeling Protocol (v1):** For all defeated trainers, I will use the standardized label 'Trainer defeated'.