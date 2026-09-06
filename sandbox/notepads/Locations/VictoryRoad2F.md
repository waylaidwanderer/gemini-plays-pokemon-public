# Victory Road 2F - Layout & Notes

## General Information
- Ladder down to 1F: Located at (0, 8) <-> 1F (1, 1)
- Ladder to 3F (Ladder B - Verified Primary Route): Located at (25, 14) <-> 3F SE Lower Purple Room (25, 14)
- Ladder to 3F (NW Ladder): Located at (1, 1) <-> 3F NW Room (2, 0)
- Tile (23, 7): Passable floor tile with wall ladder graphic (no warp trigger on 2F).
- Enclosed NE Sector: Rows 7-9, cols 25-29 (contains shutter at (27, 10) and upper ladder at (26..27, 7..8)).

## Physical Elevation & Topology
- Elevation Split:
  - Upper Plateau (Dark Checkerboard): Rows 0-7 and Row 11.
  - Lower Floor (Light Purple Floor): Rows 8-14 across columns 5-26.
  - South-Facing Cliff Boundary: Impassable horizontal ledge line between row 7 and row 8 across columns 9-13, and between row 11 and row 12.
  - Ledge at (23, 14): West-facing one-way descent jumping FROM (24, 14) DOWN TO (22, 14).
- Shutters & Corridors:
  - Shutter 1 @ (5, 10): Opened by Switch 1 @ (1, 16), connects row 13 west sector to row 8 light purple floor.
  - Shutter 3 @ (21, 15): Opened by Switch 1 @ (1, 16), connects row 14 light purple floor to row 16 lower highway.
  - Row 16 Lower Highway: Connects Shutter 3 at (21, 15) east to (29, 16).
  - Eastern Outer Corridor: Columns 28-29 (rows 11-16) form a continuous 2-tile wide vertical highway connecting Row 16 Lower Highway at (28..29, 16) north to Row 11 Highway at (28..29, 11).
  - Row 11 Highway: Connects (29, 11) west across the upper plateau to Ladder A at (23, 7) and Ladder NE at (26, 8).
  - Column 12 Barrier: Column 12 (x=12, y=10..15) is a solid rock wall separating the eastern light purple floor (cols 13-26) from the western sector (cols 1-5). Bypass via (13, 8) <-> (5, 8) <-> Shutter 1 (5, 10).

## Master Route from 2F Entrance to Ladder NE (27, 7) & 3F Upper Dark Plateau
- Boulder 2 pushed onto Switch 1 at (1, 16) opens Shutter 1 at (5, 10) and Shutter 3 at (21, 15).
- Route: From (0, 8) entrance, push Boulder 2 onto Switch 1 (1, 16) -> walk through Shutter 1 (5, 10) -> across light purple floor to (20, 14) -> south through Shutter 3 (21, 15) to Lower Highway (row 16) -> east to (29, 16) -> north up col 29 to (29, 8) -> west to Ladder NE at (27, 7) -> ascends to 3F Upper Dark Plateau.

## Return Route from Ladder A / North Area (23, 8) to Ladder NE (27, 7):
- North Area connects west via Row 8 to column 20, south to Shutter 3 (21, 15), and east along Row 16 to column 29, ascending to Ladder NE (27, 7).

## Master Boulder 2 Solution
- Initial Position: Boulder 2 @ (4, 14). Switch 1 @ (1, 16).
- Push Sequence:
  1. Stand at (5, 14) facing West -> Push Left 1 time: Boulder 2 to (3, 14).
  2. Reposition around to (3, 13) via (4, 14) -> (4, 13) -> (3, 13).
  3. Stand at (3, 13) facing South -> Push Down 2 times along Column 3: Boulder 2 to (3, 16).
  4. Reposition around to (4, 16) via (3, 15) -> (4, 15) -> (4, 16).
  5. Stand at (4, 16) facing West -> Push Left 2 times along Row 16: Boulder 2 to (1, 16) [ON SWITCH 1!].
- Outcome: Switch 1 at (1, 16) activated; Shutter 1 at (5, 10) and Shutter 3 at (21, 15) opened.

## 2F Pit Drop Landing & Route Analysis (Verified Turn 32611)
- Drop Arrival: Dropping through 3F Pit at (23, 15) lands on 2F at (22, 16) with the fallen boulder at (23, 16).
- Row 17 Bypass: Row 17 ((21..28, 17)) is completely open and bypasses the boulder at (23, 16) without needing Strength.
- Corridor Connectivity:
  - Row 16 Lower Road connects west to Shutter 3 at (21, 15) and east to Column 28/29.
  - Column 28 connects Row 16 at (28, 16) north to Row 11 Highway at (28, 11).
  - Row 11 connects east to Column 28 and west to Column 23 at (23, 11).
  - Column 23 / Row 8 connects west to Column 17 at (17, 8).
  - Column 17 connects south at (17, 8) to north at (17, 2).
  - Row 2 / Row 3 connects Column 17 at (17, 2) east to Column 27 at (27, 2).
  - Column 28 connects north at (28, 5) south to (28, 8), giving access to (27, 8) directly below Ladder NE at (27, 7).
## Central-South Boulder Puzzle (Discovered Turn 32673)
- Boulder: Located at (9, 11).
- Switch Plate: Located at (9, 16).
- Shutter: Located at (15, 15).
- Access Route to Boulder (9, 11): From row 8, descend via col 6/7 through (6, 8)->(6, 11)->(8, 11) to stand beside Boulder at (9, 11).
- Target: Push Boulder (9, 11) onto Switch (9, 16) to lower Shutter (15, 15) and open passage to Lower Highway (row 16/17).