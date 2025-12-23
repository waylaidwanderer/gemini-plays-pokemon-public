# Tile Mechanics
- **Shutters:** Act as dynamic walls.
    - **Horizontal 1 (6, 8):** CLOSED (WALL) with Switch 3 ON.
    - **Horizontal 2 (6, 12):** OPEN (FLOOR) with Switch 3 ON.
    - **Horizontal 3 (12, 8):** OPEN (FLOOR) with Switch 3 ON.
    - **Vertical 5 (20, 6):** Status in 3-ON unknown (was closed in 3-OFF).

# Map Structure & Route
- **Goldenrod Underground (3_53):** Divided into isolated sections.
  - **Main Tunnel:** Top & West areas.
  - **Southeast Room:** Isolated.
  - **Connection:** Map 3_54 connects Main Tunnel and Southeast Room.
- **Current Location:** Northwest Room (Map 3_54).
- **Goal:** Reach Emergency Switch at (20, 11).

# Strategy
- **Current Status:** All Switches (1, 2, 3) ON.
- **New Path:**
    - Switch 3 ON opened (6, 12).
    - Navigate South to Row 12, Cross (6, 12).
    - Bypass Burglar at (9, 12) via Row 13.
    - Head North via column 10/11 to Row 8.
    - Cross (12, 8) to reach East side.
- **Plan:**
    1. Navigate to (8, 12).
    2. Go around Burglar.
    3. Check (12, 8) and (20, 6).