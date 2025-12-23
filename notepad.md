# Goldenrod Underground Switch Puzzle

## Switch Logic & Hypotheses
- **Switch 1 (16, 1):**
    - **Hypothesis:** Toggles between Inner East `(12, 8)` and Outer East `(20, 6)` paths?
    - **Verified:** ON opens Inner East `(12, 8)` (Confirmed). OFF closes it.
- **Switch 2 (10, 1):**
    - **Hypothesis:** Main Power / Master Switch.
    - **Verified:** ON opens North Gate `(10, 6)` and West Gate `(6, 8)`. OFF closes them.
- **Switch 3 (2, 1):**
    - **Hypothesis:** Emergency / Override Switch.
    - **Verified:** ON opens Emergency shortcuts (e.g. `(2, 7)`) but overrides and CLOSES the main gates `(10, 6)` and `(6, 8)`.

## Current Strategy
**Goal:** Rescue Director.
**Current Config:** S1=OFF, S2=ON, S3=OFF.
**Hypothesis:**
- S2=ON provides power (Opening gates).
- S3=OFF removes the emergency lock (Opening normal paths).
- S1=OFF selects the **Outer East Path** (Since S1=ON selected Inner).
**Objective:** Navigate to `(20, 5)` and inspect the Outer East Shutter at `(20, 6)`.
**Contingency:** If `(20, 6)` is still closed, the only untried combination for S3=OFF is `S1=ON, S2=ON, S3=OFF`. But that opened `(12, 8)`.
So if S1=OFF, S2=ON, S3=OFF doesn't open `(20, 6)`, then S1 is not a simple toggle.

## Exploration Status
- **Inner East Path (12, 8):** Dead end (blocked by walls south of row 9).
- **West Path (via 2, 7 with S3=ON):** Leads to Pharmacist (4, 8) who says "Nothing down there". Dead end?
- **Outer East Path (20, 6):** Currently the main target. Contains Emergency Switch `(20, 11)` and Door `(22, 10)`.