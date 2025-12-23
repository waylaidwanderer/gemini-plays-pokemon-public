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
1. Turn S1 OFF.
2. Enter West Room via `(6, 8)`.
3. Explore West Room for hidden paths or switches.
4. Check if Emergency Switch `(20, 11)` is accessible from West Room (unlikely).

## Exploration Notes
- **Inner East (Col 12):** Explored. Dead End.
    - Path `(12, 8)` -> `(17, 9)` contains no switches or items.
    - Walls checked. No hidden switches.
- **Switch (17, 10):** Does not exist (verified by XML scan).