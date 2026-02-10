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

## Plan: Murkrow to Boss Door
1. **Escape**: Up to (10, 8). (Murkrow -> 7, 2)
2. **Setup Left**: Left to (3, 8). (Murkrow -> 1, 2)
3. **Drop 1**: Down to (3, 16). (Murkrow -> 1, 10)
4. **Shift Right**: Right to (14, 16). (Murkrow -> 12, 10)
5. **Ratchet Up**: Up to (14, 8). (Murkrow blocked at 12, 9)
6. **Drop 2**: Down to (14, 16). (Murkrow -> 12, 16)
7. **Align Row 13**: Up to (14, 13). (Murkrow -> 12, 13)
8. **Cross Gap**: Right to (25, 13). (Murkrow -> 23, 13)
9. **Finish**: Down to (25, 14). (Murkrow -> 23, 14)

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap.
  - (14, 11) Locked Shutter.