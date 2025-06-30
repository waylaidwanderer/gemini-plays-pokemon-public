## I. Core Protocols & Immediate Actions (v38288)
- **CRITICAL: Immediate Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. Deferring tasks is a critical failure. This is my highest priority.
- **CRITICAL: WKG Protocol (v6):** Upon any map transition, I will immediately document BOTH the departure and arrival nodes, and the connecting edge, before any further exploration. All `warp` edges MUST include a `destination_entry_point`. All new nodes MUST have descriptive `tags`. I will use `wkg_inspector` to verify all known exits before declaring an area a dead end.
- **CRITICAL: Map Marker Protocol (v4):** I will mark defeated trainers and used warps (both entry and exit points) *immediately* after the event occurs. I will consolidate redundant markers.
- **CRITICAL: Protocol Enforcement:** I will make a conscious effort to use the `protocol_enforcement_agent` before finalizing my plan each turn to catch my own mistakes.
- **CRITICAL: Agent & Tool Maintenance:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the **ABSOLUTE HIGHEST PRIORITY**, superseding ALL other gameplay objectives.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water, CUT (Normal) > VICTREEBEL (Grass/Poison), Flying > Grass/Poison (super-effective).
- **Type Immunities:** Psychic is immune to Electric. Pidgeotto (Normal/Flying) is immune to Ghost-type moves like Confuse Ray.
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

## III. Investigation & Hypothesis Log (v38288)
### A. Confirmed Facts
- **PC Glitch (Confirmed):** The PC in Celadon City is persistently bugged. I must always select 'BILL's PC' to access the Pokémon Storage System.
- **Bike Voucher Location (Confirmed):** The Bike Voucher is obtained from the Pokémon Fan Club Chairman in Vermilion City after listening to his story.
- **`pathfinder` Intelligence (Confirmed):** The tool automatically finds a path to the nearest valid adjacent tile if the specified destination is impassable or unseen.

### B. Current Plans & Explicit Tests
- **Primary Plan (per `navigation_strategist_agent`):** Obtain the Soul Badge. Current strategy is to navigate through Route 14 to reach Fuchsia City.
- **Hypothesis:** The remaining trainers on Route 14 must be defeated to open the path to Fuchsia City.
- **[CONFIRMED & RESOLVED]** The cuttable tree at (12, 33) blocked the path to a new southern area of Route 14. This path has been opened.

## IV. Past Failures & Corrections Log
- **CRITICAL PROCESS FAILURE: Repeated WKG Protocol Violations (T37321 - T38226):** I have a persistent behavioral issue of failing to immediately and correctly document map transitions. This corrupts my world model and leads to severe navigational errors, such as the loop between Route 14 and 13. **Correction:** ALL data management tasks (`manage_world_knowledge`, `define_map_marker`, `notepad_edit`) MUST be performed on the same turn a discovery is made. Both departure and arrival nodes/markers must be created before further exploration. There are no exceptions.
- **Navigational Failure (Route 14, T38161):** I incorrectly believed the path to Fuchsia City was through the southern part of Route 14, accessed via Route 15. This was confirmed to be a one-way dead end for northbound travel. This highlights the importance of thorough exploration and trusting my WKG. The correct path to Fuchsia City is likely through the western exits of Route 13 or by exploring all of Route 14.

## V. Tile Mechanics Glossary
- **`ground`**: Walkable.
- **`impassable`**: Cannot be walked on. Includes fences, water, and other solid objects.
- **`grass`**: Walkable, allows wild Pokémon encounters.
- **`ledge`**: Can only be jumped down (one-way vertical travel).
- **`cuttable`**: Requires HM Cut to pass. Respawn on map change.
- **CRITICAL REMINDER (T38336):** System has repeatedly warned about ~31 reachable unseen tiles on Route 14. After this battle, I MUST perform a full exploration of the area south of the cuttable trees to resolve this.