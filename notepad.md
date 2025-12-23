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
    - **Current State:** ON.

## Current Strategy
**Goal:** Rescue Director.
**Current Config:** S1=OFF, S2=ON, S3=ON.
**Hypothesis:** This config (Emergency Mode + West Select) might open the Outer East Shutter `(20, 6)`.
**Reasoning:**
- S3=ON closes the main gates but opens emergency routes.
- `(20, 6)` might be the "Outer East" emergency route leading to the Emergency Switch `(20, 11)`.
**Objective:** Navigate to `(20, 6)` and check if it's OPEN.
- If OPEN: Proceed to `(20, 11)` (Emergency Switch).
- If CLOSED: Re-evaluate switch logic.

## Exploration Notes
- **West Room (Col 2):** Blocked at Row 10 by walls. Pharmacist at `(4, 8)` says "Nothing down there".
- **Inner East (Col 12):** Blocked at `(12, 12)` when S3=ON (or maybe S1=OFF?).
- **West Gate (Col 6):** Blocked at `(6, 8)` when S3=ON.