## I. Core Principles & Lessons Learned
- **CRITICAL: Agent & Workflow Discipline:**
  - A consistently failing agent is a liability. It must be refined or deleted immediately before reuse.
  - I will strictly adhere to established protocols, especially using `encounter_tracker_agent` after every wild encounter. No exceptions.
- **CRITICAL: Map Marker Discipline:** Markers must only be placed *after* an event is verified.
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Verify Assumptions:** Do not record intel as "completed" or "confirmed" until it has been empirically verified. Non-battling trainers exist.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.

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

## III. World Knowledge Graph Manual Entry Checklist (v9 - Post-Critique)
*This is a fallback procedure for when `wkg_manager_agent_v2` is non-functional.*
1.  **Check Nodes:** `run_code` to check if both source and destination nodes exist.
2.  **Add Missing Nodes:** If any node is missing, use `manage_world_knowledge` `add_node` with a manually constructed JSON payload (including tags).
3.  **Get Node IDs:** If new nodes were added, `run_code` to get their IDs.
4.  **CRITICAL - Check Edge:** `run_code` to check if an edge *already exists* between the two nodes. **DO NOT SKIP THIS STEP.**
5.  **Add Edge:** **ONLY IF STEP 4 CONFIRMS NO EDGE EXISTS**, use `manage_world_knowledge` `add_edge` with a manually constructed JSON payload. **For warp connections, remember to include the `destination_entry_point`!**

## IV. Agent Development Log
### A. Active Agents (Reliable)
- **`pathfinding_agent_v2` (Refined T27750):** Requires monitoring after last failure.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v3):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.
- **`encounter_tracker_agent` (v1):** **CRITICAL REMINDER:** I MUST use this agent after every wild encounter.

### B. Defunct Agents
- **`wkg_manager_agent_v2`:** Deleted T27750 due to catastrophic failure.

### C. Agent Development Backlog
- `wkg_manager_agent_v3`: A simplified agent to generate JSON payloads for `manage_world_knowledge` based on source/destination data. This would reduce manual errors.
- `silph_co_teleporter_mapper_agent`: Takes the current floor's XML and the WKG. Its job would be to identify all teleporters on the current floor and try to map out where they lead based on existing WKG data or suggest which ones are unexplored.
- `damage_calculator_agent`: Takes player/opponent Pokémon data and calculates move damage ranges to confirm KOs.
- `item_finder_agent`

## V. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Explore each floor completely. Map all warps and teleporters. Defeat all grunts and scientists. Use the CARD KEY to unlock all previously inaccessible areas.
- **Unverified Assumptions:**
    1.  *Elevator System:* Are all elevators part of one system, or are there separate shafts?
    2.  *Teleporter Directionality:* Are all teleporters two-way? Must verify by attempting to return immediately after use.
    3.  *CARD KEY Location:* Assuming it's on an upper floor, but could be anywhere.
    4.  *Final Objective:* Is Giovanni the true final boss, or is the goal just to find the CARD KEY and free the President?

- **Trade Evolutions:** Confirmed that Pokémon evolve without link-cable trading.

## VI. Party Composition & Movesets
*A reference to prevent misremembering moves in critical battles.*

- **ECHO (GOLBAT):** WING ATTACK, CONFUSE RAY, FLY, BITE
- **CRAG (GRAVELER):** BODY SLAM, DIG, ROCK THROW, HARDEN
- **SPARKY (PIKACHU):** THUNDERBOLT, THUNDERPUNCH, HEADBUTT, THUNDER WAVE
- **TORRENT (SQUIRTLE):** TAIL WHIP, BUBBLE, WATER GUN, BITE
- **PRISM (EEVEE):** QUICK ATTACK, GROWL, DOUBLE KICK, HEADBUTT
- **SPOONBENDE (KADABRA):** TELEPORT, CONFUSION, DISABLE, PSYCHIC

- Psychic is NOT-VERY-EFFECTIVE against Psychic.

## VII. Type Effectiveness Chart (Observed)
*A log of confirmed type interactions in this ROM hack.*
- Psychic (player) vs. Psychic (opponent) -> Not Very Effective
- Electric (player) vs. Psychic (opponent) -> No Effect (Immune)

## VIII. Agent Idea - `silph_co_teleporter_mapper_agent`
- **Purpose:** To help navigate Silph Co.'s teleporter maze.
- **Input:** `current_map_id`
- **Functionality:** 
  1. Parse `map_xml_string` to identify all teleporter tiles (`<Warp>`) on the current floor.
  2. Parse `world_knowledge_graph_json_string` to find existing nodes and edges related to Silph Co. teleporters.
  3. **Output:** A list of teleporters on the current floor, categorized as:
     - **Mapped:** Teleporter has a known destination in the WKG. Show the destination floor and coordinates.
     - **Unmapped:** Teleporter exists but has no corresponding edge in the WKG. These are high-priority exploration targets.
     - **One-Way:** Mark any teleporters confirmed to be one-way.
- **Benefit:** Would provide a clear list of exploration targets for each floor, preventing me from getting lost or missing paths.