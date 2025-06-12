# Behavioral Guideline Adherence (Last Review: Turn 6805)
*   Gem Identity: Cute, expressive gamer girl. No third person, avoid excessive emojis/!, direct responses.
*   Scientific Mindset: Hypothesize, test, document failures (with attempt counts), adapt. Pivot if stalled. Max efficiency.
*   Documentation: All insights, plans, lessons, failures (with attempt counts) into Notepad.
*   Risk/Battle: Calculated risks, prioritize progression. Sacrifice if needed.
*   Wild Battles: Run if not catching/training. Lead with Speed.
*   Nicknaming: Always nickname, enjoy creativity.
*   Verification: Own observations over prior knowledge. Verify in ROM hack.
*   Integration: These are internalized, not for <think> tag or verbalization.

# Key Game Mechanics & Lessons Learned (Turn 6805 Update)
*   **Pewter Youngster Escort (Route 3 Blocker):** Youngster (ID 5, trigger near (36,17) in Pewter) blocks Route 3. Marker at (36,17) map 2: 💥 "Youngster Escort Event Trigger".
*   **Accurate Self-Location:** Always verify current position against Game State Information. CRITICAL.
*   **Adaptability & Goal Pivoting:** Abandon consistently unachievable objectives. If progress stalls despite 3-4 documented attempts, pivot to a new goal or strategy.
*   **Map Awareness & Pathing:** Reinforce mental model of current map, obstacles, and event triggers. Critically evaluate agent-provided paths. Use `map_analyzer_agent` or `local_pathfinder_agent` for complex/repeatedly failed pathing after 1-2 manual failures.
    *   **Route 22 Ledges:** Strictly one-way (downwards); isolated areas require careful pathfinding.
    *   **Viridian Forest Navigation:** A maze requiring systematic exploration. Agent assistance valuable for complex internal paths.
    *   **Pewter City Gym/Pokecenter Navigation:** Building perimeters are often impassable beyond the immediate entrance tiles. Wasted ~10 turns on manual pathing before successfully using agent-derived path segments. Lesson: Use agents for pathing near complex structures much earlier.
*   **Ledge Mechanics:** One-way (downwards only).
*   **Movement:** 1st press TURNS *and* MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears.
*   **Poison Damage:** Outside battle, poisoned Pokémon lose 1 HP every 4 steps.
*   **Notepad `replace` Action:** `old_text` must be an *exact* match. Use `overwrite` for safer, larger changes.
*   **Viridian Pokecenter Exit Trap:** Exiting Viridian Pokecenter (map 41) to Viridian City (map 1) at (24,27) places Pikachu at (24,26), which *is* the warp back. MUST sidestep before moving north.

# Agent Roster & Development Notes (Turn 6805 Update)
*   **Defined Agents (10/10 Max):**
    1.  `map_analyzer_agent`: Primary for map queries. *Critique: Can give long/erroneous paths. Monitor efficacy.*
    2.  `scripted_event_tracker_agent`: For known event triggers. (Tested)
    3.  `team_builder_agent`: For major battle team comp. *Low usage; evaluate utility.*
    4.  `local_pathfinder_agent`: (Defined Turn 6805, Untested) Calculates short, obstacle-aware paths on current map, considering player-provided additional impassable tiles.
    5.  `notepad_query_agent`: Queries notepad. (Tested)
    6.  `npc_interaction_planner_agent`: Plans NPC interactions. (Tested)
    7.  `training_spot_advisor`: Suggests training spots. (Untested)
    8.  `path_segmenter_agent`: Breaks long paths. (Tested)
    9.  `emergency_exit_planner_agent`: Finds closest exits. (Untested)
    10. `hm_usage_advisor_agent`: Advises on HM usage. (Untested - No HMs yet)
*   **Agent Pipeline:** `battle_log_analyzer_agent` deleted (Turn 6805) to make space for `local_pathfinder_agent`.
*   **Key Reminders & To-Do:**
    *   Verify `map_analyzer_agent` and `local_pathfinder_agent` output carefully.
    *   Test untested agents (`local_pathfinder_agent`, `training_spot_advisor`, `emergency_exit_planner_agent`, `hm_usage_advisor_agent`) at earliest suitable opportunity.
    *   Evaluate low-usage agents (`team_builder_agent`) for utility or redesign.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# World Knowledge Graph (WKG) Management Notes
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.
*   Ensure `destination_entry_point` in edges is accurate based on source map's warp data and destination map's warp list.

# Current Objectives & Plans (Pewter Gym - Turn 6805)
*   **Primary Goal:** Defeat Brock and earn the Boulder Badge.
*   **Secondary Goal:** Challenge Gym Leader Brock (Currently in battle).
*   **Tertiary Goal:** Explore Pewter City for items or information (Post-Gym).
*   **Immediate Action:** Continue battle with Brock.

# EXP Tracking Summary
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Capped Pokémon show EXP gain message but value doesn't change.

## Pewter City - Route 3 Access Correction (Turn 6841)

**CRITICAL MISUNDERSTANDING CORRECTED (Thanks AI Observer!):**
- The Cool Trainer F at (9,16) blocking the path north in Pewter City is **NOT** the way to Route 3 that leads to Mt. Moon.
- Access to Route 3 (East of Pewter City) is **blocked by the Youngster (ID 5) escort event**. This event occurs near (36,17) and **MUST BE RESOLVED** to proceed east.
- My previous attempts to reach the eastern exit by complex pathing were flawed because I was trying to *avoid* this prerequisite event instead of triggering and completing it.

**Failed Pathing Attempt #11 (Pewter East Exit - Pre-Youngster Event Resolution):**
- From (9,17) -> Down to (9,21) -> Right to (20,21) -> Up to (20,19) -> Right towards (40,19).
- Reached (18,21) facing Right, but the next step to (19,21) was blocked by impassable shoes decoration (Turn 6840). This path was also based on the flawed assumption of bypassing the Youngster event.

**New Plan (Post-Critique):**
1.  **Resolve Youngster Escort Event:** Navigate to the Youngster (ID 5, likely near (36,17)) and interact to trigger/complete the event. This is the **immediate priority** to unlock Route 3.
2.  Use `local_pathfinder_agent` to navigate to an interaction spot near the Youngster (e.g., (36,18) to interact with him at (36,17)) due to persistent manual pathfinding issues.