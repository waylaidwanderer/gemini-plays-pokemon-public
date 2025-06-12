# Current Plan - Route 22
*   **Objective:** Defeat Rival SPB. Explore Route 22 for trainers/items. Acquire funds.
*   **Reason:** Need funds for supplies. Need EXP for non-capped Pokemon. Progress towards Pewter City.
*   **Status:** On Route 22 at (30,5). Rival SPB is at (30,6). Battle imminent.

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

# Agent Usage Plan & Review Notes
*   **`map_analyzer_agent`:** Primary tool for pathfinding. Review output, validate paths in segments.
*   **`move_validator_agent`:** Use for complex/risky path segments. (Note: Has had system errors).
*   **`exploration_planner_agent`:** Currently unreliable. Review prompt for improvements (e.g., focus on smaller segments, provide more goal context) before further use.
*   **`scripted_event_tracker_agent`:** Use cautiously, effectiveness against Pewter Youngster event was limited.
*   **`route_progress_analyzer_agent`:** Use for routes to identify remaining trainers/items (e.g., Route 2).
*   **`money_management_agent`:** Use when shopping with funds.
*   Ensure agents with `agent_can_run_code: true` are NOT fed `map_xml_string` or `world_knowledge_graph_json_string` as direct inputs.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree)

# Party Status (Turn 5921)
*   **SPBARKY (PIKACHU):** Lv12 (39/39 HP, 1728 EXP - CAPPED) | Moves: THUNDERSHOCK (30 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (19 PP)
*   **FLAREE (VULPIX):** Lv8 (21/26 HP, 718 EXP) | Moves: EMBER (23 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP)
*   **ODDISH (ODDISH):** Lv12 (37/37 HP, 973 EXP - CAPPED) | Moves: TACKLE (35 PP), POISONPOWDER (35 PP), LEECH SEED (10 PP)
*   **BIRBY (PIDGEY):** Lv7 (24/24 HP, 236 EXP) | Moves: GUST (35 PP), SAND-ATTACK (15 PP)

# World Knowledge Graph (WKG) Management
*   Verify current location and that a map transition has *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.

# Route/Area Specific Notes
*   **Pewter City - Route 3:** Attempts abandoned due to Youngster escort event.
*   **Route 2:**
    *   Southern part does not directly connect north to Pewter City. Must go via Viridian City.
    *   The northern part of Route 2 (towards Pewter City) has areas blocked by cuttable trees. One is noted near a warp at (13,10) on that map segment (tree likely at (6,11)). Another is at (13,53) on the overall Route 2 map. HM Cut will be required to explore these areas fully and potentially find more trainers/items.

# EXP Tracking & Observations
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Pokémon at the level cap (e.g., SPBARKY at Lv12 with 0 badges) will show an EXP gain message but their actual EXP value will not change.