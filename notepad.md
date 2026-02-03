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
- **Location**: B1F NE Section (near stairs from B2F), entering Trap Room.
- **Items**: "RATICATE TAIL" (Password 1), "SLOWPOKETAIL" (Password 2).
- **Missing**: Murkrow Voice (Password 3 equivalent).
- **Plan**: Go to B1F NE (Trap Room) via B2F NE Stairs (27, 2). Find hidden switch or Murkrow.

## Investigation Log
- **Computers**: Top row in NE Room (20-22, 2) are SOLID. No passage.
- **Warps**: (19, 1) was safe on last pass.
- **Solid Walls**: B2F (3, 11) is solid.
- **Anomaly**: Stairs at B2F (3, 14) are `TYPE_3fe2` (Walkable) but did not trigger warp on first attempt.
- **Action**: Attempting to walk deeper into the stairs (South) to trigger warp.
- **Contingency**: If stairs fail, must re-evaluate access to B1F SW (perhaps via B1F Center/Trap Room).