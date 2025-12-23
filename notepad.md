# Goldenrod Underground Switch Puzzle
**Current Turn:** 13558 (Reflection)

## Confirmed Mechanics
- **Switch 1 (16, 1):** Currently ON.
    - Effect: Unknown. Hypothesis: Controls (12, 12).
- **Switch 2 (10, 1):** Currently ON.
    - Effect: Controls (12, 8) and (10, 6).
    - Ambiguity: Does ON open or close (10, 6)?
- **Switch 3 (2, 1):** Currently OFF.
    - Effect: Controls (6, 8), (6, 12), (2, 6).
    - State: OFF -> (6, 8) CLOSED, (6, 12) OPEN, (2, 6) CLOSED.

## Current Goal: Access Row 12
- The Emergency Switch is at (20, 11). Access is likely from the South (Row 12).
- Row 12 is blocked from the North by shutters at (6, 12), (10, ?), (12, 12), (20, ?).
- **Path 1 (West):** Through (6, 12). Requires (2, 6) open to reach it. FAILED (Sw3 OFF closes 2,6).
- **Path 2 (Middle):** Through (10, 6). Requires Sw2 correct state.
    - Plan: Check (10, 6). If open, go South. If closed, toggle Sw2.
- **Path 3 (East):** Through (20, 6). FAILED (Closed with Sw3 ON/OFF).

## Next Steps
1. Navigate to (10, 6).
2. If blocked, Toggle Switch 2 (Turn OFF).
3. If open, proceed to (12, 12).
4. If (12, 12) blocked, Toggle Switch 1.