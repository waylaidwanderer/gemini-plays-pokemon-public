# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to heal FLAREE (6/26 HP) and purchase essential supplies. Money: ¥156.
*   **Tertiary Goal:** Reach Route 3 (East Pewter Exit at (40,19)) to battle trainers for funds.

# Pewter City Navigation Challenge: The Youngster (ID 5)
*   **Youngster's Current Position (Game State is TRUTH):** (36,17). He seems to patrol this area.
*   **Escort Event Dynamics:** The Youngster at (36,17) triggers an escort event if approached in eastern Pewter City (e.g., from (37,19) or (38,19)), moving the player to (12,19) in front of the Gym. (30,19) is also a known trigger/drop-off point.
*   **New Strategy for Route 3 (Far North Route):** The western part of Pewter City around (17,19)-(18,21) is a dead-end pocket, escaped via Gym warp. The previous southern route attempts are abandoned.
    1.  **Current Location:** (17,19) in Pewter City.
    2.  **Path to Route 3 (40,19):
        *   North from (17,19) to (17,14).
        *   East from (17,14) to (28,14) (path clear until (29,14) is impassable building).
        *   South from (28,14) to (28,19).
        *   East from (28,19) to (40,19) (Route 3 exit).
    3.  This route should keep me north of the Youngster (36,17) until the final eastern approach on Y=19.
    4.  Use `scripted_event_tracker_agent` for the final eastern segment if Youngster is still at (36,17).

# Game Mechanics & Strategy Notes
*   **Ledge Mechanics:** One-way (downwards only).
*   **Movement:** 1st press TURNS if not facing, 2nd press MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **Map Marker Usage:** 💥 (Confirmed Event Trigger), 🎯 (Drop-off/Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainers), 🏛️ (Building Entrance), 📍 (Key Navigation Point / Start of a new route attempt).

# Party Status
*   SPBARKY (PIKACHU): Lv12 (38/39 HP) (Capped)
*   FLAREE (VULPIX): Lv8 (6/26 HP) - CRITICAL HP.
*   SPROUT (ODDISH): Lv12 (33/37 HP) (Capped)

# Agent Usage Plan (Post-Reflection)
*   **`scripted_event_tracker_agent`:** Use to vet *path segments* (3-5 steps) in eastern Pewter (X > 25) or when near Youngster's current coordinates. Always input Youngster's current sprite coordinates as a dynamic trigger (e.g., radius 3).
*   **`move_validator_agent`:** Use for short, complex pathing segments, especially in western Pewter or when navigating near known obstacles/impassable tiles. Also to validate initial steps of `exploration_planner_agent` paths if used.
*   **`exploration_planner_agent`:** Use for navigating complex/obstructed areas like western Pewter if manual pathing fails repeatedly. Validate its output for initial steps or risky areas.
*   **`potion_purchase_optimizer_agent`:** Use once sufficient funds ( > ¥200) are acquired to heal FLAREE.

# Agent Ideas (Low Priority / Review)
*   (Discarded `rom_hack_mechanics_discoverer_agent` and `battle_strategy_advisor_agent` as per critique to avoid stale notes).
*   **Youngster Event Predictor Agent:** Input: player_pos, player_facing, youngster_pos, youngster_facing, recent_player_path. Output: trigger_likelihood (low/medium/high), reasoning. (Low priority to define).

# Hindsight & Lessons Learned (Critique Incorporated)
*   **Pewter City Pathing (General):** Manual pathing has been highly inefficient, especially in western Pewter and for avoiding the Youngster. Must be more systematic:
    1.  Clearly define a multi-step path segment.
    2.  Verify segment against map XML for known impassable tiles.
    3.  If complex/risky, use `move_validator_agent` for the segment.
    4.  If near Youngster, use `scripted_event_tracker_agent` for the segment.
*   **Youngster Event Avoidance:** Repeatedly trying the same approach vectors (e.g., Y=19 eastwards when Youngster was at (36,17)) was ineffective. Must try significantly different routes or approach patterns. Current Youngster position (18,19) requires new avoidance patterns.
*   **Agent Path Execution:** Must be more careful translating `exploration_planner_agent` coordinate paths to button presses. Validate initial steps. Agent paths can lead to unintended warps (e.g., Pewter Gym at (17,18)).
*   **Notepad Precision:** Ensure `old_text` for `replace` actions is exact. Overwriting is safer for large changes.
*   **Trust Game State:** Always prioritize current Game State Information (NPC positions, map data) over memory or potentially outdated critiques.
*   **Critique Incorporation:** Review critiques carefully for valid points (e.g., agent usage, pathing inefficiencies) but always cross-verify factual claims (like NPC positions) with the Game State.

# Agent Ideas (Post-Reflection - Turn 5560)
*   **Youngster Event Predictor Agent:** Input: player_pos, player_facing, youngster_pos, youngster_facing, recent_player_path, map_xml. Output: trigger_likelihood (low/medium/high), reasoning, suggested safe_tile to move to next if likelihood is high.
*   **Path Refinement Agent:** Input: A high-level path (sequence of a few key coordinates from `exploration_planner_agent` or manual plan), current player pos/facing, Pikachu pos. Output: Detailed button presses for that segment, considering Pikachu turning rules, and basic obstacle avoidance for 1-2 steps using map_xml.
*   **Money Management/Shopping Agent:** Input: Current money, shopping list (potions, pokeballs), item prices, party status (for potion needs). Output: Optimal purchase plan.