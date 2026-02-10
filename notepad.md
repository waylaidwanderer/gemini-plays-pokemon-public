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

## Plan: The Under-Tree Route (Active)
- **Goal**: Place P at (14, 12) and M at (14, 10).
- **Current**: P(7, 5), M(7, 3).
- **Step 1**: Down to (7, 10). (M -> 7, 8).
  - *Reason*: Row 8 is safe for M, avoiding Wall at (8, 6).
- **Step 2**: Right to (10, 10). (M -> 10, 8).
- **Step 3**: Down to (10, 12). (M -> 10, 10 via Fake Wall).
- **Step 4**: Right to (14, 12). (M -> 14, 10).
- **Step 5**: Interact with Shutter (14, 11) or Murkrow.

## Murkrow Mechanics (Verified)
- **Mimicry**: Active. Relative offset (0, -2).
- **Reset**: Resets to (7, 2) if led astray.

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