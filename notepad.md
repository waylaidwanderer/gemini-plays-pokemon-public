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
- **Location:** Moving to Switch 3 (2, 1).
- **Hypothesis:** S2 controls the inner East Shutter (20, 6), just as it controls the inner North Shutter (10, 6).
- **Problem:** S2 ON closes the main East entrance (12, 8).
- **Solution:** Use the "Back Door" (Warehouse Key door) to enter the East Room from the other side, bypassing (12, 8).
- **Plan:**
  1. Turn Switch 3 OFF.
  2. Turn Switch 2 ON. (State: S1=OFF, S2=ON, S3=OFF).
  3. Exit the Switch Room to the Main Underground Tunnel.
  4. Enter the locked door I opened earlier (Warehouse Entrance).
  5. Navigate through the Warehouse to reach the East Room.
  6. Check if (20, 6) is OPEN.
  7. Access Emergency Switch.

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