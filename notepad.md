## I. Core Protocols & Immediate Actions (v27)
- **CRITICAL: Immediate & ACCURATE Data Management:** I will use `manage_world_knowledge`, `define_map_marker`, and `notepad_edit` on the *same turn* a discovery is made. No delays. I will verify my current map_id and coordinates from the Game State Information BEFORE every documentation action. I will also consult map markers before navigating to or interacting with a target.
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

### B. Battle Protocols (v2)
- **Agent Reliance (MANDATORY):** I will use the `battle_strategist_agent` for all significant battles (Gyms, Rival, unique encounters like Snorlax) to ensure optimal move selection. Manual control is for routine wild battles only. This protocol is a direct response to repeated AI critiques about underutilizing my agents.

### C. Navigation & Traversal Rules
- **Pikachu Movement:** A walkable object. Requires two button presses to move onto its tile if not already facing it.
- **'No Will to Fight' Mechanic:** A fainted Pokémon cannot be switched into battle.
- **Silph Co. Blackout:** Losing in Silph Co. *does* cause a blackout and returns you to the last used Pokémon Center.
- **Saffron City Navigation:** The city's layout is segmented. The `pathfinder` tool is unreliable here. Using FLY is the most efficient method for traveling between distant points.
- **Silph Co. Elevator:** Requires a two-step process. First, interact with the panel to select a floor. Second, walk onto one of the warp tiles at the back of the elevator room to trigger the map change.
- **Route 12 Pier:** The pier is segmented into isolated sections, making manual navigation tricky and the `pathfinder` tool highly unreliable (it frequently suggests paths into water). The only way to proceed south from the northern pier is to find the correct warp point, not by walking.

### D. General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.

### E. HM & Field Move Mechanics
- HMs can be used directly from the ITEM menu without being taught to a Pokémon. This is a significant time-saver for field moves like Flash and Cut. To use an HM from the bag, select the HM, choose 'USE', and then select 'NO' when prompted to teach it.
- **Flash Exception:** Flash MUST be taught to a Pokémon to be used in the field.

### F. Key Items Obtained
- **SUPER ROD:** From Fishing Guru in house on Route 12 (accessed via warp at (12, 78)).

## III. Agent & Tool Development Log (v45)
### A. Development Priorities
- **`json_payload_generator` (TOP PRIORITY):** To prevent syntax errors when calling tools like `manage_world_knowledge`. Manual JSON scripting is too slow and error-prone.
- **`dungeon_navigator_tool` (CRITICAL PRIORITY):** To plot an optimal, full-exploration path for complex, multi-floor areas like Silph Co. This must be a **tool**, not an agent, as it requires direct map data analysis.

### B. Buggy Tools & Deletion Queue
- **`overworld_navigator_tool` (BUGGY - DO NOT USE):** This tool is unreliable and calculates paths incorrectly. It has been overwritten with a non-functional placeholder to prevent accidental use. Rely on the standard `pathfinder` for now.

### C. Active Agents (Reliable)
- `pc_navigator_agent` (v2)
- `team_composition_advisor_agent` (v2)
- `protocol_enforcement_agent` (v1)
- `battle_strategist_agent` (v9)
- `encounter_tracker_agent` (v1)

### D. Active Tools (Reliable)
- `pathfinder` (limitation: unreliable for complex, segmented maps like Saffron City and Route 12).
- `select_battle_option`

## IV. Silph Co. Intel & Strategy
- **Primary Goal:** Find the CARD KEY.
- **Methodology:** Systematically explore each floor, mapping all teleporters and defeating all trainers. Use the CARD KEY on all locked doors upon acquisition.
- **Discoveries:**
    - **Hint:** The BOSS is on 11F (from a Rocket on 4F).
    - **5F:** Positional gates triggered by movement. Puzzle unsolved. The western area is inaccessible from the central room.
    - **8F:** Intra-floor teleporter loop.

## V. Trainer & Encounter Intel
*A log of noteworthy rosters and encounters.*
### A. Trainer Pokémon
- **Silph Co. 2F Scientist (6, 14):** Muk (Lv37), Weezing (Lv37), Porygon (Lv37)
- **Silph Co. 4F Rocket (10, 15):** Machoke (Lv39), Hypno (Lv39)
- **Silph Co. 4F Scientist (15, 7):** Electabuzz (Lv41)
- **Silph Co. 5F Rocket (9, 17):** Tauros (Lv40)
- **Silph Co. 9F Scientist (22, 14):** Muk (Lv40), Kabutops (Lv40)
- **Silph Co. 11F Rocket (16, 8):** Kabutops, Raticate, Muk, Golbat, Marowak, Arbok
### B. Unique Encounters
- **Route 16 Snorlax:** Defeated. Path at (27, 11) is now clear.

