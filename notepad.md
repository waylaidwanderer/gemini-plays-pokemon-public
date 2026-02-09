# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Grunt Block Method
- **Goal**: P(22, 13), M(22, 14).
- **Current**: P(20, 14), M(21, 12).
- **Plan**:
  1. `Up` -> P(20, 13), M(21, 11).
  2. `Right` -> P(21, 13), M(22, 11).
  3. `Up` -> P(21, 12), M(22, 10).
  4. `Up` -> P(21, 11). M(22, 9) (Blocked by Grunt). M(22, 10).
  5. `Down` x2 -> P(21, 13), M(22, 12).
  6. `Down` (Block P) -> P(21, 13), M(22, 13).
  7. `Down` (Block P) -> P(21, 13), M(22, 14).
  8. `Right` -> P(22, 13). M(22, 14) (Block Door).
  9. Interact Down.
- **Action**: Execute Steps 1-2 (Up, Right).