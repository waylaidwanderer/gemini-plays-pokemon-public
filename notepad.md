# Goldenrod Underground Switch Puzzle

## Confirmed Mechanics
- **Switch 1 (16, 1):** Currently OFF.
    - Effect: (20, 6) stays CLOSED. (12, 8) is CLOSED.
- **Switch 2 (10, 1):** Currently ON.
    - Effect: Controls (12, 8) and (10, 6).
- **Switch 3 (2, 1):** Turned OFF.
    - Effect: Controls (6, 8), (6, 12), (2, 6), (10, 6), (12, 8).
    - State: OFF -> (10, 6) OPEN, (12, 8) CLOSED.
    - Note: Assuming (2, 6) is OPEN.

## Current Goal: Test Switch 2
- **Action:** Move to Switch 2 (10, 1) and turn it OFF.
- **Hypothesis:** Switch 2 might control the locking mechanism for the outer doors or the East shutter (20, 6).
- **Plan:**
    1. Turn S3 OFF (Done).
    2. Turn S2 OFF.
    3. Check shutters (especially (20, 6)).
    4. Try S3 ON with S2 OFF.

## Status of Critical Shutters
- **(6, 12):** OPEN (Sw3 OFF) - *Path blocked at (2, 6)*.
- **(10, 6):** Unknown (Hypothesis: Sw2 ON opens it).
- **(12, 12):** Unknown.
- **(20, 6):** CLOSED (Sw3 ON/OFF). Testing with Sw1 OFF.