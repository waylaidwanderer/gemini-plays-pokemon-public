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

## Plan: Murkrow to Shutter (14, 10) - The Offset Method (Active)
1. **Initial State**: Player (10, 10), Murkrow (10, 8).
2. **Align X (Offset)**:
   - Right to (20, 10).
   - Murkrow blocked at (14, 8) by Wall (15, 8).
   - Result: Player (20, 10), Murkrow (14, 8). Offset = 6.
3. **Position for Drop**:
   - Left to (16, 10).
   - Murkrow moves to (10, 8).
4. **The Drop**:
   - Down to (16, 12).
   - Murkrow moves (10, 8) -> (10, 9) -> (10, 10).
5. **Final Placement**:
   - Right to (20, 12).
   - Murkrow moves to (14, 10).
6. **Interaction**:
   - Move Up to (20, 11).
   - Navigate to Shutter (14, 11) via (14, 12).

## Trap Data
- Warp Traps at (26, 9), (26, 10), (24, 11), (25, 11).
- Avoid (26, 10)! Stop at (20, 10).

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - Fake Wall at (10, 9).
  - Shutter at (14, 11) / (15, 10).

## Trap Data
- Warp Traps at (26, 9), (26, 10), (24, 11), (25, 11).
- Avoid these tiles!

## Key Info
- **Boss Door**: Needs Voice ID (Murkrow).
- **Map**: 
  - (7, 0) Wall.
  - (15, 13) Gap.
  - (14, 11) Locked Shutter.