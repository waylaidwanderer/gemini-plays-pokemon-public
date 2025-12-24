# Ice Path Strategy
- **Current State:** At Ice Path B1F (7, 9).
- **Goal:** Clear the Boulder blockade at (x=7-9, y=8-10) to access the South Room.
- **Status:** STRENGTH Active. Text box open.
- **Status:** Player at (5, 7). B2 at (5, 6). Strength Active.
- **Puzzle State:**
  - **B1:** (11, 7). Target: Pit (11, 2). Needs push Up from (11, 8).
  - **B2:** (5, 6). Target: Pit (4, 7). Needs push Left from (6, 6).
  - **B3:** (9, 11). Target: Pit (5, 12).
  - **B4:** (17, 7). Target: Pit (11, 2).
- **Execution Plan:**
  1. **Route to B1:** Go South to Row 16 -> East to Col 12 -> North to (12, 8) -> West to (11, 8).
  2. **Move B1:** Push B1 Up to (11, 5).
  3. **Route to B2:** Continue North to Row 1 -> West to Col 6 -> South to (6, 6).
  4. **Move B2:** Push Left to (4, 6) -> Down to Pit (4, 7).
  5. **B3:** Solve.
- **Next Step:** Navigate to (11, 8) via Row 16 loop.

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **South Room:** Accessed via (9, 10).
- **Known Pits:** (4, 7), (5, 12), (12, 13).
- **Known Boulders:** B2(7,8), B3(9,11), B1(11,8), B4(17,7).
- **Wild:** Golbat (B1F).