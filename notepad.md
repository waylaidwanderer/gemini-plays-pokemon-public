# Ice Path Strategy: B1F Boulder Puzzle

- **Status:** Searching for Boulders. Turn: 17415.
- **Goal:** Locate and push 4 Boulders into 4 Pits.
    - **Boulder 1:** Target Pit (12, 13). Not at (18, 12) or (17, 7).
    - **Boulder 2:** Target Pit (4, 7). Not at (5, 6).
    - **Boulder 3:** Target Pit (11, 2). Not at (11, 5).
    - **Boulder 4:** Target Pit (5, 12).
- **Pits:** `(11, 2)`, `(4, 7)`, `(5, 12)`, `(12, 13)` (Open).

## Navigation & Mechanics
- **Current Position:** `(3, 2)`.
- **Immediate Goal:** Navigate East to `(11, 1)` to check for Boulder 3.
- **Bag Status:** Full.
- Observation: Blockage at (9, 10) was a wild encounter, not a boulder.
- Status: Boulders Found on B2F!
    - Found Boulder at (3, 12) immediately upon landing.
    - This confirms boulders were already dropped (puzzle state persisted).
    - No need to push boulders on B1F.
- Goal: Solve B2F Ice Puzzle.
    - Objective: Reach the Ladder at (9, 11) using the dropped boulders.
    - Current State:
        - Boulder at (3, 12).
        - Checking for Boulder at (4, 7).
        - Checking for Boulder at (11, 3).
        - Checking for Boulder at (12, 13) (Landing spot 12, 12).
    - Plan:
        1. Slide UP from (4, 12) to check for Boulder at (4, 7).
        2. If hit, slide Right/Left to navigate towards center.
        3. Reach Ladder (9, 11).
- Pits: `(11, 2)`, `(4, 7)`, `(5, 12)`, `(12, 13)` (Open).