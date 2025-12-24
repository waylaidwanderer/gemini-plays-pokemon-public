# Ice Path Strategy
- **Current State:** At Ice Path B1F (7, 9).
- **Goal:** Clear the Boulder blockade at (x=7-9, y=8-10) to access the South Room.
- **Status:** STRENGTH Active. Text box open.
- **Status:** Player at (9, 10).
- **Observation:** B3 (9, 11) is NOT visible on screen. It might be missing/solved.
- **Immediate Action:** Attempt to move Down to (9, 11).
  - If B3 is there, this PUSHES it to (9, 12).
  - If B3 is missing, this WALKS to (9, 11).
- **Next Steps (once at 11, 8):**
  1. **B1:** Push Up to (11, 5).
  2. **B2:** Go North/West to (6, 6). Push B2 Left to (4, 6) -> Down to Pit (4, 7).
  3. **B3:** If it exists, solve from (9, 12).
- **B1 Plan:** (11, 7) -> Push Up -> (11, 5) -> Right -> (12, 5) -> Up -> (12, 2) -> Left -> Pit (11, 2).
- **Next Step:** Move Down.

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **South Room:** Accessed via (9, 10).
- **Known Pits:** (4, 7), (5, 12), (12, 13).
- **Known Boulders:** B2(7,8), B3(9,11), B1(11,8), B4(17,7).
- **Wild:** Golbat (B1F).