# Current Navigation Plan
*   **Objective:** Reach Viridian Forest North Exit at (2,1) or (3,1).
*   **Status:** Pathing through Viridian Forest. Currently in a wild battle.

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
*   **Notepad `replace` Action:** The `old_text` argument MUST be an *exact* character-for-character match of the text to be replaced. Use error message suggestions or copy directly from the notepad.

# Agent Usage Plan & Review Notes (Turn 6371 Update)
*   **`map_analyzer_agent`:** Primary tool for map queries. Generally reliable but can give very long paths. Use for path validation and map feature identification, but always verify its output.
*   **`move_validator_agent`:** (DELETED) Proven unreliable. Decision: Stopped using.
*   **`specialized_exploration_agent`:** Intended for complex exploration planning. Evaluate its effectiveness when a suitable complex area is encountered.
*   **`scripted_event_tracker_agent`:** Tracks proximity to known scripted events. Use when approaching areas with known or suspected event triggers.
*   **`pp_management_agent`:** Failed its only use. Rely on manual PP assessment for now. Avoid using this agent until its reliability can be re-evaluated.
*   **`team_builder_agent`:** Suggests team compositions for major battles. Use for Gyms, Rival, E4.
*   **`battle_log_analyzer_agent`:** Parses battle text. Use after significant battles.
*   **`notepad_query_agent`:** Queries notepad content.
*   **`npc_interaction_planner_agent`:** Plans NPC interactions. (Usage count corrected to 12).
*   **`battle_advisor_agent`:** (DELETED or never properly defined) Plan to ensure it's not taking an agent slot.
*   **`training_spot_advisor`:** Defined. Consider using for Viridian Forest.
*   **Agent Limit:** 9 agents currently defined. Plan definitions/deletions proactively.
*   **Input Data:** Ensure agents with `agent_can_run_code: true` are NOT fed `map_xml_string` or `world_knowledge_graph_json_string` as direct inputs.

# Map Marker Legend
💥 (Event Trigger), 🎯 (Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainer), 🏛️ (Key Building/Gym), 📍 (Path Start/Interesting Point), 🧱 (Impassable Obstacle), 🚪 (Used Warp), ℹ️ (Info NPC), 🌱 (Cuttable Tree), ⬆️ (Access Point), 🚧 (Ledge - Down only)

# Party Status (Turn 6371)
*   SPBARKY (PIKACHU): Lv12 (39/39 HP, EXP: 1728 - CAPPED)
*   FLAREE (VULPIX): Lv9 (27/28 HP, PSN, EXP: 808)
*   ODDISH (ODDISH): Lv12 (37/37 HP, EXP: 973 - CAPPED)
*   BIRBY (PIDGEY): Lv7 (18/24 HP, EXP: 263)

# World Knowledge Graph (WKG) Management
*   Verify map transition *just occurred* before adding edges. Nodes for known exits can be added pre-transition. Use consistent tags.

# Route/Area Specific Notes
*   **Pewter City - Route 3:** Attempts abandoned due to Youngster escort event.
*   **Route 2 (Section North of Viridian Forest - Future Access):** The section of Route 2 accessible *after* passing through Viridian Forest (from south to north) will have cuttable trees requiring HM Cut.
*   **Route 22 Summary:** This route presented significant navigational challenges due to ledges and isolated grass patches. All reachable unseen tiles eventually explored or confirmed inaccessible. Key lessons: ledges are strictly one-way; isolated areas require careful pathfinding; agent-provided paths for complex terrain must be rigorously verified.
*   **Viridian City Obstacles:** Blocked east by impassable tile at (8,15). Blocked east by cuttable tree at (15,5). Blocked south (detour attempt) by impassable tile at (13,6).
*   **Route 22 Gate:** Guard at (7,3) confirms BOULDERBADGE needed to pass west. Area fully explored.
*   **Route 2 (South of Viridian Forest):** Navigated complex ledges and paths to reach Viridian Forest South Gate.
*   **Viridian Forest:** Currently navigating this maze. Aiming for north exit. Good training spot for FLAREE and BIRBY.

# EXP Tracking & Observations
*   Wild Pokémon battles yield EXP for uncapped Pokémon. Capped Pokémon show EXP gain message but value doesn't change.

- Wild ODDISH Lv5 defeated in Viridian Forest (approx (19,38)). FLAREE used Ember (crit, super effective). Enemy used PoisonPowder, FLAREE poisoned. Message: SPBARKY gained 27 EXP (no change, still 1728, capped). FLAREE gained 27 EXP (781 -> 808).