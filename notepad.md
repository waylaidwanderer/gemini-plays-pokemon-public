# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Computer-Grunt Combo
- **Goal**: P(22, 13), M(22, 14).
- **Current**: P(22, 14), M(22, 13).
- **Plan**:
  1. `Up` x3 -> P(22, 11), M(22, 10).
  2. `Left` -> P(21, 11). M Blocked by Computer (21, 10). Stays (22, 10).
  3. `Down` x2 -> P(21, 13), M(22, 12).
  4. `Down` (Bump Grunt) -> P(21, 13). M moves (22, 13).
  5. `Down` (Bump Grunt) -> P(21, 13). M moves (22, 14).
  6. `Right` -> P(22, 13). M Stays (22, 14).
  7. Face Down, Interact.
- **Action**: Execute Step 1 (Up x3).