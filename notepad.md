# Tile Mechanics
- **Shutters:** Dynamic walls controlled by switches.
    - **Row 8 Shutters:**
        - (6, 8): CLOSED (Sw3 OFF). Hypothesis: Opens with Sw3 ON.
        - (12, 8): Status unknown.
    - **Row 12 Shutters:**
        - (6, 12): OPEN (Sw3 OFF). Hypothesis: Closes with Sw3 ON.
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
- **Switch 3:** OFF (Verified via text and shutter state).
- **Correction:** In Turn 13445, the attempt to turn Sw3 ON failed. Thus, observations from 13446-13450 were with Sw3 OFF.

# Strategy
1. Battle Burglar at (3, 8) to clear path.
2. Turn Switch 3 **ON**.
3. Verify Shutter at (6, 8) opens.
4. Proceed East to Middle Section.