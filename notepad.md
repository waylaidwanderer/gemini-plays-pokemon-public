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
- Status: Systematic Search (SE Checked). Turn: 17433.
    - Boulder 1: Not found at (18, 12), (17, 7).
    - Boulder 2: Not found at (5, 6).
    - Boulder 3: Not found at (11, 5).
    - Boulder 4: Not found at (9, 10).
    - SE Corner (17, 12): Checked, Empty.
- Goal: Locate boulders and push to pits.
    - Plan:
    1. Navigate to (11, 5) to check NE entrance.
    2. Search NE area (Rows 1-4, Cols 12+).
    3. Search NW area (3, 5).
- Note: (12, 11) area clear. Wall at x=14 (Row 12). Pit at (12, 13).
- Pits: `(11, 2)`, `(4, 7)`, `(5, 12)`, `(12, 13)` (Open).