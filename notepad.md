# Tile Mechanics
- **Shutters:** Dynamic walls controlled by switches.
    - **Row 8 Shutters:**
        - (6, 8): OPEN (Sw3 ON). CLOSED (Sw3 OFF).
        - (12, 8): Status unknown.
    - **Row 12 Shutters:**
        - (6, 12): CLOSED (Sw3 ON). OPEN (Sw3 OFF).
    - **Vertical Shutters:**
        - (20, 6): CLOSED (Sw3 OFF).
        - (10, 6): OPEN (Sw1 ON, Sw2 ON, Sw3 OFF).

# Map Structure
- **Goldenrod Underground (3_53):**
  - **Main Tunnel:** Top & West.
  - **Southeast Room:** Isolated.
- **Switch Room (3_54):**
  - **Northwest (Current):** Access to Switch 3.
  - **Middle:** Access to Switch 2.
  - **Northeast:** Access to Switch 1.
  - **South:** Warehouse area.
  - **Goal:** Reach Emergency Switch at (20, 11).

# Current State
- **Switch 1:** ON
- **Switch 2:** ON (Verified).
- **Switch 3:** ON (Verified).
- **Shutter (6, 8):** OPEN.
- **Shutter (12, 8):** CLOSED.
- **Shutter (6, 12):** CLOSED (Inferred from Sw3 ON).
- **Shutter (12, 12):** FLOOR (Open?) based on XML.

# Strategy
- **Issue:** Cannot reach East Section from Middle because (12, 8) is closed and Row 10/11 are blocked.
- **New Hypothesis:** The path to the East is via the **South** route (Row 12).
- **Plan:**
    1. Return to West Section (via open 6, 8).
    2. Turn Switch 3 **OFF**.
       - This should CLOSE (6, 8) and OPEN (6, 12).
    3. Go South through (6, 12).
    4. Travel East along Row 12 to cross (12, 12) into East Section.
    5. Reach Emergency Switch.