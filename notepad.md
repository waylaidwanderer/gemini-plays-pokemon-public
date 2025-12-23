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
- **Location:** Switch Room (12, 5).
- **Action:** Turn Switch 3 ON.
- **Plan:**
  1. Move to Switch 3 (2, 1).
  2. Turn S3 ON.
  3. Check if Shutter at (20, 6) is OPEN.
  4. If not, try S1=OFF, S3=ON.

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Access is via the East Room.
- **Blocker:** S2=ON blocks East. Must reset.