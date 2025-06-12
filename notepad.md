# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to heal FLAREE (6/26 HP) and purchase essential supplies. Money: ¥156.
*   **Tertiary Goal:** Reach Route 3 (East Pewter Exit at (40,19)) to battle trainers for funds.

# Pewter City Strategy & Current Plan
*   **Current Location:** (14,21) in Pewter City.
*   **Immediate Goal:** Reach Pewter Pokecenter at (14,26) to heal FLAREE (6/26 HP).
*   **Youngster (ID 5) Status:** Currently at (36,17). He triggers an escort event if approached in eastern Pewter City (e.g., from (37,19), (38,19), (30,19)), moving player to (12,19).
*   **Post-Healing Plan for Route 3 (East Pewter Exit at (40,19))**:
    1.  Exit Pokecenter to (14,25).
    2.  Explore eastward path from (14,25) along Y=25/26/27 or explore southern paths (e.g., via Y=31/32) to reach eastern Pewter.
    3.  The path needs to circumvent the Youngster at (36,17). A potential route could be: (14,25) -> E to (X,25) -> S to (X,Y_south) -> E to (Z_east, Y_south) -> N to (Z_east, 19) -> E to (40,19).
    4.  Use `scripted_event_tracker_agent` for path segments in eastern Pewter (X > 25) or near Youngster's coordinates.
*   **Known Pathing Obstacles in Western/Central Pewter (near Pokecenter/Gym):**
    *   (19,19) - Impassable (blocks eastward movement from Gym area pocket).
    *   (17,18) - Gym Warp (accidentally entered trying to go North from (17,19)).
    *   (17,17) through (17,15) - Impassable (blocks northward movement from (17,19)).
    *   (12,22), (13,22), (14,22), (15,22) - Impassable (blocks southward movement in X=12-15 range at Y=21).

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