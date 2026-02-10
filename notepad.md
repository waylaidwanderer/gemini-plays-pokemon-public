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

## Plan: Murkrow to Shutter (14, 10) - Via NW Stairs
1. **Start**: Player (3, 2), Murkrow (7, 2).
2. **Move Down**: To (3, 5). Murkrow -> (7, 5).
3. **Bypass Stairs**: 
   - Right to (4, 5). Murkrow -> (8, 5).
   - Down to (4, 7). Murkrow blocked at (8, 6) -> stays (8, 5).
   - Left to (3, 7). Murkrow -> (7, 5).
4. **Align Y**: Down to (3, 10). 
   - Murkrow moves (7, 5) -> (7, 8). 
   - Blocked at (7, 9).
5. **Align X (Gap)**: Right to (6, 10). Murkrow -> (10, 8).
6. **Pass Wall**: 
   - Down to (6, 12). Murkrow -> (10, 10) via Fake Wall (10, 9).
7. **Final Approach**: 
   - Right to (10, 12). Murkrow -> (14, 10).
   - Interact with Murkrow/Shutter.

## Trap Data
- Stairs at (3, 6) warp to B1F. AVOID.
- Warp Traps at (26, 9), (26, 10), (24, 11), (25, 11).

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - Wall at (8, 6) blocks Murkrow.
  - Wall at (7, 9) blocks Murkrow.
  - Fake Wall at (10, 9).
  - Gap at (6, 10).

## Trap Data
- Warp Traps at (26, 9), (26, 10), (24, 11), (25, 11).
- Avoid these tiles!

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap.
  - (14, 11) Locked Shutter.