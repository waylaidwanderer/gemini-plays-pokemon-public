# Tile Mechanics
- **Shutters:** Act as dynamic walls. State (WALL/FLOOR) toggles based on Switch configuration.
    - **Top 1-2 (6, 8):** Controlled by Switch 3. (ON=OPEN, OFF=CLOSED). *Wait, previous note said Switch 3 OFF caused it to CLOSE. So ON=OPEN? Need to re-verify if needed, but currently irrelevant.*
    - **Top 2-3 (12, 8):** Controlled by Switch 3. (OFF=OPEN).
    - **Vertical 2 (10, 6):** Closed in 1-ON/2-OFF/3-OFF config.
    - **Row 10 Shutters:**
        - (11, 10): OPEN (FLOOR) in 1-ON/2-OFF/3-OFF config.

# Map Structure & Route
- **Goldenrod Underground (3_53):** Divided into isolated sections.
  - **Main Tunnel:** Top & West areas. Contains (3, 2) Ladder and (3, 34) Ladder.
  - **Southeast Room:** Isolated. Contains Ladder (22, 27) and Warp (21, 31).
  - **Connection:** Map 3_54 (Warehouse Entrance) connects the Main Tunnel (via 3, 2) and Southeast Room (via 22, 27).
- **Current Location:** Northwest Room (Map 3_54).
- **Goal:** Reach Emergency Switch at (20, 11).

# Strategy
- **Puzzle Mechanic:** "Open one shutter, another closes." Order matters.
- **Current Status:** Switch 1 ON. Switch 2 OFF. Switch 3 OFF.
- **Observations:**
    - Vertical 4 (16, 6) is OPEN.
    - Shutter (12, 8) is OPEN.
    - Shutter (11, 10) is OPEN.
    - Shutter (12, 12) is CLOSED (Blocks path East from Middle Section).
- **New Hypothesis:** The Emergency Switch at (20, 11) is reached via the Far East Strip (Column 20).
- **Plan:**
    1. Navigate to Far East Strip via Row 4 crossing (18, 4).
    2. Inspect Vertical Shutter/Wall at (20, 6).
    3. If (20, 6) is open, proceed South to (20, 11).
    4. If closed, inspect Column 18 walls (18, 8) or (18, 12) for openings.