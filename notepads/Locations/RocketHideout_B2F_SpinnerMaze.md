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
- Elevator Door: Located at (18, 22). Tested on Turn 31901. Confirmed to be closed/locked and impassable, with no interactive text box.
- Route to Stairs: Slide from (15, 18) Left onto (13, 18) -> slides to (11, 20). Go Right to (14, 20) -> Down to (14, 22) -> Left onto (13, 22) -> slides to (9, 24). Go Right to (10, 24) -> Down onto (10, 25) -> slides to (14, 25). Walk Right to (16, 25) -> Up to (16, 21) -> Right to (21, 21) -> Down to (21, 22).