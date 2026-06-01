# Saffron Silph Co. 3F Layout & Exploration Records (Map 0_208)

## Overview & Coordinates
- **Elevator**: N/A on this floor (wait, is there an elevator on this floor? We should verify the layout, or does the elevator pass through all floors? Silph Co elevator usually goes to 11 floors).
- **Stairs**:
  - Stairs Down to 2F: at (26, 0) (ladder/staircase going down).
  - Stairs Up to 4F: at (24, 0) (staircase going up).
- **Warp**:
  - Warp at (27, 3): Labeled TYPE_dd92. Bidirectional warp connecting to Silph Co. 2F at (3, 3) (Verified Turn 41580).
- **Cleared Status**: Starting exploration of 3F.

## Floor Layout & Corridor Collisions
- Stand at (26, 1) facing Up.
- Horizontal corridor spans rows 1, 2, 3.
- Column 29 is a vertical wall (TYPE_2889).
- There is a warp tile at (27, 3).
- Let's systematically map this floor! We have the Card Key and can open doors and fight trainers. Let's document our progress.
## Western Unlocked Room (accessed via Card Key Door at 17, 8)
- **Layout**:
  - Door at (17, 8).
  - Inside room: Columns 10 to 16, Rows 5 to 12.
  - Large desk at (12, 8), (13, 8), (12, 9), (13, 9) (TYPE_2889).
  - Left side of the room (columns 0-9) has been explored.
- **Warp at (3, 11)**: Labeled TYPE_dd92. Bidirectional warp connecting to Silph Co. 9F at (9, 3) (Verified on Turn 41470).
- **Warp at (11, 11)**: Labeled TYPE_dd92. Bidirectional warp connecting to Silph Co. 7F at (5, 3) (Verified on Turn 41489).

## Permanent Spatial Constraints
- **Scientist at (7, 9)**: Defeated on Turn 41384. His sprite remains static at (7, 9) and permanently blocks column 7 on row 9.
  - To move vertically between the northern and southern parts of the western compartment, we must use column 8 or column 6, as column 7 is impassable at row 9.
- **Card Key Gate at (9, 9)**: Unlocked on Turn 41361, permanently passable.
- **Card Key Gate at (17, 8)**: Unlocked on Turn 41334, permanently passable.

## Friendly Hostage NPCs (Verified Non-Trainers)
- **Silph Employee at (24, 8)**: Met on Turn 41533. Friendly NPC, says "I work for SILPH. What should I do?"

## Newly Discovered Warp Candidates
- **Warp at (23, 11)**: Labeled TYPE_dd92. Bidirectional intra-floor warp connecting to Silph Co. 3F at (27, 15) (Verified on Turn 41542).
- **Warp at (27, 15)**: Labeled TYPE_dd92. Bidirectional intra-floor warp connecting to Silph Co. 3F at (23, 11) (Verified on Turn 41542).