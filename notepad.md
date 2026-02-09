# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Double Scrape
- **Goal**: Me(22, 13), M(22, 14).
- **Current**: Me(21, 13), M(21, 12).
- **Plan**:
  1. `Right` -> Me(22, 13), M(22, 12).
  2. `Up` x2 -> Me(22, 11), M(22, 10).
  3. `Left` -> Me(21, 11). M Blocked by Computer (21, 10). Stays (22, 10).
  4. `Down` x2 -> Me(21, 13), M(22, 12).
  5. `Down` (Blocked by Grunt) -> Me(21, 13). M moves to (22, 13).
  6. `Down` (Blocked by Grunt) -> Me(21, 13). M moves to (22, 14).
  7. `Right` -> Me(22, 13). M Stays (Blocked by Door).
  8. Face Down, Interact.
- **Action**: Execute Step 1 & 2 (Right, Up, Up).