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
- **Switch 2:** OFF (Verified).
- **Switch 3:** ON (Verified).
- **Shutter (6, 8):** OPEN.
- **Shutter (12, 8):** CLOSED.
- **Shutter (6, 12):** CLOSED (Inferred from Sw3 ON).
- **Shutter (12, 12):** FLOOR (Open?) based on XML.

# Strategy
- **Goal:** Reach East Section via South Route.
- **Plan:**
    1. Navigate to Switch 3 at (2, 2).
    2. Turn Switch 3 **OFF**.
       - This should CLOSE (6, 8) and OPEN (6, 12).
    3. Go South to Row 12.
    4. Travel East through (6, 12) along Row 12.
    5. Cross (12, 12) into East Section.
    6. Reaching Emergency Switch at (20, 11).