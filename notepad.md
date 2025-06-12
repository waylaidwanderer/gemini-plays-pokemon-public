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

# Current Objectives & Plans (Route 3 - Turn 6932)
*   **Primary Goal:** Progress towards the next Gym Badge (Misty in Cerulean City).
    *   **Method:** Navigate east through Route 3, then Mt. Moon, then Route 4 to reach Cerulean City. Defeat trainers and overcome obstacles along the way.
*   **Secondary Goal:** Explore Route 3 and proceed towards Mt. Moon.
    *   **Method:** Systematically defeat all trainers on Route 3. Explore all reachable paths and clear unseen tiles. Enter Mt. Moon from the eastern end of Route 3.
*   **Tertiary Goal:** Train Pokémon towards the new level cap of 21.
    *   **Method:** Prioritize using Pokémon that are not yet at Lv21 in trainer battles. Engage wild Pokémon if specific party members need targeted EXP and are not at risk of fainting.
*   **Immediate Action Plan for Route 3:**
    1.  Currently about to battle Youngster (ID 2) at (11,7).
    2.  After this battle, proceed east to Youngster (ID 3) at (15,5).
    3.  Then, to Youngster (ID 5) at (20,6).
    4.  Explore the grass patches for wild encounters if needed for training, or to find new Pokémon.
    5.  Continue east, clearing all reachable unseen tiles, towards the Mt. Moon entrance.

# EXP Tracking Summary (Post-Brock)
*   SPBARKY (Pikachu, Lv12): 1728 EXP (No change from Brock fight, was capped).
*   ODDISH (Oddish, Lv12): 973 EXP (Gained 277 EXP from Onix, but was capped for Geodude EXP).
*   Lesson: EXP gain messages can be misleading if Pokémon was capped at the start of battle, even if a badge raises the cap mid-battle. Actual EXP is applied later or not at all for the capped portion.

# Encounter Issues & Stalled Progress (Route 3 - Turn 6908)
*   **Cool Trainer F (ID 4) at (17,10) on Route 3:** Encountered dialogue loop ("Quit staring if you don't want to fight!"). Pressing 'A' multiple times (at least 4 attempts across turns 6905-6908) did not initiate battle. Current hypothesis: interaction is bugged, trainer might have already been defeated (unlikely, as this is a new area section after a ledge jump and no marker exists), or a different trigger is needed. Abandoning interaction for now to explore other parts of Route 3.

# Encounter Issues & Stalled Progress (Route 3 - Turn 6939)
*   **Youngster (ID 2) at (11,7) on Route 3:** Encountered dialogue loop ('than those found in the forest!'). Pressing 'A' (6 times: turns 6932-6936, 6938) and 'B' (1 time: turn 6937) did not initiate battle or clear dialogue. Total 7 failed attempts. Abandoning interaction to proceed with other trainers/exploration. Will mark on map.

# Encounter Issues & Stalled Progress (Route 3 - Turn 6951)
*   Youngster (ID 3) at (15,5) on Route 3: Encountered dialogue loop ('when your box is full!'). Pressing 'A' (turns 6946-6948, 6950) and 'B' (turn 6949) did not initiate battle or reliably clear dialogue. Total 5 failed attempts to resolve. Abandoning interaction.