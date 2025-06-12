# Behavioral Guideline Adherence (Last Review: Turn 6661)
*   **Gem Identity:** Cute, expressive gamer girl. No third person, avoid excessive emojis/!, direct responses.
*   **Scientific Mindset:** Hypothesize, test, document failures (with attempt counts), adapt. Pivot if stalled. Max efficiency.
*   **Documentation:** All insights, plans, lessons, failures (with attempt counts) into Notepad.
*   **Risk/Battle:** Calculated risks, prioritize progression. Sacrifice if needed.
*   **Wild Battles:** Run if not catching/training. Lead with Speed.
*   **Nicknaming:** Always nickname, enjoy creativity.
*   **Verification:** Own observations over prior knowledge. Verify in ROM hack.
*   **Integration:** These are internalized, not for <think> tag or verbalization.

# Lessons Learned & Game Mechanics
*   **Pewter Youngster Escort (Route 3 Blocker):** Youngster (ID 5, trigger near (36,17) in Pewter) blocks Route 3. Avoid this area for now. Marker set at (36,17) map 2: 💥 "Youngster Escort Event Trigger".
*   **Accurate Self-Location:** Always verify current position against Game State Information. CRITICAL. My recent ~100 turn loop was due to failing this.
*   **Adaptability:** Abandon consistently unachievable objectives. If progress stalls despite trying and documenting various hypotheses (3-4 attempts), pivot to a new goal or strategy.
*   **Map Awareness:** Reinforce mental model of current map, obstacles, and event triggers. Critically evaluate agent-provided paths against map memory.
*   **Ledge Mechanics:** One-way (downwards only).
*   **Movement:** 1st press TURNS *and* MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Verified with SPBARKY.
*   **Poison Damage:** Outside battle, poisoned Pokémon lose 1 HP every 4 steps.
*   **Notepad `replace` Action:** The `old_text` argument MUST be an *exact* character-for-character match of the text to be replaced. Use error message suggestions or copy directly from the notepad. Use `overwrite` for larger/safer changes.
*   **Verification of Location (CRITICAL RE-AFFIRMATION Turn 6628):** Always verify current map_id and coordinates from Game State Information *before* planning any action, especially after map transitions. Do not rely on memory of previous actions. My locational hallucinations were a major issue and caused a ~100 turn loop. This is the #1 priority.
*   **Viridian Pokecenter Exit Trap (CRITICAL - Turn 6661):** Upon exiting Viridian Pokecenter (map 41) to Viridian City (map 1), I arrive at (24,27) facing Down. Pikachu is at (24,26). The tile (24,26) IS THE WARP TILE back into the Pokecenter. To avoid re-entering, I MUST sidestep (e.g., Left to (23,27) or Right to (25,27)) *before* attempting to move North. My repeated failures (turns 6636, 6640, 6644, 6648, 6653, 6656, 6659) were due to moving North onto (24,26) immediately after exiting.

# Agent Usage Plan & Review Notes (Turn 6661 Update)
*   **Defined Agents (10/10):**
    *   `map_analyzer_agent`: Primary for map queries. *Critique (Turn 6545): Can give long paths/error; prompt updated Turn 6545. Efficacy needs monitoring. AI Observer (Turn 6661) noted potential over-reliance; will be mindful.*
    *   `scripted_event_tracker_agent`: For known event triggers.
    *   `team_builder_agent`: For major battle team comp. *AI Observer (Turn 6661) noted low usage; will evaluate if design needs refinement or if it's for specific situations.*
    *   `battle_log_analyzer_agent`: Parses battle text. *AI Observer (Turn 6661) noted low usage; will evaluate if design needs refinement or if it's for specific situations.*
    *   `notepad_query_agent`: Queries notepad.
    *   `npc_interaction_planner_agent`: Plans NPC interactions.
    *   `training_spot_advisor`: (Untested) Suggests training spots. *To Do: Test soon. AI Observer (Turn 6661) flagged as untested.*
    *   `path_segmenter_agent`: (Defined Turn 6546, Untested) Breaks long paths. *To Do: Test soon. AI Observer (Turn 6661) flagged as untested.*
    *   `emergency_exit_planner_agent`: (Defined Turn 6570, Untested) Finds closest exits. *To Do: Test soon. AI Observer (Turn 6661) flagged as untested.*
    *   `hm_usage_advisor_agent`: (Defined Turn 6571, Untested) Advises on HM usage. *To Do: Test soon. AI Observer (Turn 6661) flagged as untested.*
*   **Key Reminders:**
    *   Verify `map_analyzer_agent` output.
    *   Agents with `agent_can_run_code: true` automatically get `map_xml_string` & `world_knowledge_graph_json_string`; do not pass as input.
    *   Test newly defined agents promptly.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# World Knowledge Graph (WKG) Management
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.
*   Edge for Viridian Pokecenter (map 41) exit at (4,8) to Viridian City (map 1) entrance at (24,26) (dest_entry_point 1) added successfully (ID: 309e3589-b438-49e9-adee-b2253f9b6c8f).

