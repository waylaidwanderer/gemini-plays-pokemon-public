# Tile Mechanics
- **Shutters:** Act as dynamic walls.
    - **Horizontal 1 (6, 8):** CLOSED (WALL) with Switch 3 ON.
    - **Horizontal 2 (6, 12):** OPEN (FLOOR) with Switch 3 ON.
    - **Horizontal 3 (12, 8):** OPEN (FLOOR) with Switch 3 ON.
    - **Vertical 5 (20, 6):** Status in 3-ON unknown.

# Map Structure & Route
- **Goldenrod Underground (3_53):** Divided into isolated sections.
  - **Main Tunnel:** Top & West areas.
  - **Southeast Room:** Isolated.
  - **Connection:** Map 3_54 connects Main Tunnel and Southeast Room.
- **Current Location:** Northwest Room (Map 3_54).
- **Goal:** Reach Emergency Switch at (20, 11).

# Strategy
- **Current Status:** All Switches (1, 2, 3) ON.
- **Observation:** (6, 8) is CLOSED. Cannot go East.
- **Deduction:** Switch 3 ON closes (6, 8).
- **Plan:**
    1. Turn Switch 3 OFF to open (6, 8).
    2. Cross to Middle Area (x=7-11).
    3. Access Switch 2 at (10, 1).
    4. Manipulate switches to open path to East Area (x>12) via (12, 8).