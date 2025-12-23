# Goldenrod Underground Switch Puzzle

## Switch Logic & Hypotheses
- **Switch 1 (16, 1):**
    - **Hypothesis:** Toggles between East and West paths.
    - **Verified:** 
        - ON opens Inner East Gate `(12, 8)` (and `(16, 10)`), CLOSES `(12, 12)`.
        - OFF opens West Gate `(6, 8)`.
        - **Current State:** OFF.
- **Switch 2 (10, 1):**
    - **Hypothesis:** Main Power / Master Switch.
    - **Verified:** ON opens North Gate `(10, 6)` and powers the secondary gates.
    - **Current State:** ON.
- **Switch 3 (2, 1):**
    - **Hypothesis:** Emergency / Override Switch.
    - **Verified:** 
        - ON opens Emergency shortcuts (`2, 7`) but CLOSES main gates `(10, 6)` & `(6, 8)`.
        - ON opens Shutter `(6, 12)` and CLOSES Shutter `(12, 12)`.
        - OFF CLOSES Shutter `(6, 12)` and OPENS Shutter `(12, 12)`.
    - **Current State:** OFF (Needs to be ON).

## Current Strategy
**Target Config:** S1=OFF, S2=ON, S3=ON.
**Reasoning:**
- S3=ON opens the Emergency Shortcut at `(2, 7)` (Entry to West Room) and the Shutter at `(6, 12)` (Southbound Path).
- S1=OFF is the default "West" setting.
**Steps:**
1. Turn S1 OFF (Done).
2. Turn S3 ON (Next).
3. Enter West Room via `(2, 7)`.
4. Proceed South through `(6, 12)`.

## Lessons Learned
- **Systematic Testing:** Jumping to complex conclusions (like "Outer East vs Inner East") before verifying simple toggles (East vs West) wastes turns. Always test the binary ON/OFF state of a new switch against *all* visible gates first.
- **Visual Confirmation:** "Inferred" states are risky. Always go and look.