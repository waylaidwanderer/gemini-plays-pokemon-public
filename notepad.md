# Goldenrod Underground Switch Puzzle

## Confirmed Mechanics
- **Switch 1 (16, 1):** Currently OFF.
    - Effect: Unknown. Testing if it controls (20, 6) or (12, 12).
- **Switch 2 (10, 1):** Currently ON.
    - Effect: Controls (12, 8) and (10, 6).
- **Switch 3 (2, 1):** Currently OFF.
    - Effect: Controls (6, 8), (6, 12), (2, 6).
    - State: OFF -> (6, 8) CLOSED, (6, 12) OPEN, (2, 6) CLOSED.

## Current Goal: Test Switch 1
- **Action:** Toggle Switch 1 to OFF.
- **Next:** Check Shutter (20, 6).
- **Hypothesis:** Sw1 OFF + Sw2 ON + Sw3 OFF -> Opens (20, 6)?

## Status of Critical Shutters
- **(6, 12):** OPEN (Sw3 OFF) - *Path blocked at (2, 6)*.
- **(10, 6):** Unknown (Hypothesis: Sw2 ON opens it).
- **(12, 12):** Unknown.
- **(20, 6):** CLOSED (Sw3 ON/OFF). Testing with Sw1 OFF.