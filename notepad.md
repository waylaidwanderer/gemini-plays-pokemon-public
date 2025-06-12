# Current Plan - Route 22 & Viridian City
*   **Objective:** Fully explore Route 22 by reaching all unseen tiles. Then, return to Viridian City and proceed north via Route 2 towards Pewter City.
*   **Reason:** Completing exploration of Route 22 before moving to next major area. Primary goal is Boulder Badge in Pewter.
*   **Status:** On Route 22 at (3,15). Navigating lower path east to find access to northern grass strip for remaining unseen tiles. Encountered navigational challenges with ledges and isolated grass patches.

# Lessons Learned & Game Mechanics
*   **Pewter Youngster Escort (Route 3 Blocker):** Youngster (ID 5, trigger near (36,17) in Pewter) blocks Route 3. Avoid this area for now.
*   **Accurate Self-Location:** Always verify current position against Game State Information.
*   **Adaptability:** Abandon consistently unachievable objectives (e.g., after 3-4 failed attempts).
*   **Map Awareness:** Reinforce mental model of current map, obstacles, and event triggers.
*   **Ledge Mechanics:** One-way (downwards only).
*   **Movement:** 1st press TURNS *and* MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Verified with SPBARKY.
*   **Poison Damage:** Outside battle, poisoned Pokémon lose 1 HP every 4 steps.

# Agent Usage Plan & Review Notes (Turn 6057 Update)
*   **`map_analyzer_agent` (Many Uses):** Primary tool for map queries. Generally reliable. Continue using for path validation and map feature identification.
*   **`move_validator_agent` (Low Usage - System Errors):** Intended for complex path validation. Has had system errors. Use sparingly and with caution.
*   **`exploration_planner_agent` (Multiple Uses - Updated Prompt):** Generates exploration paths. Prompt updated (Turn 6031) to better handle ledges, but still requires cautious use and manual verification of paths involving ledges, as it has previously provided invalid paths. (Reliability Note: Repeatedly struggled with optimal pathing on Route 22, especially around ledges and isolated grass patches, even after prompt updates. Use with extreme caution for complex navigation; manual planning or `map_analyzer_agent` for segments might be better.)
*   **`scripted_event_tracker_agent` (Low Usage):** Tracks proximity to known scripted events. Use when approaching areas with known or suspected event triggers.
*   **`pp_management_agent` (1 Use - Defined Turn 6031):** Advises on PP conservation. Utilize before long routes, dungeons, or major battles.
*   **`team_builder_agent` (1 Use):** Suggests team compositions for major battles. Use for Gyms, Rival, E4.
*   **`battle_log_analyzer_agent` (1 Use):** Parses battle text into a structured summary. Use after significant or complex battles for review.
*   **`notepad_query_agent` (3 Uses):** Queries notepad content. Useful for recalling specific recorded details.
*   **`npc_interaction_planner_agent` (0 Uses - Defined Turn 6025):** Plans NPC interactions. Consider using for tricky NPC approaches.
*   **`battle_advisor_agent` (0 Uses - Defined Turn 6025):** Provides in-battle advice. Consider for tough fights.
*   **Agent Limit:** Be mindful of the 10-agent limit. Plan definitions/deletions proactively. (Lesson: Repeatedly hit limit due to poor planning turns 6025-6029, 6031, 6033-6036.)
*   **Input Data:** Ensure agents with `agent_can_run_code: true` are NOT fed `map_xml_string` or `world_knowledge_graph_json_string` as direct inputs.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree)

# Party Status (Turn 6061)
*   **SPBARKY (PIKACHU):** Lv12 (39/39 HP, EXP: 1728 - CAPPED) | Moves: THUNDERSHOCK (25 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP)
*   **FLAREE (VULPIX):** Lv8 (26/26 HP, EXP: 718) | Moves: EMBER (25 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP)
*   **ODDISH (ODDISH):** Lv12 (37/37 HP, EXP: 973 - CAPPED) | Moves: TACKLE (35 PP), POISONPOWDER (35 PP), LEECH SEED (10 PP)
*   **BIRBY (PIDGEY):** Lv7 (24/24 HP, EXP: 236) | Moves: GUST (35 PP), SAND-ATTACK (15 PP)

# World Knowledge Graph (WKG) Management
*   Verify current location and that a map transition has *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.

# Route/Area Specific Notes
*   **Pewter City - Route 3:** Attempts abandoned due to Youngster escort event.
*   **Route 2:**
    *   Southern part does not directly connect north to Pewter City. Must go via Viridian City.
    *   The northern part of Route 2 (towards Pewter City) has areas blocked by cuttable trees. One is noted near a warp at (13,10) on that map segment (tree likely at (6,11)). Another is at (13,53) on the overall Route 2 map. HM Cut will be required to explore these areas fully and potentially find more trainers/items.

