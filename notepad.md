# Ice Path Strategy (Reset & Explore)

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (2, 1).
- **Goal:** Locate B3.
- **Puzzle State:**
  - **B1:** Not at (10, 1). Likely at (11, 1).
  - **B2:** At (7, 8).
  - **B3:** Searching Left Side (Cols 1-3). Not at Top Left.
  - **B4:** At (17, 7).

## Immediate Plan
1.  **Search South:** Walk down to (2, 9).
2.  **Locate B3:** If found, mark it.
3.  **If no B3:**
    - Maybe there are only 3 boulders?
    - Or B3 is hidden elsewhere.
4.  **Solve B2:**
    - Push Left (7, 8) -> (5, 8).
    - Loop Around.
    - Push Down (5, 8) -> Pit (5, 12).