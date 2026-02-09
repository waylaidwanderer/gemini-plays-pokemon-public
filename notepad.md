# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Real Plan
- **Goal**: P(22, 13), M(22, 14).
- **Current**: P(22, 13), M(22, 12).
- **Plan**:
  1. `Left` -> P(21, 13), M(21, 12).
  2. `Up` -> P(21, 12), M(21, 11).
  3. `Right` -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
  5. `Left` -> P(21, 11). M Blocked at (21, 10). Stays (22, 10).
  6. `Down` x4 -> M moves to (22, 14) while P gets blocked by Grunt at (21, 14).
  7. `Right` -> P(22, 13). M Stays (22, 14).
  8. Face Down, Interact.
- **Action**: Execute Steps 1-2 (Left, Up).