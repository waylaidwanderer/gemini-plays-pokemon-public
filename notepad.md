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
- **Current Status:** Switch 1 ON. Switch 2 ON. Switch 3 OFF.
- **Goal:** Check Vertical 5 (20, 6).
- **Plan:**
    1. Navigate to (20, 6).
    2. Check if Vertical 5 is open.
    3. If open, proceed South to Emergency Switch.
    4. If closed, consider Switch 3 ON (Config: 1-ON, 2-ON, 3-ON).