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
- **State:** S1=ON, S2=OFF, S3=ON.
- **Location:** Near (7, 5).
- **Observation:** Attempted to go South from West side, but navigation was tricky.
- **New Plan:** Use Switch 2.
    - Logic: S2 opens the North Shutter (10, 6). This provides direct access to the Central Room from the top.
    - S2 also opens West Shutter (6, 8), so I can potentially exit West if needed.

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** The path is blocked by shutters. Need to find a combination that allows access to the South-East area.
- **Next Step:** Turn S2 ON. Enter Central Room via (10, 6). Explore connection to South.