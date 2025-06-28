## I. Core Protocols & Immediate Actions (v25)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays. I will verify my current map_id and coordinates from the Game State Information BEFORE every documentation action.
- **CRITICAL: Agent & Workflow Discipline:** I will use my custom agents whenever a task can be automated or requires complex reasoning. I will prioritize developing agents that solve my most immediate problems.
- **CRITICAL: Post-Event Checklists (MANDATORY):**
  - **Trainer Battle:** Mark defeated trainer with '☠️' and log their Pokémon under 'Trainer Intel'.
  - **Wild Encounter:** Log EVERY wild Pokémon with `encounter_tracker_agent`.
  - **Map Transition (Warp/Stairs/Edge):** Immediately use `manage_world_knowledge` to document the connection and mark used warps (entry/exit) with '🚪'.

## II. Game Mechanics & Battle Intel
### A. Confirmed ROM Hack Changes
- **Type Matchups:** Psychic > Ghost/Poison, Ghost > Psychic, Bite (Normal) > Psychic, Normal !> Psychic, Electric > Rock/Water.
- **Type Immunities:** Psychic is immune to Electric.
- **Status Ailments:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves. MUK appears to be immune to powder-based status moves (SLEEP POWDER, STUN SPORE).
- **Evasion Mechanics:** PSYWAVE, a move that should never miss, can fail against a target with extreme evasion boosts (e.g., multiple MINIMIZE uses).
- **Poison Type Effectiveness:** Poison-type moves are NOT-VERY-EFFECTIVE against Poison-types.

### B. Navigation & Traversal Rules
- **Pikachu Movement:** A walkable object. Requires two button presses to move onto its tile if not already facing it.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **No Blackout Zones:** Losing in Rocket Hideout or Silph Co. does not cause a blackout.
- **Saffron City Navigation:** The city's layout is segmented. The `pathfinder` tool is unreliable here. Using FLY is the most efficient method for traveling between distant points.
- **Silph Co. Elevator:** Requires a two-step process. First, interact with the panel to select a floor. Second, walk onto one of the warp tiles at the back of the elevator room to trigger the map change.

### C. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.

### D. HM & Field Move Mechanics
- HMs can be used directly from the ITEM menu without being taught to a Pokémon. This is a significant time-saver for field moves like Flash and Cut. To use an HM from the bag, select the HM, choose 'USE', and then select 'NO' when prompted to teach it.

## III. Agent & Tool Development Log (v39)
### A. Development Priorities
- **`json_payload_generator` (TOP PRIORITY):** To prevent syntax errors when calling tools like `manage_world_knowledge`. Manual JSON scripting is too slow and error-prone.
- **`dungeon_navigator_agent` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. This is essential for finding the CARD KEY efficiently.

### B. Active Agents (Reliable)
- `pc_navigator_agent` (v2)
- `team_composition_advisor_agent` (v2)
- `protocol_enforcement_agent` (v1)
- `encounter_tracker_agent` (v1)
- `battle_strategist_agent` (v9)

### C. Active Tools (Reliable)
- `pathfinder` (limitation: unreliable for complex, segmented city maps like Saffron City).
- `select_battle_option`

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Systematically explore each floor, mapping all teleporters and defeating all trainers. Use the CARD KEY on all locked doors upon acquisition.
- **Discoveries:**
    - **Hint:** The BOSS is on 11F (from a Rocket on 4F).
    - **5F:** Positional gates triggered by movement. Puzzle unsolved. The western area is inaccessible from the central room.
    - **8F:** Intra-floor teleporter loop.

## V. Trainer Intel
*A log of noteworthy trainer Pokémon rosters.*
- **Silph Co. 2F Scientist (6, 14):** Muk (Lv37), Weezing (Lv37), Porygon (Lv37)
- **Silph Co. 4F Rocket (10, 15):** Machoke (Lv39), Hypno (Lv39)
- **Silph Co. 4F Scientist (15, 7):** Electabuzz (Lv41)
- **Silph Co. 5F Rocket (9, 17):** Tauros (Lv40)
- **Silph Co. 9F Scientist (22, 14):** Muk (Lv40), Kabutops (Lv40)

## VI. Active Investigations & Untested Assumptions
- **Assumption 1 (CARD KEY Location):** The `CARD KEY` is a physical item (Poké Ball) on the ground. **Hypothesis:** It could be given by an NPC after a specific trigger. **Test:** Continue systematically clearing floors and talking to all NPCs.
- **Assumption 2 (Gate Puzzles):** The closed gates on various floors (5F, 7F, etc.) are part of a puzzle I can solve on that floor. **Hypothesis:** They might be opened by a master switch on a completely different floor. **Test:** Continue exploring all floors thoroughly. The `dungeon_navigator_agent` would be key here.
- **Assumption 3 (Rocket Progression):** I need to defeat all Rockets to progress. **Hypothesis:** Some might just provide flavor text. **Test:** If a Rocket doesn't battle me, mark them as non-hostile ('💬') and move on, not assuming they are a progression blocker unless they physically block the path.
- **Assumption 4 (HM Field Use):** The 'use from bag' mechanic is inconsistent. Cut can be used without teaching, but Flash MUST be taught to a Pokémon to be used in the field. Assumption: Other HMs like Fly and Surf will also need to be taught. **Test:** Next time I am outdoors, I will attempt to use Fly directly from the item menu.

## VII. Lessons Learned & Protocol Corrections
- **Protocol Failure (T30985):** I attempted to log a Silph Co. warp connection (8F 12,6 to 2F 28,16) that already existed in the World Knowledge Graph. I had clearly forgotten this path because I failed to mark the warp with '🚪' on both ends immediately after using it the first time. **Correction:** Must be more disciplined. Trust system errors. Mark ALL warps immediately.
- **Protocol Failure (T30988):** I misidentified a warp on Silph Co. 8F at (4,12) as navigable. It was in an isolated room. **Correction:** I must verify warp reachability from my current position before listing it in my validation checks.

## VIII. Post-Event Protocols (v1)
- **Post-Blackout Recovery:** 1. Use `team_composition_advisor_agent` to devise a new strategy and team. 2. Use `pc_navigator_agent` to execute the recommended changes. 3. Train the new team to the level cap if required.
- **Protocol Update (T31290):** A single bidirectional edge (`is_one_way: false`) in the WKG covers two-way travel. Do not create a second, reversed edge for the same connection.
- **Protocol Failure (T31320):** I have repeatedly hallucinated my location and map ID, leading to multiple failed tool calls and wasted turns. **Correction:** I MUST verify my current `map_id` and coordinates from the Game State Information *before* every single action, especially navigation and documentation. I will also trust system warnings about reachability and dead ends.