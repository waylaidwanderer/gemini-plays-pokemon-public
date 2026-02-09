# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Ultimate Desync
- **Goal**: Place Murkrow at (22, 14).
- **Current**: P(22, 14), M(22, 13) (Visual Confirmation).
- **Plan**:
  1. `Up` x3 -> P(22, 11), M(22, 10).
  2. `Left` -> P(21, 11). M Blocked by Computer (21, 10). Stays (22, 10).
  3. `Down` x4 -> P(21, 13), M(22, 14).
     - (P moves to 21, 13. Then blocked by Grunt at 21, 14 for last 2 steps).
  4. `Right` -> P(22, 13). M Stays (22, 14).
  5. Face Down, Interact.
- **Action**: Execute Step 1 (Up x3).