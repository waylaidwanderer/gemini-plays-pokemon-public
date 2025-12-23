# Goldenrod Underground Switch Puzzle

## Current Status
- **Location:** Switch Room (3_54), Central Area.
- **Objective:** Reach the "Target Shutter" at `(12, 12)` or the Warp at `(22, 10)`.
- **Start Turn:** ~14790 (Approx). Current Turn: 14962.

## Switch Logic (Verified)
- **S1 (16, 1):** East/West Toggle.
    - **ON:** Opens East Gate `(12, 8)` (Note: System msg says it closed when S1 toggled? Wait. Previous note said ON opens East. Let's re-verify).
        - Correction: Turn 15006 system msg said `(12, 8): FLOOR -> WALL`. This happened after I likely toggled S1. If I was at S1 and interacted, I toggled it.
        - If `(12, 8)` became WALL, it CLOSED.
        - So S1 **Toggles** the state.
        - If it was Open and became Closed, then the *new* state (S1=ON? or OFF?) closes it.
        - I need to be careful. Marker says "Switch 1 (ON)".
        - If S1 is ON and `(12, 8)` is WALL, then S1=ON **Closes** East Gate.
        - This contradicts my previous note "ON: Opens East Gate".
        - I will update to: **S1 (16, 1):** Toggles East/West. Current: ON = East Closed (Confirmed by tile change).

- **S2 (10, 1):** Main Power.
    - **ON:** Required for gates to operate reliably.
    - **OFF:** Seems to close main gates `(6, 8)`, `(10, 6)` but might open some shutters `(6, 12)`. Generally causes deadlocks.
- **S3 (2, 1):** Emergency Override.
    - **ON:** Enables "Emergency Mode".
    - **Effects with S2=ON:**
        - Opens vertical shutters like `(12, 12)`.
        - Opens the path at `(2, 6)` (Emergency West Entrance).
        - Closes North Gate `(10, 6)` if S1 is OFF? (Need to verify this interaction).

## Current Strategy: "The West Entrance"
- **Hypothesis:** The deadlock I faced earlier (Open Gate but Closed Path) was because I entered from the wrong side.
- **The Deadlock:**
    - **S1=ON:** Enter North `(10, 6)` -> Blocked at `(12, 9)`.
    - **S1=OFF:** North Gate `(10, 6)` closes.
- **The Solution:**
    - Use the **Emergency West Entrance** at `(2, 6)`.
    - Set **S1=OFF** (Opens West Gate `(6, 8)`).
    - Set **S2=ON** (Main Power).
    - Set **S3=ON** (Opens `(2, 6)` and `(12, 12)`).
    - **Path:** `(2, 6)` -> `(6, 8)` -> `(12, 12)` -> Warehouse.

## Observations & Failures
- **S2=OFF:** Failed. Closed West Gate `(6, 8)`.
- **S1=ON / S3=ON:** Reached `(12, 12)` but blocked by `(12, 9)` wall.
- **S1=OFF / S3=ON (North Entry):** Failed. North Gate `(10, 6)` closed.

## Next Steps
1. Turn S2 ON.
2. Verify S1 is OFF.
3. Enter West Room via `(2, 6)`.
4. Pass through West Gate `(6, 8)`.
5. Navigate to `(12, 12)`.
- **Observation (Turn 14976):** Attempting to move into West Gate `(6, 8)` with S1=OFF, S2=ON, S3=ON.
- **Hypothesis:** It will be blocked (WALL).
- **Reasoning:** S3=ON seems to invert S1. S1=OFF normally closes East, so Inverted -> Opens East (Confirmed). Thus West should be Closed.
- **Next Step if Blocked:** This combo opens the East Path. I must find an entry. `(10, 6)` is closed. `(6, 8)` is closed. The only remaining option is the NE Shutters `(20, 6)`. I must backtrack and check them.
- Testing Hypothesis: S1=ON (Current), S2=ON, S3=ON opens the West Gate (6, 8) via the Emergency West Entrance (2, 6).
- Rationale: Marker at (12, 8) indicates S1=OFF opens the East Gate, suggesting S1=ON corresponds to the West Gate (or S3 overrides).
- Plan: Moving to (2, 6) to enter the West corridor. Avoid Grunt at (3, 4).