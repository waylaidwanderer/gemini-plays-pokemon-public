# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to purchase essential supplies. (Current Money: ¥156)
*   **Tertiary Goal:** Explore Route 2 (south of Pewter City) for trainers/items to acquire funds.

# Current Plan - Viridian Forest Exploration
*   **Objective:** Explore Viridian Forest for trainers and items to acquire funds and EXP.
*   **Reason:** Accidentally re-entered Viridian Forest while attempting to explore Route 2. This area still offers opportunities for progress.
*   **Status:** Just defeated a wild Caterpie. Continuing south from (2,12).

# Lessons Learned - Pewter Navigation & Strategy
*   **Youngster Escort Event (Route 3 Blocker):** The Youngster (ID 5, trigger near (36,17)) is a major recurring obstacle, frequently resetting progress towards the east exit. After 8 failed attempts, Route 3 is considered temporarily inaccessible. I MUST AVOID REPEATING THIS FAILED STRATEGY.
*   **Accurate Self-Location:** CRITICAL. I have repeatedly misidentified my current position, leading to flawed pathing and WKG errors. Must always verify against Game State Information.
*   **Adaptability:** Must abandon objectives that prove consistently unachievable after a few (e.g., 3-4) attempts. Do not persist with failing strategies.
*   **Map Awareness:** Continuously reinforce mental model of the current map, especially locations of known persistent obstacles and dynamic event triggers.
*   **Path Validation:** While `move_validator_agent` is useful, over-reliance on it for simple paths is inefficient. For complex paths from `map_analyzer_agent`, validate in segments.

# Known Pathing Obstacles in Pewter City
*   (19,19), (19,21), (18,18), (5,22), (17,22), (13,17), (13,16) - Impassable tiles.
*   Cool Trainer F at (9,16) blocks passage on Y=16 unless approached correctly.
*   Gym Sign at (12,18) - Impassable background object.
*   Police Notice Sign at (34,20) - Impassable building facade.

# Agent Usage Plan & Review Notes
*   **`map_analyzer_agent`:** Primary tool for pathfinding. Review its output and validate paths in segments.
*   **`move_validator_agent`:** Use for genuinely complex, risky, or unclear path segments. Note: Has had system errors.
*   **`exploration_planner_agent`:** Currently unreliable. Avoid or review its prompt for improvements before further use.
*   **`scripted_event_tracker_agent`:** High usage, but effectiveness against Youngster event is questionable. Need to better integrate warnings or review agent logic.
*   Ensure agents with `agent_can_run_code: true` are NOT fed `map_xml_string` or `world_knowledge_graph_json_string` as direct inputs.

# Game Mechanics & Strategy Notes
*   **Ledge Mechanics:** One-way (downwards only).
*   **Movement:** 1st press TURNS if not facing, 2nd press MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **Map Marker Legend:** 💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated), 🏛️ (Building), 📍 (Path Start), 🧱 (Impassable), 🚪 (Used Warp), ℹ️ (Info NPC).

# Party Status
*   SPBARKY (PIKACHU): Lv12 (39/39 HP) (Capped)
*   FLAREE (VULPIX): Lv8 (26/26 HP)
*   ODDISH (ODDISH): Lv12 (37/37 HP) (Capped)

# World Knowledge Graph (WKG) Management
*   Verify current location and that a map transition has *just occurred* before adding edges. Nodes for known exits can be added pre-transition.

# Pewter City - Route 3 Attempts Summary (Abandoned Objective)
*   Attempted to reach Route 3 eight times. All attempts were ultimately blocked by the Youngster escort event or by impassable terrain discovered mid-path. The eastern exit is currently considered too unreliable to pursue for funds. Pivoting to Route 2 exploration.

# Route 2 Exploration Notes
*   The warp at (13,10) is blocked by a cuttable tree (likely at (6,11)) and is inaccessible without HM Cut.