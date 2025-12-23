# Goldenrod Underground Switch Puzzle

## Switch Logic & Hypotheses
- **Switch 1 (16, 1):**
    - **Hypothesis:** Toggles between Inner East `(12, 8)` and Outer East `(20, 6)` paths?
    - **Verified:** ON opens Inner East `(12, 8)` (Confirmed). OFF closes it.
- **Switch 2 (10, 1):**
    - **Hypothesis:** Main Power / Master Switch.
    - **Verified:** ON opens North Gate `(10, 6)` and West Gate `(6, 8)`. OFF closes them.
- **Switch 3 (2, 1):**
    - **Hypothesis:** Emergency / Override Switch.
    - **Verified:** ON opens Emergency shortcuts (e.g. `(2, 7)`) but overrides and CLOSES the main gates `(10, 6)` and `(6, 8)`.

## Current Strategy
**Goal:** Rescue Director.
**Current Config:** S1=OFF, S2=ON, S3=OFF.
**Hypothesis:**
- S2=ON provides power (Opening gates).
- S3=OFF removes the emergency lock (Opening normal paths).
- S1=OFF selects the **Outer East Path** (Since S1=ON selected Inner).
**Objective:** Navigate to `(20, 5)` and inspect the Outer East Shutter at `(20, 6)`.
**Contingency:** If `(20, 6)` is still closed, the only untried combination for S3=OFF is `S1=ON, S2=ON, S3=OFF`. But that opened `(12, 8)`.
So if S1=OFF, S2=ON, S3=OFF doesn't open `(20, 6)`, then S1 is not a simple toggle.

## Exploration Status
- **Inner East Path (12, 8):** Dead end (blocked by walls south of row 9).
- **West Path (via 2, 7 with S3=ON):** Leads to Pharmacist (4, 8) who says "Nothing down there". Dead end?
- **Outer East Path (20, 6):** Currently the main target. Contains Emergency Switch `(20, 11)` and Door `(22, 10)`.
- **Observation (Turn 14435):** System confirmed (10, 6) opened (WALL -> FLOOR).
    - **Conclusion:** S2=ON is active and S3=OFF removed the override on the North Gate.
- **Action:** Proceeding to check (20, 6) with high confidence that S1=OFF (Outer Path selected) + S2=ON (Power) will open it.
- **Observation (Turn 14436):** System reported (12, 8) changed FLOOR -> WALL (Closed).
    - **Confirmation:** S1=OFF closes the Inner East Shutter (12, 8).
    - **Hypothesis:** If S1 is a toggle, S1=OFF should open the Outer East Shutter (20, 6).
- **Action:** Navigating to (20, 6) to verify.
- **Result (Turn 14437):** With S1=OFF, S2=ON, S3=OFF, Shutter (20, 6) is CLOSED.
- **Action:** Turning Switch 1 ON.
- **Next Config:** S1=ON, S2=ON, S3=OFF.
- **Goal:** Verify if this opens (20, 6). We know it opens (12, 8).
- **Action:** Confirming Switch 1 ON (Pressing A on YES).
- **Hypothesis:** S1=ON, S2=ON, S3=OFF opens (12, 8). Will it open (20, 6)?
- **Plan:** After confirming, navigate to (20, 5) to inspect.
- **Verification:** Screen shows "It's labeled SWITCH 1".
- **Action:** Pressing 'A' to advance text and see if it is ON or OFF.
- **Reasoning:** I need to be 100% sure S1 is ON before walking away to check the shutter.
- **Action:** Navigating to (20, 6) to test S1=ON, S2=ON, S3=OFF.
- **Hypothesis:** S1 ON opens the East side shutters (both 12,8 and 20,6?).
- **Contingency:** If (20, 6) is closed, the only untried logical combo is S1=ON, S2=ON, S3=ON.
- **Action:** Navigating to (20, 6) to test S1=ON, S2=ON, S3=OFF.
- **Hypothesis:** S1 ON opens the East side shutters (both 12,8 and 20,6?).
- **Contingency:** If (20, 6) is closed, the only untried logical combo is S1=ON, S2=ON, S3=ON.
- **Observation:** Navigating to (20, 6) from (24, 5).
- **Current State:** S1=ON, S2=ON, S3=OFF.
- **Goal:** Check if (20, 6) is OPEN.
- **Note:** If closed, the next logical step is S1=ON, S2=ON, S3=ON.
- **Result (Turn 14449):** With S1=ON, S2=ON, S3=OFF, Shutter (20, 6) is CLOSED.
- **Action:** Navigating to Switch 3 to turn it ON.
- **Next Config:** S1=ON, S2=ON, S3=ON.
- **Reasoning:** S3 (Emergency) might be needed for the Emergency Switch path. S3 closes the central gate (10, 6), but I can reach (20, 6) via the North corridor (Row 4/5).
- **Observation (Turn 14450):** Navigating to Switch 3.
- **Current State:** S1=ON, S2=ON, S3=OFF.
- **Hypothesis Refined:** S1 likely toggles between Inner East (12, 8) and West (6, 8). Since S1 is ON, (12, 8) is OPEN and (6, 8) is CLOSED.
- **Goal:** Turn S3 ON to create state S1=ON, S2=ON, S3=ON.
- **Hope:** That S3 (Emergency) combined with S1 (East Selection) opens the Outer East Shutter (20, 6).
- **Action:** Moving to Switch 3 to turn it ON.
- **New Test Config:** S1=ON, S2=ON, S3=ON.
- **Hypothesis:** "All Systems Go" (All ON) might be the key. S3 (Emergency) combined with S1 (East) and S2 (Power) might open the path to the Emergency Switch.
- **Action:** Interacting with Switch 3 to turn it ON.
- **Target Config:** S1=ON, S2=ON, S3=ON.
- **Reasoning:** S1 (East) + S2 (Power) + S3 (Emergency) is the only untested logical combination for opening the Outer East Shutter (20, 6).
- **Action:** Pressing A to confirm turning Switch 3 ON.
- **Expectation:** Switch 3 becomes ON. State becomes S1=ON, S2=ON, S3=ON.
- **Next Step:** Verify "It's ON" text, then navigate to (20, 5).
- **Action:** Pressed A to turn Switch 3 ON.
- **Current State:** S1=ON, S2=ON, S3=ON.
- **Hypothesis:** All Switches ON should open the path to the Emergency Switch.
- **Next:** Verify text confirms "ON", then go to (20, 6).
- **Verification (Turn 14459):** Switch 3 is confirmed ON.
- **Current State:** S1=ON, S2=ON, S3=ON.
- **Action:** Closing menu (Leaving S3 ON).
- **Next Step:** Navigate to (20, 5) via Row 4 to inspect the Outer East Shutter (20, 6).
- **Action:** Navigating to (20, 6) with S1=ON, S2=ON, S3=ON.
- **Hypothesis:** This "All Systems Go" configuration might open the Outer East Shutter.
- **Action:** Navigating to (20, 6) to test S1=ON, S2=ON, S3=ON.
- **Path:** Along Row 4 (North Corridor).
- **Expectation:** If (20, 6) opens, proceeding South.
- **Note:** S3=ON likely closed the North Gate (10, 6) and West Gate (6, 8), so the only way South *must* be via the Outer East path or the West Shortcut (2, 7).
- **Observation (Turn 14463):** System notification in prev turn confirmed (12, 8) changed FLOOR -> WALL (Closed) when S3 turned ON.
    - **Conclusion:** S3=ON overrides and closes the Inner East Shutter (12, 8).
    - **Hypothesis:** S3=ON might *open* the Outer East Shutter (20, 6) in exchange.
