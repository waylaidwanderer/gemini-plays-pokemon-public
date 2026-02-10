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

## Plan: Murkrow to Shutter (14, 10) - Refined
1. **Align Murkrow X (Critical Path)**:
   - **Start**: (3, 2) on B2F.
   - **Move**: Right to (18, 2). (Murkrow blocked at 8, 2 -> stays 7, 2).
   - **Move**: Down to (18, 6). (Murkrow -> 7, 6).
2. **Setup Row 5**: Down to (18, 9). Right to (22, 9). (Murkrow -> 11, 5).
3. **Block Up**: Up to (22, 3). (Murkrow blocked at 11, 4 -> stays 11, 5).
4. **Cross East**: Right to (28, 3). (Murkrow blocked at 15, 5 -> ends 14, 5).
5. **Loop to Row 12**:
   - Down to (28, 12). (Murkrow blocked at 14, 9 -> ends 14, 8).
   - Left to (24, 12). (Murkrow -> 10, 8).
6. **Align Murkrow Y**:
   - Mash Down at (24, 12) (blocked by 24, 13). (Murkrow -> 10, 10).
7. **Final Shift**:
   - Right to (26, 12). (Murkrow -> 12, 10).
   - Mash Right at (26, 12) (blocked by 27, 12). (Murkrow -> 14, 10).
8. **Interact**: Talk to Murkrow/Shutter.

## Trap Data
- Warp Traps at (26, 9), (26, 10), (24, 11), (25, 11).
- Avoid these tiles!

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap.
  - (14, 11) Locked Shutter.