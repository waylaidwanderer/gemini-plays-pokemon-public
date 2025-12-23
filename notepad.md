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
- **Location:** Switch Room (23, 3).
- **Action:** Check Shutter at (20, 6).
- **Plan:**
  1. Walk to (20, 5).
  2. Check if Shutter at (20, 6) is OPEN.
  3. If Open, proceed South to Emergency Switch.
  4. If Closed, I need to rethink the puzzle logic. Maybe specific combinations like S2+S3?

## Tile Mechanics
- **FLOOR:** Walkable.
- **WALL/Shutter (Closed):** Impassable.
- **Shutter (Open):** Walkable.
- **Switch:** Toggles shutter states.
- **LADDER/DOOR/WARP:** Transitions to other areas.

## Switch Mechanics Log
- **Switch 1 (16, 1):** ON opens (12, 8) if S2 OFF.
- **Switch 2 (10, 1):** ON opens (10, 6) & (6, 8). Closes (12, 8). *Hypothesis: Opens (20, 6).*
- **Switch 3 (2, 1):** ON opens (12, 8). Closes (20, 6)? No, (20, 6) was closed anyway.