# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (17, 3).
- **Goal:** Solve B1 (Top Right Boulder).
- **Puzzle State:** Reset (Assumed).
  - **B1:** (11, 7).
  - **B2:** (7, 8).
  - **B3:** (9, 11).
  - **B4:** (17, 7).

## Investigation Plan
1.  **Navigate to (11, 6):** Check if B1 is at (11, 7).
2.  **Check Wall at (12, 6):** If Floor, go (12, 6) -> (12, 8) -> (11, 8).
3.  **Check Wall at (10, 8):** Go to (9, 8) via (5, 8) and check if I can cross to (11, 8).
4.  **Hypothesis:** One of the walls surrounding (11, 8) is fake or incorrect.

## Move Sequence (If (12, 6) is Floor)
1.  Go to (11, 8) via Col 12.
2.  Push B1 Up to (11, 5).
3.  Push B1 Left to (10, 5).
4.  Push B1 Up to (10, 1).
5.  Push B1 Right to (11, 1).
6.  Push B1 Down into Pit (11, 2).