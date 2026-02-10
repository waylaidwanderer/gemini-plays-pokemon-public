# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (7, 4), Murkrow (7, 2).
- **Theory**: **MIMIC** (Confirmed by T35639 success, failure due to wall at 11,4).
- **Constraint**: Murkrow hits walls and desyncs. Must check Murkrow's path for obstacles.
- **Pathing**:
  - Murkrow at (7, 2). Needs to cross Col 11.
  - Col 11 Obstacles: (11, 3), (11, 4) are Walls. (11, 2), (11, 5) are Open.
  - Current Y=2. Path blocked at (8, 2) by wall?
    - Map says (8, 2) is `TYPE_2889` (Wall).
    - So Murkrow CANNOT leave Col 7 at Y=2.
  - Must move Murkrow to Y=3?
    - (8, 3) is Open.
    - But (11, 3) is Blocked.
  - Plan:
    1. Move **Down** to (7, 5). Murkrow -> (7, 3).
    2. Move **Right** to (8, 5). Murkrow -> (8, 3).
    3. Move **Down** to (8, 7). Murkrow -> (8, 5).
    4. Move **Right** past Col 11 (row 5 is open).
- **Action**: Move **Down** to (7, 5).

## Map Notes

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