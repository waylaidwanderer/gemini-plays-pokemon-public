# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (7, 4), Murkrow (7, 2).
- **Confirmed Mechanics**:
  - **Mimicry**: Confirmed in previous turns (e.g., T35659, T35639).
  - **Constraint**: Murkrow gets stuck if path is blocked (Walls) or if Player gets too far (Range > 1?).
  - **Current Trap**: Murkrow is at (7, 2). Walls at (6, 2) and (8, 2) prevent X-axis movement.
  - **Vertical Block**: Moves to escape (7, 2) failed.
    - Player Down (7,3->7,4) -> Murkrow (7,2) STAYED.
    - Player Up (7,4->7,3) -> Murkrow (7,2) STAYED.

## Plan
- **Hypothesis**: Murkrow needs to be "bumped" or interacted with to unstick, OR specific proximity is needed.
- **Action**: 
  1. Move **Up** to (7, 3).
  2. Move **Up** to (7, 2) (Attempt to bump/interact).
  3. If it flies away, track it.
  4. If it stays, try moving **Right** from (7, 3) to (8, 3) to see if it mimics diagonally or frees itself.

## Map Notes
- **Walls**: (6, 2) and (8, 2) block Murkrow at Row 2.
- **Shutters**: (15, 10) likely Locked.
- **Traps**: Warp Trap at (26, 10).

## History
- Switches pressed: B1F (24, 1) and B1F (6, 1).
- Passwords found: "RATICATE TAIL", "SLOWPOKETAIL", "HAIL GIOVANNI".