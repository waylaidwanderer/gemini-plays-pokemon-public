# Fuchsia Gym Invisible Walls Mapping (Scratchpad)
- **Start Turn**: 43409
- **Objective**: Map the invisible walls of Fuchsia Gym (Map 0_157) through empirical testing.

## Discovered Obstacles & Wall Layout
- **Row 12**: (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12) are solid.
- **Row 11**: (0, 11), (1, 11), (2, 11), (7, 11) are solid.
- **Row 4**: (0, 4), (1, 4), (4, 4), (7, 4) are solid.
- **Row 5**: (4, 5), (7, 5) are solid.
- **Gym Statues**: (3, 14)-(3, 15) and (6, 14)-(6, 15) are solid wall blocks (TYPE_2889).

## Navigation Routes
- **Detour to West Side**: From (5, 13), detour East to Row 17, Up Column 9 to Row 1, Left along Row 1 to (3, 1) [passable boundary between (3, 1) and (4, 1)], and Down Column 1/2 to Koga at (4, 10).

## Row 16/17 Vertical Transition Testing (Turn 44105)
- **Problem**: Our 42-step pathfinder run on Turn 44098 failed to go north and left us at (5, 17), suggesting that the boundary between Row 16 and Row 17 is blocked vertically.
- **Hypothesis**: There is a horizontal invisible wall blocking some or all vertical transitions between Row 16 and Row 17.
- **Testing Plan**:
  - Step 1 (Turn 44105): Currently at (5, 17) facing Up. Press "Up" once. Check if we reach (5, 16).
  - Step 2: If blocked, we will walk left/right on Row 17 and systematically test other columns.
- **Results**: Verified on Turn 44110. Player successfully walked Up from (5, 17) to (5, 16). The boundary is completely passable.
- **Conclusion**: The vertical transition from (5, 17) to (5, 16) is NOT blocked by any invisible wall. The previous pathfinder failure must have been due to some other cause (such as the pathfinder attempting to cross a different, actual invisible wall on its way). Row 16/17 boundary is passable.