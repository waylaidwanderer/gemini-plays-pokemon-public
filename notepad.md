# Goldenrod Underground Switch Puzzle

## Switch Logic (Verified)
- **S1 (16, 1):** Toggles East/West.
    - **ON:** Inner East `(12, 8)` OPEN. West `(6, 8)` CLOSED.
    - **OFF:** West `(6, 8)` OPEN. Inner East `(12, 8)` CLOSED.
    - **Current:** OFF.
- **S2 (10, 1):** Main Power.
    - **ON:** Powers gates.
    - **OFF:** Cutting power (Current Test).
    - **Current:** OFF.
- **S3 (2, 1):** Emergency Override.
    - **ON:** Opens `(2, 7)` & `(6, 12)`. Closes main gates.
    - **OFF:** Standard operation.
    - **Current:** ON.

## Current Strategy
**Goal:** Rescue Director.
**Hypothesis:** "Fail-Safe Mode" (S2=OFF).
- Does cutting Main Power (S2=OFF) unlock the "Walls" blocking the West Room at Row 10?
- **Status:** I am at `(2, 7)` (West Shortcut is OPEN).
- **Next Step:** Proceed South to Row 10 to see if the wall at `(2, 10)` has opened.

## Exploration Notes
- **West Room (Col 2):** Previously blocked at Row 10 (S2=ON). Pharmacist at `(4, 8)`.
- **Inner East (Col 12):** Blocked at `(12, 12)` with S3=ON.
- **Outer East (Col 20):** Shutter `(20, 6)` closed (checked with S2=OFF).