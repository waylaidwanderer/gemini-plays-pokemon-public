# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (9, 3), Murkrow (7, 2).
- **Test**: Move **Down** to (9, 4).
  - Expectation (Mirror): Murkrow moves **Up** to (7, 1).
  - Expectation (Mimic): Murkrow moves **Down** to (7, 3).
- **Plan**:
  1. Move **Down** to (9, 4).
  2. If Murkrow goes Up to (7, 1):
     - I need to push it Down past (7, 3).
     - Move Left to (8, 4). Move Up to (8, 3) -> Murkrow Down to (7, 2).
     - Move Up to (8, 2) -> Blocked.
     - Move Right to (9, 3) -> Murkrow Left to (6, 2) (Blocked).
     - Need a new angle.
  3. If Murkrow goes Down to (7, 3):
     - It's Mimic.

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