## VI. Active Investigations & Untested Assumptions
- **Assumption 1 (CARD KEY Location):** The `CARD KEY` is a physical item (Poké Ball) on the ground. **Hypothesis:** It could be given by an NPC after a specific trigger. **Test:** Continue systematically clearing floors and talking to all NPCs.
- **Assumption 2 (Gate Puzzles):** The closed gates on various floors (5F, 7F, etc.) are part of a puzzle. **5F Hypothesis 1 (FAILED - 2 attempts):** Walking the northern corridor opens the central gates. **5F Hypothesis 2 (FAILED - 1 attempt):** The teleporter at (12, 6) leads to a dead-end room on 3F and is not the solution. **General Hypothesis:** Gates might be opened by a master switch on a different floor. **Test:** Continue exploring all floors thoroughly. The `dungeon_navigator_agent` would be key here.
- **Assumption 3 (Rocket Progression):** I need to defeat all Rockets to progress. **Hypothesis:** Some might just provide flavor text. **Test:** If a Rocket doesn't battle me, mark them as non-hostile ('💬') and move on, not assuming they are a progression blocker unless they physically block the path.
- **Assumption 4 (HM Field Use):** The 'use from bag' mechanic is inconsistent. Cut can be used without teaching, but Flash MUST be taught to a Pokémon to be used in the field. Assumption: Other HMs like Fly and Surf will also need to be taught. **Test:** Next time I am outdoors, I will attempt to use Fly directly from the item menu.

## VII. Lessons Learned & Protocol Corrections
- **Protocol Failure (T30985):** I attempted to log a Silph Co. warp connection (8F 12,6 to 2F 28,16) that already existed in the World Knowledge Graph. I had clearly forgotten this path because I failed to mark the warp with '🚪' on both ends immediately after using it the first time. **Correction:** Must be more disciplined. Trust system errors. Mark ALL warps immediately.
- **Protocol Failure (T30988):** I misidentified a warp on Silph Co. 8F at (4,12) as navigable. It was in an isolated room. **Correction:** I must verify warp reachability from my current position before listing it in my validation checks.
- **Protocol Update (T31290):** A single bidirectional edge (`is_one_way: false`) in the WKG covers two-way travel. Do not create a second, reversed edge for the same connection.
- **Protocol Failure (T31320):** I have repeatedly hallucinated my location and map ID, leading to multiple failed tool calls and wasted turns. **Correction:** I MUST verify my current `map_id` and coordinates from the Game State Information *before* every single action, especially navigation and documentation. I will also trust system warnings about reachability and dead ends.
- **Protocol Failure (T31322):** I have been using `select_battle_option` redundantly by also manually inputting the button presses. **Correction:** I will rely solely on the tool for battle menu selections to improve efficiency.
- **Hypothesis Failure (T31370):** The pier on Route 12 is segmented. I was stuck on an isolated section and could not reach the southern trainers or the exit to Route 13. All manual and pathfinder attempts failed. **Correction:** The game state shows reachable warps. I must trust the game state over my own perception and explore all reachable warps before assuming I am stuck.
- **Hypothesis Failure (Route 12 South Path):** The warp at (12, 78) on Route 12 leads to the Super Rod House, not south. The path south must be found elsewhere.
- **Protocol Failure (T31644):** I failed to mark the exit warp of the Route 12 Gatehouse before transitioning to Route 12. I must be more disciplined and mark both sides of a warp connection immediately.
- **Protocol Failure (T31645):** I set a navigation goal to a trainer at (15, 32) on Route 12 without checking my map markers first. The marker clearly indicated this NPC was non-battling and I had already interacted with them. This is a major failure in following my own established protocols and wasted a turn. I MUST check markers before every navigation or interaction action.

## VIII. Tile Mechanics Compendium
*   **Ledge:** One-way downward traversal. Treat as a wall from all other directions.
*   **Cuttable:** Tree that can be cut with HM Cut.
*   **Pikachu:** A unique, walkable object. Requires a double-press if not already facing it.
*   **Warp:** Triggers a map change. Includes doors, stairs, and cave entrances.
*   **Spinner:** Forces movement in a specific direction.