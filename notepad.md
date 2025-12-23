# Goldenrod Underground Switch Puzzle

## Switch Mechanics Log
- **Switch 1 (16, 1):**
    - ON: Opens (12, 8) if S2 is OFF.
    - OFF: ?
- **Switch 2 (10, 1):**
    - ON: Appears to close (10, 6) and (6, 6). Possible "Lockdown" or requires specific S1/S3.
    - OFF: Opens (10, 6). Modifies S1/S3 effects.
- **Switch 3 (2, 1):**
    - ON: Opens (6, 8) if S2 is OFF. Closes (12, 8) if S2 is OFF.
    - OFF: ?

## Navigation Correction
- **Error:** Attempted to move Left at (8, 3) into Wall (7, 3).
- **Correction:** Row 3 and Row 2 have walls at x=6,7. Must use Row 4 to bypass.
- **Current Position:** (8, 3).

## Current Goal: Test S3=ON (S1=OFF, S2=OFF, S3=ON)
- **Current State:** S1=OFF, S2=OFF, S3=OFF.
- **Observation:** (10, 6) is CLOSED (All OFF).
- **Hypothesis:** All OFF is a reset state (All Closed).
- **Test:** Turn S3 ON.
  - S3 might control the West shutter (6, 6).
- **Plan:**
  1. Navigate to Switch 3 (2, 1).
  2. Turn S3 ON.
  3. Check Shutter (6, 6).
  4. If (6, 6) opens, enter West Room.

## Pathfinding & Strategy
- **Start Turn:** 13766
- **Objective:** Reach Emergency Switch (20, 11).
- **Current Barrier:** Shutter (20, 6) or finding a path around it.
- **Hypothesis:** If (20, 6) is CLOSED with All-ON, then S2 might need to be OFF for *navigation*, but maybe ON for *unlocking*? Or I missed a combination.
- **Next Test:** If All-ON fails, try S1=OFF, S2=ON, S3=ON.

## Discrepancies & Errors
- **Corrected:** Position mismatch in T13754. Turn count mismatches in T13756, T13762.
- **Lesson:** Always verify `num_turns` and `current_position` against Game State, not just memory. Visual verification of shutters is required before pathing.