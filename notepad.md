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
- Observation: Boulder 4 located at (9, 10).
- Plan:
  1. Push Boulder 4 Down to (9, 11).
  2. Navigate around via Row 1 to (10, 11).
  3. Push Boulder 4 Left to (4, 11).
  4. Push Down to (4, 12).
  5. Push Right to (5, 12) [Pit].