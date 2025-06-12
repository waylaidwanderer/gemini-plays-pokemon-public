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

# Route 22 Navigation - Lessons & Failed Attempts (Turn 6074)
*   **Objective:** Reach 14 unseen tiles on Y=10.
*   **Current Strategy (Reconfirmed from Turn 6040):** Travel east on lower path (Y=15) to (34,15), then north to (34,11) in grass, then west along northern grass strip.
*   **Failed Attempts/Hypotheses:**
    1.  **Direct Westward Travel in Eastern Isolated Grass Patch (X=31-34, Y=9-12):** Attempted multiple times (at least 3-4 distinct attempts, e.g., turns 6030, 6032, 6043, 6045, 6064) to move west from (31,11) or (31,10). Consistently blocked by impassable tiles at X=30 on rows Y=10 and Y=11. This patch is confirmed isolated from the main western grass strip.
    2.  **Direct Upward Movement from Lower Path (Y=15) to Northern Grass (Y=10):** Attempted to move directly north from various points on the Y=15 path (e.g., around (3,15) on turn 6037, (23,15) on turn 6027). Consistently blocked by the Y=14 ledge line. Confirmed ledges are one-way (downwards only).
    3.  **Navigation within Eastern Isolated Grass Patch to find alternate exit:** Explored the eastern grass patch (X=31-34, Y=9-12) extensively (e.g., turns 6045-6057, 6064-6071). Confirmed only exit is south via ledge jumps. No westward path exists within this patch.
*   **Conclusion:** The long detour strategy (east on Y=15, north to Y=11, then west on Y=10/Y=11) remains the only viable approach to reach all unseen tiles. The current step is moving from (3,15) to (34,15).

# Current Plan - Route 22 Exploration (Turn 6077)
*   **Objective:** Reach all 14 unseen tiles on Y=10. Currently at (34,11) in the northern grass strip.
*   **Strategy:** Move west along the northern grass strip (Y=11 or Y=10) to clear the unseen tiles. First target is the cluster from X=23 to X=26 on Y=10, then the cluster from X=3 to X=12 on Y=10.

# Agent Ideas (Notepad - Turn 6077)
*   Specialized Exploration Agent: Could analyze map XML and `reachable_unseen_tiles` to identify isolated sections or complex ledge navigation requirements, providing more nuanced pathing advice than the current `exploration_planner_agent` for very tricky maps.
*   Moveset Advisor Agent: Could suggest optimal moves to learn/forget for Pokémon based on current party, upcoming challenges (Gyms, E4), and type coverage needs.