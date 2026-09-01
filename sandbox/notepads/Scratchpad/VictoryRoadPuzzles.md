# Victory Road Puzzle Mechanics & Empirical Test Log

## Floor 1F Puzzle System

### Active Test: Switch Plate 1 & Shutter Pairing
- **Boulder 1 Initial Coordinate:** (5, 15)
- **Switch Plate 1 Coordinate:** (5, 14) (directly 1 tile North of Boulder 1)
- **Baseline Shutter States (Before Push - Verified Turn 22317):**
  - Shutter at (5, 13): CLOSED (purple horizontal bars blocking path north into western corridor)
  - Shutter at (7, 7): Unverified / off-screen
  - Shutter at (15, 7): Unverified / off-screen
- **Empirical Hypothesis:** Pushing Boulder 1 North from (5, 15) onto Switch Plate 1 at (5, 14) depresses the switch and opens Shutter at (5, 13).
- **Verification Protocol:**
  1. Stand at (5, 16) facing Up into Boulder 1.
  2. Activate Strength via ATLAS (Machop).
  3. Step Up to push Boulder 1 onto (5, 14).
  4. Visually inspect tile (5, 13) to confirm Shutter state change from CLOSED (bars) to OPEN (clear passageway).
  5. Explore northern sector to inspect physical states of shutters at (7, 7) and (15, 7).

### Unverified Structural Hypotheses (To Be Tested)
- Ascent to 2F: Hypothesis that stairs/ladder exists in western/central sector (e.g. near row 10..11). Must be visually located and confirmed in-game.
- Switch Plate 2 at (17, 13): Must test which shutter it operates once reached.

### Empirical Test Log: Turn 22328
- **Action:** Boulder 1 pushed from (5, 15) onto Switch Plate 1 at (5, 14).
- **Observation:** Tile (5, 13) visually inspected. Purple horizontal shutter bars remain CLOSED.
- **Deduction:** Switch Plate 1 at (5, 14) does NOT control Shutter at (5, 13). It likely controls Shutter at (7, 7) or (15, 7).
- **Western Corridor Topology:** (1..3, 10..16) is fully open and accessible from (4, 14) by walking Left to col 1-3. Boulder 2 is visible at (2, 10).
- **Boulder 2 Test Turn 22340:** Boulder 2 pushed from (2, 10) to (2, 9). Shutter at (7, 7) remains CLOSED. Column 2 at (2, 9) terminates in rock wall (2, 8). Routing to eastern corridor via (14, 13) to inspect Switch Plate 2 at (17, 13) and Shutter at (15, 7).
### Empirical Inspection: Turn 22351
- **Observation in Eastern Chamber:**
  - Shutter at (15, 7) visually confirmed CLOSED (purple horizontal bars visible on upper elevation layer).
  - Row 10 (14..21, 10) is a solid cliff wall separating ground floor (rows 11-15) from upper plateau (rows 7-9).
  - Switch Plate 2 is at (17, 13) on ground floor.
- **Conclusion:** Switch Plate 1 at (5, 14) does NOT open Shutter (15, 7). Ground-level route to upper plateau is via western column 2 chute (pushing Boulder 2 north into row 8 hallway).

## Floor 1F Master Solution Plan
- **Mechanics Identified:**
  - Switch Plate at (17, 13) in eastern chamber controls Shutter at (15, 7).
  - Shutter at (15, 7) blocks the elevated ramp leading to the 2F ladder in the northeast corner.
  - Pushing Boulder 1 into the western corridor (5, 14) was the incorrect branch.
  - Correct route: Push Boulder 1 from its starting position into the clear horizontal hallway at row 14 (y=14), push it all the way East across (8..17, 14), and push it North onto Switch Plate at (17, 13).
  - Once Switch Plate at (17, 13) is depressed, ascend the eastern ramp at row 10, walk through the opened Shutter at (15, 7), and take the ladder up to 2F!