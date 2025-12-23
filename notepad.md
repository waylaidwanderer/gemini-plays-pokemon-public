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
- **Action:** Double-checking Switch 2 state.
- **Reason:** North Shutter (10, 6) is closed. Need to confirm if S2 is truly ON.
- **Contingency:**
  - If S2 is OFF: Turn it ON.
  - If S2 is ON: Conflict confirmed. Will proceed to turn S1 OFF.

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** The path is blocked by shutters. Need to find a combination that allows access to the South-East area.
- **Next Step:** Turn S2 ON. Enter Central Room via (10, 6). Explore connection to South.