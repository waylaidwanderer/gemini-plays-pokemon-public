# Lessons Learned & Game Mechanics
*   **Pewter Youngster Escort (Route 3 Blocker):** Youngster (ID 5, trigger near (36,17) in Pewter) blocks Route 3. Avoid this area for now.
*   **Accurate Self-Location:** Always verify current position against Game State Information.
*   **Adaptability:** Abandon consistently unachievable objectives. If progress stalls despite trying and documenting various hypotheses (3-4 attempts), pivot to a new goal or strategy.
*   **Map Awareness:** Reinforce mental model of current map, obstacles, and event triggers. Critically evaluate agent-provided paths against map memory.
*   **Ledge Mechanics:** One-way (downwards only). Crucial for Route 22 navigation and current Route 2 navigation.
*   **Movement:** 1st press TURNS *and* MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Verified with SPBARKY.
*   **Poison Damage:** Outside battle, poisoned Pokémon lose 1 HP every 4 steps.
*   **Notepad `replace` Action:** The `old_text` argument MUST be an *exact* character-for-character match of the text to be replaced. Use error message suggestions or copy directly from the notepad.
*   **Verification of Location:** CRITICAL (Turn 6545): Always verify current map_id and coordinates from Game State Information *before* planning any action, especially after map transitions. Do not rely on memory of previous actions. My locational hallucinations were a major issue.

# Agent Usage Plan & Review Notes (Turn 6585 Update)
*   **Defined Agents (9/10):**
    *   `map_analyzer_agent`: Primary for map queries. *Critique (Turn 6545): Can give long paths/error; prompt updated Turn 6545. Efficacy needs monitoring.*
    *   `scripted_event_tracker_agent`: For known event triggers.
    *   `team_builder_agent`: For major battle team comp.
    *   `battle_log_analyzer_agent`: Parses battle text.
    *   `notepad_query_agent`: Queries notepad.
    *   `npc_interaction_planner_agent`: Plans NPC interactions.
    *   `training_spot_advisor`: (Untested) Suggests training spots. *To Do: Test soon.*
    *   `path_segmenter_agent`: (Untested) Breaks long paths.
    *   `emergency_exit_planner_agent`: (Defined Turn 6546) Finds closest exits. *To Do: Test soon.*
    *   `hm_usage_advisor_agent`: (Defined Turn 6571) Advises on HM usage. *To Do: Test soon.*
*   **Key Reminders:**
    *   Verify `map_analyzer_agent` output.
    *   Agents with `agent_can_run_code: true` automatically get `map_xml_string` & `world_knowledge_graph_json_string`; do not pass as input.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# World Knowledge Graph (WKG) Management
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.

# Route/Area Specific Notes
*   **Pewter City - Route 3:** Attempts abandoned due to Youngster escort event.
*   **Route 2 (Section North of Viridian Forest - Future Access):** The section of Route 2 accessible *after* passing through Viridian Forest (from south to north) will have cuttable trees requiring HM Cut.
*   **Route 22 Summary:** This route presented significant navigational challenges due to ledges and isolated grass patches. All reachable unseen tiles eventually explored or confirmed inaccessible. Key lessons: ledges are strictly one-way; isolated areas require careful pathfinding; agent-provided paths for complex terrain must be rigorously verified.
*   **Viridian City Obstacles:** Blocked east by impassable tile at (8,15). Blocked east by cuttable tree at (15,5). Blocked south (detour attempt) by impassable tile at (13,6).
*   **Route 22 Gate:** Guard at (7,3) confirms BOULDERBADGE needed to pass west. Area fully explored.
*   **Route 2 (South of Viridian Forest):** Navigated complex ledges and paths to reach Viridian Forest South Gate.
*   **Viridian Forest:** Navigated this maze. Aimed for north exit. Good training spot for FLAREE and BIRBY. FLAREE fainted from poison before exiting south (Turn 6520). Successfully exited south (Turn 6521).

# EXP Tracking & Observations
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Capped Pokémon show EXP gain message but value doesn't change.

# Current Navigation Plan (Updated Turn 6585)
*   **Current Location:** Viridian City (24,27) - Facing Down. Pikachu at (24,26).
*   **Immediate Goal:** Reach Route 2 North Exit at (19,1).
*   **Path Segment 1 (Viridian City):** Move from (24,27) to (24,1) (26 Up presses), then from (24,1) to (19,1) (5 Left presses). This leads to Route 2 (South of Viridian Forest).
*   **Path Segment 2 (Route 2 South):** Navigate Route 2 South to Viridian Forest South Gate (warp at (4,44)).
*   **Path Segment 3 (Viridian Forest):** Navigate Viridian Forest from South Entrance (17,48) to North Exit (warp at (2,1) or (3,1)).
*   **Path Segment 4 (Route 2 North):** Navigate Route 2 North to Pewter City entrance (map edge at (9,1)).
*   **Objective:** Reach Pewter City to challenge Brock for the Boulder Badge.

# Pathing Agent Failures (Viridian Forest)
*   `map_analyzer_agent` (Path to North Exit from (22,41)) - Attempt 1: Path led to impassable sign at (25,41). Attempt 2 (Turn 6443): Agent LLM error, no path provided.
*   **Current Strategy:** Manual pathing in short segments towards North Exit. (Obsolete after exiting south)