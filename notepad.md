# Ice Path Strategy
- **Current State:** At Ice Path B1F (7, 9).
- **Goal:** Clear the Boulder blockade at (x=7-9, y=8-10) to access the South Room.
- **Status:** STRENGTH Active. Text box open.
- **Status:** Room Reset. B2 at (7, 8) (Correction: Push failed or reset).
- **Puzzle State:**
  - **B1:** (11, 7). Target: Pit (11, 2).
  - **B2:** (7, 8). Target: Pit (4, 7).
  - **B3:** (9, 11). Target: Pit (5, 12).
  - **B4:** (17, 7). Target: Pit (12, 13).
- **Execution Plan:**
  1. **B2:** Go to (8, 8). Push Left to (5, 8).
  2. **B2 Cont:** Go to (5, 9). Push Up to (5, 6).
  3. **Open Path:** Go to (11, 8). Push B1 Up to (11, 5).
  4. **B2 Finish:** Go to (6, 6). Push B2 Left to (4, 6) -> Down to Pit (4, 7).
  5. **B1 Finish:** At (11, 5). Push Right to (12, 5) -> Up to (12, 2) -> Left to Pit (11, 2).
  6. **B3:** Normal solve.
  7. **B4:** Solve last.
- **Next Step:** Navigate to (8, 8) and Push B2 Left.

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **South Room:** Accessed via (9, 10).
- **Known Pits:** (4, 7), (5, 12), (12, 13).
- **Known Boulders:** B2(7,8), B3(9,11), B1(11,8), B4(17,7).
- **Wild:** Golbat (B1F).