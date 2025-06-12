# Current Objectives
*   **Primary Goal:** Obtain the Boulder Badge from the Pewter City Gym Leader, Brock.
*   **Secondary Goal:** Acquire sufficient funds to purchase essential supplies. (Current Money: ¥156)
*   **Tertiary Goal:** Reach Route 3 (East Pewter Exit at (40,19)) to battle trainers for funds.

# Pewter City Strategy & Current Plan
*   **Current Location:** (34,21) in Pewter City, facing Up. Pikachu at (34,22).
*   **Immediate Goal:** Reach Route 3. Current plan is Attempt #5 for a northern/north-western approach after healing.
*   **Current Route 3 Strategy (Attempt #5 leading to #6 via Intentional Escort - Corrected Start Pos):**
    1.  Current Position (Turn 5617 start): (32,19) facing Left. Pikachu at (33,19).
    2.  `scripted_event_tracker_agent` (Turn 5615, when player was at (33,19)) confirmed moving east to (34,19) triggers Youngster escort (Youngster at (36,17)).
    3.  **Action for Turn 5617 (after notepad edit):** Move from (32,19) to (33,19) (Pikachu's tile), then to (34,19) to trigger escort. Expected drop-off: (12,19) near Gym.
    4.  **Contingency Plan (Attempt #6 - Southern Detour from Gym Entrance if Escorted):
        a.  From (12,19), move Left to (11,19).
        b.  From (11,19), move South to (11,21). (Path: (11,19)->(11,20)->(11,21))
        c.  From (11,21), move East to (20,21). (Path: (11,21)...(20,21))
        d.  From (20,21), move South to (20,27). (Path: (20,21)...(20,27))
        e.  From (20,27), move East to (40,27). (Path: (20,27)...(40,27))
        f.  From (40,27), move North to (40,19) (Route 3 Exit).
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