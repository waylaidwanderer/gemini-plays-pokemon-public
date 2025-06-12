# Current Navigation Plan (Viridian City)
*   **Objective:** Reach the northern exit of Viridian City at (19,1) to access Route 2.
*   **Status:** Currently at (13,5) in Viridian City. Path east was blocked by a cuttable tree at (15,5). Attempted detour south via (13,6) was blocked as (13,6) is impassable. Will use `map_analyzer_agent` to find a clear path.

# Lessons Learned & Game Mechanics
*   **Pewter Youngster Escort (Route 3 Blocker):** Youngster (ID 5, trigger near (36,17) in Pewter) blocks Route 3. Avoid this area for now.
*   **Accurate Self-Location:** Always verify current position against Game State Information.
*   **Adaptability:** Abandon consistently unachievable objectives. If progress stalls despite trying and documenting various hypotheses (3-4 attempts), pivot to a new goal or strategy.
*   **Map Awareness:** Reinforce mental model of current map, obstacles, and event triggers. Critically evaluate agent-provided paths against map memory.
*   **Ledge Mechanics:** One-way (downwards only). Crucial for Route 22 navigation.
*   **Movement:** 1st press TURNS *and* MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **EXP Cap Mechanics:** Pokémon at level cap do not gain EXP, even if message appears. Verified with SPBARKY.
*   **Poison Damage:** Outside battle, poisoned Pokémon lose 1 HP every 4 steps.

# Agent Usage Plan & Review Notes (Turn 6181 Update)
*   **`map_analyzer_agent` (Many Uses):** Primary tool for map queries. Generally reliable but has failed (e.g., Route 22, Turn 6114). Prompt updated (Turn 6128) to be stricter about ledges. Continue using for path validation and map feature identification, but always verify its output.
*   **`move_validator_agent` (137 Uses - System Errors):** Intended for complex path validation. Has had numerous system errors. **AVOID USING THIS AGENT or use with EXTREME CAUTION for very simple, verifiable paths only.** High usage despite errors was problematic.
*   **`specialized_exploration_agent` (0 Uses - Defined Turn 6128):** Intended for complex exploration planning. Evaluate its effectiveness when a suitable complex area is encountered.
*   **`scripted_event_tracker_agent` (Low Usage):** Tracks proximity to known scripted events. Use when approaching areas with known or suspected event triggers.
*   **`pp_management_agent` (1 Use - Failed Turn 6173):** Advises on PP conservation. Failed its only use. Manually assess PP or use cautiously.
*   **`team_builder_agent` (1 Use):** Suggests team compositions for major battles. Use for Gyms, Rival, E4.
*   **`battle_log_analyzer_agent` (1 Use):** Parses battle text. Use after significant battles.
*   **`notepad_query_agent` (3 Uses):** Queries notepad content.
*   **`npc_interaction_planner_agent` (0 Uses):** Plans NPC interactions.
*   **`battle_advisor_agent` (0 Uses - Defined Turn 6025):** Provides in-battle advice.
*   **Agent Limit:** 10 agents. Plan definitions/deletions proactively.
*   **Input Data:** Ensure agents with `agent_can_run_code: true` are NOT fed `map_xml_string` or `world_knowledge_graph_json_string` as direct inputs.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree)

# Party Status (Turn 6181)
*   **SPBARKY (PIKACHU):** Lv12 (39/39 HP, EXP: 1728 - CAPPED)
*   **FLAREE (VULPIX):** Lv8 (26/26 HP, EXP: 718)
*   **ODDISH (ODDISH):** Lv12 (37/37 HP, EXP: 973 - CAPPED)
*   **BIRBY (PIDGEY):** Lv7 (24/24 HP, EXP: 236)

# World Knowledge Graph (WKG) Management
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.

# Route/Area Specific Notes
*   **Pewter City - Route 3:** Attempts abandoned due to Youngster escort event.
*   **Route 2 (North of Viridian Forest):** Has areas blocked by cuttable trees. HM Cut will be required.
*   **Route 22 Summary:** This route presented significant navigational challenges due to ledges and isolated grass patches. Multiple strategies were attempted to reach all unseen tiles, involving complex paths, re-entry from Viridian City, and use of a gatehouse. Key lessons: ledges are strictly one-way; isolated areas require careful pathfinding, often via different map entry points; agent-provided paths for complex terrain must be rigorously verified. All reachable unseen tiles eventually explored or confirmed inaccessible for now.
*   **Viridian City Obstacles:** Blocked east by impassable tile at (8,15). Blocked east by cuttable tree at (15,5). Blocked south (detour attempt) by impassable tile at (13,6).

# EXP Tracking & Observations
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Capped Pokémon show EXP gain message but value doesn't change.