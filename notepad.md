# Key Game Mechanics & Lessons Learned (Turn 7021 Update)
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Badge earned mid-battle doesn't retroactively apply EXP if capped at battle start.
*   **Pikachu Movement:** 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Caps:** 0 badges = Lv12. 1 badge = Lv21.
*   **Poison Damage:** Outside battle, 1 HP every 4 steps.
*   **Notepad `replace` Action:** `old_text` must be an *exact* match. Use `overwrite` for safer, larger changes.
*   **Viridian Pokecenter Exit Trap:** Exiting Viridian Pokecenter (map 41) to Viridian City (map 1) at (24,27) places Pikachu at (24,26) (warp back). MUST sidestep.
*   **Pewter City - Route 3 Access (East):** The eastern exit of Pewter City leads directly to Route 3 (East of Pewter).
*   **Ledge Mechanics:** One-way (downwards only).
*   **Dialogue Loops:** If 'A' or 'B' presses fail to advance dialogue or initiate battle after 2-3 attempts, abandon interaction, mark NPC, and move on. Do not repeat failed interaction attempts.
*   **Map Transition Variance:** Exiting a map from different adjacent edge tiles can lead to different arrival coordinates on the destination map. Must test alternative edge tiles if the initial one leads to an undesired area (e.g., Pewter City East Exit to Route 3).

# Agent Roster & Development Notes (Turn 7021 Update)
*   **Defined Agents (10/10 Max):** `map_analyzer_agent`, `scripted_event_tracker_agent`, `team_builder_agent`, `local_pathfinder_agent` (Tested), `notepad_query_agent` (Tested), `npc_interaction_planner_agent` (Tested), `training_spot_advisor` (Untested), `path_segmenter_agent` (Tested), `emergency_exit_planner_agent` (Tested), `hm_usage_advisor_agent` (Untested - No HMs yet).
*   **Agent Usage Reflection:**
    *   `emergency_exit_planner_agent` was useful for finding an escape from Route 3.
    *   Pathfinding agents (`local_pathfinder_agent`, `map_analyzer_agent`) should be used promptly after 1-2 manual pathing failures, especially in complex areas. Consider for reaching (25,6) on Route 3.
    *   Untested agents (`training_spot_advisor`, `hm_usage_advisor_agent`) should be tested when relevant opportunities arise. `training_spot_advisor` could be useful on Route 3.
    *   Consider deleting less frequently used agents (e.g. `team_builder_agent`) if a new agent slot is needed.
*   **Key Reminders & To-Do:** Verify agent outputs. Test untested agents. Be more proactive with pathfinding agents.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Problematic NPC/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# World Knowledge Graph (WKG) Management Notes
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.
*   Ensure `destination_entry_point` in edges is accurate.
*   **Critical:** Investigate Pewter City East Exit to Route 3. My WKG node `e8788e15-95e0-437a-83bd-740c855978ec` (Route 3 (2,11) from Pewter (40,19)) conflict with arrival at Route 3 (1,11). Systematically test Pewter (40,18), (40,20), (40,17) if (40,19) continues to lead to the lower path. (This was resolved, all lead to lower path, WKG updated).

# EXP Tracking Summary (Post-Brock)
*   SPBARKY (Pikachu, Lv12 -> Lv14): Gained EXP after Brock, now 2851 EXP.
*   ODDISH (Oddish, Lv12): 973 EXP (Gained 277 EXP from Onix, but was capped for Geodude EXP). Still Lv12.
*   FLAREE (Vulpix, Lv7 -> Lv10): Gained significant EXP on Route 3, now 1233 EXP.
*   Lesson: EXP gain messages can be misleading if Pokémon was capped at the start of battle, even if a badge raises the cap mid-battle. Actual EXP is applied later or not at all for the capped portion.

# Encounter Issues & Stalled Progress (Route 3 - Documented Loops)
*   **Cool Trainer F (ID 4) at (17,10) on Route 3:** Dialogue loop ("Quit staring if you don't want to fight!"). Multiple failed attempts (approx. 5+ across turns 6905-6912). Marked with ❗. **Status: Abandoned.**
*   **Youngster (ID 2) at (11,7) on Route 3:** Dialogue loop ('than those found in the forest!'). 7 failed attempts (turns 6932-6936, 6938, 6940). Marked with ❗. **Status: Abandoned.**
*   **Youngster (ID 3) at (15,5) on Route 3:** Dialogue loop ('when your box is full!'). 6 failed attempts (turns 6946-6948, 6950-6951, 6952). Marked with ❗. **Status: Abandoned.**
*   **Youngster (ID 5) / BUG CATCHER at (20,6) on Route 3:** Battle Won. Post-battle dialogue loop ('If a POKéMON BOX...') for 10+ turns (6973-6987). Marked as defeated (☠️). **Status: Battle Won, dialogue loop problematic.**

# Route 3 Navigation Update (Turn 7051)
*   **Pewter City East Exits:** Confirmed that all tested eastern edge tiles in Pewter City ((40,17), (40,18), (40,19), (40,20)) lead to the *lower path* of Route 3. The upper path is not accessible via these specific exits. Previous WKG conflict for (40,19) resolved; it leads to Route 3 (2,11).
*   **Current Strategy for (25,6):** The current objective is to reach the last unseen tile (25,6) on the upper path of Route 3. Investigating intra-map paths to this tile first, possibly using `map_analyzer_agent`. If no intra-map path is found, the hypothesis is that re-entering Route 3 from Pewter City via (40,17) to reach (2,9), then navigating to (11,7) and eastwards, is the way to access (25,6).

# Route 3 - Reaching Unseen Tile (25,6) (Turn 7051)
*   **Target:** Unseen tile (25,6) on the upper plateau of Route 3.
*   **Hypothesis 1 (Intra-map access):** There might be a path from the current lower sections of Route 3 to the upper plateau where (25,6) is located.
    *   **Test:** Use `map_analyzer_agent` to check for a path from current position (11,13) or other accessible points on the lower path to (25,6).
*   **Hypothesis 2 (Inter-map access via Pewter):** If no intra-map path is found, access the upper plateau by:
    1.  Returning to Pewter City.
    2.  Exiting Pewter City from (40,17) to arrive at Route 3 (2,9).
    3.  On Route 3, navigate from (2,9) east to (11,9), then up to (11,7).
    4.  From (11,7), navigate east towards (25,6).
*   **Critique Note:** Prioritize exhausting intra-map solutions before resorting to inter-map travel for a 'reachable' tile.