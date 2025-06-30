## I. Core Protocols & Immediate Actions (v134)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. NO DELAYS. This includes documenting faulty tools and agents.
- **CRITICAL: WKG Protocol:** Before adding any node or edge, I will FIRST query the WKG with `wkg_checker` to confirm it doesn't already exist. All `warp` edges MUST include a `destination_entry_point`. All new nodes MUST have descriptive `tags`.
- **CRITICAL: Map Marker Protocol:** I will immediately mark defeated trainers and other key events. Redundant markers will be deleted.
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents for complex reasoning and my custom tools for computational tasks. I will use `protocol_enforcement_agent` to check my logic.
- **CRITICAL: Tool Maintenance Protocol:** If a custom tool or agent is found to be faulty or bugged, fixing it becomes the highest priority secondary goal, superseding ALL other gameplay objectives until resolved.

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
- **`reachable` Flag is Global:** The `reachable` flag for warps and map sprites is a global check for the entire map, NOT a local check based on the player's current isolated segment.
- **Saffron City Navigation:** The city's layout is segmented. Using FLY is the most efficient method for traveling between distant points.
- **Invisible Walls:** Impassable walls that are not visually represented. Discovered on Silph Co. 9F at (12, 2).
- **Silph Co. Gate Mechanic:** Gates in Silph Co. appear to be controlled by the player's X-coordinate in a corresponding, physically separate corridor.
- **HM & Field Move Mechanics:**
    - **Flash & Cut Exception:** These HMs MUST be taught to a Pokémon to be used in the field.
    - **PC Interaction:** Must be activated by standing on the tile directly below the PC object (Y+1), facing up, and then pressing A.
    - **Respawning Trees:** Cuttable trees respawn after a short time, even without leaving the map.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle (the lead) and any Pokémon that participated by switching in.

## III. Tool Development Log (v135)
### A. Active Agents & Tools
- **Agents:**
  - `team_composition_advisor_agent` (v2) - Reliable
  - `protocol_enforcement_agent` (v1) - Reliable
  - `battle_strategist_agent` (v15) - Refined and reliable.
- **Tools:**
  - `select_battle_option` (v1) - Reliable
  - `pathfinder` (v5) - Refined.
  - `object_finder` (v1) - Reliable
  - `wkg_checker` (v3) - Reliable

### B. Development Pipeline
- **PC Navigation Tool:** Need to create a tool to replace the unreliable `pc_navigator_agent`. This tool will take deposit/withdraw commands and generate the precise button sequence. To be built on next PC visit.

### C. Deprecated Agents & Tools
- `pc_navigator_agent` (v3) - **DELETED.** Unreliable for deterministic menu navigation. To be replaced with a tool.

## IV. Investigation Log (v135)
### A. Silph Co. Intel
- **Boardroom Location:** A Rocket on 10F at (2,10) confirmed the boardroom is on the 11th floor.
- **Bugged Rocket (5F West):** The Rocket at (9,17) in the western segment of 5F is bugged and soft-locks progress. The only exit is the teleporter back to 9F.

### B. Untested Assumptions & Hypotheses
- **PC Glitch:** The PC in Celadon City is persistently bugged and I must always select 'BILL's PC' to access the Pokémon Storage System. This needs to be re-verified on next use.
- **Battle Mechanic Anomaly:** During the battle with Pixel's Dodrio on Silph Co. 7F, Dodrio used Fly, but the game displayed "But, it failed!". My subsequent move, Confuse Ray, also failed. The turn then reset to the main battle menu, with Dodrio not in the air. The reason for these failures is unknown.
- **Snorlax Permanence:** I assume the Snorlax I defeated on Route 12 is gone permanently. Need to verify by returning to the location at (11,63).
- **Route 11 Blockage:** I assume the path east on Route 11 is blocked by another Snorlax, similar to the one on Route 12/16. I need to explore east to the gatehouse to confirm.
## V. Action Items & Reminders (v135)
- **Marker Cleanup (Vermilion City):** Delete redundant markers at (24, 14), (12, 4), and (13, 20) on next visit.