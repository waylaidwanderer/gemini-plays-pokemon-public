# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 1).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** At (10, 3).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Current Status
- **Position:** Player at (6, 8) (After pushing B2).
- **Goal:** Solve B2 (Bottom Left Boulder).
- **Puzzle State:**
  - **B1:** Solved.
  - **B2:** At (5, 8).
  - **B4:** At (17, 7).

## B2 Strategy (The Grand Loop)
1.  **Push Up:** Push B2 from (5, 8) to (5, 6). (Position: 5, 7).
2.  **Escape South:** Go (5, 8) -> (9, 8) -> (9, 14).
3.  **Loop North:** Go Left to Col 1 -> Up to Top Area -> (5, 5).
4.  **Position North:** Go to (6, 6) via (6, 5).
5.  **Push Left:** Push B2 from (5, 6) to (4, 6).
6.  **Push Down:** Push B2 from (4, 6) into Pit (4, 7).

## Finishing Plan
- After B2, solve B3/B4. B4 is at (17, 7).
- B4 likely goes to Pit (12, 13).
- B3 (Unseen) likely goes to Pit (5, 12).