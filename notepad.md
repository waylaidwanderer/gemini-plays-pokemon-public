# Ice Path Strategy
- **Current State:** At Ice Path B1F (7, 9).
- **Goal:** Clear the Boulder blockade at (x=7-9, y=8-10) to access the South Room.
- **Status:** STRENGTH Active. Text box open.
- **Status:** Player at (5, 7). B2 at (5, 6). Strength Active.
- **Puzzle State:**
  - **B1:** (11, 7). Plan: Don't touch. Jump Pit (11, 2).
  - **B2:** (5, 6). Target: Pit (4, 7).
  - **B3:** (9, 11). Target: Pit (5, 12).
  - **B4:** (17, 7). Target: Pit (11, 2).
- **Execution Plan:**
  1. **B2 Finish:** Navigate North around to (6, 6). Push B2 Left to (4, 6) -> Down to Pit (4, 7).
  2. **B3:** Navigate to (9, 11). Push Down -> Left -> Down -> Right to Pit (5, 12).
  3. **Right Side Access:** Walk to Pit (11, 2) and **Jump In**.
  4. **Right Side Solve:** Take Ladder (17, 1). Solve B4 -> Pit (11, 2). Solve B1 -> Pit (12, 13).
- **Next Step:** Navigate to (6, 6) via North Loop.

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **South Room:** Accessed via (9, 10).
- **Known Pits:** (4, 7), (5, 12), (12, 13).
- **Known Boulders:** B2(7,8), B3(9,11), B1(11,8), B4(17,7).
- **Wild:** Golbat (B1F).