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

## Plan: Murkrow to Shutter (14, 10) - The "Fake Wall" Path
1. **Start**: P(10, 8), M(7, 7).
2. **Move Down**: P(10, 9). M(7, 8).
3. **Move Right** x4 (Burn against Wall 12, 9):
   - P(11, 9). M(8, 8).
   - P(12, 9) [Blocked]. M(9, 8).
   - P(12, 9) [Blocked]. M(10, 8).
   - P(12, 9) [Blocked]. M(11, 8).
4. **Move Down**: P(11, 10). M(11, 9).
5. **Move Right** x2: P(13, 10). M(13, 9).
6. **Move Down** (Burn against Wall 13, 11):
   - P(13, 11) [Blocked]. M(13, 10).
7. **Move Right** (Burn against Shutter 14, 11):
   - P(14, 11) [Blocked]. M(14, 10).
8. **Finish**: P(13, 10), M(14, 10). Interact.

## Trap Data
- Warp Traps at (26, 9), (26, 10), (24, 11), (25, 11).
- Path on Col 10 is Safe.

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - Fake Wall at (10, 9) is Walkable.
  - Wall at (9, 9) and (9, 11) used for blocking.

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