# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Player (9, 5), Murkrow (8, 4).
- **Testing**:
  - Move Right (to 9, 5): FAILED. Murkrow stayed at (8, 4).
  - Hypothesis: Diagonal misalignment or mimic failure.
  - Plan:
    1. Move Down to (9, 6). (Attempt to pull Murkrow to 8, 5).
    2. If successful (Murkrow at 8, 5), Move Right.
    3. If failed, re-align.
- **Goal**: Lead Murkrow to Boss Door at (23, 14).

## Key Info
- **Passwords**: "RATICATE TAIL", "SLOWPOKETAIL", "HAIL GIOVANNI".
- **Boss Door**: Needs Voice ID (Murkrow).

## Map Notes
- **Walls**: Row 4 Wall at x=11 blocks Murkrow if it's on Row 4. Must lower it to Row 5.
- **Traps**: Warp Trap at (26, 10).