# Ice Path Strategy: B1F Boulder Puzzle

## Current Status
- **Location:** B2F, Position (19, 15).
- **Goal:** Return to B1F via Ladder at (17, 1).
- **Puzzle State:** Boulder 2 pushed into Pit (4, 7).

## Navigation Plan: Return to B1F
1.  **Exploration Slide (Executing):**
    - Move to `(1, 16)`.
    - Slide Right on Row 16 to `(16, 16)`.
    - *Purpose:* Revealing unseen tiles at `(9, 17)` etc.
2.  **Ascend:**
    - `(16, 16)` -> `(18, 16)` -> `(18, 14)`.
    - Slide Up Col 18 to `(18, 3)`.
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