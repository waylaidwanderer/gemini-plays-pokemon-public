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
- Player: (22, 14).
- Murkrow: (21, 13).
- Grunt: (21, 14) (Blocking).

## Strategy: Desync & Loop (Refined)
- **Goal**: Move Murkrow to (22, 13) and Player to (22, 14).
- **Sequence**:
  1. `Up` -> P(22,13), M(21,12).
  2. `Left` -> P(21,13), M(20,12).
  3. `Down` -> P Blocked (Grunt). M(20,13).
  4. `Right` -> P(22,13), M(21,13).
  5. `Down` -> P(22,14), M Blocked (Grunt). M(21,13).
  6. `Right` -> P Blocked (Door). M(22,13).
  7. Interact.