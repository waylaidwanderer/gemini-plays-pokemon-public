# Current Navigation Plan (Viridian Forest)
*   **Objective:** Reach Viridian Forest North Exit at (2,1) or (3,1).
*   **Status:** Currently in battle in Viridian Forest. Pathing along western side.

# Lessons Learned & Game Mechanics
*   **Pewter Youngster Escort (Route 3 Blocker):** Youngster (ID 5, trigger near (36,17) in Pewter) blocks Route 3. Avoid this area for now.
*   **Accurate Self-Location:** Always verify current position against Game State Information.
*   **Adaptability:** Abandon consistently unachievable objectives. If progress stalls despite trying and documenting various hypotheses (3-4 attempts), pivot to a new goal or strategy.
*   **Map Awareness:** Reinforce mental model of current map, obstacles, and event triggers. Critically evaluate agent-provided paths against map memory.
*   **Ledge Mechanics:** One-way (downwards only). Crucial for Route 22 navigation and current Route 2 navigation.
*   **Movement:** 1st press TURNS *and* MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Verified with SPBARKY.
*   **Poison Damage:** Outside battle, poisoned Pokémon lose 1 HP every 4 steps.

# Agent Usage Plan & Review Notes (Turn 6211 Update)
*   **`map_analyzer_agent` (Many Uses):** Primary tool for map queries. Generally reliable but has failed (e.g., Route 22, Turn 6114; Route 22, Turn 6120). Prompt updated (Turn 6128) to be stricter about ledges. Continue using for path validation and map feature identification, but always verify its output.
*   **`move_validator_agent` (137 Uses - System Errors):** Intended for complex path validation. Has had numerous system errors and proven unreliable. **DO NOT USE THIS AGENT.** Continued high usage despite these issues was a critical error in judgment.
*   **`specialized_exploration_agent` (0 Uses - Defined Turn 6128):** Intended for complex exploration planning. Evaluate its effectiveness when a suitable complex area is encountered.
*   **`scripted_event_tracker_agent` (Low Usage):** Tracks proximity to known scripted events. Use when approaching areas with known or suspected event triggers.
*   **`pp_management_agent` (1 Use - Failed Turn 6173):** Advises on PP conservation. Failed its only use. Rely on manual PP assessment for now. Avoid using this agent until its reliability can be re-evaluated under different circumstances.
*   **`team_builder_agent` (1 Use):** Suggests team compositions for major battles. Use for Gyms, Rival, E4.
*   **`battle_log_analyzer_agent` (1 Use):** Parses battle text. Use after significant battles.
*   **`notepad_query_agent` (3 Uses):** Queries notepad content.
*   **`npc_interaction_planner_agent` (0 Uses):** Plans NPC interactions.
*   **`battle_advisor_agent` (0 Uses - Defined Turn 6025):** Provides in-battle advice.
*   **Agent Limit:** 10 agents. Plan definitions/deletions proactively.
*   **Input Data:** Ensure agents with `agent_can_run_code: true` are NOT fed `map_xml_string` or `world_knowledge_graph_json_string` as direct inputs.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# Party Status (Turn 6233)
*   **SPBARKY (PIKACHU):** Lv12 (39/39 HP, EXP: 1728 - CAPPED)
*   **FLAREE (VULPIX):** Lv8 (26/26 HP, EXP: 718)
*   **ODDISH (ODDISH):** Lv12 (37/37 HP, EXP: 973 - CAPPED)
*   **BIRBY (PIDGEY):** Lv7 (24/24 HP, EXP: 236)

# World Knowledge Graph (WKG) Management
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.

# Route/Area Specific Notes
*   **Pewter City - Route 3:** Attempts abandoned due to Youngster escort event.
*   **Route 2 (Section North of Viridian Forest - Future Access):** The section of Route 2 accessible *after* passing through Viridian Forest (from south to north) will have cuttable trees requiring HM Cut.
*   **Route 22 Summary:** This route presented significant navigational challenges due to ledges and isolated grass patches. Multiple strategies were attempted. All reachable unseen tiles eventually explored or confirmed inaccessible. Key lessons: ledges are strictly one-way; isolated areas require careful pathfinding, often via different map entry points; agent-provided paths for complex terrain must be rigorously verified.
*   **Viridian City Obstacles:** Blocked east by impassable tile at (8,15). Blocked east by cuttable tree at (15,5). Blocked south (detour attempt) by impassable tile at (13,6).
*   **Route 22 Gate:** Guard at (7,3) confirms BOULDERBADGE needed to pass west. Area fully explored.
*   **Route 2 (South of Viridian Forest - Current Area):** Navigating complex ledges and paths to reach Viridian Forest South Gate. Currently at (10,48).

# EXP Tracking & Observations
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Capped Pokémon show EXP gain message but value doesn't change.