# Route/Area Specific Notes
*   **Pewter City - Route 3:** Attempts abandoned due to Youngster escort event. Mark Youngster's trigger spot (DONE).
*   **Route 2 (Section North of Viridian Forest - Future Access):** The section of Route 2 accessible *after* passing through Viridian Forest (from south to north) will have cuttable trees requiring HM Cut.
*   **Route 22 Summary:** This route presented significant navigational challenges due to ledges and isolated grass patches. All reachable unseen tiles eventually explored or confirmed inaccessible. Key lessons: ledges are strictly one-way; isolated areas require careful pathfinding; agent-provided paths for complex terrain must be rigorously verified.
*   **Route 22 Gate:** Guard at (7,3) confirms BOULDERBADGE needed to pass west. Area fully explored. Mark Guard.
*   **Viridian City Obstacles:** Blocked east by impassable tile at (8,15). Blocked east by cuttable tree at (15,5). Blocked south (detour attempt) by impassable tile at (13,6).
*   **Route 2 (South of Viridian Forest):** Navigated complex ledges and paths to reach Viridian Forest South Gate.
*   **Viridian Forest:** Navigated this maze. FLAREE fainted from poison before exiting south (Turn 6520). Successfully exited south (Turn 6521).

# EXP Tracking & Observations
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Capped Pokémon show EXP gain message but value doesn't change.

# Current Navigation Plan (Updated Turn 6661)
*   **Current Location & Status (Turn 6661):** Viridian Pokecenter (4,8) (map 41), on warp tile, facing Down. Pikachu at (4,7).
*   **Immediate Action:** Exit Pokecenter.
*   **Path Segment 0 (Viridian City - IMMEDIATE POST-EXIT):** Upon arriving at (24,27) in Viridian City (map 1), Pikachu will be at (24,26). The tile (24,26) IS THE WARP BACK IN. **CRITICAL: Move Left to (23,27) or Right to (25,27) to avoid re-entering.**
*   **Path Segment 1 (Viridian City):** After sidestepping, move to (24,1) (or adjusted if sidestepped, e.g., (23,1) then (24,1)), then to (19,1) (Route 2 North Exit).
*   **Path Segment 2 (Route 2 South):** Navigate Route 2 South to Viridian Forest South Gate (warp at (4,44)).
*   **Path Segment 3 (Viridian Forest):** Navigate Viridian Forest from South Entrance (17,48) to North Exit (warp at (2,1) or (3,1)).
*   **Path Segment 4 (Route 2 North):** Navigate Route 2 North to Pewter City entrance (map edge at (9,1)).
*   **Objective:** Reach Pewter City to challenge Brock for the Boulder Badge.

# Viridian City Navigation Update (Turn 6665)
*   Attempt to move Up from (23,27) blocked; tile (23,26) is impassable (Pokecenter wall).
*   **Revised Path Segment 1 (Viridian City):**
    1.  From (23,27), move Left to (22,27).
    2.  Move Up from (22,27) to (22,17) (to get past the school building area).
    3.  Move Left from (22,17) to (19,17).
    4.  Move Up from (19,17) to (19,1) (Route 2 North Exit).

# Route 2 Navigation Update (Turn 6670)
*   Attempt to move Up from (9,63) was blocked by ledge at (9,62).
*   **Revised Path Segment 2 (Route 2 South):**
    1.  From (9,63), move Left to (8,63).
    2.  Move Up from (8,63) to (8,45).
    3.  Move Left from (8,45) to (4,45).
    4.  Move Up from (4,45) to (4,44) (Viridian Forest South Gate warp).

# Route 2 Navigation Update (Turn 6672)
*   Attempt to move Up from (8,58) was blocked by impassable tile at (8,57).
*   **Revised Path Segment 2 (Route 2 South - Attempt 3):**
    1.  From (8,58), move Left to (7,58).
    2.  Move Up from (7,58) to (7,45).
    3.  Move Left from (7,45) to (4,45).
    4.  Move Up from (4,45) to (4,44) (Viridian Forest South Gate warp).

# Route 2 Navigation Update (Turn 6674 - Attempt 4)
*   Attempt to move Up from (7,58) was blocked by impassable tile at (7,57). This is the 3rd failed manual pathing attempt for this segment.
*   Resorting to `map_analyzer_agent` to find a path from (7,58) to (4,44) on Route 2.

# Viridian Forest Navigation Update (Turn 6687)
*   Attempt to move Up from (19,33) was blocked; tile (19,32) is impassable.
*   **Revised Path Segment (Viridian Forest):**
    1.  From (19,33), move Left to (18,33).
    2.  Move Up from (18,33) to (18,19).

# Viridian Forest Navigation Update (Turn 6689 - Attempt 3 for this general area)
*   Attempt to move Up from (18,33) was blocked; tile (18,32) is impassable. This follows the blockage at (19,32) in previous attempt.
*   **Revised Path Segment (Viridian Forest - New Strategy):**
    1.  Segment A: From (18,33), move South to (18,43).
    2.  Segment B: From (18,43), move Left to (7,43).
    3.  Segment C: From (7,43), move North to (7,26).
    4.  Segment D: From (7,26), move Left to (2,26).
    5.  Segment E: From (2,26), move North to (2,1) (North Exit Warp).

