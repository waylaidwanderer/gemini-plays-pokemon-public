# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Ultimate Desync (Step-by-Step)
- **Goal**: P(22, 13), M(22, 14).
- **Current**: P(22, 13), M(22, 12).
- **Plan**:
  1. `Left` -> P(21, 13), M(21, 12).
  2. `Up` -> P(21, 12), M(21, 11).
  3. `Right` -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
  5. `Left` -> P(21, 11). M Blocked at (21, 10). Stays (22, 10).
  6. `Down` x3 -> P(21, 13), M(22, 13). (Using Grunt Block).
  7. `Down` -> P(21, 13), M(22, 14). (Using Grunt Block).
  8. `Right` -> P(22, 13). M Stays (22, 14).
  9. Interact Down.
- **Action**: Execute Steps 1-3 (Left, Up, Right).