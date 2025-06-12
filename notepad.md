# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to heal FLAREE (6/26 HP) and purchase essential supplies. Money: ¥156.
*   **Tertiary Goal:** Reach Route 3 (East Pewter Exit at (40,19)) to battle trainers for funds.

# Pewter City Navigation Challenge: The Youngster (ID 5)
*   **Youngster's Current Position (Game State is TRUTH):** (18,19). This is a NEW position, much closer to the Gym/west side of town than his previous (36,17) spot.
*   **Escort Event Dynamics:** Still complex. His new position at (18,19) likely means his trigger zones have shifted significantly. The old triggers around (36,17) might still be active if he moves back there, but the immediate threat is his current location.
*   **Known Trigger/Drop-off Points (Markers are reminders):** (38,19) (triggered from (37,19) when Y. was at (36,17)), (30,19) (drop-off & trigger). These may behave differently with Y. at (18,19). Marked zones around (36,17) are less relevant *while he is at (18,19)*.
*   **Current Strategy for Route 3 (Accounting for Youngster at (18,19))**:
    1.  **Far South Route Attempt (Still Viable):** Navigate from current position (Gym drop-off, (12,19)) to Y=27 (e.g., (12,27)). Then head east along Y=27 to X=40, then north to Route 3 exit at (40,19). This path is south of the Youngster's new (18,19) position.
    2.  **Far North Route (Fallback):** If south fails, try Y=10-14, east, then south. This path would be north of his new (18,19) position.
    3.  Meticulously check map XML for impassable tiles for any new planned path. Use `move_validator_agent` for short, complex segments.
    4.  Use `scripted_event_tracker_agent` to vet *path segments* (3-5 steps) when approaching X=18 or moving east, always using Youngster's *current coordinates* ((18,19) with radius 3 for now).

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