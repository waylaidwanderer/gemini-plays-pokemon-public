# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to heal FLAREE (6/26 HP) and purchase essential supplies. Money: ¥156.
*   **Tertiary Goal:** Reach Route 3 (East Pewter Exit at (40,19)) to battle trainers for funds.

# Pewter City Navigation Challenge: The Youngster (ID 5)
*   **Youngster's Current Position (Game State is TRUTH):** (36,17).
*   **Escort Event Dynamics:** The trigger is complex and dynamic, not solely fixed tiles. It depends on the Youngster's *current location* (e.g., (36,17)), player's proximity, player's specific coordinates (e.g., (38,19) was triggered when moving from (37,19) with Y. at (36,17)), and possibly approach vector/facing.
*   **Known Trigger/Drop-off Points (Markers are reminders):**
    *   (38,19): Confirmed trigger when moving East from (37,19) with Youngster at (36,17).
    *   (30,19): Confirmed Youngster escort drop-off point. Also a potential trigger.
    *   Other marked zones: (36,17), (35,17), (34,19), (36,18), (38,20) - treat with extreme caution.
*   **Current Strategy for Route 3 (Post-Reflection):**
    1.  After current escort event: Navigate from drop-off point (likely Gym or (30,19)) to a significantly different starting point for an eastern approach, avoiding Y=19 initially.
    2.  Consider a path *far south* (e.g., Y=26/27, then east, then north) or *far north* (e.g., Y=10-14, then east, then south).
    3.  Meticulously check map XML for impassable tiles for any new planned path. Use `move_validator_agent` for short, complex segments.
    4.  Use `scripted_event_tracker_agent` to vet *path segments* (not single steps) in eastern Pewter (X > 25), always using Youngster's current coordinates.

# Game Mechanics & Strategy Notes
*   **Ledge Mechanics:** One-way (downwards only).
*   **Movement:** 1st press TURNS if not facing, 2nd press MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **Map Marker Usage:** 💥 (Confirmed Event Trigger), 🎯 (Drop-off/Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainers), 🏛️ (Building Entrance).

# Party Status
*   SPBARKY (PIKACHU): Lv12 (38/39 HP) (Capped)
*   FLAREE (VULPIX): Lv8 (6/26 HP) - CRITICAL HP.
*   SPROUT (ODDISH): Lv12 (33/37 HP) (Capped)

# Agent Usage Plan (Post-Reflection)
*   **`scripted_event_tracker_agent`:** Use to vet *path segments* (3-5 steps) in eastern Pewter (X > 25), always inputting Youngster's current sprite coordinates as a dynamic trigger (e.g., radius 3).
*   **`move_validator_agent`:** Use for short, complex pathing segments, especially in western Pewter or when navigating near known obstacles/impassable tiles. Also to validate initial steps of `exploration_planner_agent` paths.
*   **`exploration_planner_agent`:** Use for navigating complex/obstructed areas like western Pewter if manual pathing fails repeatedly. Validate its output for initial steps or risky areas.
*   **`potion_purchase_optimizer_agent`:** Use once sufficient funds ( > ¥200) are acquired to heal FLAREE.

# Agent Ideas
*   **Youngster Event Predictor Agent:** Input: player_pos, player_facing, youngster_pos, youngster_facing, recent_player_path. Output: trigger_likelihood (low/medium/high), reasoning. (Low priority to define).

# Hindsight & Lessons Learned (Post-Reflection)
*   **Pewter City Pathing (General):** Manual pathing has been highly inefficient, especially in western Pewter and for avoiding the Youngster. Must be more systematic:
    1.  Clearly define a multi-step path segment.
    2.  Verify segment against map XML for known impassable tiles.
    3.  If complex/risky, use `move_validator_agent` for the segment.
    4.  If near Youngster, use `scripted_event_tracker_agent` for the segment.
*   **Youngster Event Avoidance:** Repeatedly trying the same approach vectors (e.g., Y=19 eastwards when Youngster is at (36,17)) is ineffective. Must try significantly different routes or approach patterns.
*   **Agent Path Execution:** Must be more careful translating `exploration_planner_agent` coordinate paths to button presses. Validate initial steps.
*   **Notepad Precision:** Ensure `old_text` for `replace` actions is exact to avoid failed updates.
*   **Trust Game State:** Always prioritize current Game State Information (NPC positions, map data) over memory or potentially outdated critiques.