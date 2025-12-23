# Goldenrod Underground Switch Puzzle

## Confirmed Mechanics
- **Switch 1 (16, 1):** Currently OFF.
    - Effect: (20, 6) stays CLOSED. (12, 8) is CLOSED.
- **Switch 2 (10, 1):** Currently ON.
    - Effect: Controls (12, 8) and (10, 6).
- **Switch 3 (2, 1):** Turned ON.
    - Effect: Controls (6, 8), (6, 12), (2, 6).
    - State: ON -> (10, 6) CLOSED, (12, 8) OPEN, (20, 6) CLOSED.
    - **CRITICAL:** S3 ON opens the inner path (12, 8) but closes the outer paths south (2, 6) & (10, 6), trapping me in the North.

## Current Goal: Test Switch 2
- **Problem:** I need to access the South area AND pass through (12, 8). S3 ON blocks entry.
- **Hypothesis:** Switch 2 might modify which doors S3 affects, or control the outer doors independently.
- **Action:** Turn S3 OFF (to escape trap), then Turn Switch 2 OFF.
- **Next Test:** Check shutters with S1=OFF, S2=OFF, S3=OFF.

## Status of Critical Shutters
- **(6, 12):** OPEN (Sw3 OFF) - *Path blocked at (2, 6)*.
- **(10, 6):** Unknown (Hypothesis: Sw2 ON opens it).
- **(12, 12):** Unknown.
- **(20, 6):** CLOSED (Sw3 ON/OFF). Testing with Sw1 OFF.