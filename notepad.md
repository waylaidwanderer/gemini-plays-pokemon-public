# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (10, 6), Murkrow (7, 2).
- **Correction**: Murkrow did NOT follow to Col 10. It is back/still at (7, 2).
- **Hypothesis**: Murkrow has a range limit or hit a wall and desynced.
- **Plan**:
  1. Return to proximity (Col 7/8).
  2. Test Mechanics again (Mirror vs Mimic).
  3. **Escape Strategy**:
     - **If Mirror**: Align Player (7, 5) & Murkrow (7, 2). 
       - Move Up -> (7, 4) / Murkrow -> (7, 3).
       - Move Right -> (8, 4) / Murkrow Stays (Blocked Left).
       - Move Left -> (7, 4) / Murkrow Right -> (8, 3).
     - **If Mimic**: Align Player (7, 5) & Murkrow (7, 2).
       - Move Down -> (7, 7) / Murkrow -> (7, 4).
       - Move Right -> (8, 7) / Murkrow -> (8, 4).

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