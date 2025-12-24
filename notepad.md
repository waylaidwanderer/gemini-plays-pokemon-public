# Tile Mechanics
- **Ice Tiles (Light Blue):** Player slides until hitting an obstacle.
- **Boulders on Ice:** Verified: They DO NOT slide. They move 1 tile per push.
- **Strength Push:** Player does not automatically step forward.

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (11, 6).
- **Goal:** Reach (11, 8) to push B1 UP.
- **Puzzle State:** Reset Verified (B1 at 11, 7).

## Master Plan (Solution Found)
1.  **Navigate to (11, 8):**
    - **Step 1:** Go West/North/West/South to (5, 9).
      - Path: (11, 6) -> (10, 6) -> Up to (10, 1) -> Left to (6, 1) -> (5, 2) -> Slide Down to (5, 9).
    - **Step 2:** Go South/East to (17, 16).
    - **Step 3:** Go North/West to (11, 8).
      - Path: (17, 16) -> (17, 14) -> (12, 11) -> (12, 8) -> (11, 8).
2.  **Solve B1:**
    - Push Up to (11, 5).
    - Go to (10, 5). Push Right to (12, 5).
    - Go to (12, 6). Push Up to (12, 1).
    - Go to (13, 1). Push Left to (11, 1).
    - Go to (11, 0). Push Down to Pit (11, 2).