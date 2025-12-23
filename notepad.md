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
    - **Verified:** ON opens Emergency shortcuts but overrides and CLOSES the main gates `(10, 6)` and `(6, 8)`.

## Current Strategy
**Goal:** Rescue Director.
**Current Config:** S1=OFF, S2=ON, S3=OFF.
**Status:** 
- North Gate `(10, 6)` is OPEN.
- West Gate `(6, 8)` is OPEN.
**Objective:** Enter the West Room via `(10, 6)` -> `(6, 8)` and explore the deep South area.
**Reasoning:** The West Room connects to the southern part of the map which has not been fully explored. The Pharmacist's claim ("Nothing down there") likely refers to the immediate dead end, but the room extends further South.