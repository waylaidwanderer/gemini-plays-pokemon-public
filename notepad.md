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
- **Location:** Switch Room (20, 5).
- **Action:** Enter East Room via (12, 8).
- **Observation:** Vertical Shutter at (20, 6) is CLOSED.
- **Plan:**
  1. Move to (12, 8).
  2. Enter East Room.
  3. Navigate to (20, 12) to reach Emergency Switch.

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Access is via the East Room.
- **Blocker:** S2=ON blocks East. Must reset.