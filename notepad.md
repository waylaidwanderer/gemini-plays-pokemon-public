# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Validated Slide (Execution)
- **Goal**: Desync at P(21, 11), M(22, 10).
- **Current**: P(21, 13), M(21, 12).
- **Sequence**:
  1. `Left` -> P(20, 13), M(20, 12).
  2. `Up` -> P(20, 12), M(20, 11).
  3. `Right` -> P(21, 12), M(21, 11).
  4. `Right` -> P(22, 12), M(22, 11).
  5. `Up` -> P(22, 11), M(22, 10).
  6. `Left` -> P(21, 11). M Blocked at (21, 10). M Stays (22, 10).
- **Action**: Execute Steps 1-5 (Left, Up, Right, Right, Up).