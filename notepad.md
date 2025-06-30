## I. Core Protocols & Immediate Actions (v37872)
- **CRITICAL: Immediate Tool & Agent Maintenance:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the **ABSOLUTE HIGHEST PRIORITY**, superseding ALL other gameplay objectives. I will stop all other actions and use `define_tool` or `define_agent` to fix it on the very next turn. This is non-negotiable and is not a 'goal' to be deferred.
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure.
- **CRITICAL: WKG Protocol (v4):** Before adding any node or edge, I will FIRST query the WKG with `wkg_checker` to confirm it doesn't already exist. All `warp` edges MUST include a `destination_entry_point`. All new nodes MUST have descriptive `tags`. I will use `wkg_inspector` to verify all known exits before declaring an area a dead end.
- **CRITICAL: Map Marker Protocol (v2):** I will mark defeated trainers and used warps (both entry and exit points) *immediately* after the event occurs. This is not a task to be deferred.

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
- **Respawning Trees:** Cuttable trees respawn after a short time, even without leaving the map.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any Pokémon that participated by switching in.
- **Battle Initiation Mechanics:** To battle a trainer on an adjacent tile, you must face them and press 'A' to interact.

## III. Investigation & Hypothesis Log (v37872)
### A. Confirmed Facts
- **PC Glitch (Confirmed):** The PC in Celadon City is persistently bugged. I must always select 'BILL's PC' to access the Pokémon Storage System.
- **Bike Voucher Location (Confirmed):** The Bike Voucher is obtained from the Pokémon Fan Club Chairman in Vermilion City after listening to his story.
- **`pathfinder` Intelligence (Confirmed):** The tool automatically finds a path to the nearest valid adjacent tile if the specified destination is impassable or unseen.
- **Route 17 One-Way Path (Confirmed, T37818):** Route 17 is a one-way downhill path. Attempts to travel north from (10, 51) have failed repeatedly (5+ times). Attempts to travel west from (9, 88) also failed repeatedly (5+ times). This confirms I must travel south.

### B. Current Hypotheses (Untested)
- **Cycling Road Access:** Accessing Cycling Road requires a Bicycle. (Test: Attempt to enter Cycling Road after obtaining a Bicycle).
- **Snorlax Permanence:** I assume the Snorlax I defeated on Route 12 is gone permanently. (Test: Return to Route 12 at (11,63) - Low Priority).
- **Route 11 Blockage:** I assume the path east on Route 11 from the gatehouse is blocked by a Snorlax. (Test: Explore east from the Route 12/11 gatehouse - Low Priority).
- **Route 18 Gatehouse:** The gatehouse on Route 18 leads to Fuchsia City. (Test: Reach and enter the gatehouse).

### C. Current Plans
- **Route 18 Navigation:** The goal is to reach Fuchsia City. The western part of the route was a dead end. I will now explore the eastern grass patch to find the path to the gatehouse.

## IV. Future Development Ideas
- **Objective Prioritization Agent:** Create an agent to analyze the current game state (location, goals, available routes) and suggest the most logical next high-level objective to prevent getting stuck or pursuing inefficient paths.

## V. Past Failures & Corrections Log
- **CRITICAL PROCESS FAILURE: Repeated WKG Protocol Violations (T37321 - T37818):** The AI critique has correctly identified a persistent behavioral issue. I repeatedly fail to follow my own core protocol of immediately documenting map transitions. I have deferred WKG updates multiple times, which corrupts my world model and leads to navigational errors. **Correction:** ALL data management tasks (`manage_world_knowledge`, `define_map_marker`, `notepad_edit`) MUST be performed on the same turn a discovery is made. There are no exceptions.
- **Biker Bug (Route 16, T37463):** The Biker at (8, 11) is bugged. Interacting with him fails. **AVOID THIS TRAINER.**
- **CRITICAL PROCESS FAILURE: Deferred Data Management (T37853 - T37860):** The AI critique correctly identified that I delayed marking a defeated trainer and updating the WKG for several turns after the event. This is a violation of my core protocol. **Correction:** This reinforces the need for immediate data entry on the same turn as the discovery. This is non-negotiable.