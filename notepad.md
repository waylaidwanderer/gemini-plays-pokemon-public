# Ice Path Strategy: B3F Exploration

## Goal
- Explore B3F East side to find path to Item at (5, 7).

## Navigation Plan: East Side Loop
1.  **Traverse Row 1:**
    - Current Pos: `(7, 2)`.
    - Go `(7, 1)` -> East to `(11, 1)`.
2.  **Explore South:**
    - From `(11, 1)`, head South down the East side of the map.
    - Look for a path wrapping back West towards `(6, 7)`.
3.  **Retrieve Item:**
    - Access `(5, 7)` from the South/East.
4.  **Exit:**
    - Push Rock at `(6, 6)` UP (if possible) to open shortcut, or backtrack.

## Map Data
- **Ladder to B2F:** `(3, 5)`.
- **Item:** `(5, 7)`.
- **Rock:** `(6, 6)`.