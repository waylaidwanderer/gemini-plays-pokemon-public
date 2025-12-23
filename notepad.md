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
- **Current Status:** Switch 1 OFF. Switch 2 OFF. Switch 3 ON.
- **Observations:**
    - Vertical 2 (10, 6) CLOSED.
    - Vertical 3 (12, 6) CLOSED.
    - Top 1-2 (6, 8) CLOSED.
    - Top 2-3 (12, 8) OPEN (Visible on screen).
- **Hypothesis:** Need to open a Vertical Shutter (2 or 3) to reach the open horizontal path.
- **Plan:**
    1. Turn Switch 1 ON (Test Config: 1 ON, 2 OFF, 3 ON).
    2. Check Vertical 2 (10, 6) and Vertical 3 (12, 6).

# Important Locations
- **Switch 1:** Map 3_54 (ON).
- **Switch 2:** Map 3_54 (ON).
- **Switch 3:** Map 3_54 (OFF).
- **Emergency Switch:** (20, 11).
- **Eddie:** (3, 8) - West Path Dead End.

# Archive (Completed/Failed)
- **Blockage:** Path South (Row 10) blocked in all columns with previous configs.
- **West Path:** Confirmed Dead End.
- **Switch History:**
    - Sw 1 ON: Closes Vertical 2 (10, 6/7).
    - Sw 3 ON: Opens Top 1-2 (6, 8) & Bottom 2-3 (12, 12). Closes Top 2-3 (12, 8).