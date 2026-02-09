# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Validated Slide (Phase 1)
- **Goal**: Establish Offset P(21, 11), M(22, 10).
- **Current**: P(22, 14), M(22, 13).
- **Sequence**:
  1. `Up` x3 -> P(22, 11), M(22, 10).
     - (Robust: If M starts higher, it hits Grunt at 22,9 and aligns).
  2. `Left` -> P(21, 11). M Blocked by Computer (21, 10). Stays (22, 10).
- **Next Turn**: `Down` x4, `Right`, `A`.
- **Action**: Execute Setup.