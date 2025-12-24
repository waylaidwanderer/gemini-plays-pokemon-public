# Ice Path Strategy
- **Current State:** At Ice Path B1F (7, 9).
- **Goal:** Clear the Boulder blockade at (x=7-9, y=8-10) to access the South Room.
- **Status:** STRENGTH Active. Text box open.
- **Status:** Player at (6, 9). B2 at (5, 8). Strength Active.
- **Puzzle State:**
  - **B1:** (11, 7). Target: Pit (11, 2).
  - **B2:** (5, 8). Target: Pit (4, 7).
  - **B3:** (9, 11). Target: Pit (5, 12).
  - **B4:** (17, 7). Target: Pit (12, 13).
- **Execution Plan (B2):**
  1. **Push Up:** Move to (5, 9). Push B2 Up x2 to (5, 6).
  2. **Traverse:** Loop South -> East -> North to (11, 8).
  3. **B1:** Push Up to (11, 5).
  4. **B2 Finish:** Go to (6, 6). Push B2 Left to (4, 6) -> Down to Pit (4, 7).
- **Next Step:** Move Left, Push Up x2.

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **South Room:** Accessed via (9, 10).
- **Known Pits:** (4, 7), (5, 12), (12, 13).
- **Known Boulders:** B2(7,8), B3(9,11), B1(11,8), B4(17,7).
- **Wild:** Golbat (B1F).