# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow mimics player's relative movement vector.
- **Collision Rules**:
  - P Blocked: Murkrow Stays (High Confidence).
  - M Blocked: Murkrow Stays (Verified).
  - Stack/Swap: To be tested.

## Current State
- **Player**: (22, 14).
- **Murkrow**: (22, 13) (Visual Confirmation).
- **Door**: (23, 14).
- **Status**: Trapped. Needs to move Up to escape.

## Strategy: Validated Slide (Setup Phase)
- **Goal**: Desync at P(21, 11), M(22, 10).
- **Current**: P(21, 13), M(21, 12).
- **Sequence**:
  1. `Left` -> P(20, 13), M(20, 12).
  2. `Up` -> P(20, 12), M(20, 11).
  3. `Right` -> P(21, 12), M(21, 11).
  4. `Right` -> P(22, 12), M(22, 11).
  5. `Up` -> P(22, 11), M(22, 10).
  6. `Left` -> P(21, 11). M Blocked at (21, 10). Stays (22, 10).
- **Action**: Execute Setup.