# Goldenrod Underground Switch Puzzle

## Switch Logic & Hypotheses
- **Switch 1 (16, 1):**
    - **Hypothesis:** Toggles between East and West paths.
    - **Verified:** 
        - ON opens Inner East Gate `(12, 8)`.
        - OFF opens West Gate `(6, 8)`.
- **Switch 2 (10, 1):**
    - **Hypothesis:** Main Power / Master Switch.
    - **Verified:** ON opens North Gate `(10, 6)` and powers the secondary gates.
- **Switch 3 (2, 1):**
    - **Hypothesis:** Emergency / Override Switch.
    - **Verified:** 
        - ON opens Emergency shortcuts but overrides and CLOSES the main gates `(10, 6)` and `(6, 8)`.
        - ON opens Shutter `(6, 12)` and CLOSES Shutter `(12, 12)`.
        - OFF CLOSES Shutter `(6, 12)` and OPENS Shutter `(12, 12)`.

## Current Strategy
**Goal:** Rescue Director.
**Current Config:** S1=OFF, S2=ON, S3=OFF.
**Status:** 
- North Gate `(10, 6)` is OPEN.
- West Gate `(6, 8)` is OPEN.
- Shutter `(6, 12)` is CLOSED.
- Shutter `(12, 12)` is OPEN.
**Analysis:**
- Current config gives access to West Room `(6, 8)` but blocks progress at `(6, 12)`.
- **New Plan:** Set **S1=ON, S2=ON, S3=OFF**.
    - S1=ON opens `(12, 8)`.
    - S3=OFF keeps `(12, 12)` OPEN.
    - This should create a clear path South through the Inner East corridor.
**Objective:** Verify West Room dead end, then switch S1 to ON and explore Inner East path.
## Lessons Learned
- **Systematic Testing:** Jumping to complex conclusions (like "Outer East vs Inner East") before verifying simple toggles (East vs West) wastes turns. Always test the binary ON/OFF state of a new switch against *all* visible gates first.
- **Visual Confirmation:** "Inferred" states are risky. Always go and look.

## Session Log
- **Start:** Turn 14495 (Exploring Inner East Path).
- **Hypothesis:** S1=ON opens Gate (12, 8). S3=OFF leaves Shutter (12, 12) open.
- **Turn 14496:** S1 confirmed ON. Navigating to Inner East Gate (12, 8) and Shutter (12, 12).
- **Pathing Update:** Direct access to Inner East path from North (Col 12, Row 4) is blocked by walls at (12, 6-7). Must enter via Central Gate (10, 6) and loop East at Row 8.
- **Observation (Turn 14499):** System reported `(16, 10)` changed WALL -> FLOOR when S1 turned ON. This suggests a path might open at Col 16.
- **Hypothesis:** S1=ON opens (12, 8) and (16, 10). Need to check if it also opens (12, 10) or (16, 11) to allow southward progress.
- **Observation (Turn 14503):** System reported `(12, 12)` changed FLOOR -> WALL.
- **Revised Hypothesis:** S1=ON opens `(12, 8)` and `(16, 10)`, but CLOSES `(12, 12)`.
- **Conclusion:** Inner East Path (Column 12) is blocked. Must proceed down Column 16.