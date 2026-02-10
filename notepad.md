# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (10, 5), Murkrow (7, 2).
- **Correction**: Visual confirmation shows Murkrow is NOT at (9, 4) or (10, 4). It is back at (7, 2).
- **Analysis**: The "Stacking" plan failed because Murkrow stopped following (Range/Wall reset).
- **Puzzle State**: Murkrow trapped in Col 7 (Walls at x=6, x=8).
- **Solution Path**:
  1. Murkrow MUST exit Col 7 via (7, 3) -> (8, 3) because (7, 1) is a dead end (Walls at 6,1 and 8,1).
  2. To move Murkrow to (7, 3), I must trigger a Y-axis move without blocking (7, 3).
  3. Player cannot be in Col 7 during the move.
- **Plan**:
  1. Return to (8, 5).
  2. Move **Down** to (8, 6).
     - If Mimic: Murkrow (7, 2) -> (7, 3).
     - If Mirror: Murkrow (7, 2) -> (7, 1) (Bad).
  3. If that fails, try moving **Up** from (8, 6) to (8, 5) (Mirror check).

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