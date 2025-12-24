# Ice Path Strategy
- **Current State:** At Ice Path B1F (7, 9).
- **Goal:** Clear the Boulder blockade at (x=7-9, y=8-10) to access the South Room.
- **Status:** STRENGTH Active. Text box open.
- **Status:** Back on B1F (NE Corner).
- **Observation:** Row 1 connects NE corner to Main Room.
- **Goal:** Check if Boulders have reset.
- **Puzzle State to Verify:**
  - **B1:** Should be at (11, 7). (Was stuck at 11, 8).
  - **B3:** Should be at (9, 11) or GONE if solved.
  - **B2:** Should be at (7, 8).
  - **B4:** Should be at (17, 7).
- **Plan:**
  1. Navigate to (11, 7) to check B1.
  2. If B1 is reset, execute **Master Plan**.
  3. **Master Plan:**
     - **B1:** Push Up to (11, 5) -> Right to (12, 5) -> Down to (12, 12) -> Right to (13, 12) -> Down to (13, 13) -> Left to Pit (12, 13). (Wait, check B1 destination).
     - **B2:** Push Left to (5, 8) -> Up to (5, 6) -> Left -> Down to Pit (4, 7).
     - **B3:** Push Down to (9, 11) -> Loop -> Push Left -> Down -> Right to Pit (5, 12).
     - **B4:** Push Left to (11, 7) -> Up -> ... (Solve last).
- **Next Step:** Navigate to (11, 7).

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **South Room:** Accessed via (9, 10).
- **Known Pits:** (4, 7), (5, 12), (12, 13).
- **Known Boulders:** B2(7,8), B3(9,11), B1(11,8), B4(17,7).
- **Wild:** Golbat (B1F).