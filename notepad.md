## I. Core Protocols & Immediate Actions (v38162)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure. This is my highest priority.
- **CRITICAL: WKG Protocol (v5):** Before adding any node or edge, I will FIRST query the WKG with `wkg_checker` to confirm it doesn't already exist. All `warp` edges MUST include a `destination_entry_point`. All new nodes MUST have descriptive `tags`. I will use `wkg_inspector` to verify all known exits before declaring an area a dead end.
- **CRITICAL: Map Marker Protocol (v3):** I will mark defeated trainers and used warps (both entry and exit points) *immediately* after the event occurs. This is not a task to be deferred.
- **CRITICAL: Protocol Enforcement:** I will make a conscious effort to use the `protocol_enforcement_agent` before finalizing my plan each turn to catch my own mistakes.
- **CRITICAL: Agent & Tool Maintenance:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the **ABSOLUTE HIGHEST PRIORITY**, superseding ALL other gameplay objectives.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison), Flying > Grass/Poison (super-effective).
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Poison Type Effectiveness:** Poison-type moves are NOT-VERY-EFFECTIVE against Poison-types.
- **Battle Mechanics:** Multi-hit moves (e.g., FURY ATTACK) are a critical threat and can bypass the "sturdy" effect of surviving on 1 HP.

### B. Navigation & Traversal Rules
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).
- **Silph Co. Gate Mechanic:** Gates in Silph Co. appear to be controlled by the player's X-coordinate in a corresponding, physically separate corridor.
- **HM & Field Move Mechanics:** Flash, Cut, and Fly MUST be taught to a Pokémon to be used in the field. PC Interaction must be activated from the tile directly below the PC (Y+1), facing up.
- **Respawning Trees:** Cuttable trees respawn after a short time, even without leaving the map.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any Pokémon that participated by switching in.
- **Battle Initiation Mechanics:** To battle a trainer on an adjacent tile, you must face them and press 'A' to interact.

## III. Investigation & Hypothesis Log (v38162)
### A. Confirmed Facts
- **PC Glitch (Confirmed):** The PC in Celadon City is persistently bugged. I must always select 'BILL's PC' to access the Pokémon Storage System.
- **Bike Voucher Location (Confirmed):** The Bike Voucher is obtained from the Pokémon Fan Club Chairman in Vermilion City after listening to his story.
- **`pathfinder` Intelligence (Confirmed):** The tool automatically finds a path to the nearest valid adjacent tile if the specified destination is impassable or unseen.
- **Fuchsia City Warden (Confirmed, T38002):** The Safari Zone Warden is nicknamed 'SLOWPOKE' and has a speech impediment.
- **Route 14 Layout (Confirmed, T38161):** The southern part of Route 14 is a one-way path down from the northern section, accessible via ledges. It is a dead-end for northbound travel.

### B. Current Plans & Explicit Tests
- **Primary Plan (per `navigation_strategist_agent`):** Obtain the Soul Badge. Current strategy is to Fly to Lavender Town, then travel south through Routes 12 and 13 to access the northern part of Route 14, which leads to Fuchsia City. This bypasses the one-way ledge system.

## IV. Past Failures & Corrections Log
- **CRITICAL PROCESS FAILURE: Repeated WKG Protocol Violations (T37321 - T38161):** The AI critique has correctly identified a persistent behavioral issue. I repeatedly fail to follow my own core protocol of immediately documenting map transitions. This corrupts my world model and leads to navigational errors. **Correction:** ALL data management tasks (`manage_world_knowledge`, `define_map_marker`, `notepad_edit`) MUST be performed on the same turn a discovery is made. There are no exceptions. This is the root cause of most of my problems.
- **CRITICAL NAVIGATIONAL FAILURE: Directional Confusion on Route 15 (T38101 - T38161):** My `navigation_strategist_agent` correctly identified that I was moving east, away from my objective in Fuchsia City. My pathfinder then confirmed I could not go west from the upper ledge. This forced me to continue east to find a way down, which led me to the dead-end southern part of Route 14. This loop highlights a critical need to better analyze the map and my agent's advice before committing to long-distance travel.

## V. Systematic Documentation Tasks
- **Tile Mechanics Glossary:** Systematically observe and document the behavior of every unique tile type encountered (e.g., `ledge`, `grass`, `water`, `spinner`, `impassable` variants) to build a comprehensive reference.

## VI. High-Priority Tasks
- **WKG Correction:** Add a new node for Route 13 at (1, 9) and create the correct edge to the node on Route 14 at (20, 9). The current connection to the node at (1, 7) is a temporary fix.