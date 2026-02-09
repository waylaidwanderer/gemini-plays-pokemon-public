# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: Right Wall Desync
- **Goal**: P(22, 13), M(22, 14).
- **Current**: P(22, 13), M(22, 12).
- **Plan**:
  1. `Right` -> P(22, 13). M(23, 12) (If open).
  2. `Up` x2 -> P(22, 11). M(23, 11) or (23, 12).
  3. `Left` -> P(21, 11). M(22, 11) or (22, 12).
  4. `Down` x2 -> P(21, 13). M(22, 13) or (22, 14).
  5. `Down` (Grunt Block) -> P(21, 13). M(22, 14).
  6. `Right` -> P(22, 13). M(22, 14) (Door Block).
  7. Face Down, Interact.
- **Action**: Execute Steps 1-2 (Right, Up, Up).