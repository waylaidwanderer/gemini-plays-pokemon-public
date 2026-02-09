# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Real Solution (Desync Y via Top)
- **Goal**: P(22, 13), M(22, 14).
- **Current**: P(22, 13), M(22, 12).
- **Plan**:
  1. `Left`, `Up` -> P(21, 12), M(21, 11).
  2. `Right` -> P(22, 12), M(22, 11).
  3. `Up` -> P(22, 11), M(22, 10).
  4. `Left` x2 -> P(20, 11). M Stays (22, 10).
  5. `Up` -> P(20, 10). M Stays (22, 10).
  6. `Down` x3 -> P(20, 13), M(22, 13).
  7. `Down` -> P(20, 14), M(22, 14). Wait, I need P(20,13), M(22,14).
  8. From P(20,13), M(22,14) -> Right x2 -> P(22,13).
- **Action**: Execute Steps 1-2 (Left, Up, Right).