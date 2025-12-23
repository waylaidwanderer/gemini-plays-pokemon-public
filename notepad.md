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
- **Switch 2:** OFF (Turning ON to test).
- **Switch 3:** ON (Verified).
- **Shutter (6, 8):** OPEN (Verified).
- **Shutter (12, 8):** CLOSED with Sw2 OFF (Verified).

# Strategy
1. Turn Switch 2 ON.
2. Check Shutter at (12, 8).
   - If OPEN: Proceed East.
   - If CLOSED: This implies neither Sw2 ON nor OFF opens it alone. Might need Sw1 toggled? Or Sw3?
   - Hypothesis: Sw2 ON should open it.