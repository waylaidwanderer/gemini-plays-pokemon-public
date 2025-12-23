# Goldenrod Underground Switch Puzzle

## Verified Switch Logic
- **Switch 1 (16, 1):**
    - ON: Opens East Shutter (12, 8) IF S2 is OFF.
    - OFF: Default.
- **Switch 2 (10, 1):**
    - ON: Opens North (10, 6) & West (6, 8). Closes East (12, 8). (Overrides S1)
    - OFF: Default.
- **Switch 3 (2, 1):**
    - ON: Closes West (6, 8) & East (12, 8). (Overrides S2 & S1). *Likely an emergency reset or trap.*
    - OFF: Default.

## Current Plan
1. **Goal:** Open East Shutter (12, 8) to reach the Warehouse.
2. **Current State:** S1=ON, S2=ON, S3=OFF.
3. **Next Step:** Turn S2 OFF.
4. **Prediction:** With S1=ON, S2=OFF, S3=OFF -> East Shutter (12, 8) should OPEN.

## Tile Mechanics
- **FLOOR:** Walkable.
- **WALL/Shutter (Closed):** Impassable.
- **Shutter (Open):** Walkable.
- **Switch:** Toggles shutter states.
- **LADDER/DOOR/WARP:** Transitions to other areas.
- **Action:** Switch 2 is confirmed OFF. Menu is open, closing it now.
- **Current State:** S1=ON, S2=OFF, S3=OFF.
- **Hypothesis:** This combination should open the shutter at (20, 6) or (12, 8).
- **Plan:**
  1. Close Switch Menu (Press B).
  2. Navigate to (20, 6) via Row 4.
  3. If (20, 6) is open, proceed South.