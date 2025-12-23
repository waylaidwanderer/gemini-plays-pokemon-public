# Goldenrod Underground Switch Puzzle

## Switch Logic (Verified)
- **S1 (16, 1):** Toggles East/West.
    - **ON:** Should open `(16, 10)` based on Turn 14499. Retesting now.
    - **OFF:** West `(6, 8)` OPEN. Inner East `(12, 8)` CLOSED.
    - **Current:** ON.
- **S2 (10, 1):** Main Power.
    - **ON:** Powers gates.
    - **OFF:** Fail-Safe Test Failed (Row 10 Wall solid).
    - **Current:** OFF.
- **S3 (2, 1):** Emergency Override.
    - **ON:** Opens `(2, 7)` & `(6, 12)`. Closes main gates.
    - **OFF:** Standard operation.
    - **Current:** OFF.

## Current Strategy
**Goal:** Rescue Director.
**New Hypothesis:** "Standard East Mode" (Column 16 Path).
- Observations suggest S1=ON opens a path at Column 16 (`16, 10` opened).
- S3 needs to be OFF to allow normal gate operation.
- S2 needs to be ON to power the gates.
**Target Config:** S1=ON, S2=ON, S3=OFF.

**Steps:**
1. Turn S3 OFF (Done).
2. Turn S2 ON (Next).
3. Turn S1 ON.
4. Navigate South via Column 16.

## Exploration Notes
- **West Room (Col 2):** Blocked at Row 10.
- **Inner East (Col 12):** Blocked at `(12, 12)` when S1=ON.
- **Middle East (Col 16):** Path likely exists here.