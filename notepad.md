# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (10, 2), Murkrow (7, 2).
- **Mechanics**: **Inconsistent**.
  - T35620: Player Down -> Murkrow Up (Mirror).
  - T35627: Player Up -> Murkrow Stayed (Unexpected).
- **Hypothesis**:
  1. It might be a **MIMIC** and (7, 1) is blocked? (7, 1 is visually open).
  2. It might be **MIRROR** and (7, 3) is blocked? (7, 3 is visually open).
  3. It only moves when I'm in specific zones?
- **Plan**:
  1. Move **Up** to (10, 1).
  2. Observe Murkrow.
     - If it goes to (7, 1) -> Mimic.
     - If it goes to (7, 3) -> Mirror.
     - If it stays -> Stuck/Undefined.

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