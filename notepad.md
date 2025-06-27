## I. Core Protocols & Immediate Actions (v17)
- **CRITICAL: Agent & Workflow Discipline:**
  - I will use my custom agents whenever a task can be automated or requires complex reasoning.
  - I will use `protocol_enforcement_agent` before every turn to ensure I follow my documented procedures.
- **CRITICAL: Post-Event Checklists:**
  - **Trainer Battle:** Mark defeated trainer with '☠️' using `define_map_marker`, using their specific sprite name for clarity. Log their Pokémon under 'Trainer Intel'.
  - **Wild Encounter:** Log the Pokémon with `encounter_tracker_agent`.
  - **Map Transition (Warp/Stairs/Edge):** Immediately use `manage_world_knowledge` to document the connection and mark used warps (entry/exit) with '🚪'.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic.
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.

### B. Navigation & Traversal Rules
- **Pikachu Movement:** A walkable object. Requires two button presses to move onto its tile if not already facing it.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **No Blackout Zones:** Losing in Rocket Hideout or Silph Co. does not cause a blackout.

### C. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.

## III. Agent & Tool Development Log (v24)
### A. Active Agents & Tools (Reliable)
- `pathfinder` (tool)
- `pc_navigator_agent` (v2)
- `battle_strategist_agent` (v6)
- `team_composition_advisor_agent` (v2)
- `protocol_enforcement_agent` (v1) - *MUST use before every turn.*

### B. Development Backlog
- `navigator_agent`: For overworld pathfinding.
- `json_payload_generator`: To assist in creating correct JSON for tool calls.
- `dungeon_navigator_agent`: To plot a full exploration course for multi-floor dungeons like Silph Co.
- `inventory_manager_agent`: To organize and suggest item uses.
- `puzzle_solver_agent`: To analyze map XML for changes (e.g., positional gates) and propose solutions.

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Systematically explore each floor, mapping all teleporters and defeating all trainers. Use the CARD KEY on all locked doors upon acquisition.
- **Discoveries:**
    - **Hint:** The BOSS is on 11F (from a Rocket on 4F).
    - **5F:** Positional gates triggered by movement. Teleporter at (12,6) leads to 3F.
    - **8F:** Intra-floor teleporter loop between (12, 10) and (4, 12).
    - **10F -> 4F Warp:** Teleporter at (10, 12) on 10F leads to an isolated room on 4F at (12, 8). The teleporter in this room leads back to 10F.
- **Untested Assumptions (To Be Verified):**
    - *CARD KEY Location:* Could be held by an NPC, be a visible item, or a reward. Must check everything.
    - *Progression Path:* May involve non-linear travel between floors via teleporters. The BOSS on 11F might not be the key to progression.

## V. Trainer Intel
*A log of noteworthy trainer Pokémon rosters.*
- **Silph Co. 4F Rocket (10, 15):** Machoke (Lv39), Hypno (Lv39)
- **Silph Co. 4F Scientist (15, 7):** Electabuzz (Lv41)

## VI. Type Effectiveness Chart (Observed)
*A log of confirmed type interactions in this ROM hack.*
- Psychic (player) vs. Psychic (opponent) -> Not Very Effective
- Electric (player) vs. Psychic (opponent) -> No Effect (Immune)