# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow COPIES player's movement.
- **Collision**:
  - P Blocked: Murkrow MOVES (Desync).
  - M Blocked: Murkrow STAYS.

## Current State
- Player: (22, 13).
- Murkrow: (22, 12).
- Grunt: (21, 14) (Blocking).

## Strategy: Desync & Loop
- **Goal**: Move Murkrow to (22, 14) (South of Player).
- **Sequence**:
  1. `Down` -> P(22,14), M(22,13).
  2. `Left` -> P Blocked (Grunt). M(21,13).
  3. `Up` -> P(22,13), M(21,12).
  4. `Left` -> P(21,13), M(20,12).
  5. `Down` -> P Blocked (Grunt). M(20,13).
  6. `Right` -> P(22,13), M(21,13).
  7. `Right` -> P Blocked (Wall). M(22,13) (Overlap?).
  8. `Down` -> P(22,14), M(22,14).