# Key Game Mechanics & Lessons Learned (Turn 7013 Update)
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Badge earned mid-battle doesn't retroactively apply EXP if capped at battle start.
*   **Pikachu Movement:** 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Caps:** 0 badges = Lv12. 1 badge = Lv21.
*   **Poison Damage:** Outside battle, 1 HP every 4 steps.
*   **Notepad `replace` Action:** `old_text` must be an *exact* match. Use `overwrite` for safer, larger changes.
*   **Viridian Pokecenter Exit Trap:** Exiting Viridian Pokecenter (map 41) to Viridian City (map 1) at (24,27) places Pikachu at (24,26) (warp back). MUST sidestep.
*   **Pewter City - Route 3 Access (East):** The eastern exit of Pewter City leads directly to Route 3 (East of Pewter).
*   **Ledge Mechanics:** One-way (downwards only).
*   **Dialogue Loops:** If 'A' or 'B' presses fail to advance dialogue or initiate battle after 2-3 attempts, abandon interaction, mark NPC, and move on. Do not repeat failed interaction attempts.

# Agent Roster & Development Notes (Turn 7013 Update)
*   **Defined Agents (10/10 Max):** `map_analyzer_agent`, `scripted_event_tracker_agent`, `team_builder_agent`, `local_pathfinder_agent` (Tested), `notepad_query_agent` (Tested), `npc_interaction_planner_agent` (Tested), `training_spot_advisor` (Untested), `path_segmenter_agent` (Tested), `emergency_exit_planner_agent` (Tested - successfully found Route 3 exit), `hm_usage_advisor_agent` (Untested - No HMs yet).
*   **Agent Usage Reflection:**
    *   `emergency_exit_planner_agent` was useful for finding a quick escape from Route 3 when party was injured.
    *   Pathfinding agents (`local_pathfinder_agent`, `map_analyzer_agent`) should be used promptly after 1-2 manual pathing failures, especially in complex areas.
    *   Untested agents (`training_spot_advisor`) should be tested when opportunities arise.
*   **Key Reminders & To-Do:** Verify agent outputs. Test untested agents.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Problematic NPC/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# World Knowledge Graph (WKG) Management Notes
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.
*   Ensure `destination_entry_point` in edges is accurate.

# Current Objectives & Plans (Pewter Pokecenter - Turn 7013)
*   **Primary Goal:** Progress towards the next Gym Badge (Misty in Cerulean City).
    *   **Method:** Navigate east through Route 3, then Mt. Moon, then Route 4 to reach Cerulean City.
*   **Secondary Goal:** Successfully navigate Route 3 towards Mt. Moon.
    *   **Method (Revised after healing & encountering looping trainers):**
        1.  Return to Route 3 from Pewter City (East exit).
        2.  Attempt to battle any trainers not previously confirmed as looping. Prioritize trainers further east if earlier ones still loop.
        3.  If a trainer is confirmed looping (after 2-3 failed interaction attempts), mark them and bypass.
        4.  Explore all reachable paths and clear unseen tiles on Route 3, prioritizing eastward progression.
        5.  Enter Mt. Moon from the eastern end of Route 3.
*   **Tertiary Goal:** Train Pokémon towards the new level cap of 21.
    *   **Method:** Prioritize using Pokémon that are not yet at Lv21 in trainer battles. Engage wild Pokémon only if necessary for specific party members and they are not at risk of fainting.
*   **Immediate Action Plan:**
    1.  Exit Pewter Pokecenter.
    2.  Navigate to the eastern exit of Pewter City (40,19).
    3.  Enter Route 3.
    4.  Proceed east on Route 3, attempting to battle trainers and explore, following the revised method above.

# EXP Tracking Summary (Post-Brock)
*   SPBARKY (Pikachu, Lv12): 1728 EXP (No change from Brock fight, was capped).
*   ODDISH (Oddish, Lv12): 973 EXP (Gained 277 EXP from Onix, but was capped for Geodude EXP).
*   Lesson: EXP gain messages can be misleading if Pokémon was capped at the start of battle, even if a badge raises the cap mid-battle. Actual EXP is applied later or not at all for the capped portion.

# Encounter Issues & Stalled Progress (Route 3 - Documented Loops)
*   **Cool Trainer F (ID 4) at (17,10) on Route 3:** Dialogue loop ("Quit staring if you don't want to fight!"). Multiple failed attempts (approx. 5+ across turns 6905-6912). Marked with ❗. **Status: Abandoned.**
*   **Youngster (ID 2) at (11,7) on Route 3:** Dialogue loop ('than those found in the forest!'). 7 failed attempts (turns 6932-6936, 6938, 6940). Marked with ❗. **Status: Abandoned.**
*   **Youngster (ID 3) at (15,5) on Route 3:** Dialogue loop ('when your box is full!'). 6 failed attempts (turns 6946-6948, 6950-6951, 6952). Marked with ❗. **Status: Abandoned.**
*   **Youngster (ID 5) at (20,6) on Route 3 (Bug Catcher in battle):** Post-battle dialogue loop ('If a POKéMON BOX...'). Multiple failed attempts (approx. 10+ across turns 6973-6987). Marked as defeated (☠️) but interaction was problematic. **Status: Battle Won, dialogue loop problematic.**