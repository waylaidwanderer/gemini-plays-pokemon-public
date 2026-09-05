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

## Empirical Verification Protocol: 2F Shutter 3 to Ladder B / 3F (VERIFIED Turn 29111)
- Master Route:
  1. Boulder 2 pushed onto Switch 1 at (1, 16) opens Shutter 1 at (5, 10) and Shutter 3 at (21, 15).
  2. Walk through Shutter 1 at (5, 10) onto Light Purple Floor at (5, 9).
  3. Walk East along row 8: (5, 8) -> (14, 8) -> South to (14, 12).
  4. Walk East along row 12: (14, 12) -> (20, 12).
  5. Bypass trainer at (21, 13) via (20, 12) -> (20, 14) -> (21, 14).
  6. Pass South through opened Shutter 3 at (21, 15) onto Lower Highway at (21, 16).
  7. Walk East along Lower Highway: (21, 16) -> (29, 16).
  8. Walk North along Column 29: (29, 16) -> (29, 11).
  9. Walk West to Ladder B at (25, 14) or Ladder NE at (27, 7) / Ladder A at (23, 7).


## Optimal Column 4 Master Boulder 2 Solution (Verified Turn 29079)
- Note: Strength expires on floor transitions and must be re-cast upon arriving on 2F!
- Starting State: Boulder 2 at default (4, 14). Player at (4, 13). Strength active.
- Optimal Push Sequence:
  1. Stand at (4, 13) facing South -> Push Down 2 times:
     - Push Down 1: Boulder 2 to (4, 15), Player to (4, 14).
     - Push Down 2: Boulder 2 to (4, 16), Player to (4, 15).
  2. Reposition around to (5, 16) via Right to (5, 15) -> Down to (5, 16) [facing West].
  3. Stand at (5, 16) facing West -> Push Left 3 times along Row 16:
     - Push Left 1: Boulder 2 to (3, 16), Player to (4, 16).
     - Push Left 2: Boulder 2 to (2, 16), Player to (3, 16).
     - Push Left 3: Boulder 2 to (1, 16) [ON SWITCH 1!], Player to (2, 16).
- Outcome: Switch 1 at (1, 16) activated! Shutter 1 at (5, 10) and Shutter 3 at (21, 15) opened!