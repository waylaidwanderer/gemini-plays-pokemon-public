# Goldenrod Underground Switch Puzzle

## Current Status
- **Location:** Switch Room (3_54), Central Area.
- **Objective:** Explore Inner East Section.
- **Goal:** Rescue Director / Find Warehouse.

## Switch Logic (Confirmed)
- **S1 (16, 1):** East/West Toggle.
    - **ON:** Opens Inner East Gate `(12, 8)` & `(12, 9)`. Closes West Gate `(6, 8)` & `(6, 9)`.
    - **OFF:** Opens West Gate `(6, 8)` & `(6, 9)`. Closes Inner East Gate `(12, 8)` & `(12, 9)`.
- **S2 (10, 1):** Main Power.
    - **ON:** Required for gates to operate. (Currently ON).
- **S3 (2, 1):** Emergency Override.
    - **OFF:** (Currently OFF).
- **Shutters:** `(17, 6)` and `(20, 6)` remain CLOSED with S1=ON/S2=ON/S3=OFF.

## Plan
1. Enter Inner East Room via `(12, 8)`.
2. Explore for path to Warehouse or Switch `(17, 10)`.
3. If dead end, try S1=OFF for West Room path.