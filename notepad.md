# Ice Path Strategy: B3F Exploration

## Goal
- Explore B3F East side to find path to Item at (5, 7).

## Navigation Plan: East Side Loop
1.  **Traverse East:**
    - From `(12, 1)`, go Down to `(12, 2)`.
    - Traverse East: `(12, 2)` -> `(13, 2)` -> `(14, 2)` -> `(15, 2)`.
2.  **Explore South/Ladder:**
    - From `(15, 2)`, head South to `(15, 5)`.
    - **Task:** Check/Mark Ladder at `(15, 5)`.
3.  **Retrieve Item:**
    - Continue search for path wrapping back West towards `(6, 7)`.
4.  **Exit:**
    - Push Rock at `(6, 6)` UP (if possible) to open shortcut, or backtrack.

## Map Data
- **Ladder to B2F:** `(3, 5)`.
- **Ladder (Unmarked):** `(15, 5)`.
- **Item:** `(5, 7)`.
- **Rock:** `(6, 6)`.
- **IcePathB2FBlackthornSide (3_64):**
    - Accessed from B3F Ladder at (15, 5).
    - Contains `FLOOR_UP_WALL` tiles (likely ledges).
    - Need to check if this leads to the Item on B3F or the HM.
- **B2F Paths:**
    - Right path: Ice starts at `(8, 4)`.
    - Left path: Ledge at `(5, 2)/(6, 2)` leads to ice at `(6, 6)`.
    - Trying Right path first.
- **B2F Puzzle Observation:**
    - Arrived at `(8, 8)` after sliding down.
    - Path options: Hop Left at `(4, 8)` or Hop Down at Row 9.
    - Testing Left path at `(4, 8)` to see if it loops or leads to a hidden area.
- **Path verification:** Sliding Right from `(0,8)` to `(3,8)` puts me below a ledge at `(3,4)`, likely preventing return to the Ladder.
- **Action:** Sliding South from `(3,8)` to explore the unknown area.
- **B2F Loop:** Sliding Right from `(3, 14)` leads to `(8, 14)` -> `(8, 3)` -> Start `(3, 3)`. Loop confirmed.
- **Item at (8, 16):** Located on isolated floor tile. Cannot reach from current path. Likely requires dropping from B1F hole at `(8, 16)`.
- **Action:** Taking Ladder at `(3, 15)` to explore further.
- **B1F South (3_62):**
    - Arrived at `(11, 27)` from B2F `(3, 15)`.
    - Ledges at Row 24 prevent going North.
    - Only path seems to be East to `(14, 28)` onto Ice.
    - Exploration target: South-East Ice patch.