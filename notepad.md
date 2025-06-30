## I. Core Protocols & Immediate Actions (v134)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. NO DELAYS. This includes documenting faulty tools and agents.
- **CRITICAL: WKG Protocol:** Before adding any node or edge, I will FIRST query the WKG with `wkg_checker` to confirm it doesn't already exist. All `warp` edges MUST include a `destination_entry_point`. All new nodes MUST have descriptive `tags`.
- **CRITICAL: Map Marker Protocol:** I will immediately mark defeated trainers and other key events. Redundant markers will be deleted. I will migrate all trainer intel from this notepad to map markers.
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents for complex reasoning and my custom tools for computational tasks. I will use `protocol_enforcement_agent` to check my logic.
- **CRITICAL: Tool Maintenance Protocol:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the highest priority secondary goal, superseding ALL other gameplay objectives until resolved.

## II. Current Mission: Debug Navigation Tools
- **Primary Objective:** Fix the bugged `pathfinder` and `dungeon_navigator` tools.
- **Secondary Objective:** Consolidate `pathfinder` and `dungeon_navigator` into a single, robust `master_navigator` tool.
- **Tertiary Objective:** Liberate Silph Co. from Team Rocket.

## III. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison).
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Poison Type Effectiveness:** Poison-type moves are NOT-VERY-EFFECTIVE against Poison-types.

### B. Navigation & Traversal Rules
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **`reachable` Flag is Global:** The `reachable` flag for warps and map sprites is a global check for the entire map, NOT a local check based on the player's current isolated segment.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).
- **Silph Co. Gate Mechanic:** Gates in Silph Co. appear to be controlled by the player's X-coordinate in a corresponding, physically separate corridor.
- **HM & Field Move Mechanics:**
    - **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.
    - **PC Interaction:** Must be activated by standing on the tile directly below the PC object (Y+1), facing up, and then pressing A.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle (the lead) and any Pokémon that participated by switching in.

## IV. Tool Development Log (v134)
### A. Development Pipeline
- **TOP PRIORITY (BUG FIX):** `pathfinder` & `dungeon_navigator` are unreliable and generate invalid paths through impassable fences (e.g., on Route 13). **Testing Plan:** Attempt to use pathfinder to navigate around other types of impassable tiles (e.g., buildings, rocks) to see if the bug is specific to fences or all impassable tiles.
- **NEW TOOL: `pc_navigator_tool`:** Create a deterministic tool for PC menu navigation. Agents are not suitable for this task.
- **NEW: `wkg_manager_tool`:** Create a single tool to handle the 'check-then-add' logic for a map transition to improve efficiency.

### B. Active Agents & Tools
- **Agents:**
  - `team_composition_advisor_agent` (v2) - Reliable
  - `protocol_enforcement_agent` (v1) - Reliable
  - `battle_strategist_agent` (v11) - Refined and reliable.
- **Tools:**
  - `select_battle_option` (v1) - Reliable
  - `pathfinder` (v3) - **BUGGED:** Fails to navigate simple fence obstacles. DO NOT USE UNTIL FIXED.
  - `dungeon_navigator` (v1) - **DEPRECATED:** To be merged with pathfinder.
  - `object_finder` (v1) - Reliable
  - `wkg_checker` (v3) - Reliable

### C. Deprecated Agents
- `pc_navigator_agent` (v3) - **DELETED.** Unreliable for deterministic menu navigation. To be replaced with a tool.

## V. Investigation Log
### A. Silph Co. Intel
- **Boardroom Location:** A Rocket on 10F at (2,10) confirmed the boardroom is on the 11th floor.
- **Bugged Rocket (5F West):** The Rocket at (9,17) in the western segment of 5F is bugged and soft-locks progress. The only exit is the teleporter back to 9F.

### B. Untested Assumptions & Hypotheses
- **PC Glitch:** The PC in Celadon City is persistently bugged and I must always select 'BILL's PC' to access the Pokémon Storage System. This needs to be re-verified on next use.
- **Battle Mechanic Anomaly:** During the battle with Pixel's Dodrio on Silph Co. 7F, Dodrio used Fly, but the game displayed "But, it failed!". My subsequent move, Confuse Ray, also failed. The turn then reset to the main battle menu, with Dodrio not in the air. The reason for these failures is unknown.

## VI. Reflection Log (T36416)
- **Discipline Lapses:** I have been stuck on Route 12 for over 10 turns due to poor navigation. I failed to use my navigation tools promptly and did not mark dead ends, violating my own protocols. I also deferred fixing my `wkg_checker` tool after it provided a faulty result. I must be more disciplined in using my tools and documenting my environment to avoid getting stuck like this in the future.