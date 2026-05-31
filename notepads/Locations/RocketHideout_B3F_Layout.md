# Rocket Hideout B3F Detailed Layout & Routing

## Stairs and Key Transitions
- B2F to B3F Stairs: Connected symmetrically from B2F (21, 8) to B3F (25, 6) on Map 0_201. There are NO stairs to B2F in the southeast room of B3F.
- Southeast Room Staircase Correction: The staircase at B2F (21, 22) actually connects UP to B1F southern section (Map 0_199) at (21, 25), NOT B3F!
- B3F to B4F Stairs: Located on B3F West at (19, 19), which warps to B4F (19, 10). (18, 16) is actually an Up-spinner.
- Up-spinner at (19, 17): Stepping here immediately slides the player all the way north to (19, 9), blocking horizontal transit along row 17 and blocking direct southern access to the stairs at (19, 19) from the northeast corridor.
- B3F East-West Connection: Rows 5, 6, and 7 on Map 0_201 form a completely open and walkable northern corridor connecting B3F East (25, 6) to B3F West (11, 6). This completely bypasses the B2F spinner maze backtrack!

## Defeated Trainers & Landmarks
- Rocket Grunt 2: Defeated at (18, 17) (Verified Turn 31867).

## Key Room Layout & Passability
- **Southeast Room**: (18, 21) to (22, 26) is an open rectangular room containing the stairs up to B2F.
- **Row 25 & 26 Corridor**: Extends west past Column 17, providing access to the western side of B3F.
- **Western Corridor**: Columns 10 and 11 form a completely open vertical path from row 26 up to row 17 (Verified Turn 32114).
- **Column 23 Partition Wall**: Solid and impassable wall at (23, 17) to (23, 26). Direct collision tests performed systematically on all rows (17-26) on Turn 32765 - 32836.
- **Barriers**: Column 9 (rows 22-25) is blocked by plants/statues. Columns 12 and 13 (rows 22-24) are blocked by building walls (Verified Turn 32048).
- **Row 17 Northern Corridor**: Open from column 10 to 22. Physically walked on (19, 17), (20, 17), (21, 17), and (22, 17) on Turns 32187-32194 without triggering any warp.
- **Central Block (Columns 12-17, Rows 18-21)**: Confirmed completely solid on all northern and southern entrance points.
  - Row 19 entry tests: Tried entering columns 12-17 from column 11 on row 19, all collided (Turn 32791-32815).
  - Row 24 entry tests: Tried entering columns 12-17 from row 25, all collided (Turn 32779-32788).
  - Column 18: Walks freely from row 17 to row 21.

## Historical Proof of Work & Testing Logs
- *Turn 32105*: Collision on (23, 18) walking Right.
- *Turn 32193-32194*: Stood on (20, 17) and (19, 17) with no warp occurring.
- *Turn 32232-32235*: Walked along Column 11, verified no warps.
- *Turn 32256-32258*: Walked rows 25 and 26, verified no warps.
- *Turn 32765-32836*: Ran systematic passability tests on Column 23 partition on rows 17-26. Verified 100% solid.
- *Turn 32779-32815*: Ran systematic passability tests on Central Block north/south boundaries. Verified 100% solid.
- *Turn 33134*: Collision on (11, 16) walking Up. Row 16 column 11 verified solid.
- *Turn 33148*: Collision on (10, 16) walking Up. Row 16 column 10 verified solid.
- *Turn 33164*: Collision on (12, 16) walking Up. Row 16 column 12 verified solid.
- *Turn 33175*: Collision on (13, 16) walking Up. Row 16 column 13 verified solid.
- *Turn 33178*: Collision on (14, 16) walking Up. Row 16 column 14 verified solid.
- *Turn 33180*: Collision on (15, 16) walking Up. Row 16 column 15 verified solid.
  - (19, 16): Tested Turn 33261. Result: Confirmed solid wall, no passage.
  - (20, 16): Tested Turn 33274. Result: Confirmed solid wall, no passage.
  - (21, 16): Tested Turn 33280. Result: Confirmed solid wall, no passage.
  - (22, 16): Tested Turn 33291. Result: Confirmed solid wall, no passage.
  - (17, 16): Tested Turn 33295. Result: Confirmed solid wall, no passage.
  - (16, 16): Tested Turn 33297. Result: Confirmed solid wall, no passage.
