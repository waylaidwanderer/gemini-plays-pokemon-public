# Key Game Mechanics & Lessons Learned (Turn 7021 Update)
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Badge earned mid-battle doesn't retroactively apply EXP if capped at battle start.
*   **Pikachu Movement:** 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Caps:** 0 badges = Lv12. 1 badge = Lv21.
*   **Poison Damage:** Outside battle, 1 HP every 4 steps.
*   **Notepad `replace` Action:** `old_text` must be an *exact* match. Use `overwrite` for safer, larger changes.
*   **Viridian Pokecenter Exit Trap:** Exiting Viridian Pokecenter (map 41) to Viridian City (map 1) at (24,27) places Pikachu at (24,26) (warp back). MUST sidestep.
*   **Pewter City - Route 3 Access (East):** The eastern exit of Pewter City leads directly to Route 3 (East of Pewter).
*   **Ledge Mechanics:** One-way (downwards only). Cannot step *up* onto a ledge tile from a ground tile one Y-level below it, nor step directly onto a ledge from an adjacent ground tile at the same Y-level.
*   **Dialogue Loops:** If 'A' or 'B' presses fail to advance dialogue or initiate battle after 2-3 attempts, abandon interaction, mark NPC, and move on. Do not repeat failed interaction attempts.
*   **Map Transition Variance:** Exiting a map from different adjacent edge tiles can lead to different arrival coordinates on the destination map. Must test alternative edge tiles if the initial one leads to an undesired area.

# Agent Roster & Development Notes (Turn 7021 Update)
*   **Defined Agents (10/10 Max):** `map_analyzer_agent`, `scripted_event_tracker_agent`, `team_builder_agent`, `local_pathfinder_agent` (Tested), `notepad_query_agent` (Tested), `npc_interaction_planner_agent` (Tested), `training_spot_advisor` (Untested), `path_segmenter_agent` (Tested), `emergency_exit_planner_agent` (Tested), `hm_usage_advisor_agent` (Untested - No HMs yet).
*   **Agent Usage Reflection:**
    *   Pathfinding agents (`local_pathfinder_agent`, `map_analyzer_agent`) should be used promptly after 1-2 manual pathing failures, especially in complex areas. Service unavailability has been an issue.
    *   Untested agents (`training_spot_advisor`, `hm_usage_advisor_agent`) should be tested when relevant opportunities arise. `training_spot_advisor` could be useful on Route 3 or Mt. Moon.
    *   Consider deleting less frequently used agents if a new agent slot is critically needed.
*   **Key Reminders & To-Do:** Verify agent outputs. Test untested agents. Be more proactive with pathfinding agents if they are functional.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Problematic NPC/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# World Knowledge Graph (WKG) Management Notes
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.
*   Ensure `destination_entry_point` in edges is accurate.

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

# Route 3 Navigation Update (Turn 7051, Updated Turn 7056)
*   **Pewter City East Exits:** Confirmed that all tested eastern edge tiles in Pewter City ((40,17), (40,18), (40,19), (40,20)) lead to the *lower path* of Route 3. The upper path is not accessible via these specific exits.
*   **Current Strategy for Upper Path Access:** Intra-map navigation on Route 3 is the primary method to access different elevations. Avoid assuming inter-map travel is needed unless all intra-map options are exhausted.

# Route 3 - Upper Plateau & Unseen Tiles (Turn 7065)
*   **Target:** Explore remaining unseen tiles on Route 3's upper plateau, specifically (25,5) and (25,6).
*   **Access:** Successfully reached the upper plateau by navigating from the lower path: (11,9) -> (12,9) -> (12,8) -> (12,7).
*   **Current Status:** At (20,5) in battle with LASS (Cool Trainer F, ID 6) at (21,5). Defeating her is required to access the path further east towards (25,5) and (25,6).
*   **Next Steps Post-Battle:**
    1.  Move to (24,5) (past defeated LASS).
    2.  Explore (25,5).
    3.  Move to (24,6).
    4.  Explore (25,6).
    5.  Then, proceed east on Route 3 towards Mt. Moon.