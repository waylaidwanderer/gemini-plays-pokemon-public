# Goldenrod Underground Switch Puzzle

## Current Status
- **Location:** Goldenrod Underground (Map 3_53), SE Section `(22, 27)`.
- **Context:** I took the ladder at `(23, 3)` in the Switch Room (`3_54`).
- **Goal:** Rescue Director (Likely back in `3_54`).
- **Hypothesis:** The ladder might have been an exit/shortcut *out* of the puzzle area, not a path *to* the Director.
- **Immediate Plan:** Explore this small SE section. If it leads to the main tunnel (exit), return up the ladder to `3_54` and solve the Switch Puzzle.

## Switch Logic (Verified in 3_54)
- **Timestamp:** Turn 14690.
- **S1 (16, 1):** Toggles East/West.
    - **Current:** ON.
    - **Behavior with S3=ON:**
        - S1=ON -> (12, 8) CLOSED. (12, 6) CLOSED. (6, 8) CLOSED.
        - S1=OFF -> (12, 8) OPEN. (Verified).
    - **Behavior with S3=OFF:** S1=OFF -> (6, 8) OPEN.
- **S2 (10, 1):** Main Power.
    - **Current:** ON.
- **S3 (2, 1):** Emergency Override.
    - **Function:** Opens shutter at (2, 7). Controls Mode.
    - **Current:** ON.
- **Observation:** (17, 6) is CLOSED with S1=ON, S2=ON, S3=ON.
- **Hypothesis:** Checking (20, 6) with S1=ON, S2=ON, S3=ON.
- **S1 (16, 1):** Toggles East/West.
    - **Current:** ON.
    - **Behavior with S3=ON:**
        - S1=ON -> (12, 8) CLOSED. (17, 6) CLOSED.
        - S1=OFF -> (12, 8) OPEN. (Verified).
    - **Behavior with S3=OFF:** S1=OFF -> (6, 8) OPEN.
- **Emergency Switch (20, 11):** Located behind shutter (20, 6).
    - **Path A:** Blocked. Shutter (20, 6) CLOSED (S3 ON/OFF).
    - **Path B:** Ladder (23, 3) -> 3_53 (SE).
        - **Result:** Dead End. `(21, 25)` is NOT a warp. Area leads only to Main Tunnel exit.
    - **New Plan:** Return to 3_54. Turn S3 ON. Enter via `(2, 7)`. Try to navigate South via Column 2 to bypass Pharmacist.

## Switch Room Exploration Data
- **West Room (Col 2):** Blocked by shutter at Row 6. (Controlled by S3?).
- **Inner East (Col 12):** Blocked at `(12, 12)` when S1=ON.
- **Middle East (Col 17):** Likely the correct path. Needs S1=OFF?
- **Ladder (23, 3) in Switch Room:** Connects to Goldenrod Underground SE `(22, 27)`. Acts as an exit/shortcut back to the main tunnel. Not the path to the Director.
- **Action:** Returning to Switch Room to test `(17, 10)` with **S1=OFF**.
- **Observation (Turn 14633):** Blocked at `(3, 9)` in West Room when trying to go South to Ladder `(5, 25)`. Potential hidden obstacle or wall.