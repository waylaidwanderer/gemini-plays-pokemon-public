# Mechanics
- **Battle Cursor:** Remembers last move used.
- **Fly Map:** Visual Map (Cursor based). Use D-pad to select city. **Cursor persists:** Verify destination text.
- **Pokegear Map:** Visual. Roaming Beasts appear as icon.
- **Menu Memory:** Start Menu and Pokegear cursors remember their last position. Always verify state.
- **Repel Safety:** Always re-apply Repel IMMEDIATELY upon expiration, even before short travel to avoid unwanted encounters.
- **Tile Mechanics:**
    - **Route 38 Gatehouse (35,8) & (35,9):** Sticky warps.
    - **Solution:** "Double Tap" technique (press direction into warp, then press again into wall) works reliably.

# Strategic Status
- **Goal:** Register Raikou & Entei.
- **Current Task:** Hunt Roaming Beasts (Phase 2).
- **Location:** Route 38 (East Side).
- **Action:** Resume Scan (Loop 1).
- **Hunt Progress:** Repel Active. Scanning.

# Hunt Strategy
1. **Target Acquired:** Beast IS on Route 38!
2. **Action:** Fix Lead Pokemon -> Repel -> Hunt.
3. **Contingency:** If it flees, track location and pursue.

# Resources
- **Balls:** Ultra Ball x16.
- **Repels:** Max Repel x27.
- **Party:** Gyarados (Lv 37) [Lead], Lugia (Lv 60).

# Encounter Plan
- **Raikou/Entei:** They flee 100%.
- **Action:** Attack immediately to chip HP. Do not switch.
- **Note:** Roamers retain HP damage.

# Log
- **Phase 2 (Rt 38 - Turn ~40500):**
    - Hunted on Route 38 using Repel. No encounter.
    - Turn 40539: Repel expired.
    - Turn 40546: Map check confirmed Roamers moved to Rt 42/44/31. None on Rt 38.
- **Phase 3 (Gatehouse Shuffle):**
    - Turn 40548: Wade called. Handling call, then heading to Gatehouse (35, 8).
- Strategy: Performing Gatehouse Shuffle (Route 38 <-> Gatehouse) to force Roaming Beast movement. Checking Pokegear map after each transition.
- Turn 40565: Map check negative. Beasts at Rt 42/44/32.
- Turn 40566: Re-entering Gatehouse (Right x2) to shuffle.
- Turn 40567: Inside Gatehouse. Exiting back to Route 38 (Left x2) to complete shuffle.
- Turn 40568: Back on Route 38. Opening Start Menu to check map.
- Turn 40570: Attempting optimized navigation: `press_sequence_with_delays` ['Right', 'A'] to open Map immediately.
- Turn 40571: Sandbox down. 'press_sequence_with_delays' failed. Reverting to manual input: Pressing 'Right' to select Map Card.
- Turn 40573: Map check negative. Beasts at Rt 42, Rt 44, Rt 32.
- Action: Closing Pokegear (B) to re-enter Gatehouse and shuffle again.