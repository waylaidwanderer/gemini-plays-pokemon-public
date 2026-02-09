# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Current State
- **Player**: (22, 13).
- **Murkrow**: (22, 12).
- **Door**: (23, 14).

## Strategy: The Corridor Trap
- **Goal**: Trap M at (22, 14) using the Corridor Wall/Door.
- **Current**: P(22, 13). Row 12 is likely Blocked/Ledge.
- **Plan**:
  1. `Right` -> P(23, 13). M moves Right (to 22, 13 or blocked).
  2. `Down` -> P Blocked by Door. M moves Down to (22, 14) (if at 22, 13).
  3. `Left` -> P(22, 13). M moves Left (Blocked by Grunt). M stays (22, 14).
  4. `Down`, `A`.
- **Action**: Execute `Right`, `Down`, `Left`, `Down`, `A`.