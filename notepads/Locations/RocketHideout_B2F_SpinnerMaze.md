# Rocket Hideout B2F Spinner Maze Layout (Verified Turn 31668)

## Stop Tiles (TYPE_55d4)
- (2, 9)
- (8, 11)
- (14, 15)
- (9, 16)

## Spinners (Arrows)
- (4, 9): Left (TYPE_55d0)
- (4, 11): Right (TYPE_64a2)
- (4, 15): Right (TYPE_64a2)
- (5, 14): Right (TYPE_64a2)
- (8, 9): Left (TYPE_55d0)
- (8, 12): Up (TYPE_cf9b)
- (8, 15): Up (TYPE_cf9b)
- (9, 14): Down (TYPE_55cd)
- (10, 9): Left (TYPE_55d0)
- (10, 10): Up (TYPE_cf9b)
- (10, 15): Up (TYPE_cf9b)
- (11, 14): Down (TYPE_55cd)

## Impassable Obstacles (TYPE_2889)
- (6, 7)
- (2, 8), (3, 8), (4, 8), (6, 8), (8, 8), (10, 8)
- (2, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (11, 10)
- (2, 11), (11, 11)
- (2, 12), (4, 12), (5, 12), (7, 12), (9, 12), (11, 12)
- (5, 13), (6, 13), (7, 13), (9, 13)
- (2, 14), (3, 14)
- (11, 24) to (15, 24) (solid divider green blocks, verified Turn 34221)
- Screen-Verified obstacles (Turn 35582):
  - (15, 12) to (17, 12) (Green blocks)
  - (15, 13) (Green block)
  - (12, 14) to (15, 14) (Green blocks)
  - (17, 14) to (17, 16) (Green blocks)
  - (15, 15) (Green block)
  - (12, 15) to (13, 15) (Green blocks) (Physically tested on Turn 36650: attempting to walk Right from (11, 15) results in collision at (12, 15). This confirms these tiles are 100% solid walls)
  - (15, 19) to (15, 22) (Green blocks)
  - (14, 19) (Green block)
  - (11, 21) to (13, 21) (Green blocks)
  - (17, 17) to (18, 17) (Green blocks)
  - (17, 18) to (17, 19) (Green blocks)
  - (18, 14) to (18, 16) (Vertical partition wall blocks)
  - (18, 18) to (18, 19) (Vertical partition wall blocks)
  - (19, 16) to (20, 16) (Horizontal partition wall blocks)
  - (18, 22) (Elevator door block)

## Normal Walkable Floor Tiles (TYPE_3fe2)
- Row 7: (2, 7) to (5, 7), (7, 7) to (11, 7)
- Row 8: (5, 8), (7, 8), (9, 8), (11, 8)
- Row 9: (3, 9), (5, 9) to (7, 9), (9, 9), (11, 9)
- Row 10: (3, 10), (4, 10)
- Row 11: (3, 11), (5, 11) to (7, 11), (9, 11), (10, 11)
- Row 12: (3, 12), (6, 12), (10, 12)
- Row 13: (2, 13) to (4, 13), (8, 13), (10, 13), (11, 13)
- Row 14: (4, 14), (6, 14) to (8, 14), (10, 14)
- Row 15: (2, 15), (3, 15), (5, 15) to (7, 15), (11, 15)

## Southern Area Verified Layout & Routing (Turns 31720-31802)
### Stop Tiles (TYPE_55d4)
- (15, 18): Stop tile below Row 16 exit.
- (11, 20): Stop tile in south-central corridor.
- (9, 24): Stop tile in south-western corner.
- (14, 25): Stop tile in south-eastern corner.

### Spinners (Arrows)
- (13, 18): Left (TYPE_55d0) -> Slides to (11, 20) via (11, 18) Down spinner.
- (13, 22): Left (TYPE_55d0) -> Slides to (9, 24) via (9, 22) Down spinner.
- (10, 25): Right (TYPE_64a2) -> Slides to (14, 25) stop tile.

### Southern Pathways & Walkable Floors (TYPE_3fe2)
- Row 20: (10, 20) to (14, 20) [connected to 11, 20 stop tile]
- Row 21: (16, 21) to (22, 21) [fully open east-west corridor]
- Row 22: (10, 22) to (12, 22), (14, 22) [Row 14, 22 leads to 13, 22 Left spinner]
- Row 25: (11, 25) to (13, 25), (15, 25) to (16, 25) [Row 14, 25 stop tile leads right to 16, 25, then Up to Row 21]

### Key Landmarks & Transitions
- Stairs DOWN to B3F: Located in the south-east corridor at (21, 22) (Verified Turn 31802).
- Elevator Warp: Located at (25, 19). Entering this warp on Turn 32141 takes you to the Elevator Cabin (Map 0_203). It requires the LIFT KEY to operate.
- **Verified Fact (Turn 32686)**: The eastern portion of B2F is completely divided by a solid horizontal wall at row 16 extending from column 18 all the way to column 27 (TYPE_2889). No direct vertical pathway exists from the northeast area down to the southeast area on the east side of row 16. The only way to reach the stairs down at (21, 22) and the elevator at (25, 19) is to navigate the western spinner maze.
- **Spinner Maze (2, 9) to (15, 18) Bypass Route**: Fully verified and corrected on Turn 32928.
  - Starting at (2, 9), walk: `Right, Down, Down, Down, Down, Right, Down, Right, Right, Right, Right, Right, Down, Right, Right, Right, Right, Down` (18 steps).
  - *Correction Note (Turn 32928)*: The previous 17-step sequence was missing a 5th horizontal `Right` step on row 16 (index 11). This caused the player to walk `Down` into a trap at (12, 17) and slide to (16, 13) instead of stepping onto the (13, 16) Right-spinner to slide to (15, 18). Adding the 5th `Right` ensures the player steps onto (13, 16) to slide safely to (15, 18).
  - This path avoids the (8, 11) cul-de-sac trap and safely exits the maze at stop tile (15, 18).
- Route to Stairs: Slide from (15, 18) Left onto (13, 18) -> slides to (11, 20). Go Right to (14, 20) -> Down to (14, 22) -> Left onto (13, 22) -> slides to (9, 24). Go Right to (10, 24) -> Down onto (10, 25) -> slides to (14, 25). Walk Right to (16, 25) -> Up to (16, 21) -> Right to (21, 21) -> Down to (21, 22).
- **Direct Vertical Shortcut (Turn 34066)**: Rows 14 and 15 are completely open and walkable on columns 23 and 24, providing a direct horizontal walkway past the Column 23 partition wall. This allows players to walk directly from the eastern stairs landing at (27, 8) to the western area above the row 16 dividing wall, bypassing the spinners completely.