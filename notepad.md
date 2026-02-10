# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player Moving to (7, 4). Murkrow at (7, 2) [RESET].
- **Failure Analysis**:
  - Previous attempt "Row 3 Slide" failed because Murkrow was actually on Row 1 (hit walls) or Row 2 (trapped).
  - Offset calculation was wrong.
- **New Plan (The "Row 5/3 Offset")**:
  1. Return to (7, 4). Murkrow stays at (7, 2).
  2. Move Down to (7, 5). Murkrow moves to (7, 3).
     - Gap established: Player +2 Rows from Murkrow.
  3. Slide Right to (10, 5). Murkrow slides to (10, 3).
  4. Move Down 3 times to (10, 8).
     - P(10, 6) -> M(10, 4).
     - P(10, 7) -> M(10, 5).
     - P(10, 8) -> M(10, 6).
  5. Murkrow is now on Row 6 (Clear Path).
  6. Slide Right along Row 8 (Player) / Row 6 (Murkrow).
- **Goal**: Lead Murkrow to Boss Door at (23, 14).

## Key Info
- **Passwords**: "RATICATE TAIL", "SLOWPOKETAIL", "HAIL GIOVANNI".
- **Boss Door**: Needs Voice ID (Murkrow).

## Map Notes
- **Walls**: Desk at (11, 3)-(13, 4).
- **Chairs**: Row 5 has chairs (likely solid). Row 6 is clear.
- **Traps**: Warp Trap at (26, 10).