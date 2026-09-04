# Victory Road 1F - Layout & Notes

## General Information
- South exit / entrance: Route 23 at (8, 17) [Entered Turn 22138]

## Observed Layout & Physical Features
- Entrance mat: (8, 17)
- Path north: (8..9, 14..16) connects entrance to central junction (row 14)
- Row 13 Wall: Solid rock wall at (8..13, 13) separating lower entrance area from upper plateau
- Eastern Corridor Gap: Column 14 (14, 13..14) connects row 14 to upper eastern chamber (row 12 at (14, 12)). Note: (15, 13) is a solid rock wall! To walk from (16, 13/14) to (15, 12), you must bypass via column 14: (16, 14) -> (14, 14) -> (14, 12) -> (15, 12).
- Eastern Chamber: Columns 14-17 (rows 11-15). Contains Switch Plate at (17, 13). (13..14, 11..12) is a solid rock wall blocking westward passage. Ledge at (15, 10) blocks northward passage from (15, 11).
- Boulder 1 (Default Start): (5, 15)
- Western Corridor: Columns 1-3 (rows 10-16)
- Western Boulder (Boulder 2): Default initial location at (2, 10)
- Lower Rock Obstacle: (10..11, 15..16) and (6..7, 14..15) are 2x2 rock obstacles separating lower row 16 from central entrance foyer. Row 16 is the clear horizontal bypass.
- Obstacle Note: Tile (3, 14) is a rock obstacle. Bypass west via row 15: (4, 14) -> (4, 15) -> (1, 15) -> (1, 10..14).
- Boulder 2 Chokepoint: (3, 10) is a rock obstacle. Boulder 2 sits at (2, 10) between rock walls (1, 10) and (3, 10).
- Shutter (5, 13): Lowered by Switch (17, 13), allowing passage from lower floor row 14 onto the West Arm (5..7, 9..12).
- Elevated Plateau Architecture:
  - Central Cross-Highway: Row 12 (y=12) is completely open and connects columns 5 through 12 across the entire elevated plateau!
  - East Arm: cols 11..12 across rows 5..12.
  - North Arm / Arena: rows 5..6 across cols 7..12. Cooltrainer at (7, 5).
- Northern Sector Items (Elevated Plateau):
  - [ ] Item Ball at (9, 2)
  - [ ] Item Ball at (11, 0)
  - [ ] Item Ball at (14, 2)
  - Note: Row 3 is an impassable south-facing cliff wall separating rows 4-6 from upper brown plateau (rows 0-2).
## Floor Traversal & Ladder Access
- From lower floor (5, 14), pass North through lowered Shutter (5, 13) onto elevated cross-highway (row 12).
- Proceed East along row 12 to (11, 12), North to (11, 6), West across row 6 to (7, 6), and South through lowered Shutter (7, 7) to lower cave floor (7, 8).
- Proceed West and North through corridor (avoiding rock at (2, 8)) to reach 2F Ladder at (1, 1).

## Verified Master Boulder Solution (Verified Turn 28353)
- Initial State: Boulder 1 at (5, 15).
- Pre-Push Coordinate Assertions & Master Push Sequence:
  1. Stand at (5, 14) -> Push Down 1 time to (5, 16) [Boulder at (5, 16), Player at (5, 15)].
  2. Stand at (4, 16) -> Push East 4 times to (9, 16) [Boulder at (9, 16), Player at (8, 16)].
  3. Stand at (9, 17) -> Push North 2 times to (9, 14) [Boulder at (9, 14), Player at (9, 15)].
  4. Stand at (8, 14) -> Push East 7 times to (16, 14) [Boulder at (16, 14), Player at (15, 14)].
  5. Stand at (16, 15) -> Push North 2 times to (16, 12) [Boulder at (16, 12), Player at (16, 13)]. (CRITICAL: Stop at row 12!).
  6. CRITICAL DETOUR: Tile (15, 13) is a solid rock wall. Reposition around boulder by walking: (16, 13) -> Down to (16, 14) -> Left 2 to (14, 14) -> Up 2 to (14, 12) -> Right 1 to (15, 12).
  7. Stand at (15, 12) -> Push East 1 time to (17, 12) [Boulder at (17, 12), Player at (16, 12)].
  8. Reposition to (17, 11) via (16, 12) -> Up to (16, 11) -> Right to (17, 11).
  9. Stand at (17, 11) -> Push South 1 time onto Switch (17, 13) [Boulder at (17, 13), Player at (17, 12)].
- Verified Outcome: Switch at (17, 13) activated; Shutters at (5, 13) and (7, 7) opened for the duration of the current visit (note: exiting the cave to Route 23 or using Dig/Escape Rope resets the boulder puzzle and closes the shutters).

## Verified Map Boundaries & Exit Warps (Verified Turn 28092, 28200)
- South Exit Warp: Stepping South into row 17 across columns 8 and 9 (the entrance mat) immediately triggers a map transition to Route 23 at (4, 31), resetting all boulder positions and shutter states on 1F. Avoid walking South into row 17 during 1F puzzle execution!
- Verified Switch Plate on 1F: Located at (17, 13) in Eastern Chamber (target for Boulder 1). Note: (1, 16) is a standard floor tile on 1F (Switch (1, 16) is on 2F).