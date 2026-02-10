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

## Plan: Murkrow to Shutter (14, 10) - The "Code Path"
1. **Initial**: P(10, 2), M(7, 2).
2. **Setup**:
   - Down x6 to (10, 8). (Murkrow -> 7, 8).
   - Right x3 to (13, 8). (Murkrow -> 10, 8).
   - Down x2 to (13, 10). (Murkrow -> 10, 10).
3. **Delivery**:
   - Right x4. 
   - P blocked at (15, 10) (Shutter).
   - If Murkrow moves while P blocked, M -> (14, 10).
   - If not, alternate plan needed from P(13, 10), M(10, 10).

## Trap Data
- Warp Traps at (26, 9), (26, 10), (24, 11), (25, 11).
- Path on Col 10 is Safe.

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - Fake Wall at (10, 9) is Walkable.
  - Wall at (9, 9) and (9, 11) used for blocking.

## Trap Data
- Warp Traps at (26, 9), (26, 10), (24, 11), (25, 11).
- Avoid these tiles!

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap.
  - (14, 11) Locked Shutter.
## Status Update (Turn 35891)
- **Failure**: Murkrow was NOT at (14, 10) or (14, 8) after the blind sequence.
- **Hypothesis**: Murkrow got stuck earlier or reset.
- **Action**: Returning to (7, 2) to re-acquire Murkrow.
- **Note**: "Offset Method" requires visual confirmation of the desync. Blind execution is unreliable.