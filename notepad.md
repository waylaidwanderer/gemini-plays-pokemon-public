# Goldenrod Underground Switch Puzzle

## Switch Mechanics Log
- **Switch 1 (16, 1):**
    - ON: Opens (12, 8) if S2 is OFF. (Active).
    - OFF: ?
- **Status:** S1=ON, S2=OFF, S3=OFF.
- **Expected Result:** East Shutter (12, 8) OPEN.
- **Switch 2 (10, 1):**
    - ON: Opens Shutter at (10, 6) and (11, 7). AND Opens (6, 8). Closes (12, 8).
    - OFF: Default. Allows S1 to open (12, 8).
- **Current Plan:** Set S1=ON, S2=OFF, S3=OFF to open East Shutter (12, 8).
- **Switch 3 (2, 1):**
    - ON: Opens (6, 8) if S2 is OFF. Closes (12, 8) if S2 is OFF.
    - OFF: ?

## Reflection (Turn 13871)
1. **Immediate Execution:** S1/S2/S3 combo tested. (20, 6) remains CLOSED. Pivot to exploration.
2. **Pathfinding:** `find_path` fails for (20, 12) because intermediate tiles are "unseen". Manual exploration required.
3. **Hypothesis Update:** Access to Emergency Switch (20, 11) is likely via the open shutter at (12, 8), looping south around the internal walls, rather than opening (20, 6) directly.
4. **Status:** S1=ON, S2=OFF, S3=OFF.
   - (12, 8): OPEN.
   - (20, 6): CLOSED.
   - (6, 8): CLOSED (Presumed).

## Current Goal: Explore Southeast Maze to Reach Emergency Switch
- **Status:** At (20, 5). Shutter (20, 6) is closed.
- **Action:** Navigate to (12, 8) and explore the unseen area south of Row 13 to bypass the wall at Col 18.
- **Plan:**
  1. Go to (12, 9).
  2. Explore south/east into the darkness.
  3. Locate path to (20, 12) and Emergency Switch.

## Pathfinding & Strategy
- **Start Turn:** 13766
- **Objective:** Reach Emergency Switch (20, 11).
- **Current Barrier:** Shutter (20, 6) or finding a path around it.
- **Hypothesis:** If (20, 6) is CLOSED with All-ON, then S2 might need to be OFF for *navigation*, but maybe ON for *unlocking*? Or I missed a combination.
- **Next Test:** If All-ON fails, try S1=OFF, S2=ON, S3=ON.

## Discrepancies & Errors
- **Corrected:** Position mismatch in T13754. Turn count mismatches in T13756, T13762.
- **Lesson:** Always verify `num_turns` and `current_position` against Game State, not just memory. Visual verification of shutters is required before pathing.
- **Obstacle:** Rocket Grunt found at (3, 2) blocking the direct path to Switch 3.
- **Detour:** Moving around via Row 3. Expecting potential battle if he spots me.
- **Correction:** Row 2 is blocked at (19, 2). Must use Row 4 to cross East-West.
- **Plan Update:** From (20, 2), go Down to (20, 4), Left to (16, 4), Down to (16, 8), West to (12, 8), South to explore.
- **Observation:** Moving West on Row 9 triggered a map change. (6, 9) is now WALL (blocked). (6, 12) is now FLOOR (open).
- **Hypothesis:** A trigger on Row 9 or the S1=ON state controls these toggles.
- **Current Situation:** Trapped in Central Room (Cols 7-17). Need to find exit East to reach Emergency Switch.
- **Plan:** Inspect East Wall at (18, 9) for a passage.