# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to purchase essential supplies. (Current Money: ¥156)
*   **Tertiary Goal:** Reach Route 3 (East Pewter Exit at (40,19)) to battle trainers for funds.

# Pewter City Strategy & Current Plan
*   **Current Location:** (34,21) in Pewter City, facing Up. Pikachu at (34,22).
*   **Immediate Goal:** Reach Route 3. Current plan is Attempt #5 for a northern/north-western approach after healing.
*   **Current Route 3 Strategy (Attempt #6d - Gym Reset & Far West-South-East Detour):**
    1.  Attempt #6c failed: Path south along X=17 from (17,21) is blocked by impassable (17,22). Current position (17,21).
    2.  The area (X=5-18, Y=19-21) is a confirmed pocket. Only exit is Gym warp (17,18).
    3.  Plan:
        a.  From current (17,21), move North to (17,18) (Gym Warp).
        b.  Enter Gym, then immediately exit. Land at (17,19) in Pewter City.
        c.  From (17,19), navigate: West to (5,19).
        d.  From (5,19), South to (5,32).
        e.  From (5,32), East to (35,32).
        f.  From (35,32), North to (35,30).
        g.  From (35,30), East to (37,30).
        h.  From (37,30), South to (37,32).
        i.  From (37,32), East to (40,32).
        j.  From (40,32), North to (40,19) (Route 3 exit).
    4.  This is a long detour but aims to bypass all previously encountered X=19, Y=22, and X=36 blockades systematically.
*   **Known Pathing Obstacles in Pewter City:**
    *   (34,20) - Impassable building facade.
    *   (36,27) - Impassable.
    *   (35,26) - Impassable.
    *   X=36 column is largely impassable from Y=21 down to Y=32 (house structures).
    *   Western 'pocket' near Gym (X=5-18, Y=19-21) requires Gym warp to escape if entered from east/south of it.
    *   Pokecenter entrance is at (14,26), entered by moving Up from (14,27).

# Agent Usage Plan
*   **`scripted_event_tracker_agent`:** MUST use for the eastern path segment from (33,19) towards (40,19) to assess risk from Youngster (36,17).
*   **`move_validator_agent`:** Use for short, complex, or risky manual pathing segments if unsure, especially after an agent path is provided or if screen details are ambiguous.
*   **`map_analyzer_agent`:** Use for finding paths in complex areas if manual attempts fail. Critically review its output.
*   **`money_management_agent`:** Use once sufficient funds are acquired to plan purchases.

# Agent Ideas (Dormant - for future consideration)
*   **Youngster Event Predictor Agent:** Input: player_pos, player_facing, youngster_pos, youngster_facing, recent_player_path, map_xml. Output: trigger_likelihood (low/medium/high), reasoning, suggested safe_tile.
*   **Path Refinement Agent:** Input: High-level coordinate path, player pos/facing, Pikachu pos. Output: Detailed button presses for segment, considering Pikachu turning & basic obstacle avoidance.

# Game Mechanics & Strategy Notes
*   **Ledge Mechanics:** One-way (downwards only).
*   **Movement:** 1st press TURNS if not facing, 2nd press MOVES. Pikachu: 1st press turns, 2nd moves if moving *into* his tile and not facing him.
*   **Level Cap:** 0 badges = Lv12.
*   **Map Marker Legend:** 💥 (Confirmed Event Trigger), 🎯 (Drop-off/Key Nav Point), ❗ (Risky Zone/Obstacle), 💁 (Event NPCs), ☠️ (Defeated Trainers), 🏛️ (Building Entrance), 📍 (Key Navigation Point / Start of new route attempt), 🧱 (Confirmed Impassable Blocker), 🚪 (Used Warp).
*   **Tile Navigability:** Inferred from tile `type` (e.g., 'ground', 'grass') and presence of blocking objects/NPCs. 'Impassable' type is a hard block.

# Party Status
*   SPBARKY (PIKACHU): Lv12 (39/39 HP) (Capped)
*   FLAREE (VULPIX): Lv8 (26/26 HP)
*   SPROUT (ODDISH): Lv12 (37/37 HP) (Capped)

# Hindsight & Lessons Learned
*   **Notepad `replace` failures:** Using `overwrite` for major cleanups is more reliable than trying to find exact `old_text` for `replace` after many micro-updates.
*   **Screen Check Imperative:** ALWAYS check tiles immediately adjacent (especially in direction of planned movement) on screen *before* committing to multi-step moves. Don't rely solely on map memory or agent paths without visual confirmation of the very next step if possible.
*   **Agent Output Review:** Critically review agent-provided paths against screen and map XML. Agents can make mistakes (e.g., `map_analyzer_agent` suggesting path through impassable tiles on turn 5563).
*   **Youngster Avoidance:** Eastern Pewter is a minefield. High-risk paths near him should be treated with extreme caution and use `scripted_event_tracker_agent`.
*   **Pikachu & Warps:** Be mindful of Pikachu's position near warps; accidental turns can lead to re-entering warps.