- **Action:** Continuing to (20, 6) to verify.
- **Action:** Bumping (20, 6) to definitively confirm closure with S1=ON, S2=ON, S3=ON.
- **Next Step:** If closed, traverse East to check (22, 6) and (23, 6).
- **Strategy Shift:** If S2=ON fails consistently, I must test S2=OFF combinations (which require looping through the Warehouse to bypass the closed North Gate).
- **Result (Turn 14466):** Shutter (20, 6) CLOSED with S1=ON, S2=ON, S3=ON.
- **Analysis:** S1=ON, S2=ON, S3=ON fails.
- **New Strategy:** Revert to S1=ON, S2=ON, S3=OFF.
- **Reason:** This config opened (12, 8) (Inner East), but that was a dead end. However, it *also* opens (6, 8) (West Gate).
- **Hypothesis:** The West Path (6, 8) leads to the Burglar at (9, 12) and potentially the Director. The "Dead End" comment from the Pharmacist might be a trick or refer to the *visible* area only.
- **Action:** Turning S3 OFF, then checking (6, 8).
- **Action:** Turning Switch 3 OFF.
- **Target Config:** S1=ON, S2=ON, S3=OFF.
- **Hypothesis:** This opens (12, 8) AND (6, 8).
- **Goal:** Enter West Gate (6, 8) and explore the West Room thoroughly for a path to the Center/South.
- **Observation (Turn 14467):** System reported (6, 9) changed WALL -> FLOOR.
- **Current State:** S1=ON, S2=ON, S3=OFF.
- **Hypothesis:** This configuration opens the West Path as well.
- **Action:** Going to check if I can pass through the West Gate at (6, 6) and (6, 7) to reach the newly opened tile at (6, 9).
- **Result (Turn 14468):** West Gate (6, 6) was CLOSED with S1=ON, S2=ON, S3=OFF.
- **Analysis:** S1=ON opens East (12, 8). Maybe S1=OFF opens West (6, 6)?
- **Plan:** Go to Switch 1, Turn it OFF. Then check (6, 6).
- **Hypothesis:** S1 selects the active path (ON=East, OFF=West). S2 provides power. S3 is emergency.
- **Hypothesis Adjustment:** S1 ON = East Open / West Closed. S1 OFF = West Open / East Closed.
- **Plan:** Turn S1 OFF. This sets state to **S1=OFF, S2=ON, S3=OFF** (Assuming S3 is OFF? Wait, I left S3 ON in 14459).
- **Correction:** I left S3 ON.
- **Revised Plan:**
    1. Turn S1 OFF.
    2. Go to Switch 3 and turn it OFF (Because S3 ON closes the main gates `10,6` and `6,8`).
    3. Ensure S2 is ON.
    4. Go through `(10, 6)` to `(6, 8)`.
- **Action:** Turning Switch 1 OFF first.
- **Action:** Switch 1 turned OFF.
- **Current State:** S1=OFF, S2=ON, S3=ON.
- **Next Step:** Navigate to Switch 3 (2, 1) and turn it OFF.
- **Goal:** Reach state S1=OFF, S2=ON, S3=OFF.
- **Action:** Navigating to Switch 3 to turn it OFF.
- **Hypothesis:** Reaching state S1=OFF, S2=ON, S3=OFF.
- **Expectation:** This should open Gate (10, 6) and West Gate (6, 8), allowing access to the West Room from the North.
- **Observation (Turn 14472):** Navigating to Switch 3.
- **Current State:** S1=OFF, S2=ON, S3=ON.
- **Map Update:** `(12, 8)` changed WALL -> FLOOR (Opened) when S1 turned OFF (with S3=ON).
- **Hypothesis:** `(12, 8)` state depends on both S1 and S3.
- **Goal:** Reach S3 and turn it OFF to achieve S1=OFF, S2=ON, S3=OFF.
- **Target:** West Gate `(6, 8)`.