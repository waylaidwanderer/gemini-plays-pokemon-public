# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to heal FLAREE and purchase essential supplies.
*   **Tertiary Goal:** Reach Route 3 to identify trainers for battling.

# Game Mechanics & Strategy
*   **Ledge Mechanics:** One-way (downwards only). Cannot move UP onto a ledge from a lower Y.
*   **Movement Mechanic:** 1st press TURNS if not facing, 2nd press MOVES. **Pikachu Movement:** If not facing Pikachu and attempting to move onto Pikachu's tile, first press turns, second press moves. Applies only when moving *into* Pikachu's tile.
*   **Level Cap:** 0 badges = Lv12. EXP gain stops at cap.
*   **Data Trust:** Game State Information is absolute truth. Youngster (ID 5) is at (36,17) as of Turn 5458.
*   **Map Marker Usage:** ❗ (Event Trigger/Obstacle), 💁 (Event NPCs/blockers), ☠️ (Defeated Trainers), 📍 (Nav Point).

# Party Status (Turn 5458)
*   SPBARKY (PIKACHU): Lv12 (38/39 HP) (Level Cap Reached)
*   FLAREE (VULPIX): Lv8 (6/26 HP) - Critically low HP. Must be healed.
*   SPROUT (ODDISH): Lv12 (33/37 HP) (Level Cap Reached)

# Pewter City Navigation Challenge: Reaching Route 3 (East Exit)
*   **Current Location:** (16,21), facing Down. Pikachu at (17,21).
*   **Immediate Goal:** Reach (30,19) to attempt a northern path to Route 3.
*   **Youngster (ID 5) Escort Event:**
    *   NPC Location: (36,17) (per Game State).
    *   Behavior: Triggers an escort to the Gym entrance. This is not solely based on stepping on fixed map tiles. Proximity to Youngster, his facing, and player's movement vector likely play a role. The event most recently triggered when moving from (37,19) to (38,19) while Youngster was at (36,17).
    *   Marked potential trigger zones (still worth caution): (36,17), (35,17), (30,19), (34,19), (36,18), (38,19), (38,20). (30,19) is also a drop-off point.
    *   Strategy: For any movement in eastern Pewter City (approx. X > 25), use `scripted_event_tracker_agent` with Youngster's *current coordinates* from Game State as the primary trigger to monitor.
*   **Western Pewter Obstacles:** Blocked repeatedly trying to move east. Using `exploration_planner_agent` to navigate from (17,21) to (30,19). Impassable tiles exist around X=19 (Y=19-22) and X=18 Y=22.
*   **Current Route 3 Plan (Northern Attempt):** From (30,19) -> (30,16) -> (35,16), then east along Y=16 to (40,16), then south to Route 3 exit at (40,19).

# Agent Usage Plan
*   **`scripted_event_tracker_agent`:** Use for *every step* in eastern Pewter City (X > 25), inputting Youngster's current sprite coordinates as the main trigger point with a radius (e.g., r=2 or r=3).
*   **`move_validator_agent`:** Use for short, complex pathing segments near known obstacles to avoid wasted turns.
*   Other agents (route_progress, battle_log, potion_purchase) to be used when conditions are met.

# Inventory & Finances
*   POKé BALL x1
*   Money: ¥156 (Critically Low)

# Hindsight & Lessons Learned
*   **Pewter City West Pathing:** Must meticulously check map XML or use `move_validator_agent` for paths in this area to avoid hitting impassable tiles. My pathing from (12,19) towards (30,19) has been very inefficient.
*   **Youngster Event Dynamics:** The trigger is not simply fixed tiles. His current location and player's approach seem critical. Using `scripted_event_tracker_agent` dynamically with his current position is key.