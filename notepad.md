## I. Core Protocols & Immediate Actions (v23)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays. **I must verify my current map_id and coordinates from the Game State Information BEFORE every documentation action to prevent hallucinations.**
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents whenever a task can be automated or requires complex reasoning. This is not optional.
- **CRITICAL: Post-Event Checklists (MANDATORY ADHERENCE):**
  - **Trainer Battle:** Mark defeated trainer with '☠️' using `define_map_marker`, using their specific sprite name for clarity. Log their Pokémon under 'Trainer Intel'.
  - **Wild Encounter:** Log EVERY wild Pokémon with `encounter_tracker_agent`.
  - **Map Transition (Warp/Stairs/Edge):** Immediately use `manage_world_knowledge` to document the connection and mark used warps (entry/exit) with '🚪'.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water.
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).

### B. Navigation & Traversal Rules
- **Pikachu Movement:** A walkable object. Requires two button presses to move onto its tile if not already facing it.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **No Blackout Zones:** Losing in Rocket Hideout or Silph Co. does not cause a blackout.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **Saffron City Navigation:** The city's layout is segmented. The `pathfinder` tool is unreliable here. Using FLY is the most efficient method for traveling between distant points.

### C. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.

## III. Agent & Tool Development Log (v37)
### A. Active Agents (Reliable)
- `pc_navigator_agent` (v2)
- `team_composition_advisor_agent` (v2)
- `protocol_enforcement_agent` (v1)
- `encounter_tracker_agent` (v1)
- `battle_strategist_agent` (v9)

### B. Active Tools (Reliable)
- `pathfinder` (limitation: unreliable for complex, segmented city maps like Saffron City).
- `select_battle_option`

### C. Agents Under Review / Needing Refinement
- `battle_strategist_agent` (v9): Refined to be more cautious with two-turn moves at critical HP. Will continue to monitor.

### D. Development Backlog
- **`json_payload_generator` (TOP PRIORITY):** To prevent syntax errors when calling tools like `manage_world_knowledge` by taking simple inputs and generating the full JSON string. My manual scripting for WKG is too slow and error-prone.
- **`dungeon_navigator_agent` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. This is essential for finding the CARD KEY efficiently.
- **`puzzle_solver_agent` (High Priority):** To analyze map XML for changes (e.g., positional gates) and propose puzzle solutions.
- **`grinding_assistant_agent` (Medium Priority):** To automate the generation of optimal back-and-forth movement patterns for grinding wild Pokémon in a specific area.
- `reachable_warp_lister_tool` (Low Priority): A simple tool to print a list of reachable warps to prevent future hallucinations and misjudgements of dead ends.
- `navigator_agent`: For overworld pathfinding.
- `inventory_manager_agent`: To organize and suggest item uses.

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Systematically explore each floor, mapping all teleporters and defeating all trainers. Use the CARD KEY on all locked doors upon acquisition.
- **Outstanding Tasks:**
    - **Fix Contradictory Marker:** Delete the '💬' marker from the Rocket at (20, 3) on 8F. The '☠️' marker is correct.
- **Discoveries:**
    - **Hint:** The BOSS is on 11F (from a Rocket on 4F).
    - **5F:** Positional gates triggered by movement.
    - **8F:** Intra-floor teleporter loop.

## V. Trainer Intel
*A log of noteworthy trainer Pokémon rosters.*
- **Silph Co. 2F Scientist (6, 14):** Muk (Lv37), Weezing (Lv37), Porygon (Lv37)
- **Silph Co. 4F Rocket (10, 15):** Machoke (Lv39), Hypno (Lv39)
- **Silph Co. 4F Scientist (15, 7):** Electabuzz (Lv41)
- **Silph Co. 5F Rocket (9, 17):** Tauros (Lv40)
- **Silph Co. 9F Scientist (22, 14):** Muk (Lv40), Kabutops (Lv40)

## VI. Type Effectiveness Chart (Observed)
*A log of confirmed type interactions in this ROM hack.*
- Psychic (player) vs. Psychic (opponent) -> Not Very Effective
- Electric (player) vs. Psychic (opponent) -> No Effect (Immune)
- Electric (player) vs. Rock/Water (opponent) -> Super-Effective

## VII. Active Investigations & Untested Assumptions (Post-Reflection)
- **Assumption 1 (CARD KEY Location):** The `CARD KEY` is a physical item (Poké Ball) on the ground. **Hypothesis:** It could be given by an NPC after a specific trigger. **Test:** Continue systematically clearing floors and talking to all NPCs.
- **Assumption 2 (Gate Puzzles):** The closed gates on 10F are part of a puzzle I can solve on that floor. **Hypothesis:** They might be opened by a switch on a completely different floor. **Test:** Continue exploring all floors thoroughly. The `dungeon_navigator_agent` would be key here.
- **Assumption 3 (Rocket Progression):** I need to defeat all Rockets to progress. **Hypothesis:** Some might just provide flavor text. **Test:** If a Rocket doesn't battle me, mark them as non-hostile ('💬') and move on, not assuming they are a progression blocker unless they physically block the path.
- Reminder: Mark elevator warp at (3,4) on map ID 236 as leading to 7F.