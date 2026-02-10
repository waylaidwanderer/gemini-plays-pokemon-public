# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (8, 4), Murkrow (7, 2).
- **Hypothesis**: X-axis movement is blocked by walls at (6, 2) and (8, 2).
- **Test**: From (8, 4), move **Up** to (8, 3).
  - Mirror: Murkrow (7, 2) -> (7, 3) (Down).
  - Mimic: Murkrow (7, 2) -> (7, 1) (Up).
- **Plan**:
  1. Move **Left** to (8, 4).
  2. Move **Up** to (8, 3).
  3. If Mirror (M at 7, 3), move Right to ratchet M to Col 8? No, (8, 3) is Player.
     - If M is at (7, 3) and Player at (8, 3):
     - Player Right -> (9, 3). M Left -> (6, 3) (Wall). M stays at (7, 3).
     - Player Left -> (8, 3). M Right -> (8, 3) (Collision??).

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