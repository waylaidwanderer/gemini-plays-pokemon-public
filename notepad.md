# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (10, 1).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:**
  - **B1:** At (10, 3).
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Current Status
- **Position:** Player at (13, 2).
- **Goal:** Push B1 into Pit (11, 2), then go to B2.
- **Puzzle State:**
  - **B1:** At (12, 2). Ready to push Left.
  - **B2:** (7, 8).
  - **B4:** (17, 7).

## Next Steps (B2 Strategy)
1.  **Navigate to B2 (7, 8).**
2.  **Push Left:** Push B2 from (7, 8) to (5, 8).
3.  **Push Up:** Push B2 from (5, 8) to (5, 7).
4.  **Push Left:** Push B2 into Pit (4, 7).

## Finishing Plan
- After B2 is done, solve B3 (Bottom Left) and B4 (Bottom Right).
- Check B4 at (17, 7) next if closer.