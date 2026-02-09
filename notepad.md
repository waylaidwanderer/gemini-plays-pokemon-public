# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Left Shelf Scrape
- **Goal**: Use Shelf at (20, 12) to desync M.
- **Current**: P(21, 13), M(21, 12).
- **Plan**:
  1. `Left` -> P(20, 13). M Blocked by Shelf at (20, 12)? Stays (21, 12).
  2. `Down` -> P(20, 14). M moves (21, 13).
  3. `Right` (Player Blocked by Grunt at 21, 14) -> P(20, 14). M moves (22, 13).
  4. `Down` -> P(20, 15). M moves (22, 14).
  5. `Right` -> P(21, 15). M Blocked by Door. Stays (22, 14).
  6. `Right` -> P(22, 15). M Stays (22, 14).
  7. Face Up, Interact.
- **Action**: Execute Step 1 (Left).