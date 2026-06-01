# Saffron Silph Co. 4F Verified Layout & Exploration Records (Map 0_209)

## Overview & Coordinates
- **Elevator**: Located at (20, 0) (leads to all floors 1F-11F).
- **Stairs**:
  - Stairs Down to 3F: at (24, 0).
  - Stairs Up to 5F: at (26, 0).
- **Cleared Status**: Sweeping floor.

## Verified Obstacles & Corridor Collisions
- Card Key Door opened at (4, 12).
- Rocket Grunt defeated at (9, 14) on Turn 40690 (originally mapped as 12,14).
- Scientist defeated at (14, 6).
- Rocket Grunt defeated at (26, 7) on Turn 41759.

## 4F Clearance Plan (Turn 41732)
- **Current Status**: Swept eastern elevator/lobby area. Left side has been previously accessed but needs systematic verification.
- **Exploration Path**:
  1. Explore the western compartment:
     - Card Key door at (4, 12) was opened.
     - Warp at (3, 15) connects to 10F (13, 15).
     - Warp at (11, 7) connects to 10F (9, 11).
     - Warp at (17, 11) connects to 10F (13, 7).
     - Warp at (17, 3) connects to 6F (3, 3).
  2. Locate all items on 4F:
     - Full Heal (expected in west room).
     - Max Ether (expected on 4F).
     - Escape Rope (expected on 4F).
     We should systematically walk the western rooms to find these items.

## Warp Transitions
- **Warp at (17, 11)**: Labeled TYPE_dd92. Bidirectional warp connecting to Silph Co. 10F at (13, 7).
- **Warp at (17, 3)**: Labeled TYPE_dd92. Bidirectional warp connecting to Silph Co. 6F at (3, 3).
- **Warp at (3, 15)**: Labeled TYPE_dd92. Bidirectional warp connecting to Silph Co. 10F at (13, 15).
- **Warp at (11, 7)**: Labeled TYPE_dd92. Bidirectional warp connecting to Silph Co. 10F at (9, 11).

## Western Compartment Clearance Plan (Turn 42066)
- **Active Exploration Strategy**: We are currently standing at (1, 3) in the northwest corridor of Silph Co. 4F.
- **Observed Room Layout**:
  - Main desk/terminal partition blocks columns 2 to 6 on rows 2 to 7.
  - Column 1 corridor (rows 1-7) is completely open.
  - Row 1 corridor (columns 1-6) is completely open.
  - Scientist standing at (6, 2) is currently blocking row 2 at column 6.
- **Search Strategy for Missing 4F Items**:
  - We expect to find Full Heal, Max Ether, and Escape Rope in this western compartment.
  - Since the floor item sprites are solid overworld Pokéballs, let's systematically walk the perimeter of the northwest room:
    1. Walk North up Column 1 to Row 1 (1, 1).
    2. Walk East along Row 1 from (1, 1) to (5, 1) to inspect the top-right corner above the machines.
    3. Stand adjacent to the Scientist at (6, 2) from (5, 2) or (6, 1) to see if we need to battle him or if an item is behind him.
    4. If the northwest room is completely clear, we will move to the southwest room's western edge (columns 1-3, rows 13-16) to systematically inspect that corner.
    5. Once 4F is completely cleared of these items, we will walk back to the warp at (17, 11) to return to 10F, or use the warp at (3, 15) to return to 10F, or ride the elevator to proceed to the next floor.