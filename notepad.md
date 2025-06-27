## I. Core Protocols & Immediate Actions (v15)
- **CRITICAL: Agent & Workflow Discipline:**
  - I will use my custom agents whenever a task can be automated or requires complex reasoning.
  - I will use `protocol_enforcement_agent` before every turn to ensure I follow my documented procedures.
- **CRITICAL: Post-Battle Checklist:** After every trainer battle, I MUST:
  1. Mark the defeated trainer with '☠️' using `define_map_marker`.
- **CRITICAL: Wild Encounter Protocol:** After every wild encounter, I MUST:
  1. Use `encounter_tracker_agent` to log the Pokémon.
- **CRITICAL: WKG & Marker Discipline:**
  - After using any teleporter, stair, or elevator, I MUST immediately use `manage_world_knowledge` to document the connection.
  - I will mark used warps (both entry and exit) with '🚪'.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic.
- **Poison Status Immunity:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.
- **Type Immunities:** Psychic is immune to Electric.

### Navigation & Traversal Rules
- **Pikachu Movement:** Pikachu is a walkable object. If Pikachu is directly adjacent in the direction of movement, and you are not already facing it, the first button press will only turn to face it. A second press is needed to move onto its tile.

### New Battle Mechanics Discovered
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **No Blackout on Loss (Rocket Hideout/Silph Co.):** Losing a battle inside a Team Rocket controlled area does not cause a blackout.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.

## III. Agent & Tool Development Log (v21)
### A. Active Agents & Tools (Reliable)
- `pathfinder` (tool): Reliable.
- `pc_navigator_agent` (v2): Reliable.
- `battle_strategist_agent` (v6): Reliable.
- `team_composition_advisor_agent` (v2): Reliable.
- `protocol_enforcement_agent` (v1): I MUST use this before every turn.
### B. Development Backlog
- `inventory_manager_agent`: An agent to help organize and suggest uses for items.
- `dungeon_navigator_agent`: An agent to plot a full exploration course for a multi-floor dungeon like Silph Co.
- `puzzle_solver_agent`: An agent to analyze map XML for changes (like positional gates) and propose solutions to environmental puzzles.

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Explore each floor completely. Map all warps and teleporters. Defeat all trainers. Use the CARD KEY to unlock all previously inaccessible areas.
- **Positional Gate Mechanic (5F):** Gates on this floor are triggered by movement, not a key.
- **Intra-Floor Teleporters (8F):** Discovered a teleporter at (12, 10) that instantly warps to (4, 12) on the same floor.
- **Untested Assumptions (To Be Verified):**
    - *CARD KEY Location:* Could be held by an NPC, be a visible item, or a reward. Must check everything.
    - *Progression Path:* May involve non-linear travel between floors via teleporters.
    - *4 ROCKET BROTHERS:* One defeated on 9F. The location of the other three is unknown.

## V. Type Effectiveness Chart (Observed)
*A log of confirmed type interactions in this ROM hack.*
- Psychic (player) vs. Psychic (opponent) -> Not Very Effective
- Electric (player) vs. Psychic (opponent) -> No Effect (Immune)