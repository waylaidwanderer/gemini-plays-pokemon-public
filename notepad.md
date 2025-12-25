# Ice Path Strategy: B1F Boulder Puzzle

## Current Status
- **Location:** B2F, Position (11, 17).
- **Goal:** Return to B1F via Ladder at (17, 1).
- **History:** Fell through Pit at B1F (11, 2). Slid down to (11, 17).

## Navigation Plan: Return to B1F
1.  **Slide Sequence:**
    - Slide Right from `(11, 17)` to `(16, 17)` (Floor).
    - Walk to `(18, 14)` (Start of Col 18 slide).
    - Slide Up Col 18 to `(18, 3)`.
2.  **Ascend:**
    - `(18, 3)` -> `(17, 1)` Ladder.
3.  **B1F Action:**
    - Go to Hole `(12, 13)` and drop.

## Tile Mechanics
- **ICE:** Slippery. Sliding movement until wall/object.
- **FLOOR:** Standard movement.
- **PIT:** Drops player to lower floor.
- **WALL:** Impassable.
- **LADDER:** Vertical transition.

## Map Data
- **Pits:** (11, 2), (4, 7), (5, 12), (12, 13).
- **Boulders:** (5, 6) [Target], (17, 7).
- **Ladders:** (17, 3), (3, 15), (17, 1).