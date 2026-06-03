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

## Row 7/8 Column 1 Vertical Transition Testing (Turn 44129)
- **Problem**: Our 6-step path from (3, 4) to (1, 8) failed on the final step, leaving us at (1, 7) facing Down.
- **Hypothesis**: There is an invisible wall blocking the vertical boundary between Row 7 and Row 8 at Column 1.
- **Testing Plan**:
  - Step 1 (Turn 44129): Standing at (1, 7) facing Down, we pressed "Down".
- **Results**: We remained at (1, 7) on Turn 44132.
- **Conclusion**: The transition between (1, 7) and (1, 8) is blocked by an invisible wall.