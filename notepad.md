# Ice Path Strategy
- **Current State:** At Ice Path B1F (5, 9).
- **Goal:** Clear the Boulder blockade at (x=7-9, y=8-10) to access the South Room.
- **Puzzle Logic (Chokepoint):**
  - **B2** at (7, 8). **B3** at (8, 9).
  - Exit is at (9, 10).
  - **Corrected Solution (Don't move B2):**
    1. Move to (7, 9).
    2. Push **B3** Right to (9, 9).
    3. Loop around: (7, 9) -> (8, 9) -> (8, 8) -> (9, 8).
    4. From (9, 8), push **B3** Down to (9, 11).
    5. Walk South through (9, 10) -> (9, 12).
- **Plan:** Execute Step 1 & 2: Move Right to (7, 9) and push B3 Right.

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **South Room:** Accessed via (9, 10).
- **Known Pits:** (4, 7), (5, 12).
- **Known Boulders:** (7, 8), (8, 9). Need 2 more.
- **Observation:** Found a Boulder at (7, 8).
- **Hypothesis:** This is a Strength puzzle. Pushing boulders into the pits (4, 7) and (5, 12) might be the goal, or they serve as bridges.
- **Action:** Continue exploring the room to locate all boulders and pits.