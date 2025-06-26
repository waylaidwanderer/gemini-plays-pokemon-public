## I. Core Principles & Lessons Learned (v4)
- **CRITICAL: Agent & Workflow Discipline:**
  - I will use my custom agents whenever a task can be automated or requires complex reasoning. Proactive agent use is key.
  - I will **strictly** adhere to established protocols, especially using `encounter_tracker_agent` after **every** wild encounter and `silph_co_teleporter_mapper_agent` after every warp in Silph Co. No exceptions.
- **CRITICAL: Map Marker Discipline:** Markers must only be placed *after* an event is verified.
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic.
- **Poison Status Immunity:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.
- **Type Immunities:** Psychic is immune to Electric.

### Navigation & Traversal Rules
- **Defeated Trainers as Obstacles:** Defeated trainers act as impassable walls.
- **Pikachu Movement:** Pikachu is a walkable object. If Pikachu is directly adjacent in the direction of movement, and you are not already facing it, the first button press will only turn to face it. A second press is needed to move onto its tile.

### New Battle Mechanics Discovered
- **'No Will to Fight' Mechanic:** A Pokémon with very low HP may refuse to be switched into battle.
- **No Blackout on Loss (Rocket Hideout/Silph Co.):** Losing a battle inside a Team Rocket controlled area does not cause a blackout.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.
- **Repel Mechanics:** MAX REPEL lasts longer than SUPER REPEL.

## III. Agent Development Log (v5)
### A. Active Agents (Reliable)
- **`pathfinding_agent_v2`:** Highly reliable; past perceived 'failures' were due to player hallucination, not agent error.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v6 - Refined T28213):** Now incorporates damage calculation for more precise recommendations.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`encounter_tracker_agent` (v1):** **CRITICAL REMINDER:** I MUST use this agent after every wild encounter.
- **`silph_co_teleporter_mapper_agent` (v1):** New agent to map teleporters. Ready for use.
- **`wkg_payload_generator` (v2 - Refined T28311):** Generates JSON payload strings for the `manage_world_knowledge` tool.
- **`item_finder_agent` (v2 - Refined T28325):** Scans current map for item balls.

### B. Agent Development Backlog
- `inventory_manager_agent`: An agent to help organize and suggest uses for items.

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Explore each floor completely. Map all warps and teleporters. Defeat all trainers. Use the CARD KEY to unlock all previously inaccessible areas.
- **Silph Co. Protocols:**
    1.  **Teleporter Mapping:** After using any teleporter, immediately use `silph_co_teleporter_mapper_agent` to document the connection in the WKG.
    2.  **Teleporter Bidirectionality Test:** After using a teleporter, immediately attempt to use it again to confirm if it's two-way.
- **Key Discoveries & Unverified Assumptions:**
    - *CARD KEY Location:* Assuming it's a visible item ball, but could be held by an NPC or in a non-obvious interactable. Must be vigilant.
    - *Progression Path:* Assuming linear floor-by-floor progression, but the solution may involve non-linear travel between floors via teleporters.

## V. Silph Co. Exploration Plan (v2 - Granular)
*A systematic, granular checklist for clearing Silph Co.*
- **Floor 1F:** [x] Explored all rooms. [x] Mapped all warps.
- **Floor 2F:**
  - [x] SILPHCO2F_ROCKET1 defeated at (17, 12).
  - [x] SILPHCO2F_ROCKET2 defeated at (25, 8).
  - [x] SILPHCO2F_SCIENTIST2 defeated at (25, 14).
  - [ ] Defeat SILPHCO2F_SCIENTIST1 at (6, 13).
  - [ ] Explore all rooms.
  - [ ] Map all warps.
- **Floor 3F:** [x] Explored all rooms. [x] Defeated all trainers. [x] Mapped all warps.
- **Floor 4F:**
  - [ ] Defeat ROCKET at (11, 14).
  - [ ] Defeat JUGGLER at (4, 13).
  - [ ] Explore all rooms.
  - [ ] Map all warps.
- **Floor 5F:**
  - [x] ROCKET defeated at (29, 5).
  - [x] JUGGLER defeated at (24, 12).
  - [x] SCIENTIST defeated at (4, 13).
  - [ ] Explore all rooms.
  - [ ] Map all warps.
- **Floor 6F:**
  - [x] ROCKET defeated at (18, 4).
  - [x] SCIENTIST defeated at (8, 9).
  - [ ] Explore all rooms.
  - [ ] Map all warps.
- **Floor 7F:**
  - [ ] Defeat ROCKET at (26, 8).
  - [ ] Defeat JUGGLER at (10, 13).
  - [ ] Defeat ROCKET at (4, 12).
  - [ ] Explore all rooms.
  - [ ] Map all warps.
- **Floor 8F:**
  - [x] ROCKET defeated at (13, 16).
  - [ ] Defeat ROCKET at (6, 9).
  - [ ] Explore all rooms.
  - [ ] Map all warps.
- **Floor 9F:**
  - [ ] Defeat ROCKET at (24, 12).
  - [ ] Explore all rooms.
  - [ ] Map all warps.
- **Floor 10F:**
  - [x] SCIENTIST defeated at (11, 3).
  - [ ] Defeat ROCKET at (4, 13).
  - [ ] Explore all rooms.
  - [ ] Map all warps.
- **Floor 11F:**
  - [ ] Defeat ROCKET at (23, 13).
  - [ ] Explore all rooms.
  - [ ] Map all warps.

## VI. Type Effectiveness Chart (Observed)
*A log of confirmed type interactions in this ROM hack.*
- Psychic (player) vs. Psychic (opponent) -> Not Very Effective
- Electric (player) vs. Psychic (opponent) -> No Effect (Immune)