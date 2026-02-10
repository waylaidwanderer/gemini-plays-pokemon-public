# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (7, 4), Murkrow (7, 2).
- **Strategy**: Vertical Ratchet.
- **Plan**:
  1. Move **Down** to (7, 5). Expect Murkrow -> (7, 1) (Up).
  2. Move **Down** to (7, 6). Expect Murkrow -> Blocked at Top (Stay at 7, 1).
     - *This increases the distance between us.*
  3. Move **Up** repeatedly to push Murkrow South.
     - Player (7, 5) -> Murkrow (7, 2).
     - Player (7, 4) -> Murkrow (7, 3).
     - Player (7, 3) -> Murkrow (7, 4).
     - Player (7, 2) -> Murkrow (7, 5).

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