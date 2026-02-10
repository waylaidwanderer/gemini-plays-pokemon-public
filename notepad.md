# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (8, 3), Murkrow (7, 2).
- **Mechanics**: **MIRROR** (Likely).
  - Hypothesis: It toggles between (7, 1) and (7, 2) when I move Down/Up.
  - Goal: Force it to (7, 3).
- **Plan**:
  1. Move **Right** to (9, 3). Murkrow tries Left (Wall), Stays at (7, 2).
  2. Move **Up** to (9, 2) (Desk/Wall? Check map). 
     - If (9, 2) is blocked, I can't move Up.
     - Mental Map says (9, 2) is "Desk/Wall". This might be a problem.
     - (9, 1) is TYPE_2889 (Wall). (9, 2) is TYPE_2889 (Wall).
     - I CANNOT move Up at Col 9?
     - Let's check Col 10. (10, 2) is TYPE_3fe2 (Walkable).
  3. **Revised Plan**:
     - Move **Right** to (10, 3).
     - Move **Up** to (10, 2). Murkrow moves Down to (7, 3).
     - Move **Up** to (10, 1). Murkrow moves Down to (7, 4).
     - Move **Left** to (3, 1) (Ratchet).

## Map Notes
- **Walls**: (6, 2) separates NW and N areas.
- **Shutters**: (15, 10) likely Locked.
- **Traps**: Warp Trap at (26, 10) - AVOID.
- **Trap Loop**: (3, 6) on B1F/B2F connects the two floors. One-way or toggled.

## History
- Switches pressed: B1F (24, 1) and B1F (6, 1).
- Passwords found: "RATICATE TAIL", "SLOWPOKETAIL", "HAIL GIOVANNI".
- **Anomaly**: Murkrow missing from (7, 2) and expected mirrored positions (7, 0-2) after moving Right, Down x4.
- **Hypothesis**: Murkrow might have moved through walls, flown off-screen, or mechanics are different (e.g., rotation). Checking with simulation.
- **Test Result**: Moving Left kept Murkrow at (7, 2).
- **Analysis**: (6, 2) is Wall, (8, 2) is Wall. X-axis movement is blocked for both Mimic and Mirror.
- **Next Step**: Move Down to test Y-axis (both (7, 1) and (7, 3) are open).