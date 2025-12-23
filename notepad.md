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
- **State:** S1=ON, S2=OFF, S3=OFF.
- **Location:** East Corridor (16, 9).
- **Observation:** This corridor is separated from the Emergency Switch room by a wall at Column 18.
- **Goal:** Open Shutter at (20, 6) to access the Far East Room.
- **Plan:**
  1. Exit to Switch Room (12, 5).
  2. Go to Switch 3 (2, 1).
  3. Turn S3 ON.
  4. Check if (20, 6) is OPEN.
  5. Test other combinations (S1+S3, etc.).

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Access is via the East Room.
- **Blocker:** S2=ON blocks East. Must reset.