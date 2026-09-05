# Victory Road 2F - Layout & Notes

## General Information
- Ladder down to 1F: Located at (0, 8) <-> 1F (1, 1) [Verified Turns 22565, 26670]
- Ladder to 3F (Ladder B - Southeast Arrival): Located at (25, 14) <-> 3F (25, 14)
- Ladder to 3F (Ladder NE): Located at (27, 7) <-> 3F (27, 7)
- Ladder to 3F (Ladder A): Located at (23, 7) <-> 3F (23, 7) [Verified Turns 26725, 26744]
- Ladder to 3F (NW Ladder): Located at (1, 1) <-> 3F NW Room (2, 0)

## Collected Items
- [x] Item Ball at (18, 9) [Collected Turn 24170]

## Verified Physical Elevation & Topology
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
  - Row 11 Highway: Connects (29, 11) west across the upper plateau to Ladder A at (23, 7) and Ladder NE at (27, 7).
  - Column 12 Barrier: Column 12 (x=12, y=10..15) is a solid rock wall separating the eastern light purple floor (cols 13-26) from the western sector (cols 1-5). Bypass via (13, 8) <-> (5, 8) <-> Shutter 1 (5, 10).

## Empirical Verification Protocol: 2F Shutter 3 to Ladder B / 3F
- Objective: Empirically verify walkable path from opened Shutter 3 at (21, 15) to Ladder B at (25, 14) and Ladder NE at (27, 7).
- Protocol:
  1. Once Boulder 2 is pushed onto Switch 1 at (1, 16), walk East to Shutter 3 at (21, 15).
  2. Pass South through opened Shutter 3 to (21, 16) on Lower Highway.
  3. Walk East along row 16: (21, 16) -> (29, 16).
  4. Walk North along column 29: (29, 16) -> (29, 11).
  5. Log tile-by-tile coordinate traversability from (29, 11) to (25, 14) / (27, 7) before ascending.