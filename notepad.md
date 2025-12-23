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