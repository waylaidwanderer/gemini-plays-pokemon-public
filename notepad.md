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

## Strategy: The Definitive Slide Test
- **Goal**: Place M at (22, 14).
- **Hypothesis**: P Blocked by Grunt (21, 14) ALLOWS M to move.
- **Current**: P(22, 13), M(22, 12).
- **Plan**:
  1. `Up` x2 -> P(22, 11), M(22, 10).
  2. `Left` -> P(21, 11). M Blocked by Computer (21, 10). Stays (22, 10).
  3. `Down` x2 -> P(21, 13), M(22, 12).
  4. `Down` (TEST) -> P Blocked. Does M move to (22, 13)?
  5. `Down` (Continue) -> If moved, M to (22, 14).
  6. `Right`, `Down`, `A`.
- **Action**: Execute Steps 1-2 (Up, Up, Left).