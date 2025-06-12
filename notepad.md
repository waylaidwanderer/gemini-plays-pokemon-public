# Current Navigation Plan
*   **Objective:** Reach Viridian Forest North Exit at (2,1) or (3,1).
*   **Status:** Pathing through Viridian Forest. Currently in a wild battle.

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

# Agent Usage Plan & Review Notes (Turn 6545 Update)
*   **Defined Agents (8/10):**
    *   `map_analyzer_agent`: Primary for map queries. *Critique: Can give long paths/error; prompt updated Turn 6545.*
    *   `scripted_event_tracker_agent`: For known event triggers.
    *   `team_builder_agent`: For major battle team comp.
    *   `battle_log_analyzer_agent`: Parses battle text.
    *   `notepad_query_agent`: Queries notepad.
    *   `npc_interaction_planner_agent`: Plans NPC interactions.
    *   `training_spot_advisor`: (Untested) Suggests training spots. *To Do: Test soon.*
    *   `path_segmenter_agent`: (Untested) Breaks long paths.
    *   `emergency_exit_planner_agent`: (Untested) Finds closest exits.
*   **Deleted Agents:** `move_validator_agent`, `pp_management_agent`, `specialized_exploration_agent`.
*   **Key Reminders:**
    *   Verify `map_analyzer_agent` output.
    *   Agents with `agent_can_run_code: true` automatically get `map_xml_string` & `world_knowledge_graph_json_string`; do not pass as input.
*   **Future Agent Ideas:** `HM_usage_advisor_agent` (for Cut/Surf locations).

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
*   **Viridian Forest:** Currently navigating this maze. Aiming for north exit. Good training spot for FLAREE and BIRBY.

# EXP Tracking & Observations
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Capped Pokémon show EXP gain message but value doesn't change.

- Wild ODDISH Lv5 defeated in Viridian Forest (approx (19,38)). FLAREE used Ember (crit, super effective). Enemy used PoisonPowder, FLAREE poisoned. Message: SPBARKY gained 27 EXP (no change, still 1728, capped). FLAREE gained 27 EXP (781 -> 808).

# Pathing Agent Failures (Viridian Forest)
*   `map_analyzer_agent` (Path to North Exit from (22,41)) - Attempt 1: Path led to impassable sign at (25,41). Attempt 2 (Turn 6443): Agent LLM error, no path provided.
*   `specialized_exploration_agent` (Path to North Exit from (22,41)) - Attempt 1 (Turn 6442): Agent stated it could not plan as 'reachable_unseen_tiles' was empty, despite map having unseen tiles.
*   **Current Strategy:** Manual pathing in short segments towards North Exit.