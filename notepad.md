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
- **Observation:** Turning S2 OFF caused (6, 8) to Close (changed to WALL) and (10, 6) to Close.
- **Hypothesis Refined:** S2 controls the West/Middle access. S1 likely controls the East access (20, 6).
- **Plan:** Checking (20, 6). If open, this is the way forward.
- **Observation:** (20, 6) is CLOSED (WALL) with S1=ON, S2=OFF, S3=OFF.
- **Action:** Going to check (12, 8).
- **Reasoning:** Since S2 OFF allows (12, 8) to open (based on previous S2 text "Closes East"), and S1 is ON, (12, 8) *should* be open. The current marker might be stale.
- **Realization:** S2 OFF closes the gate at (10, 6), trapping me in the North section.
- **Solution:** There is a Ladder/Warp at (23, 3) labeled "To Underground SE". This likely bypasses the barriers.
- **Plan:** Since S1=ON, S2=OFF, S3=OFF is the configuration to open the East Shutter (12, 8), I will keep the switches as they are and take the ladder at (23, 3) to reach the other side.
- **Correction:** The ladder at (23, 3) on Map 3_54 led back to the Warehouse (Map 3_53) at (22, 27).
- **Current Location:** Warehouse (Map 3_53, SE Section).
- **Insight:** I previously skipped exploring this room to take the ladder. The Director might be HERE.
- **Plan:** Explore the Warehouse maze (West of the ladder) before returning to the switch puzzle.