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

## Plan: Murkrow to Shutter (14, 10)
1. **Align Gap**: Right to (18, 6). (Murkrow blocked at 8, 2).
2. **Setup Row 5**: Down to (18, 9). Right to (22, 9). (Murkrow -> 11, 5).
3. **Block Up**: Up to (22, 3). (Murkrow blocked at 11, 4).
4. **Cross East**: Right to (28, 3). (Murkrow -> 14, 5).
5. **Align Col 10**: 
   - Down to (28, 6). (Murkrow -> 14, 8).
   - Left to (24, 6). (Murkrow -> 10, 8).
6. **Drop to Row 10**: Down to (24, 10). (Murkrow -> 10, 10).
7. **Final Shift**: Navigate traps to move Murkrow Right to (14, 10).
8. **Interact**: Talk to Murkrow/Shutter.

## Trap Data
- Warp Traps suspected at (26, 9), (26, 10), (25, 11).
- If triggered, return via B1F -> B2F Stairs (NE).

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap.
  - (14, 11) Locked Shutter.