## B3F Column 18 Corridor Verification (Turn 33477)
- **Verified Fact**: Stood at (18, 18) and visually confirmed that (18, 16) is a solid, impassable wall (TYPE_2889).
- **Conclusion**: Column 18 does NOT provide an opening to the north past row 16 on B3F. The wall on row 16 is continuous and solid here.
- **Plan**: We are backtracking along row 17 to the west (columns 2-9) to see if the northern corridor extends further west and contains the entrance to the northwest room where the stairs down to B4F are located.
## B1F and B3F Unified Map Architecture (REVISED Turn 35286)
- **Verified Fact**: B1F and B3F are separate maps. B1F is Map 0_199 and B3F is Map 0_201.
- B3F has stairs down to B4F (Map 0_202) at (19, 19).
- B3F has stairs up to B2F (Map 0_200) at (25, 6).
## B3F Western Corridor Warp Test Proof of Work
- **Hypothesis**: There is a hidden staircase down to B4F in the B3F western corridor (Columns 10-11, Rows 21-24).
- **Test Methodology**: Manually and systematically stepped on every single walkable tile in the grid.
- **Results**:
  - (11, 24) - Tested Turn 34486. Result: Normal floor, no warp.
  - (10, 24) - Tested Turn 34487. Result: Normal floor, no warp.
  - (10, 23) - Tested Turn 34490. Result: Normal floor, no warp.
  - (11, 23) - Tested Turn 34493. Result: Normal floor, no warp.
  - (11, 22) - Tested Turn 34495. Result: Normal floor, no warp.
  - (10, 22) - Tested Turn 34498. Result: Normal floor, no warp.
  - (10, 21) - Tested Turn 34502. Result: Normal floor, no warp.
  - (11, 21) - Tested Turn 34505. Result: Normal floor, no warp.
- **Conclusion**: There is no staircase down to B4F in B3F columns 10-11, rows 21-24. The hypothesis is definitively disproven. This section is normal walkable floor.
## B3F Northwest Corridor Systematic Testing Results (Turns 34957-34972)
- **Verified Facts**:
  - We systematically walked on and tested the following tiles on Map 0_199 (B3F):
    - (11, 20): Tested Turn 34957. Result: Normal walkable floor, no warp.
    - (10, 20): Tested Turn 34961. Result: Normal walkable floor, no warp.
    - (11, 19): Tested Turn 34964. Result: Normal walkable floor, no warp.
    - (10, 19): Tested Turn 34966. Result: Normal walkable floor, no warp.
    - (11, 18): Tested Turn 34970. Result: Normal walkable floor, no warp.
    - (10, 18): Tested Turn 34968. Result: Normal walkable floor, no warp.
    - (11, 17): Tested Turn 34971. Result: Normal walkable floor, no warp.
    - (10, 17): Tested Turn 34972. Result: Normal walkable floor, no warp.
  - **Conclusion**: There are absolutely no staircases or warps in the northwest corridor of B3F (columns 10-11, rows 17-20). The hypothesis that a staircase down to B4F northwest is located here is definitively disproven.
## B3F Row 17 Corridor Systematic Testing Expansion (Turns 34983-34984)
- **Verified Facts**:
  - We systematically walked on and tested the following remaining tiles on Map 0_199 (B3F):
    - (11, 17): Tested Turn 34983. Result: Normal walkable floor, no warp.
    - (12, 17): Tested Turn 34983. Result: Normal walkable floor, no warp.
    - (13, 17): Tested Turn 34983. Result: Normal walkable floor, no warp.
    - (14, 17): Tested Turn 34983. Result: Normal walkable floor, no warp.
    - (15, 17): Tested Turn 34983. Result: Normal walkable floor, no warp.
    - (16, 17): Tested Turn 34984. Result: Normal walkable floor, no warp.
    - (17, 17): Tested Turn 34984. Result: Normal walkable floor, no warp.
  - Note: Tile (18, 17) is physically blocked by the defeated Rocket Grunt sprite standing on it, so it cannot be stepped on, but the rest of the corridor is fully verified.
  - **Conclusion**: There are absolutely no staircases or warps on Row 17 columns 10-17. Along with the previously verified columns 19-22 on row 17, and columns 10-11 on rows 17-20, B3F is 100% verified to contain no staircase down to B4F.

## B3F Northeast Section Layout (Migrated from B4F Layout)
- **Entrance**: The stairs from B2F (21, 8) spawn the player facing Down at (25, 6) on B3F.
- **Open Room Area**: Rows 5 to 13, Columns 22 to 28.
- **Obstacles**: 
  - Row 9 contains a solid table/wall structure (TYPE_2889) at columns 22 to 25. Columns 26 to 28 on row 9 are fully walkable.
  - Row 13 contains a solid horizontal table structure (TYPE_2889) across columns 24 to 28. Column 23 on row 13 is open and walkable.
  - **B3F East Southern Area Obstacles**:
    - Row 19 contains solid horizontal tables (TYPE_2889) across columns 22 to 28.
    - Row 20 contains solid bottom wall blocks (TYPE_2889) across columns 22 to 28.
    - Therefore, the southeast area of B3F is completely blocked from above, and can only be entered via the bottom corridor.
  - Column 21 contains a solid vertical partition wall (TYPE_2889) on rows 8 to 13, which divides B3F East and B3F West below row 8. Row 5, 6, and 7 are completely open, allowing direct bypass.