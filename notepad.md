# Goldenrod Underground Switch Puzzle

## Switch Logic (Verified)
- **S1 (16, 1):** Toggles East/West.
    - **ON:** Closes `(17, 10)`. Opens `(12, 8)`.
    - **OFF:** Opens `(6, 8)` (West). Should OPEN `(17, 10)`.
    - **Current:** OFF.
- **S2 (10, 1):** Main Power.
    - **ON:** Powers gates.
    - **OFF:** Fail-Safe Test Failed.
    - **Current:** ON.
- **S3 (2, 1):** Emergency Override.
    - **ON:** Emergency Mode.
    - **OFF:** Standard Mode.
    - **Current:** OFF.

## Current Strategy
**Goal:** Rescue Director.
**Hypothesis:** S1=OFF, S2=ON, S3=OFF opens `(17, 10)`.
**Reasoning:**
- With S1=ON, `(17, 10)` is a WALL (Closed).
- Therefore, S1 must be OFF to open it.
- This config also opens West `(6, 8)`, but we know that's a dead end.
- Perhaps S1=OFF opens *both* West and Middle East?

**Steps:**
1. Navigate to Switch 1.
2. Turn S1 OFF.
3. Navigate to `(17, 10)` to verify it opens.