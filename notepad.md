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
- **Location:** Goldenrod Underground (SE Room).
- **Action:** Warp to Main Tunnel via (21, 31).
- **Plan:**
  1. Go South to Warp at (21, 31).
  2. Arrive in Main Tunnel.
  3. Go North to Warehouse Door (18, 6).
  4. Enter Warehouse.
  5. Navigate Warehouse to East Room.
  6. Check Shutter at (20, 6).

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