# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Puzzle (B2F)
- **Status**: Interacting with Murkrow at (7, 2). Player at (7, 3).
- **Issue**: Murkrow stopped moving in previous turns. Interaction resets/wakes it.
- **Current Mechanics Hypothesis**: 
  - Murkrow mimics player inputs (Up/Down/Left/Right).
  - Tether breaks if distance > X (likely 3 or 4).
  - Walls block movement (Player moves, Murkrow hits wall -> Desync).
- **Plan**:
  1. Finish Dialogue.
  2. Test Move RIGHT to (8, 3). (Expect M -> 8, 2).
  3. If successful, use "Row 6 Slide" or similar strategy.

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap / (15, 12) Floor (Bottom Path).
  - (14, 11) Locked Shutter.