# EXP Tracking & Observations
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Pokémon at the level cap (e.g., SPBARKY at Lv12 with 0 badges) will show an EXP gain message but their actual EXP value will not change.

# Agent Reliability Notes
*   **`exploration_planner_agent`**: Prompt updated (Turn 6033) to better handle ledges, but still requires cautious use and verification of paths involving ledges. Has previously given paths that were blocked by ledges or impassable terrain.

# Route 22 Navigation Strategy (Turn 6040)
*   Current approach to clear remaining unseen tiles (all on Y=10) involves a long detour: travel east along the lower path (Y=15) to (34,15), then north to (34,11) to access the northern grass strip, then west along the northern grass strip to reach the unseen tile clusters.

# Route 22 Navigation - Lessons & Failed Attempts (Turn 6078 Update)
*   **Objective:** Reach 14 unseen tiles on Y=10.
*   **Previous Flawed Strategy (Based on Turn 6040, executed up to Turn 6077):** Travel east on lower path (Y=15) to (34,15), then north to (34,11) in the *eastern isolated grass patch*, then attempt to move west along northern grass strip. This failed because the eastern grass patch (X=31-34, Y=9-12) is isolated from the western grass strip (where unseen tiles are) by an impassable barrier at X=30 (tiles (30,10) and (30,11)).
*   **Failed Attempts/Hypotheses (Confirming Isolation & Ledge Issues):
    1.  **Direct Westward Travel in Eastern Isolated Grass Patch (X=31-34, Y=9-12):** Attempted at least 5-6 times (e.g., turns 6030, 6032, 6043, 6045, 6064, 6071, 6072). Consistently blocked by impassable tiles at X=30 on rows Y=10 and Y=11. This patch is confirmed isolated from the main western grass strip.
    2.  **Direct Upward Movement from Lower Path (Y=15) to Northern Grass (Y=10) in Western/Central Area:** Attempted to move directly north from various points on the Y=15 path (e.g., around (3,15) on turn 6037 & 6073, (23,15) on turn 6027 & 6069). Consistently blocked by the Y=14 ledge line. Confirmed ledges are one-way (downwards only).
    3.  **Navigation within Eastern Isolated Grass Patch (X=31-34, Y=9-12) to find alternate exit:** Explored this patch extensively (e.g., turns 6045-6057, 6064-6072, 6076). Confirmed only exit is south via ledge jumps. No westward path exists from this patch to the main northern grass strip.
*   **New Conclusion (Turn 6078):** To reach the unseen tiles on Y=10 (located in the western part of the northern grass strip, X=3-12 and X=23-26), the following approach is necessary:
    1.  Jump down from any isolated grass patches if currently in one (e.g., the eastern patch).
    2.  Travel west along the lower path (Y=15) to approximately X=17.
    3.  From around (17,15), move north into the *western* grass strip (e.g., to (17,10) or (17,11)).
    4.  Explore west and east from this entry point to clear all unseen tiles on Y=10.

# Current Plan - Route 22 Exploration (Turn 6084 - Revised Corrected Strategy II)
*   **Objective:** Reach all 14 unseen tiles on Y=10 (located in western/central northern grass strip).
*   **Current Position:** (17,15) on lower path.
*   **Strategy Steps (New Conclusion - Turn 6084):**
    1.  (Done) Be on the lower path (Y=15 or Y=16). Currently at (17,15).
    2.  Travel EAST along the lower path from (17,15) to (30,15). (Current action)
    3.  Move North from (30,15) to (30,13) (ground), then further north to (30,6) (ground, where rival SPB was).
    4.  Move West from (30,6) along the upper path (Y=5 or Y=6) to approximately X=17 (e.g., (17,6) or (17,5)).
    5.  From (17,5/6), move south to (17,8), which is a LEDGE.
    6.  Jump down the ledge at (17,8) to land at (17,9) (grass).
    7.  From (17,9) grass, move to (17,10) grass (seen tile, but access point to unseen areas).
    8.  Explore west from (17,10) to clear unseen tiles around (3,10)-(12,10).
    9.  Explore east from (17,10) to clear unseen tiles around (23,10)-(26,10).

# Agent Ideas (Notepad - Turn 6077)
*   Specialized Exploration Agent: Could analyze map XML and `reachable_unseen_tiles` to identify isolated sections or complex ledge navigation requirements, providing more nuanced pathing advice than the current `exploration_planner_agent` for very tricky maps.
*   Moveset Advisor Agent: Could suggest optimal moves to learn/forget for Pokémon based on current party, upcoming challenges (Gyms, E4), and type coverage needs.