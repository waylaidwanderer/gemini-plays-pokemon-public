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
- **State:** S1=OFF, S2=ON, S3=OFF.
- **Location:** West Room (2, 12).
- **Action:** Return to switches to reconfigure.
- **Plan:**
  1. Go to Switch 2 (10, 1).
  2. Turn Switch 2 OFF (Closes West/North, Allows East).
  3. Turn Switch 1 ON (Opens East).
  4. Ensure Switch 3 is OFF.
  5. Enter East Room via (12, 8).

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Access is via the East Room.
- **Blocker:** S2=ON blocks East. Must reset.