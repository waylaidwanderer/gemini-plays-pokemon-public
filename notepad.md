# Tile Mechanics
- **Shutters:** Dynamic walls controlled by switches.
    - **Row 8 Shutters:**
        - (6, 8): CLOSED (Sw3 OFF). Hypothesis: Opens with Sw3 ON.
        - (12, 8): Status unknown.
    - **Row 12 Shutters:**
        - (6, 12): OPEN (Sw3 ON).
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
- **Switch 2:** ON
- **Switch 3:** Pending Verification (Target: ON)

# Strategy
1. Verify Switch 3 is ON.
2. Check Shutter at (6, 8).
   - If OPEN: Go East to Middle Section.
   - If CLOSED: Re-evaluate logic (maybe Sw2/1 interference?).