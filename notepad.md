# Ice Path Strategy: B1F Boulder Puzzle (Turn 17145)

## Current Status
- **Location:** B1F, Position (18, 13).
- **Goal:** Push Boulder 2 from (5, 6) into Pit (4, 7).
- **Constraint:** Must reach (6, 6) to start the push sequence.

## Navigation Plan: Reach (6, 6)
**Path:** Zig-Zag North via Col 12 & 5
1.  **Leg 1:** `(12, 7)` -> ... -> `(12, 1)` (Completed).
2.  **Leg 2:** West on Row 1 to `(6, 1)`.
    - *Correction:* `(5, 1)` is a WALL. Must turn at `(6, 1)`.
3.  **Leg 3:** `(6, 1)` -> `(6, 2)` -> `(5, 2)` -> South to `(5, 5)` -> East to `(6, 5)` -> South to `(6, 6)`.
    - *Avoids Wall at `(6, 3)` and Wall at `(5, 1)`.*

## Puzzle Solution (In Progress)
1.  **Push 1:** At `(6, 6)`, push Boulder Left to `(4, 6)`. (COMPLETED)
2.  **Reposition:** Circle `(6, 6)` -> `(6, 5)` -> `(5, 5)` -> `(4, 5)`. (EXECUTING NOW)
3.  **Push 2:** Push Boulder Down into Pit `(4, 7)`.

## Item Retrieval (B2F)
1.  Drop into Pit `(4, 7)`.
2.  Land on B2F.
3.  Slide Up Col 4 -> Hit Boulder at `(4, 7)` -> Stop at `(4, 8)`.
4.  Slide Right to `(8, 8)` -> Get Item.
5.  Exit via Ladder `(9, 11)`.

## Map Data
- **Pits:** (11, 2), (4, 7), (5, 12), (12, 13).
- **Boulders:** (5, 6) [Target], (17, 7).
- **Ladders:** (17, 3) [Avoid], (3, 15), (17, 1) [Target area].