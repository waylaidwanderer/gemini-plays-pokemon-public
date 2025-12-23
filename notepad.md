# Map Structure & Route
- **Goldenrod Underground (3_53):** Divided into isolated sections.
  - **Main Tunnel:** Top & West areas. Contains (3, 2) Ladder and (3, 34) Ladder.
  - **Southeast Room:** Isolated. Contains Ladder (22, 27) and Warp (21, 31).
  - **Connection:** Map 3_54 (Warehouse Entrance) connects the Main Tunnel (via 3, 2) and Southeast Room (via 22, 27).
- **Current Location:** Northwest Room (Map 3_54).
- **Goal:** Reach Emergency Switch at (20, 11).

# Strategy
- **Puzzle Mechanic:** "Open one shutter, another closes." Order matters.
- **Sequence Attempt:** 1 -> 2 -> 3.
- **Current Status:** Switch 1 ON. Switch 2 ON. Switch 3 ON (Sequence 1-2-3 Complete).
- **Observations:**
    - Switch 3 ON: Opens Top 1-2 (6, 8) and Bottom 2-3 (12, 12). Closes Top 2-3 (12, 8).
    - Switch 1 ON: Closes Vertical 2 (10, 6/7).
- **Problem:** Need to reach Emergency Switch (Section 4). Path blocked at Top 2-3.
- **Hypothesis:** Switch 2 controls Top 2-3. Turning Switch 2 OFF might open it, allowing access to Switch 1.
- **Plan:**
    1. Turn Switch 2 OFF. Check if Top 2-3 opens.
    2. If Open, go to Switch 1 and turn OFF (to open Vertical 2).
    3. Return to Section 2, go Down via Vertical 2.
    4. Proceed East via Bottom 2-3.

# Important Locations
- **Switch 1:** Map 3_54 (ON).
- **Switch 2:** Map 3_54 (ON).
- **Switch 3:** Map 3_54 (OFF).
- **Emergency Switch:** (20, 11).
- **Eddie:** (3, 8) - West Path Dead End.

# Archive (Completed/Failed)
- **Dept Store Puzzle:** Solved.
- **Blockage:** Path South (Row 10) blocked in all columns with previous configs.
- **West Path:** Confirmed Dead End.
- **Observation:** Turning Switch 1 ON (Step 1) caused tiles (10, 6) and (10, 7) to change from FLOOR to WALL. Middle South Path is now CLOSED.
- **Continuing Sequence:** 1 (ON) -> 2 (ON) -> 3.
- **Verification Note:** Kept Switch 3 ON to visually inspect the path. Pathfinder failed likely due to stale map data.
- **Observation:** Switch 3 ON caused tile (6, 8) to change from WALL to FLOOR, opening a potential path.