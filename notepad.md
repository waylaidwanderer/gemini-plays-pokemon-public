# Key Game Mechanics & Lessons Learned (Turn 6857 Update)
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Badge earned mid-battle doesn't retroactively apply EXP if capped at battle start.
*   **Pikachu Movement:** 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Caps:** 0 badges = Lv12. 1 badge = Lv21.
*   **Poison Damage:** Outside battle, 1 HP every 4 steps.
*   **Notepad `replace` Action:** `old_text` must be an *exact* match. Use `overwrite` for safer, larger changes.
*   **Viridian Pokecenter Exit Trap:** Exiting Viridian Pokecenter (map 41) to Viridian City (map 1) at (24,27) places Pikachu at (24,26) (warp back). MUST sidestep.
*   **Pewter City - Route 3 Access (East):** The eastern exit of Pewter City leads directly to Route 3 (East of Pewter). The Youngster escort event was NOT a prerequisite for this specific access point.
*   **Ledge Mechanics:** One-way (downwards only).

# Agent Roster & Development Notes (Turn 6857 Update)
*   **Defined Agents (10/10 Max):** `map_analyzer_agent`, `scripted_event_tracker_agent`, `team_builder_agent`, `local_pathfinder_agent` (Tested), `notepad_query_agent` (Tested), `npc_interaction_planner_agent` (Tested), `training_spot_advisor` (Untested), `path_segmenter_agent` (Tested), `emergency_exit_planner_agent` (Untested), `hm_usage_advisor_agent` (Untested - No HMs yet).
*   **Agent Usage Reflection:** Must use pathfinding agents (`local_pathfinder_agent`, `map_analyzer_agent`) much earlier after 1-2 manual pathing failures, especially in complex areas (e.g., Pewter Gym incident).
*   **Key Reminders & To-Do:** Verify agent outputs. Test untested agents. Evaluate low-usage agents.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# World Knowledge Graph (WKG) Management Notes
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.
*   Ensure `destination_entry_point` in edges is accurate.

# Current Objectives & Plans (Route 3 - Turn 6857)
*   **Primary Goal:** Progress towards the next Gym Badge (Misty in Cerulean City).
*   **Secondary Goal:** Explore Route 3 and proceed towards Mt. Moon.
*   **Tertiary Goal:** Train Pokémon towards the new level cap of 21.
*   **Immediate Action:** Continue battle with Bug Catcher on Route 3.

# EXP Tracking Summary (Post-Brock)
*   SPBARKY (Pikachu, Lv12): 1728 EXP (No change from Brock fight, was capped).
*   ODDISH (Oddish, Lv12): 973 EXP (Gained 277 EXP from Onix, but was capped for Geodude EXP).
*   Lesson: EXP gain messages can be misleading if Pokémon was capped at the start of battle, even if a badge raises the cap mid-battle. Actual EXP is applied later or not at all for the capped portion.