## I. Core Principles & Lessons Learned (v5)
- **CRITICAL: Agent & Workflow Discipline:**
  - I will use my custom agents whenever a task can be automated or requires complex reasoning. Proactive agent use is key.
  - I will **strictly** adhere to established protocols, especially using `encounter_tracker_agent` after **every** wild encounter. Failure to do so is a major tactical error.
- **CRITICAL: Map Marker Discipline:** Markers must only be placed *after* an event is verified.
- **CRITICAL: Location Verification:** I must verify my `map_id` and coordinates from the Game State Information *before* every action to prevent hallucinations.
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

## III. Agent Development Log (v7)
### A. Active Agents (Reliable)
- **`pathfinding_agent_v2` (v3 - Refined T28565):** Highly reliable; can now auto-detect unseen tiles for exploration.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v6):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`encounter_tracker_agent` (v1):** **CRITICAL REMINDER:** I MUST use this agent after every wild encounter.
- **`item_finder_agent` (v2):** Scans current map for item balls.
- **`wkg_connection_manager` (v3 - Refined T28570):** Now correctly handles multi-turn node/edge creation and includes `destination_entry_point`.

### B. Agent Development Backlog
- `inventory_manager_agent`: An agent to help organize and suggest uses for items.
- `protocol_enforcement_agent`: To remind me to follow my own established procedures.
- `silph_co_pathfinder_agent`: A specialized agent that can plot multi-floor routes within Silph Co. using the WKG, once the CARD KEY is found.
- Make `wkg_connection_manager` more autonomous (handle multi-turn logic internally).

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Explore each floor completely. Map all warps and teleporters. Defeat all trainers. Use the CARD KEY to unlock all previously inaccessible areas.
- **Silph Co. Protocols:**
    1.  **Teleporter Mapping:** After using any teleporter, immediately use `wkg_connection_manager` to document the connection in the WKG.
    2.  **Teleporter Bidirectionality Test:** After using a teleporter, immediately attempt to use it again to confirm if it's two-way.
- **Key Discoveries & Unverified Assumptions:**
    - *CARD KEY Location (Hypothesis):* It could be a visible item ball, held by an NPC, hidden in an interactable object, or a reward for a specific battle. Must be vigilant and check everything.
    - *Progression Path (Hypothesis):* The solution may involve non-linear travel between floors via teleporters.
    - *One-Way Teleporters (Hypothesis):* Some teleporters may be one-way only. Must test each one.

## V. Type Effectiveness Chart (Observed)
*A log of confirmed type interactions in this ROM hack.*
- Psychic (player) vs. Psychic (opponent) -> Not Very Effective
- Electric (player) vs. Psychic (opponent) -> No Effect (Immune)