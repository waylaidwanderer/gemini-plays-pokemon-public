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
    - **Current State:** OFF.
- **Switch 3 (2, 1):**
    - **Hypothesis:** Emergency / Override Switch.
    - **Verified:** 
        - ON opens Emergency shortcuts (`2, 7`) but CLOSES main gates `(10, 6)` & `(6, 8)`.
        - ON opens Shutter `(6, 12)` and CLOSES Shutter `(12, 12)`.
        - OFF CLOSES Shutter `(6, 12)` and OPENS Shutter `(12, 12)`.
    - **Current State:** ON.

## Current Strategy
**Target Config:** S1=OFF, S2=OFF, S3=ON.
**Reasoning:**
- Testing "Emergency Power Only" mode.
- If S2 (Main Power) is OFF, but S3 (Emergency) is ON, maybe the Outer East Shutter `(20, 6)` opens.
**Steps:**
1. Turn S2 OFF.
2. Navigate to `(20, 6)` to check status.
3. If closed, check `(6, 12)` to see if Emergency Power maintains the West route.

## Exploration Notes
- **West Room (Col 2):** Blocked at Row 10. Pharmacist at `(4, 8)`.
- **Inner East (Col 12):** Blocked at `(12, 12)` with S3=ON.
- **West Gate (Col 6):** Blocked at `(6, 8)` with S3=ON.
- **Outer East (Col 20):** Shutter `(20, 6)` closed with S1=OFF, S2=ON, S3=ON.