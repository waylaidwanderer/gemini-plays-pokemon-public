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
- **Observation:**
  - (20, 6) is CLOSED with S3=ON.
  - S3 opens (12, 8) but not (20, 6).
- **Action:** Return to Switch 3 (2, 1).
- **Plan:**
  1. Turn S3 OFF.
  2. Turn S2 ON.
  3. Check if (20, 6) opens.
  4. (S2 opens North Shutter at 10,6 so maybe it opens 20,6 too).

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Switch 3 should open the Far East Shutter at (20, 6).