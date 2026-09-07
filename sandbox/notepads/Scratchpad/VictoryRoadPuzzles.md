# Scratchpad: Victory Road Empirical Traversal & Puzzle Assertions

## Current Goal
Execute clean end-to-end Victory Road traversal from 1F to Indigo Plateau.

## 1F Master Solution (Verified Protocol)
- Boulder 1 starts at (5, 15). Push Down to (5, 16) first (since (6, 15) is a rock obstacle).
- Reposition to (4, 16), push East 4 times along row 16 to (9, 16) [Player at (8, 16)].
- Reposition to (9, 17) and push North 2 times to (9, 14) [Player at (9, 15)].
- Reposition to (8, 14) and push East 7 times along row 14 to (16, 14) [Player at (15, 14)].
- Reposition to (16, 15) and push North 2 times to (16, 12) [Player at (16, 13)].
- Detour around (15, 13) rock wall to (15, 12), push East 1 time to (17, 12).
- Reposition to (17, 11) and push South 1 time onto Switch (17, 13).
- Shutters at (5, 13) and (7, 7) open! Proceed to 1F Ladder at (1, 1) -> 2F (0, 8).

## 2F Traversal to NW Ladder
- Arrive at 2F (0, 8).
- Proceed through open corridor to 2F NW Ladder at (1, 1) -> 3F (2, 0).

## 3F Master Sequence Plan (To Verify Empirically)
- Arrive at 3F NW Ladder (2, 0).
- Open menu -> PKMN -> ATLAS -> Use STRENGTH.
- Proceed East along Row 2 to find 3F Boulder.
- Push Boulder through Row 1/2 -> Column 13/14 -> Row 14 -> Pit at (23, 14).
- Jump down Pit (23, 14) to 2F.
- Push fallen boulder onto 2F switch plate to open exit shutter.
- Climb Ladder NE at (27, 7) to 3F Exit Chamber.
- Exit to Indigo Plateau!