# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (9, 4), Murkrow (9, 3).
- **Observation**:
  - T35659: Player Right (8, 4 -> 9, 4) -> Murkrow Right (8, 3 -> 9, 3).
  - **MIMIC CONFIRMED** (at least for Right movement).
- **Obstacle**: Walls at (11, 3) and (11, 4) block Eastward progress in current rows.
- **Solution**: Move Murkrow to Row 5 (Open at Col 11).
- **Plan**:
  1. Move **Down** to (9, 5). Expect Murkrow -> (9, 4).
  2. Move **Down** to (9, 6). Expect Murkrow -> (9, 5).
  3. Move **Right** to (15, 6) carrying Murkrow in Row 5.
  4. Navigate to Boss Door.

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