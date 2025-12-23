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
- **Location:** At (10, 2). Turned Switch 2 ON.
- **Action:** Check North Shutter (10, 6).
- **Logic:** S2=ON should open (10, 6). S3=ON keeps (6, 8) Open. S1=ON might keep (12, 8) Closed (override).
- **Plan:**
  1. Verify (10, 6) is OPEN.
  2. Enter Central Room.
  3. Exit West via (6, 8) [Should be open due to S2/S3].
  4. Go South to Row 12+.

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** The path is blocked by shutters. Need to find a combination that allows access to the South-East area.
- **Next Step:** Turn S2 ON. Enter Central Room via (10, 6). Explore connection to South.