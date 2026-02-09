# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Murkrow Protocol
- **Goal**: P(22, 13), M(22, 14). Interact Down.
- **Phase 1: X-Desync**
  1. `Right` -> P(22, 13), M(22, 12).
  2. `Up` x2 -> P(22, 11), M(22, 10).
  3. `Left` -> P(21, 11). M Blocked at (21, 10). (M is now Right of P).
- **Phase 2: Y-Shift (Player Block)**
  4. `Down` x2 -> P(21, 13), M(22, 12).
  5. `Down` (Blocked by Grunt) -> P(21, 13), M(22, 13).
  6. `Down` (Blocked by Grunt) -> P(21, 13), M(22, 14).
- **Phase 3: Docking**
  7. `Right` -> P(22, 13). M Blocked by Door.
  8. Face Down, Interact.
- **Action**: Execute Step 1 (Right).