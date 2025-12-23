# Goldenrod Underground Switch Puzzle

## Current Status
- **Location:** Switch Room (3_54), Central Area.
- **Objective:** Explore Inner East Section.
- **Goal:** Rescue Director / Find Warehouse.

## Switch Logic (Confirmed)
- **S1 (16, 1):** East/West Toggle.
    - **ON:** Opens East Gate `(12, 8)`. Closes West Gate `(6, 8)`.
    - **OFF:** Opens West Gate `(6, 8)`. Closes East Gate `(12, 8)`.
    - **Current State:** OFF. West Gate `(6, 8)` is OPEN. (Verified Turn 14797).
- **S2 (10, 1):** Main Power.
    - **ON:** Required for gates to operate. (Currently ON).
- **S3 (2, 1):** Emergency Override.
    - **OFF:** (Currently OFF).
- **Shutters:** `(17, 6)` and `(20, 6)` remain CLOSED with S1=ON/S2=ON/S3=OFF.

## Plan
1. Navigate to Switch 3 `(2, 1)` via `(3, 9)` -> `(3, 8)`.
2. Turn S3 ON.
3. Observe effects (check for sound or message).
4. Return to Switch Room center and check shutters `(17, 6)` and `(20, 6)`.

## Observations
- **West Room:**
    - Pharmacist at `(4, 8)` blocking `(5, 8)` to `(3, 8)` direct path? No, can go via `(4, 9)`.
    - South path blocked by walls at Row 10/11.
    - Path North to `(2, 1)` is open.
- **Switch 3 (2, 1):** Emergency Override. Currently OFF.