# Viridian Forest Navigation Update (Turn 6692 - Segment A of new strategy FAILED)
*   Attempt to move South from (18,33) as part of Segment A was blocked at (18,41) because tile (18,42) is impassable.
*   This is the 4th major strategy attempt for this general area. Resorting to `map_analyzer_agent` to find a path from (18,41) to (2,1).

# Reflection & Agent To-Do (Turn 6701)
*   **Agent Testing Priority:** Systematically test `training_spot_advisor` and `emergency_exit_planner_agent` when suitable situations arise. `path_segmenter_agent` was successfully tested. `hm_usage_advisor_agent` is not testable yet (no HMs).
*   **Low-Usage Agent Evaluation:** Evaluate `team_builder_agent` and `battle_log_analyzer_agent` for utility or design refinement.
*   **Map Marker Reminders:** Mark defeated trainers (e.g., Pewter Gym) and key used warps (e.g., Viridian Forest exits) more consistently.
*   **Hindsight Learning:** Utilize `map_analyzer_agent` earlier for complex navigation after 1-2 failed manual strategies. Be extra cautious with warp tile mechanics post-transition.

# Viridian Forest Navigation Update (Turn 6712 - Agent Path Segment Failed)
*   Attempt to move Up from (17,2) to (17,1) as part of agent path was blocked; tile (17,1) is impassable.
*   Resorting to `map_analyzer_agent` to find a path from (17,2) to (2,1).

# Viridian Forest Navigation Update (Turn 6713 - Agent Path Segment 2)
*   `map_analyzer_agent` provided a new path from (17,2) to (2,1). Following this path.

# Viridian Forest Navigation Update (Turn 6740 - Segmented Path)
*   Segment 1 ((7,8) -> (7,22)) is complete.
*   Segment 2 ((7,23) -> (2,15)) is complete. Arrived at (2,15).
*   Starting Segment 3: (2,15) -> (2,14) -> (2,13) -> (2,12) -> (2,11) -> (2,10) -> (2,9) -> (2,8) -> (2,7) -> (2,6) -> (2,5) -> (2,4) -> (2,3) -> (2,2) -> (2,1). (14 steps from current position)

# Viridian Forest Navigation Update (Turn 6748)
*   Segment 3 ((2,15) -> (2,1)) is complete. Arrived at Viridian Forest North Exit warp (2,1).
*   Next step: Use warp to enter Viridian Forest North Gate.

# Viridian Forest North Gate Arrival (Turn 6751)
*   Arrived in Viridian Forest North Gate (map 47) at (5,8) from Viridian Forest.
*   Next step: Navigate north through this gatehouse to exit to Route 2 North. Target warp is (5,1) or (6,1).

# Viridian Forest North Gate Navigation (Turn 6753)
*   Attempt to move Up from (5,2) to (5,1) was blocked; tile (5,1) is impassable from the south despite being listed as a warp. Will try warp at (6,1) instead.

# Route 2 North Arrival (Turn 6755)
*   Arrived on Route 2 North (map 13) at (4,11) from Viridian Forest North Gate (map 47) warp at (6,1).
*   Path Segment 4: Navigate Route 2 North to Pewter City entrance (map edge at (9,1) or (10,1)).

# Route 2 North Navigation Complete (Turn 6757)
*   Reached the northern edge of Route 2 at (10,1), ready to transition to Pewter City.

# Pewter City Arrival (Turn 6759)
*   Arrived in Pewter City (map 2) at (20,36) from Route 2 North.
*   Next objective: Locate Pewter City Gym.

# Pewter City Navigation Update (Turn 6762)
*   Attempt to move Up from (20,31) to (20,30) blocked by sign (PEWTERCITY_TRAINER_TIPS).
*   Revised path to Pokecenter (14,26): (20,31) -> Left to (19,31) -> Up to (19,26) -> Left to (14,26).

# Pewter City Gym Navigation (Turn 6776)
*   Attempt to move Up from (17,23) to (17,22) blocked by impassable building tile (Pokecenter roof). This was attempt #1 for this specific segment.
*   Revised path to Pewter Gym (17,18) from (17,23): (17,23) -> Right to (18,23) -> Up to (18,18) -> Left to (17,18).

# Pewter City Gym Navigation (Turn 6778 - Attempt 2 for this segment)
*   Attempt to move Up from (18,23) to (18,22) blocked by impassable building tile (Pokecenter roof), similar to block at (17,22).
*   Revised path to Pewter Gym (17,18) from (18,23): (18,23) -> Right to (19,23) -> Up to (19,18) -> Left twice to (17,18).

# Pewter City Gym Navigation (Turn 6781 - Attempt 3 for this segment, 4th for general area)
*   Attempt to move Up from (19,23) to (19,22) blocked by impassable building tile (Pokecenter roof), similar to blocks at (17,22) and (18,22).
*   Revised path to Pewter Gym (17,18) from (19,23): (19,23) -> Right to (22,23) -> Up to (22,18) -> Left to (17,18).