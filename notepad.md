# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (10, 2), Murkrow (7, 2).
- **Goal**: Guide Murkrow to Boss Door (23, 14).
- **Mechanics**: **MIRROR** (Axis Y=3, X=8).
- **Problem**: Murkrow stuck in Col 7. Needs to reach (7, 3) to escape to Col 8.
- **Hypothesis**: Direct P(Y=4->3) failed. Need to "pump" it from a different sync state.
- **Plan**:
  1. Move **Down** to (10, 3). Expect M -> (7, 1).
  2. Move **Down** to (10, 4). Expect M -> Stay (7, 1) (Hit Wall).
  3. Move **Up** to (10, 3). Expect M -> (7, 2).
  4. Move **Up** to (10, 2). Expect M -> (7, 3).

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