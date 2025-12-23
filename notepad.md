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
**New Plan:** Flank via Ladder.
- The direct paths South (Cols 12, 16, 17) have proven difficult/blocked or require specific switch combos I haven't perfectly nailed down or traversed.
- **Ladder at (23, 3)** provides an alternative route to the Southeast section.
- **Status:** S1=OFF, S2=ON, S3=OFF.
- **Next Step:** Take Ladder at (23, 3).