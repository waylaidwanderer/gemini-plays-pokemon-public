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
- Status: Search Complete. No Boulders on B1F.
    - Swept all corners. 0 Boulders found.
    - Pits are marked as Open Warps in XML.
- Hypothesis: Puzzle state issue or boulders already dropped?
- Goal: Solve B1F Boulder Puzzle.
    - Plan:
    1. Fall into Pit (5, 12) to check B2F layout.
    2. If boulders present on B2F -> Puzzle Solved.
    3. If not, take ladder back to B1F (this should reset the boulders).
- Note: If boulders don't spawn after reset, I'm missing a trigger or they are elsewhere.
- Pits: `(11, 2)`, `(4, 7)`, `(5, 12)`, `(12, 13)` (Open).