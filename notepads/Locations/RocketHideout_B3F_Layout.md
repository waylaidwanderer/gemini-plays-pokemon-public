# Rocket Hideout B3F Detailed Layout & Routing

## Stairs and Key Transitions
- B2F to B3F Stairs: Entrance warp at B3F (21, 25), leading from B2F (21, 22). Located in the southeast open room.
- B3F to B4F Stairs: Under Systematic Testing.
  - (19, 18): Tested Turn 33001. Result: Normal floor, no warp.
  - (20, 18): Tested Turn 33006. Result: Normal floor, no warp.
  - (21, 18): Tested Turn 33015. Result: Normal floor, no warp.
  - (22, 18): Tested Turn 33016. Result: Normal floor, no warp.
  - (19, 19): Tested Turn 33018. Result: Normal floor, no warp.
  - (18, 19): Tested Turn 33029. Result: Normal floor, no warp.

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