# Goldenrod Underground Switch Puzzle

## Switch Mechanics Log
- **Switch 1 (16, 1):**
    - ON: Opens (12, 8) if S2 is OFF. (Active).
    - OFF: ?
- **Switch 2 (10, 1):**
    - ON: Opens North Shutters (10, 6)/(11, 7). Opens West Shutter (6, 8). Closes East Shutter (12, 8).
    - OFF: Default. Allows S1 to open (12, 8).
- **Switch 3 (2, 1):**
    - ON: Opens West Shutter (6, 8). Closes East Shutter (12, 8). (Active).
    - OFF: Default. Allows S1 to open (12, 8).

## Current Status
- **State:** S1=ON, S2=ON, S3=ON.
- **Location:** At (10, 2). Switch 2 is ON.
- **Observation:** With S1=ON, S2=ON, S3=ON, the North Shutter (10, 6) is CLOSED.
- **Conclusion:** S1=ON or S3=ON interferes with S2's ability to open the North Shutter.
- **Goal:** Reach South Area via West Path.
- **Requirement:** West Shutter (6, 8) OPEN (requires S3=ON). North Shutter (10, 6) OPEN (requires S2=ON).
- **Hypothesis:** S1=ON is the conflict.
- **Plan:**
  1. Navigate to Switch 1 (16, 1).
  2. Turn S1 OFF.
  3. Verify (10, 6) opens (or check if East Shutter closes).
  4. Return to (10, 6) and enter.

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** The path is blocked by shutters. Need to find a combination that allows access to the South-East area.
- **Next Step:** Turn S2 ON. Enter Central Room via (10, 6). Explore connection to South.