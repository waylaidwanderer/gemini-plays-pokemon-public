# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow COPIES player's movement input.
- **Collision**:
  - P Blocked: Murkrow MOVES (Desync Source).
  - M Blocked: Murkrow STAYS.

## Current State
- Player: (22, 14).
- Murkrow: (21, 13) (Confirmed by logic).

## Strategy: The Perfect Overlap (Revised)
- **Sequence**:
  1. `Down` -> P(22, 14). M(22, 13). (Done).
  2. `Left` -> P Blocked (Grunt). M(21, 13). (Done).
  3. `Up` -> P(22, 13). M(21, 12).
  4. `Up` -> P(22, 12). M(21, 11).
  5. `Up` -> P(22, 11). M Blocked by Wall (21, 10). M Stays (21, 11). (Desync Y).
  6. `Right` -> P Blocked by Wall (23, 11). M(22, 11). (Overlap!).
  7. `Down` -> P(22, 12). M(22, 12).
  8. `Down` -> P(22, 13). M(22, 13).
  9. `Down` -> P(22, 14). M(22, 14).
  10. `Right`, `A`.