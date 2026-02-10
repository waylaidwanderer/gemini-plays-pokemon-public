# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (7, 5), Murkrow (7, 2).
- **Hypothesis**: **MIMIC** mechanics require Distance <= 1 (Y-axis).
  - Failed at Y-Dist 2 and 3.
  - Succeeded at Y-Dist 1 (Turn 35658).
- **Plan**:
  1. Move **Up** to (7, 4). (No reaction expected).
  2. Move **Up** to (7, 3). (No reaction expected).
  3. **Trigger**: Move **Down** to (7, 4).
     - Player `dy=1`. Murkrow `dy=1` -> (7, 3).
  4. **Escape**: Move **Right** to (8, 4).
     - Player `dx=1`. Murkrow `dx=1` -> (8, 3). **ESCAPE!**

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