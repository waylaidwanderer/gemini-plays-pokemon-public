# Mechanics
- **Battle Cursor:** Remembers last move used.
- **Fly Map:** Visual Map (Cursor based). Use D-pad to select city. **Cursor persists:** Always verify "Currently selected destination" text before confirming flight.
- **Pokegear Map:** Visual. Roaming Beasts appear as icon.
- **Menu Memory:** Start Menu and Pokegear cursors remember their last position. Always verify state.

# Strategic Status
- **Goal:** Register Raikou & Entei.
- **Current Task:** Hunt Roaming Beasts (Phase 2).
- **Location:** Route 38 (West of Ecruteak).
- **Action:** Hunt Loop: Transition between Rt 38 and Gatehouse.
- **Hunt Progress:** Phase 2 Loop 1/50. Started Turn 40029.
- **Beast Status:** Checking Route 38.
- **Hunt Strategy:**
    1. Check Pokegear on Route 38.
    2. If Beast is present: Max Repel -> Grass -> Search.
    3. If not: Enter Gatehouse -> Return to Route 38.
    4. Repeat.

# Past Attempts
- **Phase 1 (Rt 37):** 75 loops. 0 Encounters. Failed.

# Strategy (Encounter)
- **Raikou/Entei:** Flee immediately.
- **Plan:** Sleep (Gengar/Haunter/Butterfree if available, currently have none? Check Party).
- **Party Check:**
  - Gyarados (Lead, Intimidate might lower attack but they flee).
  - Machoke.
  - Oddish (Status fodder).
  - Quilava.
  - Lugia (Tank).
  - Pidgey.
  - **Correction:** I don't have a reliable sleeper in the party. Oddish is Lv 5.
  - **Note:** Roamers retain damage. Hitting them hard is better than nothing if I can't sleep them.
  - **Master Ball:** I don't have one? Check Inventory. No Master Ball listed.
  - **Action:** Just hit them for now. Track HP.

# Resources
- **Money:** ¥15644.
- **Items:** Max Repel x30.
- **Key Items:** Pass (Magnet Train).
- **Status:** Route 38 (35,9). Loop 25 Negative. Resetting.
- **Next Step:** Close Map (B) -> Close Gear (B) -> Enter Gate (Right).
- **Note:** Beasts on Rt 42 & Rt 32. Not here.
- **Roamer Check:** Negative. Resetting for Loop 26.
- **Strategy:** Manual Reset: Enter -> Exit -> Check.
- **Strategy:** Manual Reset: Right (Enter) -> Left (Exit) -> Check Map.
- **Strategy:** Manual Reset Loop: Check Map -> B -> Right (Enter Gate) -> Left (Exit Gate) -> Start (Map).
- **Lesson:** Gatehouse warps can be sticky. Automate resets to avoid 'doorway effect'.
## Tile Mechanics
- **Route 38 Gatehouse Warp (35,8) & (35,9):**
  - **(35,9):** Confirmed entry from Left (Route 38). Standard warp.
  - **(35,8):** Inconsistent/Sticky. Possible exit-only or requires specific alignment.
  - **Gatehouse Interior (0,4) & (0,5):**
    - **(0,4):** Exit to (35,8).
    - **(0,5):** Exit to (35,9).
  - **Recommendation:** Always use (35,9) [Bottom Tile] for entry from Route 38. Use (0,5) [Bottom Tile] for exit from Gatehouse to maintain alignment.
- **Tool Dev Lesson:** Tools CANNOT execute sequences that span across map transitions. The harness interrupts execution when the map ID changes. Automating "Enter -> Exit" is impossible in one tool call. Must split into step-by-step or use single-map tools.