# Ice Path Strategy: B1F Boulder Puzzle

## Current Status
- **Location:** B2F, Position (18, 1).
- **Goal:** Return to B1F via Ladder at (17, 1).
- **History:** Fell through Pit at B1F (11, 2). Recovered to Ladder.

## Critical Verification Needed (B1F)
- **Hypothesis:** To solve the B2F item puzzle, I might need a second boulder at (3, 12) on B2F.
- **Task:** Upon returning to B1F, check for a second movable boulder near Pit (5, 12).
- **If no boulder:** Drop down Hole (12, 13) and attempt navigation with existing layout.

## Navigation Plan: Return to B1F
1.  **Ascend:**
    - Move Left to `(17, 1)` Ladder. (Current Action)
2.  **B1F Exploration:**
    - Navigate to Pit `(5, 12)` area.
    - Check for boulders.
    - Go to Hole `(12, 13)` and drop.

## Tile Mechanics
- **ICE:** Slippery. Sliding movement until wall/object.
- **FLOOR:** Standard movement.
- **PIT:** Drops player to lower floor.
- **WALL:** Impassable.
- **LADDER:** Vertical transition.

## Map Data
- **Pits:** (11, 2), (4, 7), (5, 12), (12, 13).
- **Boulders:** (5, 6) [Pushed to 4,7], (17, 7) [Check status].
- **Ladders:** (17, 3), (3, 15), (17, 1).