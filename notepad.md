# Tile Mechanics
- **Shutters:** Act as dynamic walls. State (WALL/FLOOR) toggles based on Switch configuration.
    - **Horizontal 1 (6, 8):** Controlled by Switch 3. (ON=OPEN, OFF=CLOSED).
    - **Horizontal 2 (12, 8):** Controlled by Switch 3. (OFF=OPEN, ON=CLOSED?). *Hypothesis to verify.*
    - **Vertical 2 (10, 6):** Status in 1-ON/2-ON/3-ON unknown.
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
- **Current Status:** Switch 1 ON. Switch 2 ON. Switch 3 ON.
- **Observations:**
    - Vertical 5 (20, 6) was CLOSED in 3-OFF.
- **Hypothesis:** Switch 3 ON opens (6, 8) allowing eastward travel.
- **Plan:**
    1. Verify (6, 8) is OPEN.
    2. Move East.
    3. Check other shutters ((12, 8), (20, 6), etc.).