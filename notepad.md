## I. Core Protocols & Immediate Actions (v21)
- **CRITICAL: Agent & Workflow Discipline:**
  - I will use my custom agents whenever a task can be automated or requires complex reasoning. This is not optional.
  - I will use `protocol_enforcement_agent` before every turn to ensure I follow my documented procedures.
- **CRITICAL: Post-Event Checklists (MANDATORY ADHERENCE):**
  - **Trainer Battle:** Mark defeated trainer with '☠️' using `define_map_marker`, using their specific sprite name for clarity (e.g., 'SILPHCO4F_ROCKET2'). Log their Pokémon under 'Trainer Intel'.
  - **Wild Encounter:** Log EVERY wild Pokémon with `encounter_tracker_agent`. NO EXCEPTIONS.
  - **Map Transition (Warp/Stairs/Edge):** Immediately use `manage_world_knowledge` to document the connection and mark used warps (entry/exit) with '🚪'.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic.
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).

### B. Navigation & Traversal Rules
- **Pikachu Movement:** A walkable object. Requires two button presses to move onto its tile if not already facing it.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **No Blackout Zones:** Losing in Rocket Hideout or Silph Co. does not cause a blackout.

### C. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.

## III. Agent & Tool Development Log (v31)
### A. Active Agents & Tools (Reliable)
- `pathfinder` (tool)
- `pc_navigator_agent` (v2)
- `team_composition_advisor_agent` (v2)
- `protocol_enforcement_agent` (v1)
- `select_battle_option` (tool)
- `encounter_tracker_agent` (v1)

### B. Agents Under Review / Needing Refinement
- `battle_strategist_agent` (v7): Needs refinement to better handle high-evasion opponents. Must prioritize moves that cannot miss (e.g., Swift) or status moves over standard attacks when evasion is boosted.

### C. Development Backlog
- **`json_payload_generator` (CRITICAL PRIORITY):** To prevent syntax errors when calling tools like `manage_world_knowledge` by taking simple inputs and generating the full JSON string.
- **`dungeon_navigator_agent` (High Priority):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co.
- **`puzzle_solver_agent` (High Priority):** To analyze map XML for changes (e.g., positional gates) and propose puzzle solutions.
- `navigator_agent`: For overworld pathfinding.
- `inventory_manager_agent`: To organize and suggest item uses.
- **`grinding_assistant_agent` (High Priority):** To automate the generation of optimal back-and-forth movement patterns for grinding wild Pokémon in a specific area.

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Systematically explore each floor, mapping all teleporters and defeating all trainers. Use the CARD KEY on all locked doors upon acquisition.
- **Discoveries:**
    - **Hint:** The BOSS is on 11F (from a Rocket on 4F).
    - **5F:** Positional gates triggered by movement. Teleporter at (12,6) leads to 3F.
    - **8F:** Intra-floor teleporter loop between (12, 10) and (4, 12).
    - **10F -> 4F Warp:** Teleporter at (10, 12) on 10F leads to an isolated room on 4F at (12, 8). The teleporter in this room leads back to 10F.
    - **10F -> 11F Warp:** Teleporter at (11, 1) on 10F leads to an isolated room on 11F.

## V. Trainer Intel
*A log of noteworthy trainer Pokémon rosters.*
- **Silph Co. 2F Scientist (6, 14):** Muk (Lv37), Weezing (Lv37), Porygon (Lv37)
- **Silph Co. 4F Rocket (10, 15):** Machoke (Lv39), Hypno (Lv39)
- **Silph Co. 4F Scientist (15, 7):** Electabuzz (Lv41)

## VI. Type Effectiveness Chart (Observed)
*A log of confirmed type interactions in this ROM hack.*
- Psychic (player) vs. Psychic (opponent) -> Not Very Effective
- Electric (player) vs. Psychic (opponent) -> No Effect (Immune)

## VII. Active Investigations & Untested Assumptions (Post-Reflection)
- **Assumption 1 (Training Efficiency):** The Pokémon Tower is the *best* place to train SPOONBENDE and PRISM. **Test:** Monitor EXP gain per battle. If too slow, re-evaluate training location.
- **Assumption 2 (Level Sufficiency):** Leveling to 35 will be *enough* for Silph Co. The agent's confidence was near-zero. **Test:** After training, re-run `team_composition_advisor_agent`. If confidence remains critically low, I must find an alternative path to progression, possibly in a different city or by finding a key item like HM04 (Strength).
- **Assumption 3 (HM Requirements):** I may need HM04 (Strength) to progress in Silph Co. or elsewhere. **Test:** Be vigilant for any NPCs mentioning Strength or any visible boulders that could be moved.