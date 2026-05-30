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
  - (18, 20): Tested Turn 33037. Result: Normal floor, no warp.
  - (19, 20): Tested Turn 33042. Result: Normal floor, no warp.
  - (20, 20): Tested Turn 33043. Result: Normal floor, no warp.
  - (21, 20): Tested Turn 33050. Result: Normal floor, no warp.
  - (22, 20): Tested Turn 33057. Result: Normal floor, no warp.
  - (22, 21): Tested Turn 33064. Result: Normal floor, no warp.
  - (21, 21): Tested Turn 33068. Result: Normal floor, no warp.
  - (20, 21): Tested Turn 33078. Result: Normal floor, no warp.
  - (19, 21): Tested Turn 33084. Result: Normal floor, no warp.
  - (18, 21): Tested Turn 33086. Result: Normal floor, no warp.
  - (18, 22): Tested Turn 33097. Result: Normal floor, no warp.
  - (19, 22): Tested Turn 33100. Result: Normal floor, no warp.
  - (20, 22): Tested Turn 33101. Result: Normal floor, no warp.
  - (21, 22): Tested Turn 33103. Result: Normal floor, no warp.
  - (22, 22): Tested Turn 33105. Result: Normal floor, no warp.
  - (22, 23): Tested Turn 33107. Result: Normal floor, no warp.
  - (21, 23): Tested Turn 33109. Result: Normal floor, no warp.
  - (18, 23): Tested Turn 33200. Result: Normal floor, no warp.
  - (19, 23): Tested Turn 33200. Result: Normal floor, no warp.
  - (20, 23): Tested Turn 33200. Result: Normal floor, no warp.
  - (18, 24): Tested Turn 33201. Result: Normal floor, no warp.
  - (19, 24): Tested Turn 33201. Result: Normal floor, no warp.
  - (20, 24): Tested Turn 33201. Result: Normal floor, no warp.
  - (22, 24): Tested Turn 33213. Result: Normal floor, no warp.
  - (20, 25): Tested Turn 33213. Result: Normal floor, no warp.
  - (21, 25): Tested Turn 33213. Result: Normal floor, no warp.
  - (22, 25): Tested Turn 33213. Result: Normal floor, no warp.
  - (18, 25): Tested Turn 33215. Result: Normal floor, no warp.
  - (19, 25): Tested Turn 33215. Result: Normal floor, no warp.
  - (18, 26): Tested Turn 33215. Result: Normal floor, no warp.
  - (19, 26): Tested Turn 33215. Result: Normal floor, no warp.
  - (20, 26): Tested Turn 33215. Result: Normal floor, no warp.
  - (21, 26): Tested Turn 33215. Result: Normal floor, no warp.
  - (22, 26): Tested Turn 33215. Result: Normal floor, no warp.

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