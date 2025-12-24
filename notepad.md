# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (17, 3).
- **Goal:** Verify Puzzle Reset (Check B1 at 11, 7).
- **Puzzle State:** Assumed Reset.
  - **B1:** (11, 7).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Master Plan
1.  **Verify Reset:** Go to (11, 6) and check (11, 7).
2.  **Navigate to (11, 8):**
    - Via West Side -> South Side -> East Side Loop.
3.  **Solve B1:**
    - Push Up to (11, 5).
    - Go to (10, 5). Push Right to (12, 5).
    - Go to (12, 6). Push Up to (12, 1).
    - Go to (13, 1). Push Left to (11, 1).
    - Go to (11, 0). Push Down to Pit (11, 2).
4.  **Next:** Solve B2.