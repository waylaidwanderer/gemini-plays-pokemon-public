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
- **Verified (Turn 15009):** S1=ON, S2=ON, S3=ON opens West Gate (6, 8) and closes East Gate (12, 8).
- **Target Shutter (12, 12):** Confirmed OPEN (FLOOR) with S3=ON.
- **Plan:** Entering the Southern Area via West Gate to reach the Warehouse.
- **Tile Change (Turn 15013):** `(6, 13)` changed from FLOOR to WALL. Possibly a shutter closing as I moved south?
- **Plan:** Moving through the open path at `(12, 12)` to explore the southern section.
- **Tile Update (Turn 15027):** `(17, 10)` and `(17, 11)` changed WALL -> FLOOR.
- **Hypothesis:** This opens a vertical corridor at x=17, likely connecting the area I am in to the northern part or further east.
- **Plan:** Moving East to investigate this new path at x=17.
- **Tile Update (Turn 15028):** `(18, 12)` and `(18, 13)` changed WALL -> FLOOR.
- **Observation:** The path continues to open up as I advance East. This suggests proximity-based shutters or just map reveal mechanics.
- **Plan:** Continue East to (18, 12). Expecting to encounter the Rocket Girl marked at (19, 12).
- **Interaction (Turn 15040):** Interacted with switch at `(20, 11)`. Text: "It's labeled EMERGENCY."
- **Next Step:** Clear text. If no prompt, move to investigate doors `(22, 10)` and `(23, 10)`.
- **Action (Turn 15041):** Turned Emergency Switch `(20, 11)` ON.
- **Hypothesis:** This should open the nearby shutters (likely `(20, 6)` or `(17, 6)`) or unlock the doors `(22, 10)` and `(23, 10)`.
- **Plan:** Investigate the doors at `(22, 10)` and `(23, 10)` immediately.
- **Transition (Turn 15043):** Entered Door at `(22, 10)` in Switch Room. Arrived in **Goldenrod Underground Warehouse (3_56)** at `(2, 12)`.
- **Current Location:** A corridor on the west side of the Warehouse map.
- **Plan:** Explore North.
- **Observation (Turn 15046):** Found an Item Ball at `(2, 1)` blocking the path East.
- **Action:** Picking it up to clear the path.
- **Hypothesis:** This path likely leads to the eastern part of the Warehouse where the Director might be.
- **Action (Turn 15049):** Picked up Ultra Ball at `(2, 1)`.
- **Plan:** Path East is now clear. Proceeding East to explore the rest of the Warehouse.