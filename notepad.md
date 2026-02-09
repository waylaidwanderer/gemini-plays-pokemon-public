# Team Rocket HQ Log

## Objectives
- **Primary**: Open Boss Door at B2F (23, 14).
- **Secondary**: Defeat Team Rocket Executives.

## Mechanics (Verified)
- **Mimicry**: Murkrow COPIES player's movement input.
- **Collision**:
  - P Blocked: Murkrow MOVES (Desync Source).
  - M Blocked: Murkrow STAYS.
  - Overlap: Possible if P blocked and M moves into P's tile? Or M Blocked and P moves into M? We will try to overlap at (22, 13).

## Current State
- Player: (22, 14).
- Murkrow: (22, 13).
- Grunt: (21, 14) (Blocking).

## Strategy: The Overlap Maneuver
- **Goal**: Co-locate P and M at (22, 14).
- **Sequence**:
  1. `Left` -> P Blocked (Grunt). M(21, 13).
  2. `Up` -> P(22, 13). M(21, 12).
  3. `Left` -> P(21, 13). M(20, 12).
  4. `Down` -> P Blocked (Grunt). M(20, 13).
  5. `Right` -> P(22, 13). M(21, 13).
  6. `Right` -> P Blocked (Wall). M(22, 13) (OVERLAP!).
  7. `Down` -> P(22, 14). M(22, 14).
  8. `Right` -> Face Door.
  9. `A` -> Open.