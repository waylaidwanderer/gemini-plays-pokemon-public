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
- **State:** S1=OFF, S2=ON, S3=OFF.
- **Location:** Central Room (10, 9).
- **Action:** Verify shutter states.
- **Plan:**
  1. Check if (6, 8) is OPEN.
  2. Check if (12, 8) is CLOSED.
  3. If East is blocked, exit North.
  4. Try S1=ON, S2=OFF, S3=OFF to open East Entry (20, 6).

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Switch 1 ON opens the North-East Shutter at (20, 6).
- **Observation:** S2 ON allows entry to Central, but closes East path. S3 ON allows entry to West, but closes East path.

- **Next Step:** Turn S2 ON. Enter Central Room via (10, 6). Explore connection to South.