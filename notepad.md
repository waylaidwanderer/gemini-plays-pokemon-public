# Ice Path Strategy
- **Current State:** At Ice Path B1F (7, 9).
- **Goal:** Clear the Boulder blockade at (x=7-9, y=8-10) to access the South Room.
- **Status:** STRENGTH Active. Text box open.
- **Puzzle Logic (Updated):**
  - **Sokoban Hypothesis:** 4 Boulders -> 4 Pits.
    - **B3 (9, 11)** -> **Pit (5, 12)** (Left Side)
    - **B2 (7, 8)** -> **Pit (4, 7)** (Left Side)
    - **B1 (11, 8)** -> **Pit (12, 13)** OR **Pit (11, 2)** (Right Side)
    - **B4 (17, 7)** -> **Pit (11, 2)** OR **Pit (12, 13)** (Right Side)
  - **Plan:**
    1. **B3 Execution:** At (10, 11), push B3 Left to (4, 11), Down to (4, 12), Right to **Pit (5, 12)**.
    2. **B2 Execution:** Navigate to B2, push to Pit (4, 7).
    3. **Right Side:** Solve B1/B4 pair.
- **Next Step:** Navigate to (10, 11).

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **South Room:** Accessed via (9, 10).
- **Known Pits:** (4, 7), (5, 12), (12, 13).
- **Known Boulders:** (7, 8), (8, 9), (11, 7). Need 1 more.
- **Wild:** Golbat (B1F).