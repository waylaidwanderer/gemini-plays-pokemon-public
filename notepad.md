# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Murkrow Mechanics (Verified)
- **Mimicry**: Intended behavior is mimicry.
- **Status**: Currently unresponsive/static at (7, 2).
- **Hypothesis**: Previous "Move Down" input was ignored due to active text box.
- **Test**: Clean Move Down to (7, 4).
  - Expectation: Murkrow moves to (7, 3).
  - If Failure: Reset Map via Stairs at (3, 2).

## Plan: Eastern Flank (Col 17)
1. **Reset**: Return to (10, 8). Murkrow will be at (7, 4).
2. **Align Y**: Move Up to (10, 6). Murkrow -> (7, 2).
3. **Align X (Gap 11)**:
   - Move Right to (28, 6). Murkrow blocked at (15, 2) -> (14, 2).
   - Move Left until Murkrow blocked at (7, 2).
   - Move Right to establish Gap 11 (Player 18, Murkrow 7).
   - Move Right to (28, 6). Murkrow -> (17, 2).
4. **Descent**:
   - Down Col 28 (Player) / Col 17 (Murkrow).
   - Murkrow target: (17, 14).
5. **Final Approach**:
   - Align Murkrow to Row 14.
   - Shift Murkrow Right to (22, 14).
   - Drop to Door.

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap.
  - (14, 11) Locked Shutter.