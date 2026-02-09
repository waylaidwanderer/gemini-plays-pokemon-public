# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Ultimate Murkrow Solution
- **Logic**: Use X-Block (Computer) then Y-Block (Grunt/Wall) to position M at (22, 14).
- **Current**: P(21, 13), M(21, 12).
- **Phase 1: X-Desync**
  1. `Right` -> P(22, 13), M(22, 12).
  2. `Up` x2 -> P(22, 11), M(22, 10).
  3. `Left` -> P(21, 11). M(22, 10) (Blocked by Computer 21, 10).
- **Phase 2: Y-Desync (Grunt)**
  4. `Up` x2 -> P(21, 9). M(22, 10) (Blocked by Grunt 22, 9).
- **Phase 3: Docking**
  5. `Down` x4 -> P(21, 13), M(22, 14).
  6. `Down` -> P(21, 14). M(22, 14) (Blocked by Wall 22, 15).
  7. Face Right, Interact.
- **Action**: Execute Phase 1 (Right, Up, Up, Left).