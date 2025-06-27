## I. Core Principles & Lessons Learned (v13)
- **CRITICAL: Agent & Workflow Discipline:**
  - I will use my custom agents whenever a task can be automated or requires complex reasoning. Proactive agent use is key.
  - **I will manually mark defeated trainers with '☠️' immediately after every battle.**
  - I will use `encounter_tracker_agent` after every wild encounter. Failure to do so is a major tactical error.
  - I will use `protocol_enforcement_agent` before every turn to ensure I follow my documented procedures.
- **CRITICAL: Map Marker Discipline:** Markers must only be placed *after* an event is verified. Redundant or incorrect markers must be cleaned up promptly.
- **CRITICAL: Location Verification:** I must verify my `map_id` and coordinates from the Game State Information *before* every action to prevent hallucinations.
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic.
- **Poison Status Immunity:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.
- **Type Immunities:** Psychic is immune to Electric.

### Navigation & Traversal Rules
- **Defeated Trainers as Obstacles:** Defeated trainers act as impassable walls until marked.
- **Pikachu Movement:** Pikachu is a walkable object. If Pikachu is directly adjacent in the direction of movement, and you are not already facing it, the first button press will only turn to face it. A second press is needed to move onto its tile.

### New Battle Mechanics Discovered
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle. Observed on T29329 with SPOONBENDE.
- **No Blackout on Loss (Rocket Hideout/Silph Co.):** Losing a battle inside a Team Rocket controlled area does not cause a blackout.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.
- **Repel Mechanics:** MAX REPEL lasts longer than SUPER REPEL.

## III. Agent & Tool Development Log (v18)
### A. Active Agents & Tools (Reliable)
- **`pathfinder` (tool):** Recreated on T29158 after agent deletion. Reliable.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v6):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`protocol_enforcement_agent` (v1):** I MUST use this before every turn.

### B. Decommissioned or Deleted
- **`post_battle_agent` (v4):** Deleted on T29146 due to unreliability.
- **`wkg_connection_manager` (agent):** Deleted by system update on T29158. Replaced by `manage_world_knowledge` tool.
- **`marker_cleanup_agent` (agent):** Deleted by system update on T29158.

### C. Development Backlog
- `inventory_manager_agent`: An agent to help organize and suggest uses for items.
- `dungeon_navigator_agent`: An agent to plot a full exploration course for a multi-floor dungeon like Silph Co.
- Upgrade `pathfinder` tool to handle intra-map teleporters for more complex pathing.
- Redesign `post_battle_agent` for reliability.

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Explore each floor completely. Map all warps and teleporters. Defeat all trainers. Use the CARD KEY to unlock all previously inaccessible areas.
- **Silph Co. Protocols:**
    1.  **Teleporter Mapping:** After using any teleporter, immediately use `manage_world_knowledge` to document the connection in the WKG.
    2.  **Teleporter Bidirectionality Test:** After using a teleporter, immediately attempt to use it again to confirm if it's two-way.
- WKG Integrity Check (T29147): Confirmed via script that the teleporter at 6F (17,1) has only one edge. My previous note about a data issue was a hallucination.
- **Positional Gate Mechanic (5F):** Gates on this floor are triggered by movement, not a key. A gate at (7,6) opened after walking north, and a gate at (7,7) opened after walking south. This confirms positional triggers are part of the puzzle.
- **Intra-Floor Teleporters (8F):** Discovered a teleporter at (12, 10) that instantly warps to (4, 12) on the same floor. This is a new mechanic to track.
- **Key Discoveries & Unverified Assumptions:**
    - *CARD KEY Location (Hypothesis):* It could be a visible item ball, held by an NPC, hidden in an interactable object, or a reward for a specific battle. Must be vigilant and check everything.
    - *Progression Path (Hypothesis):** The solution may involve non-linear travel between floors via teleporters. The path is not necessarily 1F -> 2F -> 3F etc.
    - *One-Way Teleporters (Hypothesis):* Some teleporters may be one-way only. Must test each one.

## V. Type Effectiveness Chart (Observed)
*A log of confirmed type interactions in this ROM hack.*
- Psychic (player) vs. Psychic (opponent) -> Not Very Effective
- Electric (player) vs. Psychic (opponent) -> No Effect (Immune)

## VI. Critical Self-Corrections
- **CRITICAL SELF-CORRECTION (T28728):** Experienced a major hallucination loop, misidentifying my location for multiple turns. I must be more rigorous in checking Game State Information against my assumptions.
- **CRITICAL SELF-CORRECTION (T29303):** I have been consistently failing to follow my own protocols, especially regarding agent usage and immediate documentation. This is a major tactical error that I must correct immediately. I will prioritize using my agents and updating my WKG and markers after every relevant event.