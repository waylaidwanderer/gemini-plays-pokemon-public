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
- **Location:** Moving to West Room via (6, 8).
- **Action:** Get Item at (1, 12).
- **Plan:**
  1. Enter West Room via shutter at (6, 8).
  2. Pick up item at (1, 12).
  3. Check if (6, 12) allows access to the Pharmacist at (9, 12).

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Need to find path to South-East.
- **Observation:** Row 10-11 in Central Room are Walls. Must find way around.