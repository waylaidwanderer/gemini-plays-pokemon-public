# Goldenrod Underground Switch Puzzle

## Confirmed Mechanics
- **Switch 1 (16, 1):** Currently OFF.
    - Effect: (20, 6) stays CLOSED. (12, 8) is CLOSED.
- **Switch 2 (10, 1):** Currently ON.
    - Effect: Controls (12, 8) and (10, 6).
- **Switch 3 (2, 1):** Turned ON.
    - Effect: Controls (6, 8), (6, 12), (2, 6).
    - State: OFF -> (6, 8) OPEN, (6, 12) OPEN, (2, 6) OPEN.
    - State: ON -> Testing now.

## Current Goal: Open Shutter (20, 6)
- **Problem:** (20, 6) blocks access to the East Corridor and Emergency Switch.
- **Hypothesis:** Switch 3 might control it.
- **Current Test:** Checking (20, 6) with S1=OFF, S2=ON, S3=ON.

## Status of Critical Shutters
- **(6, 12):** OPEN (Sw3 OFF) - *Path blocked at (2, 6)*.
- **(10, 6):** Unknown (Hypothesis: Sw2 ON opens it).
- **(12, 12):** Unknown.
- **(20, 6):** CLOSED (Sw3 ON/OFF). Testing with Sw1 OFF.