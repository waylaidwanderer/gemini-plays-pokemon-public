# Goldenrod Underground Switch Puzzle

## Confirmed Mechanics
- **Switch 1 (16, 1):** Currently ON.
    - Effect: Unknown. Hypothesis: Controls (12, 12).
- **Switch 2 (10, 1):** Currently ON.
    - Effect: Controls (12, 8) and (10, 6).
- **Switch 3 (2, 1):** Currently OFF.
    - Effect: Controls (6, 8), (6, 12), (2, 6).
    - State: OFF -> (6, 8) CLOSED, (6, 12) OPEN, (2, 6) CLOSED.

## Current Goal: Access Row 12 (South)
- **Target:** Emergency Switch at (20, 11).
- **Current Strategy:** Middle Path (Column 10).
    - Check Shutter at (10, 6).
    - If OPEN: Proceed South to (12, 12).
    - If CLOSED: Toggle Switch 2 (OFF).

## Status of Critical Shutters
- **(6, 12):** OPEN (Sw3 OFF) - *Path blocked at (2, 6)*.
- **(10, 6):** Unknown (Checking).
- **(12, 12):** Unknown (Hypothesis: Sw1 ON opens).
- **(20, 6):** CLOSED (Sw3 ON/OFF).