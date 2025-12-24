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

## Master Plan (Revised - Long Loop)
1.  **Goal:** Reach (11, 8) (South of B1) to push B1 UP.
2.  **Path:** Go North, then West, then South, then East.
    - **Step 1 (North Loop):**
        - (11, 6) Left -> (10, 6).
        - Up -> (10, 0).
        - Right -> (11, 0).
        - Down -> (11, 1).
        - Left -> (6, 1).
    - **Step 2 (West Side):**
        - Down -> (6, 2).
        - Left -> (5, 2).
        - Down -> (5, 9).
    - **Step 3 (South Loop):**
        - (5, 9) -> (5, 16) -> (17, 16).
    - **Step 4 (East Side):**
        - (17, 16) -> (17, 14) -> (12, 11) -> (12, 8).
    - **Step 5 (Position):**
        - Left -> (11, 8).
3.  **Solve B1:**
    - Push Up to (11, 5).
    - Go to (10, 5). Push Right to (12, 5).
    - Go to (12, 6). Push Up to (12, 1).
    - Go to (13, 1). Push Left to (11, 1).
    - Go to (11, 0). Push Down to (11, 2) (PIT).