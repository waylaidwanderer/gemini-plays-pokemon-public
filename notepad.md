# Goldenrod Underground Switch Puzzle

## Confirmed Mechanics
- **Switch 1 (16, 1):** Currently OFF.
    - Effect: (20, 6) stays CLOSED. (12, 8) is CLOSED.
- **Switch 2 (10, 1):** Currently ON.
    - Effect: Controls (12, 8) and (10, 6).
- **Switch 3 (2, 1):** Currently ON.
    - Effect: Controls (6, 8), (6, 12), (2, 6), (10, 6), (12, 8).
    - State: ON -> (10, 6) CLOSED, (12, 8) OPEN, (20, 6) CLOSED.
    - **Confirmed:** S3 ON opens the inner path (12, 8) but closes the outer paths (2, 6) & (10, 6).

## Current Goal: Test Switch 2
- **Problem:** S3 ON traps me in the North.
- **Action:** Turn S3 OFF (to escape).
- **Next:** Go to Switch 2 and turn it OFF.
- **Hypothesis:** Switch 2 might control the locking mechanism for the outer doors or the East shutter (20, 6).
- **Plan:** S1=OFF, S2=OFF, S3=OFF (Baseline check). Then try S3 ON with S2 OFF.

## Status of Critical Shutters
- **(6, 12):** OPEN (Sw3 OFF) - *Path blocked at (2, 6)*.
- **(10, 6):** Unknown (Hypothesis: Sw2 ON opens it).
- **(12, 12):** Unknown.
- **(20, 6):** CLOSED (Sw3 ON/OFF). Testing with Sw1 OFF.