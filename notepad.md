# Team Rocket HQ (Mahogany Town)
## Objectives
- **Primary**: Open Boss Door on B2F (Requires Murkrow Voice + "Raticate Tail").
- **Secondary**: Find Hidden Switch in B1F NE Room to open Shutters/Boss Door.
- **Tertiary**: Catch Murkrow.

## Map Structure & Navigation
- **IDs**: Map `3_51` = B1F (Upper). Map `3_50` = B2F (Lower).
- **B1F (Upper Floor)**:
  - **North Corridor (Row 1-2)**: Connects NW and NE.
    - **Hazard**: Warp Trap likely near x=19 (Row 1). Row 2 is safe.
    - **Blocker**: Grunt at (4, 1). Bypass via (3, 1)->(3, 2)->(4, 2)->(5, 2)->(5, 1).
  - **NE Room ("Trap Room")**:
    - **Entrances**: Gap at (24, 2).
    - **Contents**: Statues, Voltorb traps, Grunts, Murkrow (inaccessible area?), Computers (Row 2 are SOLID).
- **B2F (Lower Floor)**:
  - **West Section**: Segmented.
    - **NW Room**: Small viewing room with Silver. Stairs at (3, 2) lead to B1F NW.
    - **West Mid**: Dead end pocket via (3, 6).
    - **SW**: Access to South Corridor via (3, 14).
  - **Center**: Contains Boss Door. Blocked by shutters.
  - **East**: Access via SE Stairs (27, 14) or NE Stairs (27, 2).

## Current Status
- **Location**: B2F SE Section (at stairs).
- **Items**: "RATICATE TAIL" (Password 1), "SLOWPOKETAIL" (Password 2).
- **Missing**: Murkrow Voice (Password 3 equivalent).
- **Plan**: Ascend to B1F SE via stairs (27, 14), then navigate to False Computer at (26, 10).

## Investigation Log
- **Computers**: Top row in NE Room (20-22, 2) are SOLID. No passage.
- **Warps**: (19, 1) was safe on last pass.
- **Solid Walls**: B2F (3, 11) is solid.
- **Anomaly**: Stairs at B2F (3, 14) are `TYPE_3fe2` (Walkable) but did not trigger warp on first attempt.
- **Action**: Attempting to walk deeper into the stairs (South) to trigger warp.
- **Contingency**: If stairs fail, must re-evaluate access to B1F SW (perhaps via B1F Center/Trap Room).
- **Anomaly**: Turn 26918 - Found myself back on B2F (3_50) at (27, 14) after attempting to navigate B1F. Possible stair warp loop or input error.
- **Action**: Manually re-triggering warp to B1F by stepping Left then Right.
- **Transition**: Successfully warped to B1F (3_51) at (27, 14).
- **Navigation**: Heading North via East Corridor (Col 28) to access NE Room from the North, targeting False Computer at (26, 10).
- **Hazard**: Path West from SE Stairs on B1F (Row 14 -> Up) triggers a warp back to B2F. Likely a statue alarm.
- **Strategy**: Try hugging the East wall (Col 27) North from the stairs to reach the computer at (26, 10).
- **Tactical Update**: Direct North path from SE Stairs is blocked by Statue Alarms (Col 26/27).
- **New Route**: Flank South along the bottom wall (Row 16).
  1. Go East to Col 28 (Safe).
  2. Go South to Row 16.
  3. Go West along Row 16 to Col 22.
  4. Go North up Col 22 to access the center area from the West.
  5. Approach False Computer (26, 10) from the West/South-West.
- **Route Update**: Moving North via safe East Corridor (Col 28) to bypass Statue Alarms at (27, 12-13) and Wall at (27, 4-11).
- **Target**: Cross West at Row 3, then South down Col 26 to False Computer at (26, 10).
- **Investigation**:
  - Investigated Backstage Area (Row 5).
  - Checked Wall (Row 4) and Back of Obstacles (Row 6) from Col 26 to 23. Empty so far.
  - Checked Computer Stack at Col 27. Empty.
  - Checked Computers at Col 25. Empty.
- **Current Action**: Continuing sweep West along Row 5 to (19, 5).
- **Goal**: Find Hidden Switch to open Boss Door.