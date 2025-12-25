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
- Status: Systematic Search (NW Corner). Turn: 17438.
    - Boulder 1: Not found at (18, 12), (17, 7).
    - Boulder 2: Not found at (5, 6).
    - Boulder 3: Not found at (11, 5).
    - Boulder 4: Not found at (9, 10).
    - SE Corner: Checked, Empty.
    - NE Corner: Checked.
- Goal: Locate boulders and push to pits.
    - Plan:
    1. Resume navigation West to (3, 2) (bypass wall at 5,1 via 6,2).
    2. Search NW area (3, 5) and surround.
    3. If nothing, search Center/SW areas.
- Note: Pits are open. Row 1 has wall at (4,1)-(5,1).
- Pits: `(11, 2)`, `(4, 7)`, `(5, 12)`, `(12, 13)` (Open).