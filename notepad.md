# Goldenrod Underground Switch Puzzle

## Tile Mechanics
- **FLOOR:** Walkable.
- **WALL/Shutter (Closed):** Impassable.
- **Shutter (Open):** Walkable.
- **Switch:** Toggles shutter states.
- **LADDER/DOOR/WARP:** Transitions to other areas.

## Switch Mechanics Log
- **Switch 1 (16, 1):**
    - ON: Opens East Shutter (12, 8) if S2 is OFF.
    - OFF: Default.
- **Switch 2 (10, 1):**
    - ON: Opens North (10, 6) & West (6, 8). Closes East (12, 8).
    - OFF: Default. Allows S1 to open East.
- **Switch 3 (2, 1):**
    - ON: Opens West Shutter (6, 8). Closes East Shutter (12, 8).
    - OFF: Default.

## Current Status
- **State:** S1=OFF, S2=OFF, S3=ON.
- **Location:** Switch Room (20, 5).
- **Action:** Test Shutter at (20, 6).
- **Observation:**
  - (12, 8) is OPEN with S3=ON (and S1/S2 OFF).
  - (20, 6) is the next target.
- **Plan:**
  1. Attempt to enter (20, 6).
  2. If blocked, the combination for (20, 6) is different.
  3. Possible next test: S2=ON (since S2 opens North Shutter (10, 6)).

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Switch 3 should open the Far East Shutter at (20, 6).