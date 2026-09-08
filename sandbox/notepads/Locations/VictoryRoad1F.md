# Victory Road 1F - Layout & Notes

## General Information
- South exit / entrance: Route 23 at (8, 17)

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
- Northern Sector Elevated Plateau:
  - Note: Row 3 is an impassable south-facing cliff wall separating rows 4-6 from upper brown plateau (rows 0-2).

## Floor Traversal & Ladder Access
- From lower floor (5, 14), pass North through lowered Shutter (5, 13) onto elevated cross-highway (row 12).
- Proceed East along row 12 to (11, 12), North to (11, 6), West across row 6 to (7, 6), and South through lowered Shutter (7, 7) to lower cave floor (7, 8).
- Proceed West along row 8 to (3, 8) (note: (2, 8) is a rock obstacle and col 1 is solid wall; do not enter col 1/row 9). Walk North along Column 3 through (3, 7)->(3, 6)->(3, 5)->(3, 4)->(3, 3)->(3, 2)->(3, 1), then Left 2 steps through (2, 1) to reach the 2F Ladder at (1, 1) (connecting to 2F at (0, 8)).

## Planned Master Boulder Solution (Verified Atomic Checkpoint Protocol)
- Initial State: Boulder 1 at (5, 15), Player at (5, 14), Strength active.
- Note: Tile (6, 15) is a solid rock obstacle, so Boulder 1 cannot be pushed directly East from (5, 15). It must be pushed Down to row 16 first.

### Atomic Checkpoints Matrix (Safe Northern Route - Never touches Row 17):
- **Checkpoint 1 (Push North to Row 14)**:
  - Approach: From entrance foyer (8, 14), walk Left 4 to (4, 14) -> Down 2 to (4, 16) -> Right 1 to (5, 16) facing North.
  - Push: From (5, 16) facing North, push UP 1 time.
  - State: Boulder at (5, 14), Player at (5, 15).
  - Reposition: Down 1 to (5, 16) -> Left 1 to (4, 16) -> Up 2 to (4, 14).
  - End State: Boulder at (5, 14), Player at (4, 14) facing East.
- **Checkpoint 2 (East along Row 14 all the way to Col 16)**:
  - From (4, 14) facing East: Push East 11 times along row 14.
  - State: Boulder at (16, 14), Player at (15, 14).
  - Reposition: Down 1 to (15, 15) -> Right 1 to (16, 15) facing North.
  - End State: Boulder at (16, 14), Player at (16, 15) facing North.
- **Checkpoint 3 (North along Col 16 to Row 12)**:
  - From (16, 15) facing North: Push North 2 times.
  - State: Boulder at (16, 12), Player at (16, 13).
  - Reposition (Detour around (15, 13) rock wall): Down 1 to (16, 14) -> Left 2 to (14, 14) -> Up 2 to (14, 12) -> Right 1 to (15, 12).
  - End State: Boulder at (16, 12), Player at (15, 12) facing East.
- **Checkpoint 4 (East to Col 17 & Lock onto Switch (17, 13))**:
  - From (15, 12) facing East: Push East 1 time to (17, 12) [Boulder at (17, 12), Player at (16, 12)].
  - Reposition: Up 1 to (16, 11) -> Right 1 to (17, 11).
  - From (17, 11) facing South: Push South 1 time onto Switch (17, 13).
  - End State: Boulder at (17, 13) [SWITCH DEPRESSED], Player at (17, 12).
  - Outcome: Shutters at (5, 13) and (7, 7) lowered permanently for current visit!
- **Checkpoint 5 (Ascent to 2F Southwest Ladder at (1, 1))**:
  - Path: From Switch chamber (17, 12), walk Left 3 along row 12 to (14, 12) -> Down 2 to row 14 at (14, 14) -> West 9 along row 14 to (5, 14) -> North 2 through lowered Shutter (5, 13) onto elevated cross-highway at (5, 12) -> East 6 along row 12 to (11, 12) -> North 6 along col 11 to (11, 6) -> West 4 along row 6 to (7, 6) -> South 2 through lowered Shutter (7, 7) to lower cave floor (7, 8) -> West 4 along row 8 to (3, 8) -> North 7 along col 3 to (3, 1) -> Left 2 through (2, 1) onto 2F Ladder at (1, 1) [Transitions to 2F at (0, 8)]!

## Map Boundaries & Exit Warps
- South Exit Warp: Stepping South into row 17 across columns 8 and 9 (the entrance mat) immediately triggers a map transition to Route 23 at (4, 31), resetting all boulder positions and shutter states on 1F. Avoid walking South into row 17 during 1F puzzle execution!
- Verified Switch Plate on 1F: Located at (17, 13) in Eastern Chamber (target for Boulder 1). Note: (1, 16) is a standard floor tile on 1F (Switch (1, 16) is on 2F).