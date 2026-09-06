# Victory Road 3F - Layout & Topology

## Ladders & Subsector Connectivity (VERIFIED Turn 31234)
- 3F is divided into TWO isolated subsectors:
  1. **Upper Dark Plateau (rows 0-11, cols 6-29)**:
     - Contains Boulder 1 @ (22, 3), Northern Highway (Row 1), Central Bridge (cols 6-7), NW Room (cols 0-5) with Switch Plate @ (3, 5), and Shutter @ (17, 5).
     - Accessed from 2F via **Ladder NE @ (27, 7)** (or descent arrival at (23, 7)).
     - Separated from the southern lower sector by solid rock wall at row 10 and closed Shutter @ (17, 5).
  2. **SE Lower Purple Sector (rows 11-17, cols 9-29)**:
     - Contains Ladder B @ (25, 14) <-> 2F (25, 14), The Pit @ (23, 14), Pit Boulder @ (9, 16), Item Ball @ (9, 11), and Shutters @ (15, 15) & (21, 15).
     - Accessible from 2F via **Ladder B @ (25, 14)** or from Upper Plateau via Shutter @ (17, 5) once opened.
- NW Ladder: Located at (2, 0) in NW Room <-> 2F NW (1, 1).

## Discovered Points of Interest & Topology
- [ ] Item Ball at (9, 11) in SE Lower Purple sector.
- [ ] Item Ball at (11, 0) in northern corridor of western sector.
- Shutter at (17, 5): Horizontal purple bars blocking passage south from row 4 purple room to row 6.
- Shutters at (15, 15) and (21, 15): Block passage between row 14 and row 16 lower highway until Switch (3, 5) is activated.

## Master Boulder 1 to Switch (3, 5) Solution (VERIFIED Turn 30921, Re-verified Turn 31486)
1. Strength activated by ATLAS on 3F Upper Dark Plateau.
2. Initial State: Boulder 1 at (22, 3).
3. Position at (22, 4) -> Push North 2 times to (22, 1) on Row 1 (Northern Highway).
4. Reposition via (22, 3) -> (23, 3) -> (23, 1).
5. Push West along Row 1: (22, 1) -> (21, 1) -> (20, 1) -> ... -> (6, 1).
6. At (6, 1), stand at (6, 0) and push South 1 time to (6, 2) on Central Bridge.
7. Stand at (7, 2) and push West into NW Room at (5, 2) -> (4, 2) -> (3, 2).
8. Note: Tile (3, 3) is a rock obstacle! Bypass to (2, 2):
   - From (4, 2), push Left to (2, 2) [Boulder at (2, 2)].
   - Reposition to (2, 1) via (3, 2) -> (3, 1) -> (2, 1).
   - Push South down Column 2: (2, 2) -> (2, 3) -> (2, 4) -> (2, 5) [Boulder at (2, 5), Player at (2, 4)].
   - Reposition to (1, 5) via (2, 4) -> Left to (1, 4) -> Down to (1, 5).
   - Stand at (1, 5) facing East -> Push Right 1 time onto Switch Plate (3, 5)!
9. Outcome: Switch (3, 5) ACTIVATED! Shutters at (17, 5), (15, 15), and (21, 15) OPEN!

## Final Pit & Exit Puzzle Coordinates (Verified Turn 31486-31497)
- Pit Boulder: Located at (22, 15) on Row 15, immediately west of The Pit.
- The Pit: Located at (23, 15) on Row 15.
- Other Boulders on 3F: Boulder 2 at (13, 13) (pushed south from (13, 12)).
- Pit Drop Execution:
  1. Stand at (21, 15) facing East.
  2. Push Right 1 time: Boulder moves from (22, 15) into Pit at (23, 15) (falls to 2F). Player moves to (22, 15).
  3. Step Right 1 time into Pit at (23, 15) -> Player drops through hole and lands on 2F at (22, 16).
