# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: Murkrow Computer Scraping
- **Goal**: Use the Solid Computer at (21, 10) to desync X-axis.
- **Path**:
  1. `Left` -> P(21, 13), M(21, 12).
  2. `Up` -> P(21, 12), M(21, 11).
  3. `Right` -> P(22, 12), M(22, 11).
  4. `Up` -> P(22, 11), M(22, 10).
  5. `Left` x2 -> P(20, 11). (M Blocked at 21,10, stays at 22,10).
  6. `Down` x4 -> P(20, 15). M(22, 14).
  7. `Right` x2 -> P(22, 15). M(22, 14) (Blocked by Wall).
  8. Face Up, Interact.
- **Action**: Execute Steps 1-4.