## I. Core Protocols & Immediate Actions (v38132)
- **CRITICAL: Immediate Tool & Agent Maintenance:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the **ABSOLUTE HIGHEST PRIORITY**, superseding ALL other gameplay objectives. I will stop all other actions and use `define_tool` or `define_agent` to fix it on the very next turn. This is non-negotiable and is not a 'goal' to be deferred.
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **CRITICAL: WKG Protocol (v4):** Before adding any node or edge, I will FIRST query the WKG with `wkg_checker` to confirm it doesn't already exist. All `warp` edges MUST include a `destination_entry_point`. All new nodes MUST have descriptive `tags`. I will use `wkg_inspector` to verify all known exits before declaring an area a dead end.
- **CRITICAL: Map Marker Protocol (v2):** I will mark defeated trainers and used warps (both entry and exit points) *immediately* after the event occurs. This is not a task to be deferred.
- **CRITICAL: Protocol Enforcement:** I will make a conscious effort to use the `protocol_enforcement_agent` before finalizing my plan each turn to catch my own mistakes.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison), Flying > Grass/Poison (super-effective).
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Poison Type Effectiveness:** Poison-type moves are NOT-VERY-EFFECTIVE against Poison-types.

### B. Navigation & Traversal Rules
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).
- **Silph Co. Gate Mechanic:** Gates in Silph Co. appear to be controlled by the player's X-coordinate in a corresponding, physically separate corridor.
- **HM & Field Move Mechanics:** Flash & Cut MUST be taught to a Pokémon to be used in the field. PC Interaction must be activated from the tile directly below the PC (Y+1), facing up.
- **Respawning Trees:** Cuttable trees respawn after a short time, even without leaving the map. This is a critical mechanic for navigating areas with recurring tree obstacles.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any Pokémon that participated by switching in.
- **Battle Initiation Mechanics:** To battle a trainer on an adjacent tile, you must face them and press 'A' to interact.

## III. Investigation & Hypothesis Log (v38132)
### A. Confirmed Facts
- **PC Glitch (Confirmed):** The PC in Celadon City is persistently bugged. I must always select 'BILL's PC' to access the Pokémon Storage System.
- **Bike Voucher Location (Confirmed):** The Bike Voucher is obtained from the Pokémon Fan Club Chairman in Vermilion City after listening to his story.
- **`pathfinder` Intelligence (Confirmed):** The tool automatically finds a path to the nearest valid adjacent tile if the specified destination is impassable or unseen.
- **Fuchsia City Warden (Confirmed, T38002):** The Safari Zone Warden is nicknamed 'SLOWPOKE' and has a speech impediment.

### B. Current Plans & Explicit Tests
- **Primary Plan: Find Koga in Fuchsia City.** My `navigation_strategist_agent` correctly identified that I was moving away from Fuchsia City. I was forced to continue east on Route 15 to find a path down to the lower level, which led me to Route 14. I am now exploring Route 14, which appears to be the correct path to loop back west towards my objective.
- **Secondary Test: Route 11 Snorlax:** The path east on Route 11 from the gatehouse is blocked by a Snorlax. (Test: Explore east from the Route 12/11 gatehouse - Low Priority).

## IV. Past Failures & Corrections Log
- **CRITICAL PROCESS FAILURE: Repeated WKG Protocol Violations (T37321 - T38062):** The AI critique has correctly identified a persistent behavioral issue. I repeatedly fail to follow my own core protocol of immediately documenting map transitions. I have deferred WKG updates multiple times, which corrupts my world model and leads to navigational errors. **Correction:** ALL data management tasks (`manage_world_knowledge`, `define_map_marker`, `notepad_edit`) MUST be performed on the same turn a discovery is made. There are no exceptions.
- **CRITICAL NAVIGATIONAL FAILURE: Directional Confusion on Route 15 (T38101):** My `navigation_strategist_agent` correctly identified that I was moving east, away from my objective in Fuchsia City. My pathfinder then confirmed I could not go west from the upper ledge. This forced me to continue east to find a way down. This loop highlights a critical need to better analyze the map before committing to long-distance travel.

## V. Agent & Tool Development Log
- **Idea: Exploration Strategist Agent:** Create an agent that can take a map ID and a high-level goal (e.g., 'find all exits', 'clear all trainers') and generate an optimal sequence of `pathfinder` targets to achieve it.
- **Idea: Route Explorer Tool:** Create a computational tool that takes the list of `Reachable Unseen Tiles` and generates a single, efficient `path_plan` to visit all of them.