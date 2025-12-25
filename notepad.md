# Ice Path Strategy: B1F Boulder Puzzle

## Current Status
- **Location:** B2F, Position (16, 16).
- **Goal:** Return to B1F via Ladder at (17, 1).
- **Action:** Aligning for ascent via Col 17.

## Navigation Plan: Return to B1F
1.  **Ascend:**
    - Move Right to `(17, 16)`.
    - Slide Up Col 17.
    - *Expected Stop:* `(17, 3)` (Floor) or `(17, 1)` (Ladder/Wall).
2.  **To Ladder:**
    - If stopped at `(17, 3)`, walk North to `(17, 1)`.
3.  **B1F Action:**
    - Go to Hole `(12, 13)` and drop.

## Map Data
- **Pits:** (11, 2), (4, 7), (5, 12), (12, 13).
- **Boulders:** (5, 6) [Pushed to 4,7], (17, 7) [Check status].
- **Ladders:** (17, 3), (3, 15), (17, 1).