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
- **Location:** West Room (6, 9).
- **Action:** Get Item at (1, 12).
- **Observation:** Row 12 is blocked by a wall at (6, 12).
- **Plan:**
  1. Pick up item at (1, 12).
  2. Verify if (6, 12) is passable or affected by switches.
  3. Return to Switches (Exit via North).
  4. Set S2=OFF, S1=ON to open East Path.
  5. Explore East Room (access to Pharmacist & Emergency Switch).

## Strategic Goal
- **Objective:** Reach Emergency Switch at (20, 11).
- **Hypothesis:** Access is via the East Room.
- **Blocker:** S2=ON blocks East. Must reset.