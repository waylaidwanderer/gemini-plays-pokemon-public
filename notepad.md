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
- Murkrow: (22, 13).

## Strategy: The Perfect Overlap
- **Concept**: Block M against the top wall (21, 10) to align Y, then block P against the right wall (23, 12) to align X.
- **Sequence**:
  1. `Left` -> P Blocked (Grunt). M(21, 13).
  2. `Up` -> P(22, 13). M(21, 12).
  3. `Up` -> P(22, 12). M(21, 11).
  4. `Up` -> P(22, 11). M Blocked by Wall (21, 10). M Stays (21, 11).
  5. `Down` -> P(22, 12). M(21, 12). (Y Aligned!)
  6. `Right` -> P Blocked by Wall (23, 12). M(22, 12). (Overlap!)
  7. `Down` -> P(22, 13). M(22, 13).
  8. `Down` -> P(22, 14). M(22, 14).
  9. `Right`, `A`.