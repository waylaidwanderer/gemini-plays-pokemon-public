# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Grunt Scrape
- **Goal**: Place M at (22, 13) while P is at (21, 13).
- **Theory**: Followers move if they can, even if Player is blocked.
- **Plan**:
  1. `Up` x2 -> P(22, 11), M(22, 10).
  2. `Left` -> P(21, 11). M Blocked by Computer (21, 10). Stays (22, 10).
  3. `Down` x2 -> P(21, 13), M(22, 12).
  4. `Down` -> P Blocked by Grunt (21, 14). M moves to (22, 13).
  5. Face Right, Interact.
- **Action**: Execute Step 1 (Up x2).