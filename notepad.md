# Mechanics
- **Battle Cursor:** Remembers last move used.
- **Fly Map:** Visual Map (Cursor based). Use D-pad to select city. **Cursor persists:** Verify destination text.
- **Pokegear Map:** Visual. Roaming Beasts appear as icon.
- **Menu Memory:** Start Menu and Pokegear cursors remember their last position. Always verify state.
- **Tool Dev Lesson:** `define_tool` Python scripts must print a JSON *list* (array) for `autopress_buttons`, not a JSON object.
- **Tile Mechanics:**
    - **Route 38 Gatehouse (35,8) & (35,9):** Sticky warps.
    - **Solution:** "Double Tap" technique (press direction into warp, then press again into wall) works reliably.

# Strategic Status
- **Goal:** Register Raikou & Entei.
- **Current Task:** Hunt Roaming Beasts (Phase 2).
- **Location:** Route 38 (West of Ecruteak).
- **Hunt Start:** Turn ~40000.
- **Current Loop:** 7 (Finished).
- **Action:** Exit Pokegear -> Shuffle Roamers.
- **Hunt Progress:** Beasts NOT on Route 38. Locations: Rt 42 & Rt 32.
- **Beast Status:** **NEGATIVE**.
- **Plan:**
    1. Exit Menu.
    2. Enter Gatehouse (shuffle).
    3. Check Map again.

# Hunt Strategy
1. **Target Acquired:** Beast IS on Route 38!
2. **Action:** Fix Lead Pokemon -> Repel -> Hunt.
3. **Contingency:** If it flees, track location and pursue.

# Resources
- **Balls:** Ultra Ball x16.
- **Repels:** Max Repel x29.
- **Party:** Gyarados (Lv 37) [Target Lead], Lugia (Lv 60) [Old Lead].

# Encounter Plan
- **Raikou/Entei:** They flee 100%.
- **Action:** Attack immediately to chip HP. Do not switch.
- **Note:** Roamers retain HP damage.

# Log
- **Phase 1 (Rt 37):** 75 loops. Failed.
- **Phase 2 (Rt 38):**
    - Loops 1-8: Negative (Bad Config).
    - Turn 40411: Reset. Fixed Lead/Repel.
    - Loop 1: Negative.