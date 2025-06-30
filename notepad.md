## I. Core Protocols & Immediate Actions (v37214)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure. This includes documenting faulty tools and agents.
- **CRITICAL: WKG Protocol (v3):** Before adding any node or edge, I will FIRST query the WKG with `wkg_checker` to confirm it doesn't already exist. When using `wkg_checker`, I MUST use numeric map IDs for the `map_name` and `to_map_name` arguments. All `warp` edges MUST include a `destination_entry_point`. All new nodes MUST have descriptive `tags`. I will use `wkg_inspector` to verify all known exits before declaring an area a dead end.
- **NEW: Pre-Navigation Check:** Before setting a major navigation goal, I will first consult my World Knowledge Graph and relevant Map Markers to ensure the path is not already explored or known to be a dead end.
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents for complex reasoning and my custom tools for computational tasks. I will use `protocol_enforcement_agent` to check my logic. I will use `navigation_strategist_agent` when facing navigational difficulties.
- **CRITICAL: Tool Maintenance Protocol:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the highest priority secondary goal, superseding ALL other gameplay objectives until resolved.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison), Flying > Grass/Poison (super-effective).
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Poison Type Effectiveness:** Poison-type moves are NOT-VERY-EFFECTIVE against Poison-types.

### B. Navigation & Traversal Rules
- 'No Will to Fight' Mechanic: A fainted Pokémon cannot be switched into battle.
- Silph Co. Blackout: Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- `reachable` Flag is Global: The `reachable` flag for warps and map sprites is a global check for the entire map, NOT a local check based on the player's current isolated segment.
- Saffron City Navigation: The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- Invisible Walls: Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).
- Silph Co. Gate Mechanic: Gates in Silph Co. appear to be controlled by the player's X-coordinate in a corresponding, physically separate corridor.
- HM & Field Move Mechanics:
    - Flash & Cut Exception: These HMs MUST be taught to a Pokémon to be used in the field.
    - PC Interaction: Must be activated by standing on the tile directly below the PC object (Y+1), facing up, and then pressing A.
    - Respawning Trees: Cuttable trees respawn after a short time, even without leaving the map.
- EXP Distribution: Experience is shared between the Pokémon that started the battle (the lead) and any Pokémon that participated by switching in.
- Battle Initiation Mechanics: To battle a trainer on an adjacent tile, you must face them and press 'A' to interact. Moving into their tile is not possible as they act as impassable objects.

### C. Tile Type Glossary (v3)
- *Commitment:* I will document every new tile type and its traversal rules here immediately upon discovery.
- `ground`: Walkable.
- `impassable`: Not walkable (e.g., walls, counters, rocks).
- `impassable_fence`: A specific type of impassable wall, found on Route 13.
- `cuttable`: A tree that can be cut with HM Cut. Becomes `ground` after cutting, but respawns.
- `ledge`: One-way traversal. Can be jumped down (from Y-1 to Y+2), but not climbed up. Acts as a wall from below or sides.
- `grass`: Tall grass for wild Pokémon encounters. Walkable like `ground`.
- `water`: Crossable with HM Surf.
- `steps`: Allows vertical movement between different elevations (e.g., `ground` and `elevated_ground`).
- `elevated_ground`: Walkable ground at a higher elevation.
- `teleporter`: Instant warp tile within the same logical location.
- `hole`: A warp tile leading to a lower map area.
- `spinner_*`: Forces movement in the specified direction.
- `ladder_*`: A warp tile leading to a higher or lower floor.
- `closed_gate`: An impassable gate that can become an `open_gate`.

## III. Tool Development Log (v37214)
### A. Active Agents & Tools
- **Agents:** `team_composition_advisor_agent`, `protocol_enforcement_agent`, `battle_strategist_agent`, `navigation_strategist_agent`
- **Tools:** `select_battle_option`, `pathfinder`, `object_finder`, `wkg_checker`, `wkg_inspector`

## IV. Investigation Log (v37214)
### A. Confirmed Hypotheses
- **PC Glitch (Confirmed):** The PC in Celadon City is persistently bugged. I must always select 'BILL's PC' to access the Pokémon Storage System.
- **Bike Voucher Location (Confirmed):** The Bike Voucher is obtained from the Pokémon Fan Club Chairman in Vermilion City after listening to his story.

### B. Untested Hypotheses
- **Cycling Road Access:** Accessing Cycling Road requires a Bicycle. (Test: Attempt to enter Cycling Road after obtaining a Bicycle).
- **Battle Mechanic Anomaly:** During the battle with Pixel's Dodrio on Silph Co. 7F, Dodrio used Fly, but the game displayed "But, it failed!". My subsequent move, Confuse Ray, also failed. The turn then reset to the main battle menu, with Dodrio not in the air. The reason for these failures is unknown.
- **Snorlax Permanence:** I assume the Snorlax I defeated on Route 12 is gone permanently. (Test: Return to Route 12 at (11,63) - Low Priority).
- **Route 11 Blockage:** I assume the path east on Route 11 from the gatehouse is blocked by a Snorlax. (Test: Explore east from the Route 12/11 gatehouse - Low Priority).

### C. Agent & Tool Failures
- `wkg_inspector` Misinterpretation (T36940): My `wkg_inspector` tool correctly identified the two exits from Route 13. My conclusion that it was a dead end was a failure of interpretation, not a tool bug. I must be more careful in analyzing tool output against game state warnings.
- `wkg_checker` Failure (T37214): The tool fails to find existing nodes/edges if the map is specified by its string name (e.g., "ROUTE_16") instead of its numeric ID (e.g., "27"). PROTOCOL: Always use numeric map IDs when calling `wkg_checker`.