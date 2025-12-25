# Ice Path Strategy (Reset & Explore)

## Current Status
- **Position:** Player at (3, 13).
- **Goal:** Escape to B1F, Find B3, Solve Puzzle.
- **Puzzle State:**
  - **B2:** Stuck at (3, 12) (B2F). Cannot push on Ice.
  - **B1:** Stuck at (11, 3) (B2F).
  - **Pits:** 4 Pits found (11, 2), (5, 12), (4, 7), (12, 13).
  - **Boulders:** Only 3 found (B1, B2, B4). Need B3?

## Navigation Plan
1.  **Escape B2F:**
    - Slide Down to (3, 16).
    - Slide Right to (16, 16).
    - Slide Up to (16, 1).
    - Walk to Ladder (17, 1).
2.  **Explore B1F:**
    - Look for 4th Boulder (B3).
    - Look for optimal pit assignments.
    - B1 -> Pit (4, 7)?
    - B2 -> Pit (12, 13)?
    - B4 -> Pit (11, 2)?