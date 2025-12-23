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

## Current Goal: Test S2=ON with S1=OFF
- **Observation:**
    - (10, 6) is CLOSED (Verified).
    - S1=OFF, S2=ON, S3=ON.
- **Plan:**
  1. Navigate to (20, 5) to check Shutter (20, 6).
  2. If (20, 6) is CLOSED, the next test is S1=OFF, S2=ON, S3=OFF.
  3. This requires going to Switch 3 (2, 1).

## Pathfinding & Strategy
- **Start Turn:** 13766
- **Objective:** Reach Emergency Switch (20, 11).
- **Current Barrier:** Shutter (20, 6) or finding a path around it.
- **Hypothesis:** If (20, 6) is CLOSED with All-ON, then S2 might need to be OFF for *navigation*, but maybe ON for *unlocking*? Or I missed a combination.
- **Next Test:** If All-ON fails, try S1=OFF, S2=ON, S3=ON.

## Discrepancies & Errors
- **Corrected:** Position mismatch in T13754. Turn count mismatches in T13756, T13762.
- **Lesson:** Always verify `num_turns` and `current_position` against Game State, not just memory. Visual verification of shutters is required before pathing.