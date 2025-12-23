# Tile Mechanics
- **Shutters:** Act as dynamic walls.
    - **Horizontal 1 (6, 8):** CLOSED (WALL) with Switch 3 OFF. *Hypothesis: Switch 3 ON opens it.*
    - **Horizontal 2 (6, 12):** Status unknown.
    - **Horizontal 3 (12, 8):** Status unknown.
    - **Vertical 5 (20, 6):** CLOSED (WALL) with Switch 3 OFF.

# Map Structure & Route
- **Goldenrod Underground (3_53):** Divided into isolated sections.
  - **Main Tunnel:** Top & West areas.
  - **Southeast Room:** Isolated.
  - **Connection:** Map 3_54 connects Main Tunnel and Southeast Room.
- **Current Location:** Northwest Room (Map 3_54).
- **Goal:** Reach Emergency Switch at (20, 11).

# Strategy
- **Current Status:** Switch 1 ON, Switch 2 ON, Switch 3 OFF.
- **Correction:** Previous attempt to turn Switch 3 ON failed due to input truncation.
- **Plan:**
    1. Turn Switch 3 ON.
    2. Check if (6, 8) opens.
    3. If open, proceed East.
    4. If not, re-evaluate.