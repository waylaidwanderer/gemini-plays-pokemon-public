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


## Optimal Master Boulder 2 Solution (VERIFIED & ACTIVATED Turn 29308)
- Initial Position: Boulder 2 @ (4, 14). Switch 1 @ (1, 16).
- Master Column 3 -> Row 16 Push Sequence:
  1. Stand at (5, 14) facing West -> Push Left 1 time: Boulder 2 to (3, 14) [Player at (4, 14)].
  2. Reposition around to (3, 13) via (4, 14) -> Up to (4, 13) -> Left to (3, 13) [facing South].
  3. Stand at (3, 13) facing South -> Push Down 2 times along Column 3:
     - Push Down 1: Boulder 2 to (3, 15), Player to (3, 14).
     - Push Down 2: Boulder 2 to (3, 16), Player to (3, 15).
  4. Reposition around to (4, 16) via (3, 15) -> Right to (4, 15) -> Down to (4, 16) [facing West].
  5. Stand at (4, 16) facing West -> Push Left 2 times along Row 16:
     - Push Left 1: Boulder 2 to (2, 16), Player to (3, 16).
     - Push Left 2: Boulder 2 to (1, 16) [ON SWITCH 1!], Player to (2, 16).
- Outcome: Switch 1 at (1, 16) ACTIVATED! Shutter 1 at (5, 10) and Shutter 3 at (21, 15) opened for the active visit (resets upon changing floors).

## NW Sector Topology (Verified Turn 30512)
- Arrival Ladder from 3F NW (2, 0): Located at (1, 1) on 2F NW.
- Trainer (Blackbelt) at (4, 2).
- Elevated checkerboard platform spans cols 1-3 (rows 2-4) and cols 2-7 (rows 6-7).
- Boulder gate at (5, 5), pushed south to (5, 6) connects row 4/5 light purple floor to checkerboard platform (cols 4-7, rows 6-7).
- 1F Ladder at (0, 8) connects to west corridor (cols 0-4).

## Shutter 1 & Elevation Verification (Turn 30515)
- Empirically verified: Transitioning between 2F and 3F reloads 2F, resetting Shutter 1 at (5, 10) to CLOSED and Boulder 2 to default position at (4, 14).
- Row 7 checkerboard to Row 8 purple floor is a solid vertical cliff boundary (cannot walk/hop down from (5..7, 7) to (5..7, 8)).
- To access Row 8 Light Purple Highway, Boulder 2 at (4, 14) MUST be pushed onto Switch 1 at (1, 16) via the west corridor to open Shutter 1 at (5, 10) and Shutter 3 at (21, 15).